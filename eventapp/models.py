from django.db import models


class EventUser(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    birth = models.DateField(auto_now=False, auto_now_add=False)

    # Allowing to use model in admin panel and if we call the record we only get names
    def __str__(self):
        return self.name
