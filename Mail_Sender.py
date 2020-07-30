import smtplib
import os
from dotenv import load_dotenv

my_mail = 'From: alex.balakin52@gmail.com \n'
friend_mail = 'To: alex.balakin52@gmail.com \n'
subject_mail = 'Subject: Приглашение_3 \n'
mail_text = '''\n\n Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно 
столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub.
Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление
о релизе сразу на имейл.'''
my_name = 'Евгений'
friend_name = 'Алексей'
web_site = 'dvmn.org'
mail_text = mail_text.replace('%website%', web_site)
mail_text = mail_text.replace('%friend_name%', friend_name)
mail_text = mail_text.replace('%my_name%', my_name)
mail_to_send = my_mail + friend_mail + subject_mail + mail_text

mail_to_send = mail_to_send.encode("UTF-8")
log_in = load_dotenv("LOGIN")
password = load_dotenv("PASSWORD")
email_from = 'alex.balakin52@gmail.com'
email_to = 'alex.balakin52@gmail.com'
server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login(log_in, password)
server.sendmail(email_from, email_to, mail_to_send)
server.quit()
