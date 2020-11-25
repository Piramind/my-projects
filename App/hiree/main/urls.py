from django.urls import path
from . import vievs
urlpatterns = [
    path('', vievs.index)]