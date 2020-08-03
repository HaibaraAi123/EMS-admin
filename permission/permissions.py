from rest_framework.permissions import BasePermission


class ModelPermission(BasePermission):
    massage = "权限验证失败，没有对应权限"
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            print("notaa")
            return False
        if user.is_superuser:
            print("ssssss")
            return True
        if hasattr(view,'get_model_perms_conf'):
            perms = view.get_model_perms_conf()
            print(111111)
        else:
            print(222222)
            perms = ()
        return user.has_perms(perms)







