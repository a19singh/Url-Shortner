# UrlShortner

A Url-Shortening API service built using flask micro web framework written in Python and deployed on WSGI server.

## Getting started

### Prerequisites

- Download Docker engine
- Pull the official mysql:5.7 image from docker h

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```sh
$ yum install docker-ce
```
- Activate Docker services using

```sh
$ systemctl start docker
```

- Pull the MySQL image using

```sh
$ docker pull mysql:5.7
```
### Setting Up the Environment

- Create a volume 

```sh
$ docker volume create mydbstorage
```

- Run the MySQL Server

```sh
$ docker run -dit -e MYSQL_ROOT_PASSWORD=redhat -e MYSQL_USER=root
                -e MYSQL_PASSWORD=redhat      -e MYSQL_DATABASE=mydatabase
		-v mydbstorage:/var/lib/mysql --name dbos mysql:5.7
```

- Check the ip address of the database container 

```sh
$ docker inspect dbos
```

- Now go to the app.py file and change the Ip adress in the connection

## Deployment

- Build the image

```sh 
$ docker build --tag url-shortner:v1 .
```

- Run the image

```sh
$ docker run --name flaskapp -p 5000:5000 url-shortner:v1
```

## Running the tests

Open the web browser and access to the page 

```
http://0.0.0.0:5000
```
- Enter the url to be shortened 
- Copy and paste the url in the address location when required to fetch the original url 






