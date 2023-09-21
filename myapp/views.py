from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from git import Repo
from django.http import HttpResponse


def home(request):
    return render(request, 'sample.html')


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        repo = Repo("./")
        git = repo.git
        git.checkout('main')
        git.pull()
        return HttpResponse("pull_success", status=200)
    return HttpResponse("fail", status=400)
