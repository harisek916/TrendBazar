from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from api import views






urlpatterns=[
    path("register/",views.SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
]