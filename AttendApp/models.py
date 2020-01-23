from django.db import models

# Create your models here.


class Zone(models.Model):
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Home(models.Model):
    key = models.CharField(max_length=100)
    data = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.key


class Shift(models.Model):
    in_time = models.TimeField()
    out_time = models.TimeField()

    def __str__(self):
        return self.in_time.strftime("%H:%M") + ' to ' + self.out_time.strftime("%H:%M")


class AttendanceRecord(models.Model):
    employee_name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    zonal_manager = models.CharField(max_length=100)
    shift = models.ForeignKey(Shift, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.employee_name + ': ' + self.timestamp.strftime("%d/%m/%Y")
