from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    formatDate = datetime.date.today().strftime("%B %Y")
    context = {"format_date":formatDate}
    return render(request,"unity/index.html",context)