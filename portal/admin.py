from django.contrib import admin
from .models import GasCompanyTheme, GasProduct, PaymentQR, Booking, DemoGasConnection


@admin.register(GasCompanyTheme)
class GasCompanyThemeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("1. Company-style Demo Profile", {"fields": ("profile_key", "theme_style"), "description": "यह किसी वास्तविक provider की official branding नहीं है।"}),
        ("2. Independent Demo Branding", {"fields": ("portal_name", "logo_text", "logo_image", "tagline")}),
        ("3. Homepage & Navigation", {"fields": ("hero_title", "hero_description", "nav_home_label", "nav_services_label", "nav_booking_label")}),
        ("4. Demo Notice & Support", {"fields": ("announcement", "support_phone")}),
        ("5. System", {"fields": ("updated_at",)}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not GasCompanyTheme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(DemoGasConnection)
class DemoGasConnectionAdmin(admin.ModelAdmin):
    list_display = ("connection_number", "owner_name", "area_label", "status", "demo_due_amount", "updated_at")
    list_filter = ("status",)
    search_fields = ("connection_number", "owner_name")
    fieldsets = (
        ("Fictional Demo Record Only", {"fields": ("connection_number", "owner_name", "area_label", "status", "demo_due_amount")}),
    )


@admin.register(GasProduct)
class GasProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "active")
    list_filter = ("active",)
    search_fields = ("name",)


@admin.register(PaymentQR)
class PaymentQRAdmin(admin.ModelAdmin):
    list_display = ("title", "active", "updated_at")
    list_filter = ("active",)
    fields = ("title", "image", "instructions", "active")

    def has_add_permission(self, request):
        return not PaymentQR.objects.exists()


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "mobile", "product", "amount", "status", "created_at")
    list_filter = ("status", "created_at", "product")
    search_fields = ("customer_name", "mobile")
    list_editable = ("status",)
    readonly_fields = ("amount", "created_at")
