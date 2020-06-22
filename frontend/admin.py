from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from .models import *


class AccountAdmin(UserAdmin):
	list_display = ('pk', 'email','username',
                    'date_joined', 
                    'last_login',
                    'is_staff')
	search_fields = ('pk', 'email','username',)
	readonly_fields=('pk', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class OrganisationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'address', 'city', 'postcode',)
    search_fields = ['name', 'postcode', ]
    can_delete = False
    verbose_name_plural = 'Organisation'


class BranchAdmin(ImportExportModelAdmin):
    list_display = ('name', 'code', 'address', 'city', 'postcode',)
    list_select_related = ('organisation', )
    verbose_name_plural = 'Branches'



class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id','name','department',)
    # exclude = ['createdOn', 'createdBy','lastEditOn','lastEditBy']
    search_fields = ['name', ]


class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id','subject','qty','start_date','due_date','status')
    # exclude = ['createdOn', 'createdBy','lastEditOn','lastEditBy']
    search_fields = ['id','status' ]


class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('id','name','address','postcode', 'phone',)
    # exclude = ['createdOn', 'createdBy','lastEditOn','lastEditBy']
    search_fields = ['name', 'location', ]


class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('id','name',)


class StatusAdmin(ImportExportModelAdmin):
    list_display = ('id','name',)


class PriorityAdmin(ImportExportModelAdmin):
    list_display = ('id','name',)


# admin.site.unregister(User)
admin.site.register(User, AccountAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Priority, PriorityAdmin)

