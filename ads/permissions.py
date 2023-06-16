from rest_framework import permissions

from users.models import User


class AdChangePermission(permissions.BasePermission):
    message = "Changing ad can only admins or user who create the ad"
    def has_permission(self, request, view):
        if request.user.role in [User.ADMIN, User.MODERATOR] or request.body.author == request.user.id:
            return True
        return False