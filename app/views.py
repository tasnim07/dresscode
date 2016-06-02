# Third party import
import requests

# Django Import
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect

# App import
from dresscode import settings


def facebook_login(request):
    url = 'https://graph.facebook.com/oauth/'
    user = User.objects.get(username=request.user.username)
    social = user.social_auth.get(provider='facebook')
    # social.extra_data['access_token']
    response = requests.get(
        url,
        params={
            'access_token': social.extra_data['access_token'],
            'redirect_uri': 'http://localhost:8000/app/callback',
            'client_id': settings.SOCIAL_AUTH_FACEBOOK_KEY,
            'client_secret': settings.SOCIAL_AUTH_FACEBOOK_SECRET,
            'grant_type': 'client_credentials'})

    response.raise_for_status()
    return HttpResponse(response.content)


def post_auth_callback(request):
    return HttpResponse("Authenticated")


def facebook_logout(request):
    logout(request)
    return HttpResponse("Successfull logged out")


def user_login(request):
    return render(request, 'app/login.html')


def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('http://youtube.com')
    else:
        return HttpResponse("Could not Authenticate")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user_login/")
    else:
        form = UserCreationForm()
    return render(request, "app/register.html", {
        'form': form,
    })

# # Authenticate users using Google OAuth2
# def authenticate(request):
#     # Callback URL based on HTTP Referer
#     http_referer = request.META.get('HTTP_REFERER', DEFAULT_CALLBACK)
#     request.session['callback'] = http_referer
#     # logout from any existing sessions
#     user = None
#     logout(request)
#     # login method
#     method = request.GET.get('method', 'login')
#     request.session['method'] = method
#     # logging in users token
#     token = request.GET.get('token')
#     if method in ASSOC_METHODS:
#         if not token:
#             return redirect(http_referer)
#         user = get_auth_user(token)
#         if not user:
#             return redirect(http_referer)
#         request.session['user_id'] = user.id
#     callback = reverse('youtube:callback')
#     login_url = reverse('social:begin', args=('google-oauth2', ))
#     login_url += '?next={}&method={}'.format(callback, method)
#     if user:
#         login_url += '&user={}'.format(user.id)
#     return redirect(login_url)
