from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('auth/login')
