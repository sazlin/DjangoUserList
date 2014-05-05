from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    def __str__(self):
        return self.last_name + ", " + self.first_name + ", " + self.email
