from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import CustomUser, Patient, Doctor, PatientDoctorMapping
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.create_user(username=email, email=email, password=password, name=name)
        user.save()
        return redirect('login')

    return render(request, 'register.html')

def jwt_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Send POST request to /api/auth/login/ for JWT
        response = requests.post(
            request.build_absolute_uri('/api/auth/login/'),
            json={'username': email, 'password': password}
        )

        if response.status_code == 200:
            tokens = response.json()
            access = tokens.get('access')
            refresh = tokens.get('refresh')

            # Store in session (optional)
            request.session['access_token'] = access
            request.session['refresh_token'] = refresh

            return redirect('index')  # or wherever you want

        else:
            error = response.json().get('detail', 'Invalid credentials')
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

# def login_view(request): 
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = CustomUser.objects.get(email=email)
#         except CustomUser.DoesNotExist:
#             error = "User not registered. Please sign up first."
#             return render(request, 'login.html', {'error': error})

#         user = authenticate(request, username=user.username, password=password)

#         if user is not None:
#             auth_login(request, user)  
#             return redirect('index')
#         else:
#             error = "Invalid email or password"
#             return render(request, 'login.html', {'error': error})
        
# Patient view's----------------------------------------------------------------        

    return render(request, 'login.html')

def patient_management(request):
    
    patients = Patient.objects.all()
    return render(request, 'patient/patient_management.html', {
        'patients': patients,
    })

def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        blood_group = request.POST.get('blood_group')
        allergies = request.POST.get('allergies')

        created_by = request.user

        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            phone_number=phone_number,
            blood_group=blood_group,
            allergies=allergies,
            created_by=created_by
        )
        messages.success(request, 'Patient added successfully.')
        return redirect('patient_management')

    return render(request, 'patient/add_patient.html')

def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, "patient/patient_detail.html", {"patient": patient})

def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.name = request.POST.get("name")
        patient.age = request.POST.get("age")
        patient.gender = request.POST.get("gender")
        patient.phone_number = request.POST.get("phone_number")
        patient.blood_group = request.POST.get("blood_group")
        patient.allergies = request.POST.get("allergies")
        patient.save()
        return redirect("patient_management")
    return render(request, "patient/update_patient.html", {"patient": patient})

def delete_patient(request):
    if request.method == "POST":
        patient_id = request.POST.get("id")
        patient = get_object_or_404(Patient, id=patient_id)
        patient.delete()
    return redirect("patient_management")

# Doctor view's----------------------------------------------------------------

def doctor_management(request):
    
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_management.html', {
        'doctor': doctors,
    })

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        specialization = request.POST.get('specialization')
        consultation_fee = request.POST.get('consultation_fee')

        created_by = request.user

        Doctor.objects.create(
            name=name,
            gender=gender,
            phone_number=phone_number,
            specialization=specialization,
            consultation_fee=consultation_fee,
            created_by=created_by
        )
        messages.success(request, 'Doctor added successfully.')
        return redirect('doctor_management')

    return render(request, 'doctor/add_doctor.html')

def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, "doctor/doctor_details.html", {"doctor": doctor})

def update_doctor(request, id):
    doctor_obj = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor_obj.name = request.POST.get("name")
        doctor_obj.gender = request.POST.get("gender")
        doctor_obj.phone_number = request.POST.get("phone_number")
        doctor_obj.blood_group = request.POST.get("specialization")
        doctor_obj.allergies = request.POST.get("consultation_fee")
        doctor_obj.specialization = request.POST.get("specialization")
        doctor_obj.save()
        return redirect("doctor_management")
    return render(request, "doctor/update_doctor.html", {"doctor": doctor_obj})

def delete_doctor(request):
    if request.method == "POST":
        doctor_id = request.POST.get("id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        doctor.delete()
    return redirect("doctor_management")

# Mapping view's ------------------------------------------------------------------------------------
from django.contrib import messages

def assign_doctor(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        doctor_name = request.POST.get("doctor_name")

        if not patient_name or not doctor_name:
            messages.error(request, "Both Patient name and Doctor name are required.")
        else:
            try:
                patient = Patient.objects.get(name=patient_name)
                doctor = Doctor.objects.get(name=doctor_name)
                PatientDoctorMapping.objects.create(patient=patient, doctor=doctor)
                return redirect('get_all_mappings')  # Redirect to your all mappings page
            except Patient.DoesNotExist:
                messages.error(request, "Patient not found.")
            except Doctor.DoesNotExist:
                messages.error(request, "Doctor not found.")

    return render(request, "mapping/assign_mapping.html", {"patients": patients, "doctors": doctors})


def get_all_mappings(request):
    # Renders list of all mappings in all_mappings.html
    mappings = PatientDoctorMapping.objects.select_related("patient", "doctor").all()
    return render(request, "mapping/all_mappings.html", {"mappings": mappings})


def delete_mapping(request, mapping_id):
    mapping = get_object_or_404(PatientDoctorMapping, id=mapping_id)
    mapping.delete()
    return redirect('get_all_mappings')
