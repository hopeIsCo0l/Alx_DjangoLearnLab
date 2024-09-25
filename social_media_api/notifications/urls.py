from django.urls import path
from .views import UserNotificationView

urlpatterns = [
    path('notifications/', UserNotificationView.as_view(), name='user-notifications'),
]
