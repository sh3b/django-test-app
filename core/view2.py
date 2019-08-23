from django.http import HttpResponse
from djangobarebone.decorators import group_required


@group_required("View2 Viewers")
def view2(request):
    text = "This is View 2"
    return HttpResponse(text)
