from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


from django.utils.html import mark_safe

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'price', 'payment_method', 'transaction_id', 'verification_action', 'order_status_action', 'customer_message_note', 'date']
    list_filter = ['payment_status', 'payment_method', 'status', 'date']
    search_fields = ['transaction_id', 'phone', 'address', 'customer_message']
    actions = ['mark_payment_verified', 'mark_order_shipped', 'mark_order_delivered']

    def verification_action(self, obj):
        if 'Verified' in obj.payment_status or 'Approved' in obj.payment_status or 'Paid' in obj.payment_status:
            return mark_safe('<span style="color: #10b981; font-weight: bold; background: #d1fae5; padding: 4px 10px; border-radius: 12px;">✅ Verified</span>')
        else:
            return mark_safe(f'<a class="button" href="/admin/verify-payment/{obj.id}/" style="background-color: #eab308; color: black; font-weight: bold; padding: 4px 10px; border-radius: 6px; text-decoration: none;">⏳ Pending — Click to Accept</a>')
    verification_action.short_description = "Payment Verification"

    def order_status_action(self, obj):
        status_str = str(obj.status)
        if 'Delivered' in status_str or obj.status is True:
            return mark_safe('<span style="color: #059669; font-weight: bold; background: #ecfdf5; padding: 4px 10px; border-radius: 12px;">🎉 Delivered</span>')
        elif 'Shipped' in status_str:
            return mark_safe(f'<span style="color: #0284c7; font-weight: bold; margin-right: 5px;">🚚 Shipped</span> <a class="button" href="/admin/mark-delivered/{obj.id}/" style="background-color: #10b981; color: white; font-weight: bold; padding: 3px 8px; border-radius: 6px; text-decoration: none;">Mark Delivered</a>')
        else:
            return mark_safe(f'<span style="color: #2563eb; font-weight: bold; margin-right: 5px;">📦 Processing</span> <a class="button" href="/admin/mark-delivered/{obj.id}/" style="background-color: #0284c7; color: white; font-weight: bold; padding: 3px 8px; border-radius: 6px; text-decoration: none;">Mark Delivered</a>')
    order_status_action.short_description = "Order Status"

    def customer_message_note(self, obj):
        if obj.customer_message:
            return mark_safe(f'<div style="background: #fef08a; padding: 4px 8px; border-radius: 6px; font-weight: bold; color: #854d0e; border: 1px solid #fde047;">💬 {obj.customer_message}</div>')
        return "—"
    customer_message_note.short_description = "Customer Alert Message"

    def mark_payment_verified(self, request, queryset):
        rows_updated = queryset.update(payment_status='Verified & Approved')
        self.message_user(request, f"{rows_updated} order(s) successfully marked as Verified & Approved!")
    mark_payment_verified.short_description = "✅ Verify & Approve Selected Payments"

    def mark_order_shipped(self, request, queryset):
        rows_updated = queryset.update(status='Shipped')
        self.message_user(request, f"{rows_updated} order(s) successfully marked as Shipped!")
    mark_order_shipped.short_description = "🚚 Mark Selected Orders as Shipped"

    def mark_order_delivered(self, request, queryset):
        rows_updated = queryset.update(status='Delivered')
        self.message_user(request, f"{rows_updated} order(s) successfully marked as Delivered!")
    mark_order_delivered.short_description = "🎉 Mark Selected Orders as Delivered"


admin.site.register(Products, AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
