from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, ContactView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',HomeView.as_view(),name='home'),
    path('contact/', ContactView.as_view(),name='contact'),
    path('cart/',include('cart.urls',namespace='cart')),
    path('profile/',ProfileView.as_view(),name='profile'),
    #path('account-login/',),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
