from django.urls import path,include
from . import views
urlpatterns = [
    path('register',views.register,name="register"),
    path('logins',views.logins,name="login"),
    path('logouts',views.logouts,name="logout"),
    path('',views.home,name="home"),
    path('order',views.order,name="order")
]

