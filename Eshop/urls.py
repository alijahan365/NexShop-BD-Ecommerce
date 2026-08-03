from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib import messages
from store.models.orders import Order
from . import settings

def admin_verify_payment(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.payment_status = 'Verified & Approved'
        order.save()
        messages.success(request, f"Order #{order_id} payment has been Verified & Approved!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return redirect('/admin/store/order/')

def admin_mark_delivered(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.status = True
        order.save()
        messages.success(request, f"Order #{order_id} status has been updated to Delivered!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return redirect('/admin/store/order/')

from django.http import JsonResponse
from store.sms_service import send_otp_sms

def send_otp_sms_api(request):
    mobile = request.GET.get('mobile', '01784299242')
    otp = request.GET.get('otp', '123456')
    gateway = request.GET.get('gateway', 'bKash')
    result = send_otp_sms(mobile, otp, gateway)
    return JsonResponse(result)

from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('send-otp-sms/', send_otp_sms_api),
    path('admin/verify-payment/<int:order_id>/', admin_verify_payment),
    path('admin/mark-delivered/<int:order_id>/', admin_mark_delivered),
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

