from rest_framework import permissions

from ads.models import Ad, Selection
from users.models import User


class AdChangePermission(permissions.BasePermission):
    message = "Changing ad can only admins or user who create the ad"

    def has_permission(self, request, view):
        if request.user.role in [User.ADMIN, User.MODERATOR]:
            return True
        entity = Ad.objects.get(pk=view.kwargs["pk"])
        if entity.author_id == request.user.id:
            return True
        return False


class SelectionChangePermission(permissions.BasePermission):
    message = "Change selection can only user who created selection"

    def has_permission(self, request, view):
        entity = Selection.objects.get(pk=view.kwargs['pk'])
        print(entity)
        if entity.owner_id == request.user.id:
            return True
        return False
