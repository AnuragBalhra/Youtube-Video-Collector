from __future__ import absolute_import, unicode_literals

import logging
import random
from datetime import datetime, timedelta

from video.models import Thumbnail, Video
from youtube.celery import app
from youtube.settings import YOUTUBE_APIKEYS, ASYNC_TASK_TIME_INTERVAL
from youtube.client import fetch_list_of_video

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.task
def fetch_youtube_videos(topic):
    current_time = datetime.now()
    published_after = datetime_to_str(current_time - timedelta(seconds=ASYNC_TASK_TIME_INTERVAL))

    APIKEY = random.choice(YOUTUBE_APIKEYS)

    next_page_token = None
    while True:
        api_resp = fetch_list_of_video(published_after, topic, APIKEY, next_page_token)
        if api_resp.status_code == 403:
            APIKEY = random.choice(YOUTUBE_APIKEYS)
            continue

        api_data = api_resp.json()
        logger.info(api_data)
        videos_data = api_data['items']
        for video_data in videos_data:
            try:
                video = Video.objects.get(video_id=video_data['id']['videoId'])
                continue
            except Video.DoesNotExist:
                pass

            snippet = video_data['snippet']
            video = Video(
                video_id=video_data['id']['videoId'],
                title=snippet['title'],
                description=snippet['description'],
                channel_id=snippet['channelId'],
                channel_title=snippet['channelTitle'],
                etag=video_data['etag'],
                published_at=datetime.strptime(snippet['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            )
            video.full_clean()
            video.save()

            thumbnails_data = snippet['thumbnails']
            for k, v in thumbnails_data.items():
                thumbnail = Thumbnail(
                    video=video,
                    type=k,
                    url=v['url'],
                    width=v['width'],
                    height=v['height']
                )
                thumbnail.full_clean()
                thumbnail.save()

        if api_data.get('nextPageToken', None):
            next_page_token = api_data['nextPageToken']
        else:
            break


def datetime_to_str(dt):
    return datetime.strftime(dt, "%Y-%m-%dT%H:%M:%SZ")


if __name__ == "__main__":
    fetch_youtube_videos.apply_async(countdown=30)

    # fetch_videos("sports")
