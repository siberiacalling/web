from django.contrib.auth.models import User
from django.db import models
from django.http import Http404
from django.utils import timezone


class AnswerManager(models.Manager):
    def by_id(self, id):
        return self.filter(question=id)

    def new_answer(self, text, author, question):
        a = Answer(text=text, author=author, question=question)
        a.save()
        return self.get(id=a.id)

    def get_page(self, a_id, answers_per_page):
        q = Answer.objects.get(id=a_id).question
        return int(len(Answer.objects.filter(question=q)) / answers_per_page + 1)

    def by_username(self, username):
        u = User.objects.get(username=username)
        return self.filter(author=u)


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

    def by_username(self, username):
        current_user = User.objects.get(username=username)
        return self.filter(author=current_user)


class ProfileManager(models.Manager):
    def by_username(self, username):
        u = User.objects.get(username=username)
        return self.get(avatar=u)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey('questions.Question', on_delete=models.PROTECT)
    is_like = models.BooleanField(default=True)


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField('questions.Tag')
    likes = models.ManyToManyField(User, related_name='likes_users', through='Like')
    objects = QuestionManager()

    def __str__(self):
        return self.title

    def _count_rating(self):
        votes = Like.objects.filter(question=self)
        return len(votes.filter(is_like=True)) - len(votes.filter(is_like=False))

    likes_amount = property(_count_rating)


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey('questions.Question', on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    is_correct = models.BooleanField(default=False)
    objects = AnswerManager()

    def __str__(self):
        return self.text


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    avatar = models.OneToOneField(User, on_delete=models.PROTECT)
    pic = models.CharField(max_length=128)
    picture = models.ImageField()
    objects = ProfileManager()
