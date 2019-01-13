from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('portfolio', portfolio, name='portfolio'),
    path('contact', Contact, name='contact'),
    path('automail', automail, name='automail'),
    path('sendmail', sendmail, name='sendmail')

]
