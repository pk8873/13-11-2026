from decimal import Decimal
from types import SimpleNamespace

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
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
    # This is intentionally a sample generator, NOT a real LPG lookup.
    # Do not save or query the submitted reference/name against real customer records.
    connection_number = request.POST.get("connection_number", "").strip()[:24]
    owner_name = request.POST.get("owner_name", "").strip()[:120]
    if not connection_number or not owner_name:
        messages.error(request, "कृपया दोनों Demo fields भरें।")
        return redirect("home")

    sample = SimpleNamespace(
        connection_number=connection_number,
        owner_name=owner_name,
        area_label="Illustrative sample only — provider/area not verified",
        updated_at=timezone.now(),
        demo_due_amount=Decimal("350.00"),
    )
    return render(request, "portal/connection_lookup.html", {
        "connection": sample,
        "site_theme": get_site_theme(),
        "payment_qr": None,
        "sample_statement": True,
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
        "payment_qr": None,
        "sample_statement": False,
    })


@require_http_methods(["POST"])
def demo_checkout(request):
    # Entirely simulated checkout: no payment gateway, QR payload, or money transfer.
    connection_number = request.POST.get("connection_number", "").strip()[:24]
    owner_name = request.POST.get("owner_name", "").strip()[:120]
    stage = request.POST.get("stage", "checkout")
    if not connection_number or not owner_name:
        messages.error(request, "Sample statement से checkout शुरू करें।")
        return redirect("home")
    completed = stage == "complete"
    return render(request, "portal/demo_payment.html", {
        "connection_number": connection_number,
        "owner_name": owner_name,
        "amount": Decimal("350.00"),
        "completed": completed,
        "site_theme": get_site_theme(),
    })


def create_booking(request):
    if request.method != "POST":
        return redirect("home")
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
