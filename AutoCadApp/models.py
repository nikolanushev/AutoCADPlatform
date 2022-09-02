from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True)
    time = models.IntegerField()
    video = EmbedVideoField(null=True)

    def __str__(self):
        return self.title


class AppUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    date_of_birth = models.DateField
    photo = models.ImageField(upload_to="images/", null=True, blank=True, )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Test(models.Model):
    title = models.CharField(max_length=20)
    question = models.CharField(max_length=100)
    op1 = models.CharField(max_length=40, null=True)
    op2 = models.CharField(max_length=40, null=True)
    op3 = models.CharField(max_length=40, null=True)
    answer = models.CharField(max_length=40, null=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generated_on = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    lecture = models.ForeignKey(Tutorial, on_delete=models.CASCADE)


class TutorialTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)