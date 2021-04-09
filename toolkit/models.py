from django.db import models

# Create your models here.
class Mongo_Credentials(models.Model):
    use = models.CharField(max_length=100)
    db = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    uri = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.use

# class Bucket_Credentials(models.Model):
#     use = models.CharField(max_length=100)
#     bucket = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     access_key = models.CharField(max_length=100)
#     access_secret = models.BooleanField(default=False)

#     def __str__(self):
#         return self.use