from rest_framework.request import Request
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):

    def has_permission(self, request: Request, view):
        return request.user and request.user.is_superuser


class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request: Request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_staff


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request: Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.is_superuser
            or request.user == obj.author
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request: Request, view):
        if (
            request.method in SAFE_METHODS
            and request.user.is_authenticated
            and request.user.is_staff
        ):
            return True
        return request.user.is_superuser
