from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/token/', obtain_auth_token, name='api_token_auth'),
    path('books/', BookList.as_view(), name='book-list'),

]
