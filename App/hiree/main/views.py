from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
#from main import hiree
#from .hiree import get_offers_links

# Create your views here.
def index(request):
    return render(request, 'main/viev.html')

'''
class MyAction(View):
    def post(self, *args, **kwargs):
            data = {}
# Получаем данные из запроса
            action = self.request.POST.get('action')

            if action == 'Submit':
                data['result'] = all_links
            else:
                data['result'] = 'Error'
            return JsonResponse(data) 
'''