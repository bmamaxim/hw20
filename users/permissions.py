from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Класс прав доступа модераторов.
    """
    massage = 'moderatos only'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsAdmin(permissions.BasePermission):
    """
    Класс прав доступа администратора.
    """
    massage = 'admin only'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()


class IsOwner(permissions.BasePermission):
    """
    Класс пермишон прав доступа для объектов.
    """

    def has_object_permission(self, request, view, obj):

        if obj.owner == request.user:
            return True
        return False
