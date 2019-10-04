import random

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError
from faker import Factory
from questions.models import Question, Tag, Answer, Like, Profile

fake = Factory.create('en_US')


class Command(BaseCommand):
    help = 'Fill the database'

    USERS_AMOUNT = 10000
    TAG_AMOUNT = 10000
    QUESTIONS_AMOUNT = 100000
    ANSWERS_AMOUNT = 206325

    def handle(self, *args, **options):
        # generating profiles
        for i in range(0, self.USERS_AMOUNT):
            u = Profile.objects.create_user(
                username=fake.first_name() + ' ' + fake.last_name() + str(random.randint(0, self.USERS_AMOUNT)),
                email=fake.email(),
                password=fake.word())
            print(i)
            try:
                u.save()
            except IntegrityError as e:
                pass  # ignore duplicate tags

        # generating tags
        for i in range(0, self.TAG_AMOUNT):
            t = Tag(title=fake.word() + str(random.randint(0, self.USERS_AMOUNT)))
            print(i)
            try:
                t.save()
            except IntegrityError as e:
                pass  # ignore duplicate tags

        # generating questions
        for i in range(0, self.QUESTIONS_AMOUNT):
            q = Question(title=fake.street_address(),
                         text=fake.text()[:100],
                         author=Profile.objects.get(id=random.randint(1, self.USERS_AMOUNT)))
            q.save()
            random_tag_id = random.randint(2, self.TAG_AMOUNT - 2)
            try:
                q.tags.add(Tag.objects.get(id=random_tag_id),
                           Tag.objects.get(id=random_tag_id + 1),
                           Tag.objects.get(id=random_tag_id - 1))
            except ObjectDoesNotExist:
                pass
            q.save()
            print(i)

        # generating answers
        for i in range(0, self.ANSWERS_AMOUNT):
            a = Answer(text=fake.text()[:100],
                       author=Profile.objects.get(id=random.randint(1, self.USERS_AMOUNT)),
                       question=Question.objects.get(id=random.randint(1, self.QUESTIONS_AMOUNT)))
            try:
                a.save()
            except ObjectDoesNotExist:
                pass
            print(i)

        # generating likes
        for i in range(0, self.QUESTIONS_AMOUNT):
            try:
                random_user_id = random.randint(2, self.USERS_AMOUNT - 2)
                random_question_id = random.randint(1, self.QUESTIONS_AMOUNT)
                q = Question.objects.get(id=random_question_id)
                positive = random.randint(0, 1)
                like = Like(user=Profile.objects.get(id=random_user_id), content_object=q,
                            positive=positive)
                q.rating = q.rating + 1 if positive else q.rating - 1
                with transaction.atomic():
                    like.save()
                    q.save()
                print(i)
            except IntegrityError as e:
                pass  # ignore duplicate likes
        for i in range(0, self.ANSWERS_AMOUNT):
            try:
                random_user_id = random.randint(2, self.USERS_AMOUNT - 1)
                random_answer_id = random.randint(1, self.ANSWERS_AMOUNT)
                a = Answer.objects.get(id=random_answer_id)
                positive = random.randint(0, 1)
                like = Like(user=Profile.objects.get(id=random_user_id), content_object=a,
                            positive=positive)
                a.rating = a.rating + 1 if positive else a.rating - 1
                with transaction.atomic():
                    like.save()
                    a.save()
                print(i)
            except IntegrityError as e:
                pass  # ignore duplicate likes
