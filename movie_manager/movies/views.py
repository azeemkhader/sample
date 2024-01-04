from django.shortcuts import render
from .models import MovieInfo
from . forms import Movieform
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login/')
def edit(request,pk):
    instance_edited=MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=Movieform(request.POST,instance=instance_edited)
        if frm.is_valid():
            instance_edited.save()
    else:

        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits

        frm=Movieform(instance=instance_edited)    
    return render(request,'create.html',{'frm':frm})


@login_required(login_url='login/')
def list(request):
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count
    recent_visits=MovieInfo.objects.filter(pk__in=recent_visits)


    
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    response=render(request,'list.html',{'movies':movie_set , 'visits':count , 'recent_visits':recent_visits })
    
    return  response

@login_required(login_url='login/')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()

    movie_set=MovieInfo.objects.all()
    
    return render(request,'list.html',{'movies':movie_set})

@login_required(login_url='login/')
def create(request):
    frm=Movieform()
    if request.POST:
       frm=Movieform(request.POST,request.FILES)
    if frm.is_valid:
           frm.save()
              
    else:
           frm=Movieform()    



    return render(request,'create.html',{'frm':frm})


def create(request):
    frm=Movieform()
    if request.POST:
       frm=Movieform(request.POST,request.FILES)
       if frm.is_valid():
           frm.save()
       else:
           frm=Movieform()    



    return render(request,'create.html',{'frm':frm})





     

    
