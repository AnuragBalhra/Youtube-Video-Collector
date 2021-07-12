import operator
from functools import reduce

from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video


class AllVideosView(APIView):
    def get(self, request):
        videos = Video.objects.all().order_by('-published_at').values()
        page = int(request.query_params.get('page', 1))
        per_page = int(request.query_params.get('per_page', 10))
        paginator = Paginator(videos, per_page)
        paginated_response = paginator.get_page(page)
        return Response(list(paginated_response))


class SearchVideoView(APIView):
    def get(self, request):
        q = request.query_params['q']
        words = q.split(' ')

        # If all words of query string lies in either title or description
        title_query = Q()  # empty Q object
        for word in words:
            title_query |= Q(title__icontains=word)

        description_query = Q()  # empty Q object
        for word in words:
            description_query |= Q(description__icontains=word)

        videos = Video.objects.filter(
            reduce(operator.or_, [title_query, description_query])
        ).order_by('-published_at').values()

        page = int(request.query_params.get('page', 1))
        per_page = int(request.query_params.get('per_page', 10))
        paginator = Paginator(videos, per_page)
        paginated_response = paginator.get_page(page)
        return Response(list(paginated_response))
