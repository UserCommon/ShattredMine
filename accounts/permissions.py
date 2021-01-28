from rest_framework import permissions


class PostOnlyPermissions(permissions.BasePermission):
    permissions = ['PUT', 'POST']

    def has_permission(self, request, view):
        if not request.user.is_staff:
            if request.method in self.permissions: # for POST method the action in DRF is create
                return True
            return False
        else:
            return True

