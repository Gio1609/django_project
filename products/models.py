from django.db import models

class Weblog(models.Model):
    #file = models.CharFiled(max_length)

    def __str__(self):
        return f'{self.user.username} Weblog'