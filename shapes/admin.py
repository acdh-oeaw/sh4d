from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import TangibleObject, Bricks


class BricksAdmin(LeafletGeoAdmin):
    list_display = (
        'excavation',
        'stratum_id',
        'phase_id',
        'brick_type',
        'brick_mate',
    )
    list_filter = [
        'excavation',
        'phase_id',
        'stratum_id',
    ]
    search_fields = [
        'phase_id',
        'find_type',
    ]


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
admin.site.register(Bricks, BricksAdmin)
