from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Tag, Answer, Like
from django.contrib.auth.models import User
from faker import Factory
import random

fake = Factory.create('en_US')


class Command(BaseCommand):
    help = 'Fill the database'

    def handle(self, *args, **options):
        # generating tags
        unique_tags = []
        #for word in unique_tags:

        for i in range(0, 10):
            while 1:
                t = Tag(title=fake.word())
                if t not in unique_tags:
                    unique_tags.append(t)
                    t.save()
                    break

        # generating  users
        for i in range(0, 10):
            u = User.objects.create_user(fake.first_name(), email=fake.email(), password=fake.word())
            u.save()

        # generating questions
        for i in range(0, 100):
            user = User.objects.get(id=random.randint(2, 9))
            q = Question(author=user, text=fake.text(), title=fake.street_address(), rating=random.randint(0, 1000))
            q.save()
            random_tag_id = random.randint(2, 9)
            q.tags.add(Tag.objects.get(id=random_tag_id), Tag.objects.get(id=random_tag_id + 1),
                       Tag.objects.get(id=random_tag_id - 1))
            q.save()

        # generating answers
        for i in range(0, 1000):
            user = User.objects.get(id=random.randint(1, 10))
            q = Question.objects.get(id=random.randint(1, 100))
            a = Answer(author=user, text=fake.text(), question=q)
            a.save()

        # generating likes
        for i in range(0, 100):
            random_user_id = random.randint(2, 9)
            random_question_id = random.randint(1, 100)
            q = Question.objects.get(id=random_question_id)
            l = Like(user=User.objects.get(id=random_user_id), question=q, is_like=random.randint(0, 1))
            l.save()
            l = Like(user=User.objects.get(id=random_user_id+1), question=q, is_like=random.randint(0, 1))
            l.save()
            l = Like(user=User.objects.get(id=random_user_id-1), question=q, is_like=random.randint(0, 1))
            l.save()