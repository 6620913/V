from django.shortcuts import render

# Create your views here.

def main_view(requst):
    context ={}
    return render(requst,'chat/main.html',context=context)