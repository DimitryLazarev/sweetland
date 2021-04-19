from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sweetlandapp.views import main_page, specific_product, cart, add_to_cart, products_showcase, order_page, \
    send_mail_sw, adding_prod, cart_clear, prod_clear

urlpatterns = [
    path('', main_page, name='main-page'),
    path('products_showcase/<str:product_type>&<int:product_id>', products_showcase, name='products-showcase'),
    path('specific_product/<int:product_id>', specific_product, name='specific-product'),
    path('cart', cart, name='cart'),
    path('add_to_cart/<int:id>', add_to_cart, name='add-to-cart'),
    path('order_page', order_page, name='order-page'),
    path('send_mail_sw', send_mail_sw, name='send-mail-sw'),
    path('adding/', adding_prod, name='wewe'),
    path('cart_clear', cart_clear, name='cart-clear'),
    path('prod_clear', prod_clear, name='prod-clear')
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
