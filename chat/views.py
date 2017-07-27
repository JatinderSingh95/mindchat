from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.mail import send_mail, BadHeaderError
from chat.form import ContactForm
from .models import Chat
from django.conf import settings
from chat.models import Createclass
from django.contrib.auth.models import User
from chat.form import SignUpForm, UserChangeForm, EditProfileform
#ProfileForm
data={}

def SubscriptionView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
	
	form_message = form.cleaned_data.get('message')
	emailto = form.cleaned_data.get('email_to')
	form_full_name = form.cleaned_data.get('full_name')
	sub = form.cleaned_data.get('subject')
	subject = sub
	from_email = settings.EMAIL_HOST_USER
	to_email =[from_email, emailto]
	contact_message = " %s "%(
            
            form_message)			
	send_mail(subject,
	        contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)
	return redirect('Function')		
    else:
        form = ContactForm()
    return render(request, 'forn.html', {'form': form})
	
class ServerForm(ModelForm):
    class Meta:
        model = Createclass
        fields = ['Title','Subject','date','From','to','instructor','description']
		
def server_list1(request, template_name='rest.html'):
    chat = Createclass.objects.all()
    data = {}
    data['object_list'] = chat
    return render(request, template_name, data)
	
def server_create(request, template_name='server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
		Createclass =form.save(commit=False)
		Createclass.user=request.user
		Createclass.save()
		return redirect('Function')
    return render(request, template_name, {'form':form})
	
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.utype = form.cleaned_data.get('utype')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('server_list')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


#class ServerForm(ModelForm):
 #   class Meta:
  #      model = Class
   #     fields = ['Title','user']
	
		
def server_list(request, template_name='server_list.html'):
	users = User.objects.all()
	#data = {}
	data['object_list'] = users
		
	return render(request, template_name)
	
def Function(request, template_name='rest.html'):
	chat = Createclass.objects.all()
	
	data['object_list'] = chat
	return render(request, template_name, data)	
	
def Ateacher1(request, template_name='update.html'):

    users = User.objects.all()
	#data = {}
    data['object_list'] = users
    return render(request, template_name, data)

			
def server_update(request, pk, template_name='Addrest.html'):
    users = get_object_or_404(User, pk=pk) 
	
    form = EditProfileform(request.POST or None, instance=users)
    if form.is_valid():
        user=form.save()
		#user.refresh_from_db()  # load the profile instance created by the signal
        user.profile.utype = form.cleaned_data.get('utype')
        user.save()
        return redirect('Ateacher1')
    return render(request, template_name, {'form':form})	
		   
def Home(request,pk,template_name='home.html'):
    createclass = get_object_or_404(Createclass, pk=pk)
    c = Chat.objects.all()
    return render(request, template_name, {'home': 'active', 'chat': c, 'object':createclass})

	
def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')
	
def Messages1(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})
	
def Messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})

def server_delete(request, pk, template_name='server_confirm_delete.html'):
    createclass = get_object_or_404(Createclass, pk=pk)    
    if request.method=='POST':
        createclass.delete()
        return redirect('Function')
    return render(request, template_name, {'object':createclass})
	
def server_class(request, pk, template_name='server_class.html'):
    createclass = get_object_or_404(Createclass, pk=pk)    
    if request.method=='POST':
        
        return redirect('')
    return render(request, template_name, {'object':createclass})	
		