from django.db import models
from django.conf import settings

# Create your models here.

class spot(models.Model):
    spot_id = models.IntegerField()

    def __str__(self):
        return f'spot id  {self.spot_id} '

class booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    spot=models.ForeignKey(spot,on_delete=models.CASCADE)
    car_no = models.TextField()
    time_in =models.DateTimeField()
    time_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.spot} from {self.time_in} to {self.time_out}'
