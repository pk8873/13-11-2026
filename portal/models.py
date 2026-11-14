from django.db import models


class GasCompanyTheme(models.Model):
    THEME_CHOICES = [
        ("indigo", "Indigo Corporate"),
        ("saffron", "Saffron Service"),
        ("green", "Green Energy"),
        ("blue", "Blue Utility"),
    ]
    portal_name = models.CharField(max_length=100, default="Gas Seva Demo")
    tagline = models.CharField(max_length=180, default="Your demo LPG service portal")
    theme_style = models.CharField(max_length=20, choices=THEME_CHOICES, default="indigo")
    support_phone = models.CharField(max_length=30, blank=True, default="1800-000-0000")
    announcement = models.CharField(max_length=220, blank=True, default="Demo portal: services and payment are simulated.")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website Appearance Settings"
        verbose_name_plural = "Website Appearance Settings"

    def __str__(self):
        return f"{self.portal_name} ({self.get_theme_style_display()})"


class GasProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=240, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class PaymentQR(models.Model):
    title = models.CharField(max_length=100, default="Demo QR")
    image = models.ImageField(upload_to="payment_qr/")
    instructions = models.CharField(max_length=240, default="यह केवल परीक्षण QR है। वास्तविक भुगतान न करें।")
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Payment QR Settings"
        verbose_name_plural = "Payment QR Settings"

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("DELIVERED", "Delivered"),
    ]
    customer_name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    product = models.ForeignKey(GasProduct, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Booking #{self.pk} - {self.customer_name}"
