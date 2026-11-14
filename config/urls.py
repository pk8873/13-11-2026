from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("book/", views.create_booking, name="create_booking"),
    path("booking/<int:pk>/payment-info/", views.payment_info, name="payment_info"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
