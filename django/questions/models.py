from django.db import models
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(models.Model):
    auth_user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Like(models.Model):
    TYPES = [
        (1, 'LIKE'),
        (-1, 'DISLIKE'),
        (0, 'NONE'),
    ]
    type = models.SmallIntegerField(choices=TYPES, default=0)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class QuestionManager(models.Manager):
    def get_new_questions(self):
        pass

    def get_hot_questions(self):
        pass

    def get_questions_by_tag(self, tag_title):
        pass



