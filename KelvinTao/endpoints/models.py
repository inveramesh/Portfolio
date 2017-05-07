from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Forticlient(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    version = models.CharField(max_length=10)

    def __str__(self):
        return '{}: {}'.format(self.device, self.version)
    