from django.shortcuts import  render_to_response
from django.template.context import RequestContext
# Create your views here.
def index_view(request):
    #redes = Social.objects.filter(status=True)
    #sett = Setting.objects.filter(status=True)[0]
    #ctx = {'redes':redes,'sett':sett} 
    return render_to_response('main/index.html',context_instance = RequestContext(request))