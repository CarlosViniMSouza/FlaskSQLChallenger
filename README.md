## Challenger Code with Python, Flask and SQL (with MongoDB)

*application build by Documentation Flask*

```shell
$ pip list
Package          Version
---------------- -------
Flask-SQLAlchemy 2.5.1
greenlet         1.1.2
itsdangerous     2.1.2
Jinja2           3.1.1
MarkupSafe       2.1.1
pip              22.0.4
setuptools       60.9.3
SQLAlchemy       1.4.35
Werkzeug         2.1.1
wheel            0.37.1
```

## Theoretical Test:

1. **How does one combine two Pandas dataframes?**

*ans.:* Using the method 'merge()'

2. **What is the difference between a local variable and a global variable?**

*ans.:* A 'global variable' can be used anywhere in the program; a 'local variable' can only be used in a specific part of the program. Also, global variable is not a good choice for performing operations (because it affects software processing and security)

3. **How does one create a copy of a dataframe using Pandas?**

*ans.:* Using the method 'copy()'

4. **How does one handle concurrent requests in Flask?**

*ans.:* With 'threaded=True' each request is treated as a new thread. The number of threads your server can process simultaneously depends largely on the operating system and the limits it sets on the number of threads in processes.

5. **What is a Replica Set in MongoDB?**

*ans.:* Union of several processes that maintain the database on several servers

6. **What is a Transaction in a database context?**

*ans.:* Set of operations that make up a task or logical unit of work to be performed (example: Creation, Deletion, etc).

### Images Application

![img-pokedex](/Docs/img-pokedex.jpg)

### Image from MongoDB connected to application 

![img-Mongo](/Docs/img-MongoDB-connected.jpg)

## How to execute (using Git Bash):

1 - install the project in your machine way: `$ git clone https://github.com/CarlosViniMSouza/FlaskSQLChallenger.git`

2 - create a python virtual enviroment: `$ python -m virtualenv venv`

3 - access the `venv` folder on terminal: `$ source venv/Scripts/activate`

4 - execute the project: `$ flask run`

5 - access the localhost: `http://127.0.0.1:5000`