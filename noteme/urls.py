from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from noteme import views

urlpatterns = [
    url(r'^todo/$', views.ToDoList.as_view()),
    url(r'^todo$', views.ToDoList.as_view()), #enable search via different parms such as body/done etc
    #url(r'^todo/(?P<pk>\w+)/?$', views.ToDoDetail.as_view()), #should we be using alphanumeric here? i.e. w+ instead of [0-9]+?
    url(r'^todo/(?P<title>[\w|\W]+)/?$', views.ToDoDetail.as_view()), #get using title, accomodate for spaces(%20s) by using this regex
    #(r'^todo', include('haystack.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)


#from django.conf.urls import url, include
#from noteme import views
#from rest_framework.routers import DefaultRouter
#
## Create a router and register our viewsets with it.
#router = DefaultRouter()
#router.register(r'todo', views.ToDoViewSet)
#router.register(r'search', views.ToDoViewSet, base_name='search')
#urlpatterns = [
#    url(r'^', include(router.urls)),
#]

