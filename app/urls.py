from django.conf.urls import include, url

import views

urlpatterns = [
	# url(r'^$', views.index, name = "index"),
	# url(r'^login/(\w*)', views.login, name = "login"),
    url(r'^$', views.login, name = "login"),
    # url(r'^home/$', views.home, name = "home"),
    url(r'^logout/$', views.logout, name = "logout"),
    # url(r'^test/$', views.social_user_profile, name = "test"),
]