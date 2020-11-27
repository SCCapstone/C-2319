#from django.shortcuts import render
from .forms import UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('../login')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'users/delete_account.html', context)
