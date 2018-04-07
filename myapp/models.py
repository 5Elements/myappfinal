from django.db import models

# Create your models here.
class Tweet(models.Model):
    tw_text = models.TextField()
    tw_user = models.CharField(max_length=200)
    tw_cat = models.FloatField(max_length=200)
    tw_img_src =  models.TextField()
    tw_desc =  models.TextField()
    tw_id = models.TextField(unique=True)
    created_at = models.CharField(max_length=200)