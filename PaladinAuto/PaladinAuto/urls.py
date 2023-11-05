
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
]

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Paladin Auto'