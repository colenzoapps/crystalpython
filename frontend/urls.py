from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf.urls import include, url
from rest_framework import routers, serializers, viewsets

app_name = 'frontend'

router = routers.DefaultRouter()
#router.register(r'branch', views.BranchViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    # path('device/', views.device_list),
    # path('device/<int:pk>', views.device_details),
    # path('device_page/', views.device_page, name='device_page'),
    # path('clients/', views.clients, name='clients'),
    # path('clientList/', views.ClientList.as_view(),),
    # path('clientList/<int:pk>/', views.ClientDetail.as_view()),
    # path('appointments/', views.appointments, name='appointments'),
    # path('appointmentList/', views.AppointmentList.as_view(),),
    # path('appointmentList/<int:pk>/', views.AppointmentDetail.as_view()),

    # path('branchList/', views.BranchList.as_view()),
    # path('careplanList/', views.CarePlanList.as_view()),
    # path('careproviderList/', views.CareProviderList.as_view()),
    # path('statusList/', views.StatusList.as_view()),
]
