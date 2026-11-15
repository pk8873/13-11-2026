from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import GasCompanyTheme, GasProduct, Booking, DemoGasConnection, PaymentQR


def get_site_theme():
    theme, _ = GasCompanyTheme.objects.get_or_create(
        pk=1,
        defaults={"portal_name": "Gas Seva Demo", "theme_style": "indigo"},
    )
    return theme


def home(request):
    products = GasProduct.objects.filter(active=True)
    return render(request, "portal/home.html", {
        "products": products,
        "site_theme": get_site_theme(),
    })


@require_http_methods(["POST"])
def lookup_demo_connection(request):
    connection_number = request.POST.get("connection_number", "").strip().upper()
    owner_name = request.POST.get("owner_name", "").strip()
    if not connection_number or not owner_name:
        messages.error(request, "Demo Connection ID और Demo Customer Name दोनों भरें।")
        return redirect("home")
    connection = DemoGasConnection.objects.filter(
        connection_number__iexact=connection_number,
        owner_name__iexact=owner_name,
    ).first()
    if connection is None:
        messages.error(request, "Demo रिकॉर्ड नहीं मिला। Admin में बनाए गए काल्पनिक Demo ID और नाम का उपयोग करें।")
        return redirect("home")
    return render(request, "portal/connection_lookup.html", {
        "connection": connection,
        "site_theme": get_site_theme(),
        "payment_qr": PaymentQR.objects.filter(active=True).first(),
    })


@require_http_methods(["POST"])
def simulate_connection_payment(request, pk):
    connection = get_object_or_404(DemoGasConnection, pk=pk)
    if connection.status == "HOLD":
        connection.status = "ACTIVE"
        connection.save(update_fields=["status", "updated_at"])
        messages.success(request, "Demo simulation पूरी हुई। रिकॉर्ड अब ACTIVE है। कोई वास्तविक भुगतान नहीं हुआ।")
    return render(request, "portal/connection_lookup.html", {
        "connection": connection,
        "site_theme": get_site_theme(),
        "payment_qr": PaymentQR.objects.filter(active=True).first(),
    })


@require_http_methods(["POST"])
def create_booking(request):
    name = request.POST.get("customer_name", "").strip()
    mobile = request.POST.get("mobile", "").strip()
    address = request.POST.get("address", "").strip()
    product_id = request.POST.get("product")
    if not name or not mobile or not address or not product_id:
        messages.error(request, "कृपया सभी जानकारी भरें।")
        return redirect("home")
    if not mobile.isdigit() or not 10 <= len(mobile) <= 15:
        messages.error(request, "कृपया टेस्ट मोबाइल नंबर सही दर्ज करें।")
        return redirect("home")
    product = get_object_or_404(GasProduct, pk=product_id, active=True)
    booking = Booking.objects.create(customer_name=name, mobile=mobile, address=address, product=product, amount=product.price)
    return redirect("payment_info", pk=booking.pk)


def payment_info(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, "portal/payment_info.html", {"booking": booking, "site_theme": get_site_theme()})


@require_http_methods(["POST"])
def simulate_payment(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if booking.status != "APPROVED":
        booking.status = "APPROVED"
        booking.save(update_fields=["status"])
    return redirect("connection_status", pk=booking.pk)


def connection_status(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    restored = booking.status == "APPROVED"
    return render(request, "portal/connection_status.html", {
        "booking": booking, "restored": restored, "site_theme": get_site_theme(),
    })
