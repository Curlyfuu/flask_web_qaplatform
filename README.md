# flask_web_qaplatform
a web app about Q&amp;A platform based on flask and python 3

##Rewquirement:
###1.packages:
1. flask 1.0.2
2. flask-sqlalchemy
3. flask-migrate
4. flask-script
###2.software:
1. python 3.7
2. mysql


##How to use:
```
###1. mysql
>>mysql -uroot -p
>>password:
>>create database zlktqa_demo;
>>exit;
```

###2. start-up app
```
>>python manage.py db init
>>python manage.py db migrate
>>python manage.py db upgrade
>>python zlktqa.py

#The-end



