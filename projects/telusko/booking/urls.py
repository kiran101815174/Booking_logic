from django.urls import path
from .views import BookingView,SpotList
from . import views
app_name = 'booking'

urlpatterns = [
    path('',views.home,name='home'),
    path('book/',BookingView.as_view(),name='Booking_form'),
    path('spots/',SpotList.as_view(),name='spot_list')
]