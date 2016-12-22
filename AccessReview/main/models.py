from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    master_userlist = models.CharField(max_length=100) #probably change to file later, right now url.
    business_owner = models.CharField(max_length=100) #email
    technical_owner = models.CharField(max_length=100) #email
    most_recent_review = models.CharField(max_length=100)


    def __str__(self):
        return self.name


#class Review(models.Model):
#    start_date
#    status
#    review_status =
#    technical_status =

#class Business_signoff
