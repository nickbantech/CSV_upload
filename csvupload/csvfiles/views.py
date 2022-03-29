from django.shortcuts import render
import csv,io
from django.contrib import messages
from . import models

def csv_upload(request):
    template = "Csv_uploader.html"
    data = models.Student.objects.all()
    prompt = {
        'order': 'Order of the CSV should be student_F_name,student_M_name,student_L_name,student_state,student_city',
        'student': data    
              }

    if request.method == "GET":
        return render(request,template,prompt)
    csv_file =request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is Not CSV file')  
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        _ , created = models.Student.objects.update_or_create(
            student_F_name =column[0],
            student_M_name =column[1],
            student_L_name = column[2],
            student_state =column[3],
            student_city =column[4],
        )  

    context = {}
    return render(request,template,context)        




