from rest_framework import permissions

class BlocklistPermissions(permissions.BasePermission):
    BLOCKED_IPS=['127.0.0.2']

    def has_permission(self, request, view):
        ip_addr=request.META.get('REMOTE_ADDR')
        return ip_addr not in self.BLOCKED_IPS
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner==request.user