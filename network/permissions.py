from rest_framework import permissions


class IsActiveUserPermission(permissions.BasePermission):
    """
    Право доступа, которое разрешает доступ только активным пользователям.
    """
    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        if request.user.is_authenticated:
            # Проверяем, что пользователь активен
            return request.user.is_active
        return False
