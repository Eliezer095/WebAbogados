from django.views.generic import View
from django.shortcuts import render

class HomeViews(View):
    def get(self, request):
        context={

        }
        return  render (request, "Index.html", context)