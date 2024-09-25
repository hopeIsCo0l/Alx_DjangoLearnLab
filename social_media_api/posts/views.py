from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters, response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from notifications.models import Notification
from rest_framework import status
from rest_framework import generics



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 


class UserFeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
       
        following_users = request.user.following.all()

      
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        
       
        return response.Response(serializer.data)




# class LikePostView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#             like, created = Like.objects.get_or_create(user=request.user, post=post)
#             if created:
                
#                 Notification.objects.create(
#                     recipient=post.author, 
#                     actor=request.user,
#                     verb='liked',
#                     target=post
#                 )
#                 return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'message': 'Post already liked.'}, status=status.HTTP_400_BAD_REQUEST)
#         except Post.DoesNotExist:
#             return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

# class UnlikePostView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#             like = Like.objects.filter(user=request.user, post=post)
#             if like.exists():
#                 like.delete()
#                 return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'Post not liked yet.'}, status=status.HTTP_400_BAD_REQUEST)
#         except Post.DoesNotExist:
#             return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)



class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification for the post author
            Notification.objects.create(
                recipient=post.author,  # The author of the post receives the notification
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Post already liked.'}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        
        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Post not liked yet.'}, status=status.HTTP_400_BAD_REQUEST)
