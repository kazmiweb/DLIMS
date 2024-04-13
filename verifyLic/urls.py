# license_app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('verify/save/', views.save_license, name='save_license'),
    path('verify/', views.verify_license, name='verify_license'),
    # path('result/', views.verification_done, name='verification_done'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

