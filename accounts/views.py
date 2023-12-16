import os
from django.http import HttpResponsePermanentRedirect
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from .emails import *
import jwt, datetime
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.generics import ListAPIView
from rest_framework import generics
from accounts.models import User
class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class UserViewApi(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.User.objects.all()

class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response(
                    {
                        "status": 200,
                        "massage": "Registration successfully. Check your email",
                        "data": serializer.data
                    }
                )

            return Response(
                {
                    "status": 400,
                    "massage": "Somthing went wrong",
                    "data": serializer.errors
                }
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Something went wrong"
                }
            )


class VerifyOTP(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            "status": 400,
                            "massage": "Somthing went wrong",
                            "data": "invalid email"
                        }
                    )
                if not user[0].otp == otp:
                    return Response(
                        {
                            "status": 400,
                            "massage": "Somthing went wrong",
                            "data": "wrong otp"
                        }
                    )
                user = user.first()
                user.is_verified = True
                user.save()

                return Response(
                    {
                        "status": 200,
                        "massage": "Accound verified",
                        "data": {}
                    }
                )

            return Response(
                {
                    "status": 400,
                    "massage": "Something went wrong",
                    "data": serializer.errors
                }
            )


        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Something went wrong"
                }
            )


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            AuthenticationFailed('Incorrect password')

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
                "jwt": token
            }
        return response


class LoginRefreshView(TokenRefreshView):
    serializer_class = LoginRefreshSerializer


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "massage": "You successfully logged out"
        }
        return response

