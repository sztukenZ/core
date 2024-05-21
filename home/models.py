from django.db import models
import datetime

class Event(models.Model):

    

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Event_detail", kwargs={"pk": self.pk})

    name = models.CharField(max_length=255)
    event_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.date.today)