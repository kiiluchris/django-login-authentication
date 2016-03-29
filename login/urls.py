from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))
    url(r'^$', 'django_social_app.views.login'),
    url(r'^home/$', 'django_social_app.views.home'),
    url(r'^logout/$', 'django_social_app.views.logout'),
]
