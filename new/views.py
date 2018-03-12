
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.core.mail import send_mail

class register(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class HomePageView(TemplateView):
    template_name= 'home.html'
    def get_context_data(self, **kwargs):
        users =self.request.user
        number = users.id
        post=Post.objects.filter(user=number)
        userprof=User.objects.exclude(username=users)
        context = super(HomePageView , self).get_context_data( **kwargs)
        context.update({'users': users,'post':post,'userprof': userprof, 'form': PostForm,})
        return context




def Profile(request):
     number=request.GET['username']
     usser=User.objects.get(username__iexact=number)
     c = relation.objects.filter(connected=request.user).filter(main= number).filter(flag=True)
     if(not c):
         post = Post.objects.filter(user=usser).filter(privacy__in=['public', ])
         context = {'post': post, 'number': number, 'usser': usser}
         return render(request, 'profile.html', context)

     else:
         post = Post.objects.filter(user=usser).filter(privacy__in=['public', 'friends'])
         context={'post':post,'number':number,'ussr':usser}
         return render(request,'profile.html',context)



class performs(View):


    def get(self,request):
        form = PostForm()
        return render(request, 'home.html', {'form': form})



    def post(self,request):

            form = PostForm(request.POST)

            if form.is_valid():

              #  permission=form.cleaned_data.get('privacy') #getting the permission element
                useris = request.user.id
                obj = form.save(commit=False)
                obj.user=request.user
                obj.save()

            return HttpResponseRedirect('http://127.0.0.1:8000')


def details(request):
    number = request.GET['username']
    usser = User.objects.get(username__iexact=number)
    context = {'usser': usser }
    return render(request, 'details.html', context)


class connect(View):

    def get(self,request):
        form1 = connectform()
        return render(request, 'aa.html', {'form1': form1})



    def post(self,request):

        form1 = connectform(request.POST)
        name=  request.GET.get("username")
        obj=  request.user
        r=relation(connected=request.user,main=name)
        send_mail(
            'FRIEND REQUEST from '+str(request.user),
            'HEY YOU GOT A REQUEST TO ACCEPT CLICK http://127.0.0.1:8000/newjoin/?username='+str(obj),
            'webmaster@localhost',
            ['to@example.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect('http://127.0.0.1:8000')



class newjoin(View):


    def get(self,request):
        name=  request.GET.get("username")
        obj=  User.objects.get(username=name)

        r1=relation.objects.filter(main=request.user).filter(connected=obj).filter(flag=True)
        if(r1):
             return render(request, "error.html", {'error': "alreadyfriends"})

        else:
            r = relation(connected=obj, main=request.user,flag=True)
            if(r is not None):
              r.save()
              return render(request,'connected.html',{'cont':"congratulations you are connected "})









