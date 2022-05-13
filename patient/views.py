from requests import delete, request
from . serializers import userserializer
from . models import p_users
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class userapi(APIView):
   def get(self,request):
      user=p_users.objects.all()
      serializer=userserializer(user,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

   def post(self,request):
      data=request.data 
      serializer=userserializer(data=data)
      if serializer .is_valid():
         serializer.save
         rs={'msg':'Data saved successfully'}
         return Response(rs,status=status.HTTP_201_CREATED)
      return Response({'msg':serializer.errors})

   def delete(self,request):
      data=request.data
      id=data.get('id')
      stu=p_users.objects.get(id=id)
      stu.delete()
      rs={'msg':'User deleted succesfully'}
      return Response(rs,status=status.HTTP_200_OK)

