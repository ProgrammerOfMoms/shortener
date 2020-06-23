from django.http import HttpResponseRedirect

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Url
from .serializers import UrlSerializer

class UrlList(ListAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

class UrlShort(APIView):
    def post(self, request):
        origin_uri = request.data["url"]
        url, is_created = Url.objects.get_or_create(url=origin_uri)
        short_url = url.short_url
        http_status = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
        return Response(short_url, status=http_status)

class UrlView(APIView):
    def get(self, request, hash):
        uri = Url.objects.get(url_hash=hash).url
        return HttpResponseRedirect(uri)


        

        

