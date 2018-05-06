from django.contrib.gis.db import models


class TangibleObject(models.Model):

    """ merge of polygons describing tangible objects """

    orea_gis_i = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    excavation = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    planum_gis = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    stratum_gi = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    stratum_id = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    phase_id = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    locus_wall = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    archaeolog = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    archaeol_1 = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    archaeol_2 = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    orientatio = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    brick_mate = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    wall_brick = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    height_top = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    height_t_1 = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    height_bot = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    height_b_1 = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    wall_cours = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    wall_conne = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    wall_funct = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    gis_commen = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    extrusion = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    base_heigh = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    resources_field = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    shape_leng = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    shape_area = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    shape_clas = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    archaeol_3 = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    pit_find_g = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    eigner_map = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    brick_type = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    height_max = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    add_phase_field = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=50)
    add_phase1 = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=50)
    find_mater = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    find_type = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    height = models.FloatField(
        blank=True, null=True,
        help_text="provide_some"
    )
    find_gis_c = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    find_local = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    find_inven = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    phase_gis_field = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=254)
    locus_id = models.CharField(
        blank=True, null=True,
        help_text="provide some",
        max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return "{}".format(self.orea_gis_i)
