# hello_world_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse
from rest_framework import status

class HelloWorldView(APIView):
    print("inside class")
    # Use TokenAuthentication for authentication
    authentication_classes = [TokenAuthentication]
    # Require users to be authenticated to access this view
    print("befor permission")
    permission_classes = [IsAuthenticated]
    print("after permission")
     
    

    def get(self, request):
        print("in get")
         # Print the user information for debugging
        print("User:", request.user)

         # Check if the user is authenticated
        if request.user.is_authenticated:
            # Print the user information
            print("User:", request.user," is authenticated")
       
            try:
                print("inside try")
            # Try to retrieve the user's profile information
                user_profile = UserProfile.objects.get(user=request.user)
                print("user:-",user_profile)
             # Serialize the user profile data
                serializer = UserProfileSerializer(user_profile)
            
            # Compose the response message
                content = {
            'message': f'Hello, {request.user.username}!',
            'latitude': serializer.data['latitude'],
            'longitude': serializer.data['longitude'],
            }
                return Response(content)
        
            except UserProfile.DoesNotExist as e:
    # If the UserProfile doesn't exist, print the exception message
                print(f"UserProfile.DoesNotExist: {str(e)}")
                return Response({'error': 'User profile not found'}, status=404)
    
        else:
            # If the user is not authenticated, return a 401 response
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


    

        

        
