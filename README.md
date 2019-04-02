# Flast Starter App

###### This is a basic example that shows how to setup a flask application

Here's the basic directory structure;
```
├── app
│   ├── config.py
│   ├── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── resources
│   │   └── __init__.py
│   ├── templates
│   │   └── index.html
│   ├── utils
│   │   └── __init__.py
│   └── views
│       └── __init__.py
├── README.md
├── requirements.txt
├── test
│   └── __init__.py
└── wsgi.py

```

**models** - This holds all your data classes and utility functions that interact with any kind of persitence 
(Mongo, Mysql etc) 

**resources** - This package usually holds endpoints related to an API. Try to avoid putting view endpoints here. Put them
in the `view` package instead

**view** - This package holds any endpoint that deals with any visual representation i.e endpoints that return html

**templates** - Put all your `.html` files here

**utils** - Put utility functions here. Mostly reusable logic used in the `view` and `resources`

**config.py** - All app your configuration goes here. Remember to put the right config in the right class. Anything 
reusable should go in `Config`


This is not a strict **life or death** way of structuring a flask app. Remember programming is art. As long as your app 
can be testable go with whatever makes you sleep at night :relieved:

**Tips (Frequent updates expected):**
1. For any file in the `models` package. Make sure it's within a class or method/function. It makes it easy to mock stuff
during testing
2. While organizing your models be careful while using the `orgranize imports` feature available in text editors and IDEs
it can affect how your models are loaded(i.e relationships) thus prevent your app from starting.
3. While testing your endpoints start with **negative vibes first**. Basically, start testing for non 200/201 responses first
4. Any method/function/class in the `utils` package should not depend on anything outside the utils package (Scope of your code. They can depend on libraries).
5. Make use of Flask extensions. They save a lot of time! [Here](http://flask.pocoo.org/extensions/) is a good place to start.
should be passed in as parameters. It helps prevent cyclic dependencies

**Further References:**

- [Flask Project Layout](http://flask.pocoo.org/docs/1.0/tutorial/layout/)
- [Organizing your project](http://exploreflask.com/en/latest/organizing.html)
- [Structure of a flask project](https://lepture.com/en/2018/structure-of-a-flask-project)
