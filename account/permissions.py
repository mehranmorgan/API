from rest_framework.permissions import BasePermission
from .models import BlackList



class UserPermission(BasePermission):
    def has_permission(self, request, view):
        block=BlackList.objects.filter(username=request.user).exists()
        return not block
