from django.shortcuts import render,HttpResponse
from .models import booking
from django.views.generic import ListView, FormView
from .forms import AvailabilityForm
from booking.booking_functions.availability import check_availability
from .models import spot
# Create your views here.

def home(request):
    return render(request,'home.html')
class SpotList(ListView):
    model = spot

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name='availability_form.html'

    def form_valid(self,form):
        data= form.cleaned_data
        spot_list= spot.objects.all()
        avail_spot_list =[]
        for s in spot_list:
            if check_availability(s, data['time_in'],data['time_out']):
                avail_spot_list.append(s)
        if len(avail_spot_list)>0:
            spo = avail_spot_list[0]
            boo = booking.objects.create(user= self.request.user,
                                            spot = spo,car_no = data['car_no'],
                                            time_in = data['time_in'],
                                            time_out=data['time_out'])
            boo.save()
            return HttpResponse(boo)
        else:
            return HttpResponse('this time all spots are booked')






