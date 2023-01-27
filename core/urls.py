from django.urls import path

from core.views import first

urlpatterns = [
    path('', first)
]
