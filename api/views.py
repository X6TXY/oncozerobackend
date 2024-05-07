from rest_framework import  viewsets


from api.models import Patient, Scan
from api.serializers import  PatientSerializer, ScanSerializer
from api.permissions import IsOwnerOrAdmin
from rest_framework.exceptions import PermissionDenied


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Patient.objects.all()  
        return Patient.objects.filter(user=self.request.user)  

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")
        serializer.save(user=self.request.user)


class ScanViewSet(viewsets.ModelViewSet):
    serializer_class = ScanSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Scan.objects.all() 
        return Scan.objects.filter(patient__user=self.request.user)  

    def perform_create(self, serializer):
        patient = serializer.validated_data.get('patient')
        if not self.request.user.is_staff and patient.user != self.request.user:
            raise PermissionDenied("You do not have permission to add scans for this patient.")
        serializer.save()
