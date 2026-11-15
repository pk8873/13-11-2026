from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from .models import GasCompanyTheme, GasProduct, PaymentQR, Booking, DemoGasConnection


class PaymentQRAdminForm(forms.ModelForm):
    class Meta:
        model = PaymentQR
        fields = "__all__"

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image
        allowed = {".png", ".jpg", ".jpeg", ".webp"}
        name = (image.name or "").lower()
        extension = "." + name.rsplit(".", 1)[-1] if "." in name else ""
        if extension not in allowed:
            raise ValidationError("केवल PNG, JPG या WEBP image upload करें।")
        if image.size > 3 * 1024 * 1024:
            raise ValidationError("Demo preview image अधिकतम 3 MB की हो सकती है।")
        # Django's ImageField validates that the uploaded file is a readable image.
        return image


@admin.register(GasCompanyTheme)
class GasCompanyThemeAdmin(admin.ModelAdmin):
    list_display = ("portal_name", "theme_style", "logo_preview", "updated_at")
    fieldsets = (
        ("1. Independent Demo Profile", {
            "fields": ("profile_key", "theme_style"),
            "description": "यह किसी वास्तविक LPG provider की official branding नहीं है।",
        }),
        ("2. Independent Demo Branding", {
            "fields": ("portal_name", "logo_text", "logo_image", "logo_preview", "tagline"),
            "description": "केवल अपना बनाया हुआ या उपयोग की अनुमति वाला independent demo logo इस्तेमाल करें।",
        }),
        ("3. Homepage & Navigation", {
            "fields": ("hero_title", "hero_description", "nav_home_label", "nav_services_label", "nav_booking_label"),
        }),
        ("4. Demo Notice & Support", {"fields": ("announcement", "support_phone")}),
        ("5. System", {"fields": ("updated_at",)}),
    )
    readonly_fields = ("updated_at", "logo_preview")

    @admin.display(description="Logo preview")
    def logo_preview(self, obj):
        if obj and obj.logo_image:
            return format_html(
                '<img src="{}" alt="Demo logo preview" style="max-width:180px;max-height:90px;object-fit:contain;background:#f3f6fa;padding:8px;border:1px solid #dbe3ed;border-radius:10px;">',
                obj.logo_image.url,
            )
        return format_html('<span style="color:#64748b">Default GasCare demo mark</span>')

    def has_add_permission(self, request):
        return not GasCompanyTheme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(DemoGasConnection)
class DemoGasConnectionAdmin(admin.ModelAdmin):
    list_display = ("connection_number", "owner_name", "area_label", "status", "demo_due_amount", "updated_at")
    list_filter = ("status",)
    search_fields = ("connection_number", "owner_name")
    readonly_fields = ("updated_at",)
    fieldsets = (
        ("Fictional Demo Record Only", {
            "fields": ("connection_number", "owner_name", "area_label", "status", "demo_due_amount", "updated_at"),
            "description": "केवल काल्पनिक test records रखें। वास्तविक LPG उपभोक्ता की जानकारी न जोड़ें।",
        }),
    )


@admin.register(GasProduct)
class GasProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "active")
    list_filter = ("active",)
    search_fields = ("name",)
    list_editable = ("active",)


@admin.register(PaymentQR)
class PaymentQRAdmin(admin.ModelAdmin):
    form = PaymentQRAdminForm
    list_display = ("title", "active", "qr_preview", "updated_at")
    list_filter = ("active",)
    search_fields = ("title",)
    readonly_fields = ("qr_preview", "updated_at")
    fieldsets = (
        ("Admin-only Demo Image Library", {
            "fields": ("title", "image", "qr_preview", "instructions", "active", "updated_at"),
            "description": (
                "यह image केवल Admin में preview/reference के लिए save होती है। "
                "Customer statement या checkout इसे नहीं दिखाते। Customer checkout पर अलग, "
                "स्थिर और non-scannable TEST visual रहता है। केवल non-functional demo artwork upload करें; "
                "कभी वास्तविक UPI, bank या payment QR upload न करें।"
            ),
        }),
    )

    @admin.display(description="Uploaded image")
    def qr_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" alt="Admin-only demo image preview" style="width:112px;height:112px;object-fit:contain;background:#fff;padding:6px;border:1px solid #dbe3ed;border-radius:10px;">',
                obj.image.url,
            )
        return format_html('<span style="color:#64748b">No demo image uploaded</span>')

    def has_add_permission(self, request):
        return not PaymentQR.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "product", "amount", "status", "created_at")
    list_filter = ("status", "created_at", "product")
    search_fields = ("customer_name",)
    date_hierarchy = "created_at"
    readonly_fields = ("amount", "created_at")
    fieldsets = (
        ("Test Booking Record", {
            "fields": ("customer_name", "mobile", "address", "product", "amount", "status", "created_at"),
            "description": "यह demo booking data है। वास्तविक ग्राहक का मोबाइल या पता दर्ज न करें।",
        }),
    )
