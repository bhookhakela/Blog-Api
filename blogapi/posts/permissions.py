from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: # If the request method is safe, then
            return True
        return request.user.is_authenticated    # Only the author can make unsafe requests to the post
    def has_object_permission(self, request, view, obj):
        # print('hello')
        print(request.user)
        if request.user.is_anonymous: # If the user is not authenticated, then
            return False
        if request.method in SAFE_METHODS: # If the request method is safe, then return True
            return True
        return obj.author==request.user # Only the author can make a change to the post
