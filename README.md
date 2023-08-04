# BookShop

A backend service that can request Api for helping in Application Development (Android, IOS).

## Getting Started with PyCharm

Open project using Pycharm. Open sqlcreator.py and run it. 'books.db' will be created.

Click Terminal on PyCharm. Copy below values to terminal.

```
export DEV_DATABASE_URL=sqlite:///books.db
```
```
export FLASK_APP=bookshop.py
```


Add 
```
flask shell
```
command in terminal.


Open bulkbooks.py file. Copy all codes and paste to terminal. Dummy data will be added.
Use Control+C to exit.

command 
```
flask run
```
command in terminal.

## Api Endpoints

### List All Books
GET Request
```
http://127.0.0.1:5000/book/list
```

### List Books By Limit And Offset
GET Request
```
http://127.0.0.1:5000/book/list?limit=20&page=0
```

### Get Book By Id
GET Request
```
http://127.0.0.1:5000/book/0
```

### Create Book
POST Request
```
http://127.0.0.1:5000/book

body
{
  "image": "xxxx.jpg",
  "title": "xxx",
  "author": "xxx",
  "price": 71.25
}
```

### Update Book By Id
PUT Request
```
http://127.0.0.1:5000/book/1

body
{
  "image": "xxxx.jpg",
  "title": "xxx",
  "author": "xxx",
  "price": 71.25
}
```


### Update Book By Id
DELETE Request
```
http://127.0.0.1:5000/book/1
```
