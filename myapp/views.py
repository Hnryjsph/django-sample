from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import git
from django.http import HttpResponse


def home(request):
    return render(request, 'sample.html')


@csrf_exempt
def webhook(request):
    try:
        if request.method == 'POST':
            repo = git.Repo('./')
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse("pull_success", status=200)
        return HttpResponse("fail", status=400)
    except:
        print("_________________")
