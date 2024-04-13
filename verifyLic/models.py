from django.db import models

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Verified', 'Verified'),
    ('Canceled', 'Canceled'),
    ('Under Processing', 'Under Processing')
)

class License(models.Model):
    CNIC = models.CharField(max_length=13)
    Name = models.CharField(max_length=100)
    Father_Husband_Name = models.CharField(max_length=255)
    City = models.CharField(max_length=100)
    License_Number = models.CharField(max_length=6)
    Issue_Date = models.DateField()
    Valid_From = models.DateField()
    Valid_To = models.DateField()
    Allowed_Vehicles = models.CharField(max_length=255)
    Status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='pending')
    license_holder_image = models.ImageField(upload_to='images', blank=True, null=True)