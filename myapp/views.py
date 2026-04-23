
from .models import ticket


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

def home(request):
    return render(request, template_name='myapp/home.html')

def about(request):
    return render(request, template_name='myapp/about.html')

def help(request):
    return render(request, template_name='help.html')

def ticket_list(request):
    q = request.GET.get('q', '')
    if q:
        tickets = ticket.objects.filter(ticket_name__icontains=q)
    else:
        tickets = ticket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, template_name='myapp/all_tickets.html', context=context)

def ticket_details(request, id):
    ticket_obj = get_object_or_404(ticket, id=id)
    return render(request, 'myapp/details_ticket.html', {'ticket': ticket_obj})

def upload_ticket(request):
    form = ticketForm()
    if request.method == 'POST':
        form = ticketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_tickets')
    context = {'form': form}
    return render(request, template_name='myapp/ticket_form.html', context=context)

def update_ticket(request, id):
    ticket_obj = ticket.objects.get(pk=id)
    form = ticketForm(instance=ticket_obj)
    if request.method == 'POST':
        form = ticketForm(request.POST, request.FILES, instance=ticket_obj)
        if form.is_valid():
            form.save()
            return redirect('all_tickets')
    context = {'form': form}
    return render(request, template_name='myapp/ticket_form.html', context=context)

def delete_ticket(request, id):
    ticket_obj = ticket.objects.get(pk=id)
    if request.method == 'POST':
        ticket_obj.delete()
        return redirect('all_tickets')
    return render(request, template_name='myapp/delete_ticket.html')

def purchase_ticket(request, ticket_id):
    ticket_obj = get_object_or_404(ticket, id=ticket_id)
    return render(request, 'purchase-ticket.html', {'ticket': ticket_obj})

def contact(request):
    return render(request, 'contact.html')