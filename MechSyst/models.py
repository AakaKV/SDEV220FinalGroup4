from django.db import models
from django.conf import settings
from django.db import models
#Time zone in Repair page
from django.utils import timezone
# Create your models here.
class RepDetails(models.Model):
    #Python has a user model where a password is built in(Like PHP admin interface and sql w/ users)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #This is the max amount of characters for the vehicle post
    Vehicle = models.CharField(max_length=600)
    repair_Details = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    check_in_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        #Checks the current time and stores as self?
        self.check_in_date = timezone.now()
        #saves the current self(which is the time)
        self.save()

    def __str__(self):
        return self.Vehicle