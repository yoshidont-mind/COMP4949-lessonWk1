from django.urls import path
from .views import homePageView, aboutPageView, tatsuyaPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('tatsuya/', tatsuyaPageView, name='tatsuya'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
