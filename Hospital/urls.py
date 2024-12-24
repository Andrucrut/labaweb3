from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PatientListView, AppointmentListView, PatientPaymentView, MedicalCardListView, \
    DoctorScheduleView, CabinetListView, DoctorViewSet, EmploymentPeriodViewSet, ServicePaymentViewSet, ServicesViewSet, \
    AppointmentsByDoctorAPIView, OtolaryngologistPatientsApiView, DoctorsWithWorkDayAPIView, \
    AppointmentsCountByDateAPIView, TotalTreatmentCostByDayAndDoctorAPIView, PaidPatientsAPIView

router = DefaultRouter()
router.register('patients', PatientListView)
router.register('doctors', DoctorViewSet)
router.register('appointments', AppointmentListView)
router.register('payments', PatientPaymentView)
router.register('medical_cards', MedicalCardListView)
router.register("doctor_schedule", DoctorScheduleView)
router.register('cabinets', CabinetListView)
router.register('employment-periods', EmploymentPeriodViewSet)
router.register('service-payments', ServicePaymentViewSet)
router.register('service', ServicesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('doctors/<int:doctor_id>/appointments/', AppointmentsByDoctorAPIView.as_view(), name="doctor-appointments"),
    path('otolaryngologist-patients/', OtolaryngologistPatientsApiView.as_view(), name='otolaryngologist-patients'),
    path('doctors-with-workday/', DoctorsWithWorkDayAPIView.as_view(), name='doctors-with-workday'),
    path('appointments-count-by-date/', AppointmentsCountByDateAPIView.as_view(), name='appointments-count-by-date'),
    path('total-treatment-cost-by-day-and-doctor/', TotalTreatmentCostByDayAndDoctorAPIView.as_view(), name='total-treatment-cost-by-day-and-doctor'),
    path('paid-patients/', PaidPatientsAPIView.as_view(), name='paid-patients'),
]