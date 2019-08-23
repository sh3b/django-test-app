from django.http import HttpResponse
from django.shortcuts import render

from djangobarebone.decorators import group_required


@group_required("View1 Viewers")
def view1(request):
    text = "This is View 1"
    return HttpResponse(text)
