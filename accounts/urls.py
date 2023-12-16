from django.urls import path
from accounts.views import RegisterView, VerifyOTP, LoginView, UserView, LogoutView, LoginRefreshView, UserViewApi


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('verify_code/', VerifyOTP.as_view()),
    path('login/', LoginView.as_view()),
    path('login/refresh/', LoginRefreshView.as_view()),
    path('user_profile/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('accounts/', UserViewApi.as_view())
]
