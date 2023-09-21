from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import git
from django.http import HttpResponse

username = 'hnryjsph9'
api_token = '66ae059404887ef91d6cc7fc13f958ed31e43e32'
domain_name = 'hnryjsph9.pythonanywhere.com'


def home(request):
    return render(request, 'sample.html')


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        repo = git.Repo('django-sample')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("pull_success", status=200)
    return HttpResponse("fail", status=400)
