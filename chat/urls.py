from django.urls import path, include
from chat import views as chat_views

from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path("", chat_views.chatPage, name = "chat-page"),
    path("auth/login", LoginView.as_view (template_name = "chat/LoginPage.html"), name = "login-user"),
    path("/logout", chat_views.UserLogoutView.as_view (http_method_names = ['get', 'post', 'options']), name = "logout-user" )
]