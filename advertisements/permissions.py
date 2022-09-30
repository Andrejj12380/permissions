from rest_framework import permissions

from advertisements.models import Advertisement


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        print(request.user, obj.creator)
        return  request.user == obj.creator