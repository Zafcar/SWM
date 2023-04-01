from django.db import models


class static_route(models.Model):
    Time = models.TimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return '%s %s %s' % (self.Time, self.Latitude, self.Longitude)


class realtime_location(models.Model):
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Weight = models.FloatField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.Date, self.Time, self.Latitude, self.Longitude, self.Weight)
    
class collection_location(models.Model):

    waste=(
        ("CW", "Cloth Waste"),
        ("GW", "Glass Waste"),
        ("EW", "Electronic Waste")
    )

    Garbage_type = models.CharField(choices=waste,max_length = 10)

    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Start_date = models.DateField()
    End_date = models.DateField()
    Start_time = models.TimeField()
    End_time = models.TimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.Name, self.Phone, self.Start_date, self.End_date, self.Start_time, self.End_time, self.Latitude, self.Longitude, self.Garbage_type)


# Create your models here.
