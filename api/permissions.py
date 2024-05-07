from rest_framework import permissions
from api.models import Patient,Scan

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request user is an admin
        if request.user.is_staff:
            return True


        if isinstance(obj, Patient):
            owner = obj.user
        elif isinstance(obj, Scan):
            owner = obj.patient.user  
        else:
            return False  


        return owner == request.user
