from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('friend-request/', FriendRequestAPIView.as_view(), name='friend-request'),
    path('friend-request/<int:friend_id>/', FriendActionAPIView.as_view(), name='friend-request-action'),
    path('friends/', FriendAPIView.as_view(), name='friend-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # авторизация по токену
]
