from django.conf.urls import patterns, url
from pdp import views

urlpatterns = patterns('',
        url(r'^login/', views.login, name='login'),
        url(r'^mentor/', views.mentor_dashboard, name='mentor_dashboard'),
        url(r'^mentee/', views.mentee_dashboard, name='mentee_dashboard'),
        url(r'^admin/', views.admin_dashboard, name='admin_dashboard'),
        url(r'^moderator/', views.moderator_dashboard, name='moderator_dashboard'),
        )
