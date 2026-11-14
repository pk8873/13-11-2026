from django.contrib import admin
from .models import GasCompanyTheme, GasProduct, PaymentQR, Booking


@admin.register(GasCompanyTheme)
class GasCompanyThemeAdmin(admin.ModelAdmin):
    list_display = ("portal_name", "theme_style", "updated_at")
    fields = ("portal_name", "tagline", "theme_style", "support_phone", "announcement")
    def has_add_permission(self, request):
        return not GasCompanyTheme.objects.exists()


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
