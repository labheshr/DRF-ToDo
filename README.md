# DRF-ToDo
a single user todo app using Django Rest Framework, MongoDb, and Haystack(elastic search)

This software is an attempt to put all of the below to work together in a simple application:
1. Django Rest Framework
2. Mongo Db (via django nonrel)
3. Haystack/Elastic search (powered by heroku searchbox/searchly)
4. Another rest service (Twilio) to send SMS to oneself

If you'd like to see a working demo on Heroku, please contact me at labheshr@gmail.com

Endpoint description:
(If possible please use google Postman rest client for a "nicer" experience.)

1. GET: mysite/todo/ to view all Todo notes by a single user
2. GET: mysite/todo/<<titlename>> to view the Todo note by a specific title
3. GET: mysite/todo?title=<<title of todo note>> OR mysite/todo?body=<<body of todo note>> (search via haystack)
4. POST: mysite/todo/ body of request must have "title" and "body" fields populated
5. DELETE: mysite/todo/<<titlename>>
6. PUT: mysite/todo/<<titlename>> with key value pair in the body as: title=xxx, body=yyy, done=True or False

Bugs/Todos/Improvements:
1. provide support for deleting/querying multiple todos with same titles
2. allow an interface for multiple users
3. better search handling via haystack framework

Please feel free to use this project or get back to me comments/questions

Regards,

Labhesh
