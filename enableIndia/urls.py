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
    url(r'^login/', views.login, name='login'),
    url(r'^loginconfirm/', views.loginconfirm, name='loginconfirm'),
    url(r'^mentor/', views.mentor_dashboard, name='mentor_dashboard'),
    url(r'^mentee/', views.mentee_dashboard, name='mentee_dashboard'),
    url(r'^administrator/', views.admin_dashboard, name='admin_dashboard'),
    url(r'^moderator/', views.moderator_dashboard, name='moderator_dashboard'),
    url(r'^register/', views.register, name='register'),
    url(r'^search/', views.search, name='search'),
    url(r'^checklist/[a-zA-Z]+/[a-zA-Z:/\.]+/', views.checklist, name='checklist'),



)
