from rest_framework import permissions

from ads.models import Ad
from users.models import User


class AdChangePermission(permissions.BasePermission):#TODO
    message = "Changing ad can only admins or user who create the ad"
    def has_permission(self, request, view):
        if request.user.role in [User.ADMIN, User.MODERATOR]:
            return True
        entity = Ad.objects.get(pk=view.kwargs["pk"])
        if entity.author_id == request.user.id:
            return True
        return False