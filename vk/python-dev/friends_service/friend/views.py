from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth import authenticate
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from serializers import *

class Registration(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        serializer = UserSerializer(user)

        return Response(serializer.data)

class FriendRequestAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]  # авторизация по токену
    permission_classes = [permissions.IsAuthenticated]  # требуется авторизация

    def post(self, request, format=None):
        from_user = request.user
        to_user_id = request.data.get('to_user_id')

        if from_user.id == to_user_id:
            return Response({'error': 'You cannot send a friend request to yourself.'})

        to_user = User.objects.get(id=to_user_id)

        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists() or \
                FriendRequest.objects.filter(from_user=to_user, to_user=from_user).exists():
            return Response({'error': 'Friend request already exists.'})

        friend_request = FriendRequest(from_user=from_user, to_user=to_user)
        friend_request.save()

        return Response({'status': 'Friend request has been sent successfully.'})

    def get(self, request, format=None):
        user = request.user
        incoming_requests = FriendRequest.objects.filter(to_user=user)
        outgoing_requests = FriendRequest.objects.filter(from_user=user)

        incoming_serializer = FriendRequestSerializer(incoming_requests, many=True)
        outgoing_serializer = FriendRequestSerializer(outgoing_requests, many=True)

        data = {
            'incoming_requests': incoming_serializer.data,

'outgoing_requests': outgoing_serializer.data
        }
        return Response(data)

class FriendActionAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, friend_id, format=None):
        user = request.user
        friend = User.objects.get(id=friend_id)

        if friend == user:
            return Response({'status': 'You cannot be friend with yourself.'})
        if Friend.objects.filter(Q(user=user, friend=friend) | Q(user=friend, friend=user)).exists():
            return Response({'status': 'You are already friend.'})
        if FriendRequest.objects.filter(from_user=user, to_user=friend).exists():
            return Response({'status': 'Friend request has been already sent from you.'})
        if FriendRequest.objects.filter(from_user=friend, to_user=user).exists():
            return Response({'status': 'You have received friend request, please accept it.'})
        return Response({'status': 'You are not friend yet.'})

    def post(self, request, friend_id, format=None):
        user = request.user
        friend = User.objects.get(id=friend_id)

        if friend == user:
            return Response({'status': 'You cannot be friend with yourself.'})
        if Friend.objects.filter(Q(user=user, friend=friend) | Q(user=friend, friend=user)).exists():
            return Response({'status': 'You are already friend.'})
        if FriendRequest.objects.filter(from_user=user, to_user=friend).exists():
            return Response({'status': 'Friend request has been already sent from you.'})
        if FriendRequest.objects.filter(from_user=friend, to_user=user).exists():
            # Принимаем входящую заявку и добавляем друга
            Friend.objects.create(user=user, friend=friend)
            Friend.objects.create(user=friend, friend=user)
            FriendRequest.objects.filter(from_user=friend, to_user=user).delete()
            FriendRequest.objects.filter(from_user=user, to_user=friend).delete()
            return Response({'status': 'Friends request has been accepted successfully.'})

        friend_request = FriendRequest(from_user=user, to_user=friend)
        friend_request.save()

        return Response({'status': 'Friend request has been sent successfully.'})

    def delete(self, request, friend_id, format=None):
        user = request.user
        friend = User.objects.get(id=friend_id)

        if not Friend.objects.filter(user=user, friend=friend).exists():
            return Response({'status': 'You are not friend yet.'})

        Friend.objects.filter(user=user, friend=friend).delete()
        Friend.objects.filter(user=friend, friend=user).delete()

        return Response({'status': 'Friends request has been deleted successfully.'})

class FriendAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        friends = Friend.objects.filter(user=user)

        serializer = FriendSerializer(friends, many=True)

        return Response(serializer.data)
