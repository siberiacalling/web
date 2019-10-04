from django.db import models
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class AnswerManager(models.Manager):
    def by_id(self, q_id):
        return self.filter(question=q_id)

    def new_answer(self, text, author, question):
        a = Answer(text=text, author=author, question=question)
        a.save()
        return self.get(id=a.id)

    def new(self, q_id):
        return self.by_id(q_id).order_by('-date')


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-date')

    def hot(self):
        return self.order_by('-rating')

    def by_tags(self, tag):
        return self.filter(tags__title=tag)

    def by_id(self, q_id):
        try:
            return self.get(id=q_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")


class Like(models.Model):
    user = models.ForeignKey('questions.Profile', on_delete=models.PROTECT)
    positive = models.BooleanField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('questions.Profile', on_delete=models.PROTECT)
    tags = models.ManyToManyField('questions.Tag')

    rating = models.IntegerField(default=0)

    likes = GenericRelation(Like)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey('questions.Profile', on_delete=models.PROTECT)
    question = models.ForeignKey('questions.Question', on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    is_correct = models.BooleanField(default=False)

    # см. Question#likes
    rating = models.IntegerField(default=0)

    likes = GenericRelation(Like)

    objects = AnswerManager()

    def __str__(self):
        return self.text


class Tag(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title


class Profile(AbstractUser):
    pic = models.ImageField(default='anon.png')
