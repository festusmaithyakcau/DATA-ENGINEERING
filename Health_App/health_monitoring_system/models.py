from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    # You can add more patient information fields here

    # Optional fields for storing recent ECG data and statistics
    # (These ones adapt based on your data structure)
    last_ecg_data = models.TextField(blank=True, null=True)  # Store raw ECG data as text
    heart_rate = models.FloatField(blank=True, null=True)
    # You can also add other ECG statistics here

    def __str__(self):
        return self.name