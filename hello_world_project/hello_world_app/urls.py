# hello_world_app/urls.py
#api paths
from django.urls import path
from .views import HelloWorldView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Define a URL pattern for the HelloWorldView
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    # ... your existing URL patterns
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
