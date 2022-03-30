from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home_view, redirect_url_view

appname = "shortener"

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)