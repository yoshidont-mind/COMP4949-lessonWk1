from django.urls import path, include
from .views import homePageView, aboutPageView, tatsuyaPageView, homePost, results, todos, register, message, logoutView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('tatsuya/', tatsuyaPageView, name='tatsuya'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('todos', todos, name='todos'),
    path("register/", register, name="register"),
    path('message/<str:msg>/<str:title>/', message, name="message"),
    path('', include("django.contrib.auth.urls")),
    path("logout/", logoutView, name="logout"),
]
