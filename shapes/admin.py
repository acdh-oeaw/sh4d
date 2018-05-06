from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import TangibleObject


class TangibleObjectAdmin(LeafletGeoAdmin):
    list_display = (
        'orea_gis_i',
        'excavation',
        'planum_gis',
        'archaeolog',
    )
    list_filter = [
        'excavation',
        'planum_gis',
        'stratum_gi',
    ]
    search_fields = [
        'phase_id',
        'find_type',
    ]


admin.site.register(TangibleObject, TangibleObjectAdmin)
