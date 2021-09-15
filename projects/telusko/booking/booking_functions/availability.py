import datetime
from booking.models import booking

def check_availability(spot,time_in,time_out):
    avail_list=[]
    booking_list= booking.objects.filter(spot=spot)
    for boo in booking_list:
        if (boo.time_in > time_out) or (boo.time_out < time_in):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
    
