from django.urls import path
from django.conf.urls import url
from polls import views
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login
#from .urls import *
#import polls.urls


app_name = "polls"


urlpatterns = [
        path('', views.index, name='index'),
        path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
        path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
        #url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
        #url(r'^logout/$', auth_views.LogoutView.as_view(next_page="login"), name='logout'),
]
