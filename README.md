# Youtube Videos Collector Service

## Introduction

This is a simple project that uses Youtube v3 API's to fetch a list of videos for a predefined video tag. We have a background async task that executes periodically and collects the latest videos published related to the predefined search query on Youtube.

## Setup

This is a dockerized project, so the only that we need to do is start docker containers but before that make sure you have the following environment variable set

> YOUTUBE_API_KEYS

This should be a space separated list of Youtube API keys. These keys would be used while calling Youtube v3 API's.
Once you've added above env variable use the following command to bring up your containerised service

> docker-compose up

## API

All the APIs are unauthenticated

API to Get Paginated List of Videos -
http://0.0.0.0:8000/youtube/video/?page=1&per_page=20

API To Search all videos for a given query -
http://0.0.0.0:8000/youtube/video/search/?q={query_string}

## Dashboard

To access dashboard you need to first create a superuser

Open a session in currently running django container using following command

> docker exec -ti {django container name} /bin/bash

In the created Docker session. Execute the following command

> python manage.py createsuperuser

It would ask you to set username, email and password for superuser, using which you can access admin dashboard

Admin Dashboard Link - 

> http://0.0.0.0:8000/youtube/admin/

Admin pages are authenticated and can be accessed by superuser credentials created above. The awesome Django admin dashboard allows us to view the stored videos with various filters.

## Backend Task

This service executes a backend job periodically to asyncronously fetch videos from Youtube and update the database. This background task is implemented using celery for scheduling async tasks.

Also, we could provide multiple API keys during configuration(see setup section above), so that if quota for any one API Key is exhausted, the async task automatically uses the next available key.

## Logging

Logs of all contianers or specific containers can be monitored using following command -

> docker-compose logs

or

> docker-compose logs service



