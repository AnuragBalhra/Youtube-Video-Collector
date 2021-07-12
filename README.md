# Youtube Videos Collector Service

## Introduction

This is a simple project that uses Youtube v3 API's to fetch a list of videos for a predefined video tag. We have a background async task that executes periodically and collects the latest videos published related to the predefined search query on Youtube.

## Setup

This is a dockerized project, so the only that we need to do is start docker containers using following command
> docker-compose up

## Logging

Logs of all contianers or specific containers can be monitored using following command -
> docker-compose logs

or

> docker-compose logs worker

## API

All the APIs are unauthenticated

API to Get Paginated List of Videos -
http://0.0.0.0:8000/youtube/video/?page=1&per_page=20

API To Search all videos for a given query -
http://0.0.0.0:8000/youtube/video/search/?q={query_string}

## Dashboard

To access dashboard you need to first create a superuser

Open a session in currently running container using following command
> docker exec -ti {docker container name} /bin/bash

In the created Docker session. Execute the following command
> > python manage.py createsuperuser

It would ask you to set username, email and password for superuser, using which you can access admin dashboard

Admin Dashboard -

> http://0.0.0.0:8000/youtube/admin/

Admin page are authenticated and can be accessed by superuser credentials created above.
The awesome Django admin dashboard allows us to view the stored videos with various filters. Also, We could filter for keywords that match in any attributes the stored videos 

## Backend Task

This service executes a backend job periodically to asyncronously fetch videos from Youtube and update the database.
This background task is implemented using celery for scheduling async tasks.
Also, we could provide multiple API keys in the settings.py configuration parameters, so that if quota is exhausted on one, the async task automatically uses the next available key.


