from django.contrib import admin
from .models import License
# Register your models here.

@admin.register(License)
class Verify_License_Admin(admin.ModelAdmin):
    list_display = ['id','CNIC', 'Name', 'Father_Husband_Name', 'City', 'License_Number', 'Issue_Date', 'Valid_From', 'Valid_To', 'Allowed_Vehicles','Status', 'license_holder_image']

    # , 'license_holder_image'