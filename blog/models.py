from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=900)
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.name) + "|" + str(self.date_time)


class BlogPost(models.Model):
    title = models.CharField(max_length=5000)
    content = models.TextField()
    author = models.CharField(max_length=500)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "|" + str(self.author)
