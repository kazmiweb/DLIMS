# license_app/forms.py
from django import forms
from .models import License

class VerifyForm(forms.Form):
    CNIC = forms.CharField(max_length=13)
    License_Number = forms.CharField(max_length=15)

class LicenseFormModel(forms.ModelForm):
    class Meta:
        model = License
        # fields = ['id','CNIC', 'Name', 'Father_Husband_Name', 'City', 'License_Number','Issue_Date','Valid_From','Valid_To','Allowed_Vehicles','Status', 'license_holder_image']
        fields = '__all__'
        widgets = {
        'CNIC': forms.TextInput(attrs={'class': 'only_number', 'placeholder': "CNIC without dashes. e.g., (1111122222223)"}),
        'field_name_2': forms.Select(attrs={'class': 'custom-select', 'placeholder':'Please Enter License Number'}),
    }

    # CNIC = forms.CharField(max_length=13)
    # License_Number = forms.CharField(max_length=20)
    # Father_Husband_Name = forms.CharField(max_length=255)
    # City = forms.CharField(max_length=100)
    # License_Number = forms.CharField(max_length=20)
    # Issue_Date = forms.DateField()
    # Valid_From = forms.DateField()
    # Valid_To = forms.DateField()
    # Allowed_Vehicles = forms.CharField(max_length=255)
    # Status = forms.CharField(max_length=50)


