from rest_framework import permissions


class HasExpiringLinkPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.tier.allow_expiring_link
