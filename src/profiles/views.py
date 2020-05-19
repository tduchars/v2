from django.shortcuts import render, redirect

from .models import UserAccount
from .forms import UserAccountForm
from smtp.smtpmail import account_mail_sender

def register(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['account_email']
            form.save()
            account_mail_sender(email, "confirmation")
            return redirect('/')
    
    else:
        form = UserAccountForm()
        context = {
            'form': form
        }

        return render(request, 'registration/register_user.html', context)