# license_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import License
from .forms import LicenseFormModel, VerifyForm

def save_license(request):
    if request.method=='POST':
        form = LicenseFormModel(request.POST, request.FILES)
        if form.is_valid():
            # Save the license data to the database
            license = License.objects.create(
                CNIC=form.cleaned_data['CNIC'],
                Name = form.cleaned_data['Name'],
                Father_Husband_Name = form.cleaned_data['Father_Husband_Name'],
                City = form.cleaned_data['City'],
                License_Number=form.cleaned_data['License_Number'],
                Issue_Date = form.cleaned_data['Issue_Date'],
                Valid_From = form.cleaned_data['Valid_From'],
                Valid_To = form.cleaned_data['Valid_To'],
                Allowed_Vehicles = form.cleaned_data['Allowed_Vehicles'],
                Status = form.cleaned_data['Status'],
            )
            license.save()
            # return render(request, 'success.html', {'license': license})
            form = LicenseFormModel()
    else:
        form = LicenseFormModel()
    return render(request, 'save_license.html', {'form': form})

def verify_license(request):
    if request.method=='POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            cnic = form.cleaned_data['CNIC']
            license_number = form.cleaned_data['License_Number']
            # license = get_object_or_404(License, CNIC=cnic, License_Number=license_number)
            license = License.objects.filter(CNIC=cnic)
            anchor = './anchor.html'
            saved_resource = './saved_resource.html'
            return render(request, 'DLIMS.html', {'license': license, 'form': form, 'anchor':anchor, 'saved_resource':saved_resource})
    else:
        form = VerifyForm()
    return render(request, 'DLIMS.html', {'form': form})


# def verification_done(request):
#     id = License.objects.get(pk=id)
#     return render(request, 'result.html', {'person':id})