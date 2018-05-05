from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *


class BrickAdmin(LeafletGeoAdmin):
    list_display = (
        'id',
        'excavation',
        'stratum_id',
        'phase_id',
        'archaeolog',
        'archaeol_1',
        'brick_type'
    )
    list_filter = [
        'brick_type',
        'stratum_id',
        'archaeolog',
    ]
    search_fields = [
        'archaeol_1',
        'resources_field'
    ]


admin.site.register(Brick, BrickAdmin)
