from rest_framework.permissions import BasePermission


class StaffOnly(BasePermission):

    def has_permission(self, request, view):
        result = request.user.is_authenticated and request.user.is_staff
        return result # and request.user.name == 'moderator'