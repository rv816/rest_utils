from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from copysc.copyscreen import convert_clipboard

# Create your views here.



@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response('Hello world')

@api_view(['GET', 'POST', 'PUT'])
def process_url(request):
    data = request.data
    link = data.get('link')
    response = {}
    try:
        converted_link = convert_clipboard(link)
        response['link'] = converted_link
        return Response(response, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


