from django.urls import path 
from core.views import *

urlpatterns = [
    path('redmi2/', Redmi),
    path('iphone/', Iphone),
    path('samsung/', Samsung),
]
