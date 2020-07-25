from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from tractebel.models import BusinessLine, ProfitCenter

admin.site.register(BusinessLine)


@admin.register(ProfitCenter)
class ContratoResource(ImportExportModelAdmin):
    pass
