from django.views.generic import View
from django.shortcuts import render

class HomeViews(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return  render (request, "Index.html", context)