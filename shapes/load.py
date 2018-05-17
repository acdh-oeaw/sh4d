import os
from django.contrib.gis.utils import LayerMapping
from .models import TangibleObject, Bricks


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

bricks_shps = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shp_EPSG4326', 'orig', 'TD_FI_j21_Bricks.shp',)
)


def import_bricks(verbose=True):
    lm = LayerMapping(
        Bricks, bricks_shps, bricks_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)


tangibleobject_mapping = {
    'orea_gis_i': 'OREA_GIS_i',
    'excavation': 'Excavation',
    'planum_gis': 'Planum_GIS',
    'stratum_gi': 'Stratum_GI',
    'stratum_id': 'Stratum_ID',
    'phase_id': 'Phase_ID',
    'locus_wall': 'Locus_wall',
    'archaeolog': 'Archaeolog',
    'archaeol_1': 'Archaeol_1',
    'archaeol_2': 'Archaeol_2',
    'orientatio': 'Orientatio',
    'brick_mate': 'Brick_mate',
    'wall_brick': 'Wall_brick',
    'height_top': 'Height_top',
    'height_t_1': 'Height_t_1',
    'height_bot': 'Height_bot',
    'height_b_1': 'Height_b_1',
    'wall_cours': 'Wall_cours',
    'wall_conne': 'Wall_conne',
    'wall_funct': 'Wall_funct',
    'gis_commen': 'GIS_commen',
    'extrusion': 'Extrusion',
    'base_heigh': 'Base_heigh',
    'resources_field': 'Resources_',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'shape_clas': 'Shape_clas',
    'archaeol_3': 'Archaeol_3',
    'pit_find_g': 'Pit_find_G',
    'eigner_map': 'Eigner_map',
    'brick_type': 'Brick_type',
    'height_max': 'Height_max',
    'add_phase_field': 'Add_phase_',
    'add_phase1': 'Add_phase1',
    'find_mater': 'Find_mater',
    'find_type': 'Find_type',
    'height': 'Height',
    'find_gis_c': 'Find_GIS_c',
    'find_local': 'Find_local',
    'find_inven': 'Find_inven',
    'phase_gis_field': 'Phase_GIS_',
    'locus_id': 'Locus_ID',
    'geom': 'MULTIPOLYGON',
}

tangible_object_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shp_EPSG4326', 'tangible_things.shp',)
)


def import_tangible_object(verbose=True):
    lm = LayerMapping(
        TangibleObject, tangible_object_shp, tangibleobject_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)
