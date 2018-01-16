from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Voter(models.Model):
    description = models.CharField(max_length=250)
    voter_one = models.CharField(max_length=250)
    voter_two = models.CharField(max_length=250)
    voter_one_count = models.IntegerField(default=0)
    voter_two_count = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.voter_one+" vs "+self.voter_two
