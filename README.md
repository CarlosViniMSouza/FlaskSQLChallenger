## Challenger Code with Python, Flask and SQL (with MongoDB)

*application build by Documentation Flask*

## How to execute (using Git Bash):

1 - install the project in your machine way: `$ git clone https://github.com/CarlosViniMSouza/FlaskSQLChallenger.git`

2 - create a python virtual enviroment: `$ python -m virtualenv venv`

3 - access the `venv` folder on terminal: `$ source venv/Scripts/activate`

4 - boot the db: `$ flask init-db`

5 - execute the project: `$ flask run`

6 - access the localhost: `http://127.0.0.1:5000`

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

```shell
$ pip list
Package          Version
---------------- -------
PyYAML             6.0
requests           2.27.1
setuptools         60.9.3
six                1.16.0
SQLAlchemy         1.4.35
tomli              2.0.1
urllib3            1.26.9
waitress           2.1.1
Werkzeug           2.1.1
wheel              0.37.1
```

### Images Application

![img-register](/Docs/img-register_pg.jpg)

![img-login](/Docs/img-login.jpg)

![img-pokedex](/Docs/img-pokedex.jpg)

### Image from MongoDB connected to application 

![img-Mongo](/Docs/img-MongoDB-connected.jpg)

```
PROBLEMS (FAILS):

It was not possible to make the delimitations of email and password. The login flask libs were causing difficulties in meeting these requirements.
```
