from django.contrib import admin
from django.urls import path, include # urls을 따로 관리할 겁니다.
from mystorage import urls
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api-auth/', include('rest_framework.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)