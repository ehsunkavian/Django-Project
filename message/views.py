# from django.shortcuts import render
from django.views.generic import TemplateView

# def messageview(request):
#    return render(request, 'home.html')


class MessageView(TemplateView):
    template_name = 'home.html'

#    def get(self, request):
#        return render(request, 'home.html')
