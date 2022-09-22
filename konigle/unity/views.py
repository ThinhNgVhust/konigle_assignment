import email
from django.shortcuts import render
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer
# Create your views here.
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def is_valid(email):
    print("valid ",email)
    if re.fullmatch(regex, email):
        print("True")
        return True
    return False

@api_view(['GET'])
def index(request):
    all_emails  = Email.objects.order_by("-date").all()
    email_this_month  =Email.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month)
    number_unsubscribed = Email.objects.filter(status = False)
    # serializer = EmailSerializer(all_emails,many = True)
    # return Response(serializer.data)
    return render(request,"unity/index.html",{"all_emails":all_emails,"email_this_month":len(email_this_month),"number_unsubscribed":number_unsubscribed})

@api_view(['POST'])
def get_mail(request):
    data = request.data
    email_name = data["email"]
    if is_valid(email_name):
        if  Email.objects.filter(name = email_name):
            return Response({"message":"already exists"},status=409)      
        content = data
        email = Email(name=email_name)
        email.save()
        return Response(content,status=201)
    else:
        return Response({"message":"email not valid"},status=400)