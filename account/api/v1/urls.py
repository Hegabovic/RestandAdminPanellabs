from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from account.api.v1.views import sign_up

urlpatterns = [
    path('authenticate', ObtainAuthToken.as_view(), name='login'),
    path('signup', sign_up, name='sign_up')
]
