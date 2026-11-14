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
        messages.error(request, "कृपया सही मोबाइल नंबर दर्ज करें।")
        return redirect("home")
    product = get_object_or_404(GasProduct, pk=product_id, active=True)
    booking = Booking.objects.create(
        customer_name=name, mobile=mobile, address=address,
        product=product, amount=product.price
    )
    return redirect("payment_info", pk=booking.pk)

def payment_info(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    qr = PaymentQR.objects.filter(active=True).first()
    return render(request, "portal/payment_info.html", {"booking": booking, "qr": qr})
