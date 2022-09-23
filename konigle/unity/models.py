from django.db import models

# Create your models here.
class Email(models.Model):
    name = models.EmailField(max_length=256)
    date = models.DateTimeField(auto_now=True,  null=False, blank=False)
    status = models.BooleanField(default=True,blank=True,null=True)
    def __str__(self) -> str:
        return f"{self.name} {self.date}"