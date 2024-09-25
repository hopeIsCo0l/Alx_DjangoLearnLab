from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status, generics
from .models import CustomUser

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class FollowUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         user_to_follow = get_object_or_404(CustomUser, id = user_id)
#         if user_to_follow == request.user:
#             return Response({"detail": "You can not follow your self."}, status=status.HTTP_400_BAD_REQUEST)
        
#         request.user.following.add(user_to_follow)
#         return Response({"detail": "Successfully Followed."}, status=status.HTTP_200_OK)

# class UnFollowUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         user_to_unfollow = get_object_or_404(CustomUser, id = user_id)
#         if user_to_unfollow == request.user:
#             return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

#         request.user.following.remove(user_to_unfollow)
#         return Response({"detail": "Successfully unFollowed."}, status=status.HTTP_200_OK)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
           
            user_to_follow = CustomUser.objects.get(id=user_id)

            request.user.following.add(user_to_follow)
            return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            # The user to unfollow
            user_to_unfollow = CustomUser.objects.get(id=user_id)

            # Remove the user from the following list
            request.user.following.remove(user_to_unfollow)
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)