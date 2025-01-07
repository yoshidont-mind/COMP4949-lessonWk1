from django.urls import path
from .views import homePageView, aboutPageView, tatsuyaPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('tatsuya/', tatsuyaPageView, name='tatsuya'),
]
