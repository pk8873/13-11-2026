from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import GasProduct, PaymentQR, Booking


def home(request):
    products = GasProduct.objects.filter(active=True)
    return render(request, "portal/home.html", {"products": products})


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
    booking = Booking.objects.create(
        customer_name=name, mobile=mobile, address=address,
        product=product, amount=product.price
    )
    return redirect("payment_info", pk=booking.pk)


def payment_info(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    # Deliberately no live UPI/QR payment: this is a safe payment simulation.
    return render(request, "portal/payment_info.html", {"booking": booking})


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
        "booking": booking,
        "restored": restored,
    })
