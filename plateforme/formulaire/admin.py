from django.contrib import admin
from .models import AutoEntrepreneur
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AutoEntrepreneurResource(resources.ModelResource):
    class Meta:
        model = AutoEntrepreneur
       
resources_class = AutoEntrepreneurResource


admin.site.register(AutoEntrepreneur,ImportExportModelAdmin)
