from django.contrib.auth.models import update_last_login
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import User

from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',  'username', 'email', 'password', 'is_verified')


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.CharField()
    otp = serializers.CharField()



class LoginRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        access_token_instance = AccessToken(data['access'])
        user_id = access_token_instance['user_id']
        user = get_object_or_404(User, id=user_id)
        update_last_login(None, user)
        return data


