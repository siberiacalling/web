<p align="center">
  <a href="https://park.mail.ru/">
    <img
      alt="Технопарк Mail.ru"
      src="/img/tpark_logo.jpg"
      width="400"
    />
  </a>
</p>

## Технопарк Mail.ru / 1й семестр / Web-технологии
- Техническое задание ([Markdown](markdown/technical_details.md))
- Домашнее задание 1 ([Markdown](/markdown/task-1.md))
- Домашнее задание 2 ([Markdown](/markdown/task-2.md))
- Домашнее задание 3 ([Markdown](/markdown/task-3.md))
- Домашнее задание 4 ([Markdown](/markdown/task-4.md))
- Домашнее задание 5 ([Markdown](/markdown/task-5.md))
- Домашнее задание 6 ([Markdown](/markdown/task-6.md))
- Домашнее задание 7 ([Markdown](/markdown/task-7.md))

## Как запустить
1. Поставить `python3`, `mysql`, `virtualenv`
2. `pip install -r requirements.txt`
3. `mysql -u root -p < setup.sql`
4. `django/manage.py migrate`
5. `django/manage.py fill_db`
6. `django/manage.py runserver`