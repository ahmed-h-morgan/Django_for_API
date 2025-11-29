from rest_framework import permissions

# all permissions are inherited from permissions.BasePermission as below 

# class BasePermission(object): 
#     """ A base class from which all permission classes should inherit. """ 
    
#     def has_permission(self, request, view): 
#         """ Return `True` if permission is granted, `False` otherwise. """ 
#         return True 
    
#     def has_object_permission(self, request, view, obj): 
#         """ Return `True` if permission is granted, `False` otherwise."""
#         return True

class IsAuthorOrReadOnly(permissions.BasePermission): 
    
    def has_permission(self, request, view):
        # Authenticated users only can see list view 
        if request.user.is_authenticated: 
            return True 
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
    