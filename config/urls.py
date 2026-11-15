from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("demo-connection/lookup/", views.lookup_demo_connection, name="lookup_demo_connection"),
    path("demo-checkout/", views.demo_checkout, name="demo_checkout"),
    path("demo-connection/<int:pk>/simulate-payment/", views.simulate_connection_payment, name="simulate_connection_payment"),
    path("book/", views.create_booking, name="create_booking"),
    path("booking/<int:pk>/payment-info/", views.payment_info, name="payment_info"),
    path("booking/<int:pk>/simulate-payment/", views.simulate_payment, name="simulate_payment"),
    path("booking/<int:pk>/connection-status/", views.connection_status, name="connection_status"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
