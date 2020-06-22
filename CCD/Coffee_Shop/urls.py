from django.conf.urls import url
from Coffee_Shop import views

#Template tagging
app_name = 'Coffee_Shop'
urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
