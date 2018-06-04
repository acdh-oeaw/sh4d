from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from entities.apis_views import PlaceViewSet, GeoJsonViewSet

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r'geojson', GeoJsonViewSet, base_name='places')
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^entities-ac/', include('entities.dal_urls', namespace='entities-ac')),
    url(r'^entities/', include('entities.urls', namespace='entities')),
    url(r'^shapes/', include('shapes.urls', namespace='shapes')),
    url(r'^shapes-ac/', include('shapes.dal_urls', namespace='shapes-ac')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]
