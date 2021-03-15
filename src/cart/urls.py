from django.urls import path
from .views import( 
    ProductListView, 
    ProductDetailView, 
    CartView, 
    IncreaseQuantityView, 
    DecreaseQuantityView,
    RemoveFromCartView,
    CheckoutView,
    PaymentView,
    ThankYouView,
    ConfirmOrderView,
    OrderDetailView
)

app_name = 'cart'

urlpatterns = [
    path('',CartView.as_view(),name = 'summary'),
    path('shop/',ProductListView.as_view(),name = 'product-list'),
    path('shop/<slug>/', ProductDetailView.as_view(), name = 'product-detail'),
    path('increase-quantity/<pk>/', IncreaseQuantityView.as_view(),name='increase-quantity'),
    path('decrease-quantity/<pk>/', DecreaseQuantityView.as_view(),name='decrease-quantity'),
    path('remove-from-cart/<pk>/',RemoveFromCartView.as_view(),name = 'remove-from-cart'),
    path('checkout/', CheckoutView.as_view(),name='checkout'),
    path('payment/',PaymentView.as_view(),name='payment'),
    path('thank-you/',ThankYouView.as_view(),name='thank-you'),
    path('confirm-order/',ConfirmOrderView.as_view(),name='confirm-order'),
    path('orders/<pk>/',OrderDetailView.as_view(),name = 'order-detail')
]
