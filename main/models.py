from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User

# Create your models here.




class Genre(models.Model):

    GENRE_CHOICES = [
    ("NEWS", "News"),
    ("COMEDY", "Comedy"),
    ("EDUCATION", "Education"),
    ("SPORTS", "Sports"),
    ("MUSIC", "Music"),
    ("TECHNOLOGY", "Technology"),
    ("BUSINESS", "Business"),
    ("TRUE_CRIME", "True Crime"),
    ("LIFESTYLE", "Lifestyle"),
    ("SCIENCE", "Science"),
    ("HISTORY", "History"),
    ("FICTION", "Fiction"),
    ("ARTS", "Arts"),
    ("RELIGION", "Religion"),
    ]

    genrepod = models.CharField(max_length = 10 ,choices = GENRE_CHOICES, default = "TECHNOLOGY")
    
    def __str__(self):
        return self.genrepod

class podcastDetails(models.Model):
    podname = models.CharField('Podcast Name',max_length=20)
    podcreator = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    liked = models.BooleanField(default=False)
    poddata = models.FileField(upload_to="Podcast Data")
    genre = models.ForeignKey(Genre,on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.podname