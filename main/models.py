from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User

# Create your models here.
# class Language(models.Model):
#     LANGUAGE_CHOICES = [
#     ("EN", "English"),
#     ("ES", "Spanish"),
#     ("FR", "French"),
#     ("DE", "German"),
#     ("IT", "Italian"),
#     ("PT", "Portuguese"),
#     ("RU", "Russian"),
#     ("ZH", "Chinese"),
#     ("JA", "Japanese"),
#     ("KO", "Korean"),
#     ("AR", "Arabic"),
#     ("HI", "Hindi"),
#     ("BN", "Bengali"),
#     ("UR", "Urdu"),
#     ("FA", "Persian"),
# ]
#     lang = models.CharField(max_length =15, choices = LANGUAGE_CHOICES  )
    

#     class Meta:
#         verbose_name = ("Language")
#         verbose_name_plural = ("Languages")

#     def __str__(self):
#         return self.lang

#     # def get_absolute_url(self):
#     #     return reverse("Language_detail", kwargs={"pk": self.pk})

# class typeofPod(models.Model):
    # TYPE_CHOICES = [
    #     ("AUDIO","audio"),
    #     ("VIDEO","video"),
    # ]
    
    # type = models.CharField(max_length = 10 ,choices = TYPE_CHOICES, default = "AUDIO")

#     def __str__(self):
#         return self.type


# class Genre(models.Model):

#     GENRE_CHOICES = [
#     ("NEWS", "News"),
#     ("COMEDY", "Comedy"),
#     ("EDUCATION", "Education"),
#     ("SPORTS", "Sports"),
#     ("MUSIC", "Music"),
#     ("TECHNOLOGY", "Technology"),
#     ("BUSINESS", "Business"),
#     ("TRUE_CRIME", "True Crime"),
#     ("LIFESTYLE", "Lifestyle"),
#     ("SCIENCE", "Science"),
#     ("HISTORY", "History"),
#     ("FICTION", "Fiction"),
#     ("ARTS", "Arts"),
#     ("RELIGION", "Religion"),
#     ]

#     genrepod = models.CharField(max_length = 10 ,choices = GENRE_CHOICES, default = "TECHNOLOGY")
    
#     def __str__(self):
#         return self.genrepod

class podcastDetails(models.Model):
    podname = models.CharField('Podcast Name',max_length=20)
    poddesc = models.CharField('Podcast Description',max_length=100)
    podcreator = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    liked = models.BooleanField(default=False)
    likes = models.IntegerField('Likes',null=True,blank=True)
    poddata = models.FileField(upload_to="Podcast Data")
    # genre = models.ForeignKey(Genre,on_delete=SET_NULL, null=True)
    # Land = models.ForeignKey(Language,on_delete=SET_NULL, null=True)
    # typeofPodcast = models.ForeignKey(typeofPod,on_delete=SET_NULL, null=True)
    dateuploaded = models.DateTimeField("Date Uploaded", auto_now_add=True)
    Views = models.IntegerField('Views',default= 0,null= True)


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



    LANGUAGE_CHOICES = [
    ("EN", "English"),
    ("ES", "Spanish"),
    ("FR", "French"),
    ("DE", "German"),
    ("IT", "Italian"),
    ("PT", "Portuguese"),
    ("RU", "Russian"),
    ("ZH", "Chinese"),
    ("JA", "Japanese"),
    ("KO", "Korean"),
    ("AR", "Arabic"),
    ("HI", "Hindi"),
    ("BN", "Bengali"),
    ("UR", "Urdu"),
    ("FA", "Persian"),
]
    lang = models.CharField(max_length =15, choices = LANGUAGE_CHOICES, null=True  )

    def __str__(self):
        return self.podname
    

    TYPE_CHOICES = [
        ("AUDIO","audio"),
        ("VIDEO","video"),
    ]
    
    type = models.CharField(max_length = 10 ,choices = TYPE_CHOICES, default = "AUDIO")
    
class playlist(models.Model):

    myplaylist = models.CharField("Playlist Name", max_length=15)
    addpod =  models.ForeignKey(podcastDetails,on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.myplaylist

    
