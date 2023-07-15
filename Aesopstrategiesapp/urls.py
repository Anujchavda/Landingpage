from django.urls import path
from .views import index
from .views import innerpage
from .views import portfoliodetails

urlpatterns = [
    path('', index, name='index.html'),
    path('', innerpage, name='inner-page.html'),
    path('', portfoliodetails, name='portfolio-details.html'),
]
