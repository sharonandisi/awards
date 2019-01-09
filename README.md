# awards
An app similiar to the awwwards web application. It allows users to upload projects and review each others projects.

## Description
This is an application where users get to create an account , login and upload projects to the site. they can review , view and get api endpoints, and they can also edit their profiles and delete posts.
#### Link to deployed site
 

## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Deployment](#deployment)
4. [Contributing](#contributing)
5. [Bugs](#bugs)
6. [Contact me](#support-and-contact-details)
7. [Licensing](#license)


## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 3
    - Heroku
    - Postgresql

#### Clone the Repo and checkout into the project folder.
```bash
git clone git@github.com:sharonandisi/foodgram.git && cd foodgram
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
DBNAME='foodies'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='<your-email>'
EMAIL_HOST_PASSWORD='<your-password>'
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE cards;
```

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```
#### Django admin
```bash
USERNAME: sharon
PASSWORD: Sharon13
```


#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Deployment
To deploy the application, please follow these instructions:
[this gist](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)

## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute.


## Bugs
Create an issue mentioning the bug you have found

#### Known bugs
 - cannot copy image link



## Support and contact details
Contact [Sharon Andisi](sharonandisi.sa@gmail.com) for further help/support

### License
MIT

Copyright (c)2018 **Sharon Andisi**
