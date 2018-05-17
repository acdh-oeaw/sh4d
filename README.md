# sh4d

A djangobaseproject based project to publish GIS data gathered in the [4dpuzzle project](https://4dpuzzle.orea.oeaw.ac.at/).


# how to import shape files into geodjango

## derive a model definition from your shapefile using [ogrinspect](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/#try-ogrinspect)

e.g. to create a model definition (and a mapping file) for the shapefile `shapes\data\shp_EPSG4326\orig\TD_FI_j21_Bricks.dbf` you would need to type:
`python manage.py ogrinspect shapes\data\shp_EPSG4326\orig\TD_FI_j21_Bricks.dbf Bricks --srid=4326 --mapping --multi > temp.py --settings=sh4d.settings.pg_local`

This command creates a `temp.py` file in you project's root directory.

## Define and customize a 'Bricks' class:
* copy and paste the class definition form 'temp.py' into the `models.py` located in your dedicated application directory, e.g. `shapes/models.py`
* customize this barebone class definition according to your needs, e.g. add `verbose_name` and `help_text` attributes or change the mandatory settings by adding `blank` and `null` attributes like in the example below.
* The value of `verbose_name` attribute will be the one visible to the users.

### default class definition

```
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
```

### customized class definition

```
class Bricks(models.Model):

    """ defines a Brick """

    excavation = models.CharField(
        blank=True, null=True,
        max_length=254, verbose_name="Excavation",
        help_text="What was the excavation responsible for the discovery of this object"
        )
    stratum_id = models.CharField(
        blank=True, null=True,
        max_length=254)
    phase_id = models.CharField(
        blank=True, null=True,
        max_length=254)
    archaeolog = models.CharField(
        blank=True, null=True,
        max_length=254)
    archaeol_1 = models.CharField(
        blank=True, null=True,
        max_length=254)
    brick_type = models.CharField(
        blank=True, null=True,
        max_length=254)
    brick_mate = models.CharField(
        blank=True, null=True,
        max_length=254)
    height_max = models.FloatField(
        blank=True, null=True)
    extrusion = models.FloatField(
        blank=True, null=True)
    base_heigh = models.FloatField(
        blank=True, null=True)
    orientatio = models.CharField(
        blank=True, null=True,
        max_length=254)
    resources_field = models.CharField(
        blank=True, null=True,
        max_length=254)
    shape_leng = models.FloatField(
        blank=True, null=True)
    shape_area = models.FloatField(
        blank=True, null=True)
    orea_gis_i = models.CharField(
        blank=True, null=True,
        max_length=50, verbose_name="OREA_GIS_ID")
    archaeol_2 = models.CharField(
        blank=True, null=True,
        max_length=100)
    add_phase_field = models.CharField(
        blank=True, null=True,
        max_length=50)
    add_phase1 = models.CharField(
        blank=True, null=True,
        max_length=50)
    geom = models.MultiPolygonField(blank=True, srid=4326)

    def __str__(self):
        return "{}".format(self.orea_gis_i)
```

* after this, run the usual `makemigrations` and `migrate` django-commands.

  * `python manage.py makemigrations shapes --settings=sh4d.settings.pg_local`
  * `python manage.py migrate --settings=sh4d.settings.pg_local`

## Write and run import script

The last thing to do is to write and execute a script which reads your shapefile and import it's content into your application's database as described [here](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/#layermapping). An import script for our Bricks class can be found in `shapes/load.py`.
* To execute the script run the following command to open a django-shell session: `python manage.py shell --settings=sh4d.settings.pg_local`
* And in the shell-session type:
  * `from shapes impmort load`
  * `import bricks`

## register Admin views

To actually inspect, curate and query your imported data in an easy manner, simply register you Bricks class in the admin-interface `shapes/admin.py`.
After this you can inspect your data at `http://127.0.0.1:8000/admin/shapes/bricks/`


# Django Base Project

[![DOI](https://zenodo.org/badge/95352230.svg)](https://zenodo.org/badge/latestdoi/95352230)

## About

As the name suggests, this is a basic Django project. The idea of this base project is mainly to bootstrap the web application development process through setting up such a Django Base Project which already provides a couple of Django apps providing quite generic functionalities needed for building web application bound to the Digital Humanities Domain.

## Install

1. Download or clone this repository.
2. Rename the root folder of this project `sh4d` and the `sh4d` folder in your projects root folder to the name chosen for your new project (e.g. to `mynewproject`).
3. In all files in the project directory, rename `sh4d` to the name chosen for your new project. (Use `Find and Replace All` feature provided by your code editor.)
4. Adapt the information in `webpage/metadata.py` according to your needs.
5. Create and activate a virtual environment and run `pip install -r requirements.txt`.

## First steps

This project uses modularized settings (to keep sensitive information out of version control or to be able to use the same code for development and production). Therefore you'll have to append a `--settings` parameter pointing to the settings file you'd like to run the code with to all `manage.py` commands.

For development just append `--settings={nameOfYouProject}.settings.dev` to the following commands, e.g. `python manage.py makemigrations --settings=sh4d.settings.dev`.

6. Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Jupyter notebook

In case you want to use [Jupyter Notebook and Django-Extensions](https://andrewbrookins.com/python/using-ipython-notebook-with-django/) use the `requirements_dev.txt` for your virtual environment.

## Next steps

Build your custom awesome Web App.

## Tests

Install required packages

    pip install -r requirements_test.txt

Run tests

    python manage.py test --settings=sh4d.settings.test

After running the test a HTML coverage report will be available at cover/index.html
