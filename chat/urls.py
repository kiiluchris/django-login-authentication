from django.conf.urls import include, url

import views

urlpatterns = [
	# url(r'^$', views.index, name = "index"),
	# url(r'^login/(\w*)', views.login, name = "login"),
    url(r'^$', views.main, name = "main"),
]