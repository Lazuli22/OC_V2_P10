from rest_framework import permissions


class IsOwnerOrContributor(permissions.BasePermission):
    """
    Custom permissions to only allow owners or contributors of an project.
    """

    def has_permission(self, request, view):
        if request.user:
            return request.user.is_authenticated
