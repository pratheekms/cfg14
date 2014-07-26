from django.conf.urls import patterns, include, url
from pdp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'enableIndia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login),
    url(r'login/', views.login, name='login'),
    url(r'mentor/', views.mentor_dashboard, name='mentor_dashboard'),
    url(r'mentee/', views.mentee_dashboard, name='mentee_dashboard'),
    url(r'admin/', views.admin_dashboard, name='admin_dashboard'),
    url(r'moderator/', views.moderator_dashboard, name='moderator_dashboard'),
)
