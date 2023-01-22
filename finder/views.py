from django.shortcuts import render
from django.views import View
from .forms import FinderForm
import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt





# Create your views here.
class Index(View):
    def get(self, request):
        form = FinderForm()
        return render(request, 'finder/index.html', {'form': form})

    def post(self,request):
        form = FinderForm(request.POST)

        if form. is_valid():
            total_result = form.cleaned_data['site_area']/form.cleaned_data['builtup_area']

        context = {
            'total_result' : total_result
        }
    
        return render(request, 'finder/results.html',context )

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("test.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")