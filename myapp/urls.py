from django.urls import path
from . import views
from .views import jwt_login_view

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.register, name="register"),
    # path("login_view", views.login_view, name="login"),
    path('login/', jwt_login_view, name='jwt_login'),

    # Patient section
    path("api/patients/", views.patient_management, name="patient_management"),
    path("api/patients/create/", views.add_patient, name="add_patient"),
    path("api/patients/detail/<int:id>/", views.patient_detail, name="patient_detail"),
    path('api/patients/update/<int:id>/', views.update_patient, name='update_patient'),
    path("api/patients/delete/", views.delete_patient, name="delete_patient"),

    # Doctor section
    path("api/doctors/", views.doctor_management, name="doctor_management"),
    path("api/doctors/create/", views.add_doctor, name="add_doctor"),
    path("api/doctors/detail/<int:id>/", views.doctor_detail, name="doctor_detail"),
    path('api/doctors/update/<int:id>/', views.update_doctor, name='update_doctor'),
    path("api/doctors/delete/", views.delete_doctor, name="delete_doctor"),

    #Mapping section
    path('api/mappings/create/', views.assign_doctor, name='assign_doctor'),
    path('api/mappings/', views.get_all_mappings, name='get_all_mappings'),
    path('api/mappings/<int:mapping_id>/delete/', views.delete_mapping, name='delete_mapping'),

]