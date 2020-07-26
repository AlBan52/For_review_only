import smtplib

my_mail = 'From: alban.nn@yandex.ru'
friend_mail = 'To: alban.nn@yandex.ru'
subject_mail = 'Subject: Приглашение'
mail_text = '''\n Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

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

# print(mail_to_send)
mail_to_send = mail_to_send.encode("UTF-8")
# print(mail_to_send)
log_in = 'alban.nn@yandex.ru'
password = 'PUPpets@431'
email_from = 'alban.nn@yandex.ru'
email_to = 'alban.nn@yandex.ru'
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(log_in, password)
server.sendmail(email_from, email_to, mail_to_send)
server.quit()
