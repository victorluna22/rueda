from django.conf.urls import patterns, include, url
from app.views.person import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView, person_search
from app.views.log import LogListView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^pessoa/$', PersonListView.as_view(), name='person_list'),
    url(r'^pessoa/cadastrar/$', PersonCreateView.as_view(), name='person_create'),
    url(r'^pessoa/editar/(?P<pk>\d+)/$', PersonUpdateView.as_view(), name='person_update'),
    url(r'^pessoa/excluir/(?P<pk>\d+)/$', PersonDeleteView.as_view(), name='person_delete'),
    url(r'^pessoa/buscar/$', person_search, name='person_search'),


    url(r'^log/$', LogListView.as_view(), name='log_list'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
