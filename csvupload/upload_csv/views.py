from django.shortcuts import render
import csv,io
from django.contrib import messages
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms



def csv_upload(request):
	template = "Csv_uploader.html"
	data = models.Student_1.objects.all()
	prompt = {
		'order': 'Order of the CSV should be student_F_name,student_M_name,student_L_name,student_state,student_city student_gender',
		'student': data    
			  }

	if request.method == "GET":
		return render(request,template,prompt)

	csv_file =request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'This is Not CSV file')  

	data_set = csv_file.read().decode('UTF-8')

	lines = data_set.split('\n')
	for line in lines:
		fields = line.split(",")
		data_dict={}
		data_dict["student_F_name"]=fields[0]
		data_dict["student_M_name"]=fields[1]
		data_dict["student_L_name"]=fields[2]
		data_dict["student_state"]=fields[3]
		data_dict["student_city"]=fields[4]
		data_dict["student_gender"]=fields[5]


	# io_string = io.StringIO(data_set)
	# next(io_string)


	# for column in csv.reader(io_string,delimiter=',',quotechar='|'):
	# 	_ , city = models.City_1.objects.update_or_create(city=column[4])
	# 	_,state = models.State_1.objects.update_or_create(state=column[3])
	# 	_ , created = models.Student_1.objects.update_or_create(
	# 		student_F_name =column[0],
	# 		student_M_name =column[1],
	# 		student_L_name = column[2],
	# 		student_state =models.State_1.objects.get(state=column[3]),
	# 		student_city =models.City_1.objects.get(city=column[4]),
	# 		student_gender = column[5]
	# 	) 

		
		
	# context = {}
	# return render(request,template,context)   





