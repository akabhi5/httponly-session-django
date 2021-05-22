from django.urls import path
from cookieapp.views import login_view, get_csrf_token


urlpatterns = [
    path('login/', login_view),
    path('csrf/', get_csrf_token),
]