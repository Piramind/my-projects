from django.urls import path
from main import views
urlpatterns = [
    path('', views.index),
    #path('myaction/', MyAction.as_view(), name='my-action')
    ]