import email
from django.shortcuts import render
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer
from django.core.paginator import Paginator
# Create your views here.
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 
# function to check if user typed a valid email or not.
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
def is_valid(email):
    if re.fullmatch(regex, email):
        return True
    return False

PAGINATE_BY = 15


#view for user see statistic
def index(request):
    
    """ View: Show all emails """

    all_emails  = Email.objects.order_by("-date").all()
    email_this_month  =Email.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month)
    number_unsubscribed = Email.objects.filter(status = False)
    paginator = Paginator(all_emails, PAGINATE_BY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"unity/index.html",{
        "page_obj":page_obj,
        "total_emails":len(all_emails),
        "email_this_month":len(email_this_month),
        "number_unsubscribed":number_unsubscribed}
        )

@api_view(['POST'])
def get_mail(request):
    """ 
    Validate email.
    If it is a valid email and not exist in database, then save it into database 
    Otherwise, response a error
    """
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