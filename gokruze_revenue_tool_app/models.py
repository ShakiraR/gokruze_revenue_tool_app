from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Routes_Master(models.Model):
    Routes_Master_Route_Code = models.CharField(max_length=264,blank=True)
    Routes_Master_Route_Starts_From = models.CharField(max_length=264,blank=True)
    Routes_Master_Route_Starts_From = models.CharField(max_length=264,blank=True)
    Routes_Master_Route_Ends_From = models.CharField(max_length=264,blank=True)
    Routes_Master_Duty = models.CharField(max_length=264,blank=True)
    Routes_Master_Bus_No = models.CharField(max_length=264,blank=True)
    Routes_Master_Seating_Capacity = models.IntegerField(blank=True)
    Routes_Master_Manufacturing_Company = models.CharField(max_length=264,blank=True)
    Routes_Master_Km = models.IntegerField(blank=True)
    Routes_Master_Costing = models.IntegerField(blank=True)
    Routes_Master_Bus_Vendor = models.CharField(max_length=264,blank=True)

    def __str__(self):
        return self.Routes_Master_Route_Code

class Data_Dump(models.Model):
    Data_Dump_Date_Of_Data_Dump_Created = models.DateTimeField(auto_now_add=True)
    Data_Dump_Route_Code = models.ForeignKey(Routes_Master,on_delete=models.CASCADE)
    Data_Dump_Daily_AM = models.IntegerField(blank=True)
    Data_Dump_Monthly_AM = models.IntegerField(blank=True)
    Data_Dump_Daily_PM = models.IntegerField(blank=True)
    Data_Dump_Monthly_PM = models.IntegerField(blank=True)
    Data_Dump_Total = models.IntegerField(blank=True)

            
