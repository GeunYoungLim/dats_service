from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
import rest_framework.authentication
# 예제
class ExampleView(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)
    authentication_classes = ()

    # get
    def get(self, request):
        content = {'return content': 'hello world'}


        return Response(content)


    # put
    def put(self, request):

        lat = request.data['lat']
        lon = request.data['lon']

        if not len(lat) > 0 or not len(lon) > 0:
            Response(status=status.HTTP_400_BAD_REQUEST)

        return Response({'received data': request.data }, status=status.HTTP_200_OK)
