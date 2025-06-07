from django.db import models

class User_acc(models.Model):
    name = models.CharField(max_length=255, default="")
    pn = models.IntegerField(default=1234567890)
    pass_wrd = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.name
