from django.conf.urls import url
from ...apps.reportes.views import *
urlpatterns = [
    url(r'^Reportes/(?P<pk>\d+)$', ReportesTemplateView.as_view(), name='alum_Reportes'),
    url(r'^Reportes/$', ReportesPageTemplateView.as_view(), name='ReportesPage'),

]
