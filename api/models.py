from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients', null=True)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Scan(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='scans', on_delete=models.CASCADE)
    scan_file = models.FileField(upload_to='scans/')
