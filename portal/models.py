from django.db import models


class GasCompanyTheme(models.Model):
    PROFILE_CHOICES = [
        ("indian_style", "Indian-style LPG Demo Profile"),
        ("bharat_style", "Bharat-style LPG Demo Profile"),
        ("green_energy", "Green Energy Utility Demo Profile"),
        ("custom", "Custom Independent Demo Profile"),
    ]
    THEME_CHOICES = [
        ("indigo", "Indigo Corporate"),
        ("saffron", "Saffron Service"),
        ("green", "Green Energy"),
        ("blue", "Blue Utility"),
    ]
    profile_key = models.CharField(max_length=24, choices=PROFILE_CHOICES, default="indian_style")
    portal_name = models.CharField(max_length=100, default="Gas Seva Demo")
    logo_text = models.CharField(max_length=10, default="GS")
    logo_image = models.ImageField(
        upload_to="demo_branding/",
        blank=True,
        help_text="केवल अपना बनाया हुआ या उपयोग की अनुमति वाला Demo logo upload करें। वास्तविक provider का logo नहीं।",
    )
    tagline = models.CharField(max_length=180, default="Your independent demo LPG service portal")
    theme_style = models.CharField(max_length=20, choices=THEME_CHOICES, default="indigo")
    hero_title = models.CharField(max_length=160, default="LPG सेवाएँ, अब एक ही Demo पोर्टल पर")
    hero_description = models.CharField(max_length=260, default="बुकिंग और सर्विस अनुभव का अभ्यास इस स्वतंत्र Demo वातावरण में करें।")
    nav_home_label = models.CharField(max_length=40, default="होम")
    nav_services_label = models.CharField(max_length=40, default="सेवाएँ")
    nav_booking_label = models.CharField(max_length=40, default="बुकिंग")
    support_phone = models.CharField(max_length=30, blank=True, default="1800-000-0000")
    announcement = models.CharField(max_length=220, blank=True, default="Demo portal: services and payment are simulated.")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website Company Profile Switcher"
        verbose_name_plural = "Website Company Profile Switcher"

    def save(self, *args, **kwargs):
        preset_themes = {
            "indian_style": "saffron",
            "bharat_style": "blue",
            "green_energy": "green",
        }
        if self.profile_key in preset_themes:
            self.theme_style = preset_themes[self.profile_key]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.portal_name} ({self.get_profile_key_display()})"


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
