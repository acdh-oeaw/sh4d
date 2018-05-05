import os
from django.contrib.gis.utils import LayerMapping
from .models import *


bricks_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shp_EPSG4326', 'TD_FI_j21_Bricks.shp'),
)


def import_bricks(verbose=True):
    lm = LayerMapping(
        Brick, bricks_shp, brick_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)
