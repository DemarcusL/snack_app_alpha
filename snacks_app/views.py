from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from .models import Snack
from .forms import SnackForm
# Create your views here.

def home(request):
    # return HttpResponse("<h6> Hello ! You have touched the home endpoint in your app ! Proceed to other routes for more options. <h6>")
    return render(request, 'base.html')

# --------------------------------------------------------------------------------------------------------->


def all_things(request):
    object_things = Snack.objects.all()
    return render(request, 'thing_list.html', {'all_object_things': object_things})

# --------------------------------------------------------------------------------------------------------->


# we passsed in the pk so we can use it when passing into a template
def thing_read(request, pk):
    # get specific thing by id 
    thing = get_object_or_404(Snack, pk=pk)
    return render(request, 'thing_read.html', {'the_thing': thing})

# --------------------------------------------------------------------------------------------------------->

def thing_create(request):
    # lets create an instance of a form for each hit
    # when we pass it here, we a passing an instanc eof creation, calling the if loop with form.save it save in the db in this project
    form = SnackForm(request.POST or None )

    if form.is_valid():
        form.save()
    
        return redirect('all_things')

        # you pass in the arguments, the third group is setting what those will be available to use in the template.
    return render(request, 'thing_create.html', {'form':form})

# --------------------------------------------------------------------------------------------------------->

def thing_update(request, pk):
    # return HttpResponse("<h6> Hello ! You have touched the home endpoint in your app ! Proceed to other routes for more options. <h6>")
    thing = get_object_or_404(Snack, pk=pk)
    # print(thing.name)

    form = SnackForm(request.POST or None )

    if form.is_valid():
        form.save()
    
        return redirect('all_things')

    return render(request, 'thing_update.html' , {'form':form, 'the_thing':thing})

# --------------------------------------------------------------------------------------------------------->

def thing_delete(request, pk):
    thing = get_object_or_404(Snack, pk=pk)

    if request.method == 'POST':
        thing.delete()
    
        return redirect('all_things')
    return render(request, 'thing_delete.html', {'the_thing': thing})

# --------------------------------------------------------------------------------------------------------->







