from django.db import models
from django.utils import timezone

class HDFS_Browser(models.Model):
    uid = models.BooleanField()
    name = models.CharField(max_length=50)
    permission = models.CharField(max_length=50)
    size = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    owner = models.CharField(max_length=50)
    date_modify = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name