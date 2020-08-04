from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hotel(models.Model):
    h_id = models.AutoField(primary_key=True)
    h_name = models.CharField(max_length=50, default="")
    h_address = models.CharField(max_length=100, default="")
    h_zipcode = models.CharField(max_length=10, default="")
    h_contact = models.CharField(max_length=10, default="")
    h_email = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.h_name


class Room(models.Model):
    r_id = models.AutoField(primary_key=True)
    h_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    r_no = models.IntegerField(default=-1)
    r_price = models.IntegerField(default=-1)
    r_bed = models.IntegerField(default=1)
    r_view = models.CharField(max_length=50, default="N/A")

    def __str__(self):
        return "Room no. " + str(self.r_no) + " at " + self.h_id.h_name


class Booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    r_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    b_cin = models.DateField()
    b_cot = models.DateField()
    b_A = models.IntegerField(default=1)
    b_C = models.IntegerField(default=0)
    b_dt = models.DateField(auto_now_add=True)
    b_pid = models.CharField(max_length=100, default="N/A")

    def __str__(self):
        return "Room no. " + str(self.r_id.r_no) + " at " + self.r_id.h_id.h_name + " by " + self.u_id.username
