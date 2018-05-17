# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Bricks(models.Model):
    excavation = models.CharField(max_length=254)
    stratum_id = models.CharField(max_length=254)
    phase_id = models.CharField(max_length=254)
    archaeolog = models.CharField(max_length=254)
    archaeol_1 = models.CharField(max_length=254)
    brick_type = models.CharField(max_length=254)
    brick_mate = models.CharField(max_length=254)
    height_max = models.FloatField()
    extrusion = models.FloatField()
    base_heigh = models.FloatField()
    orientatio = models.CharField(max_length=254)
    resources_field = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    orea_gis_i = models.CharField(max_length=50)
    archaeol_2 = models.CharField(max_length=100)
    add_phase_field = models.CharField(max_length=50)
    add_phase1 = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for Bricks model
bricks_mapping = {
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'phase_id': 'Phase_ID',
    'archaeolog': 'Archaeolog',
    'archaeol_1': 'Archaeol_1',
    'brick_type': 'Brick_type',
    'brick_mate': 'Brick_mate',
    'height_max': 'Height_max',
    'extrusion': 'Extrusion',
    'base_heigh': 'Base_heigh',
    'orientatio': 'Orientatio',
    'resources_field': 'Resources_',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'orea_gis_i': 'OREA_GIS_I',
    'archaeol_2': 'Archaeol_2',
    'add_phase_field': 'Add_phase_',
    'add_phase1': 'Add_phase1',
    'geom': 'MULTIPOLYGON',
}
