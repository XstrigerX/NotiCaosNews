
from django.contrib import admin
from django.urls import path
from nota3.vista import index

urlpatterns = [
    path('index/', index),
    path('admin/', admin.site.urls),
]
