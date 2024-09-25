# notifications/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification

class UserNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all().order_by('-timestamp')
        data = [
            {
                'actor': str(notification.actor),
                'verb': notification.verb,
                'target': str(notification.target),
                'timestamp': notification.timestamp,
                'read': notification.read
            }
            for notification in notifications
        ]
        return Response(data)
