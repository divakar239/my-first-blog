from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]													# We're assigning a view called post_list to the ^$ URL. the ^$ creates an empty string 