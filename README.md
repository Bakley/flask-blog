# Setting up your system

Make sure you already have Python 3, Pip and Virtualenv installed in your system.

# How to get started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir flaskblog
```

After which we go into the directory:

```
cd flaskblog
```

## Create a Python Virtual Environment for our Project

Since we are using Python 3, create a virtual environment by typing:

```
virtualenv -p python3 .
```

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:

```
source bin/activate
```

## Clone and Configure a Flask Project

Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:

```
git clone https://github.com/Bakley/flask-blog.git .
```

If you get something similar to:

```
fatal: destination path '.' already exists and is not an empty directory.
```

Then follow the following instructions:

```
git init
```

```
git remote add -t \* -f origin https://github.com/Bakley/flask-blog.git
```

```
git checkout develop
```

Next, install the requirements by typing:

```
pip install -r requirements.txt
```

## How to run the app

On the terminal type:

```
export 	FLASK_ENV=development
```

```
export FLASK_APP=run.py
```

```
flask run
```


### Commands
  The application was tested using `nose` and `coverage`. To run the tests on the bash terminal use

     nosetests --with-coverage --cover-package=app  && coverage report
