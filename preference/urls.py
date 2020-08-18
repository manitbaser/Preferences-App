from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('article/', include('article.urls')),
    path('preferences/', include('preferences.urls')),
]
