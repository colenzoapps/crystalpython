
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views
from .views import(
    home,
	registration_view,
)
import crystalp.settings as settings
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('frontend/', include('frontend.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
	path('register_form', registration_view, name="register_form"),

    path('api/statusList/', views.StatusList.as_view(),),
    path('api/priorityList/', views.PriorityList.as_view(),),
    path('api/orderList/', views.OrderList.as_view()),
    path('api/orderList/<int:pk>/', views.OrderDetail.as_view()),
    path('api/departmentList/', views.DepartmentList.as_view()),
    path('api/departmentList/<int:pk>/', views.DepartmentDetail.as_view()),
    path('api/productList/', views.ProductList.as_view()),
    path('api/productList/<int:pk>/', views.ProductDetail.as_view()),
    path('api/customerList/', views.CustomerList.as_view()),
    path('api/customerList/<int:pk>/', views.CustomerDetail.as_view()),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]

admin.site.site_title = "CrystalP"
admin.site.site_header = "CrystalP Administrator"
