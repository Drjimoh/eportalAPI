from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response 
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer



class StudentsList(APIView):

	def get(self, request):
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)
	def post(self):
		pass