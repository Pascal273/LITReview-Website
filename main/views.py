from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from. import forms


# redirect to Homepage
def index(request):
    return redirect("/home")


@login_required    # redirect to login-page if not logged in
def home(request):
    return render(request, "main/home.html", {})


@login_required
def following(request):

    form = forms.FollowUserForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, "main/following.html", {'form': form})


@login_required
def create_ticket(request):
    form = forms.CreateTicketForm()
    if request.method == 'POST':
        form = forms.CreateTicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('home')
    return render(request, 'main/create_ticket.html', {'form': form})


@login_required
def create_review(request):
    form = forms.CreateReviewForm()
    if request.method == 'POST':
        form = forms.CreateReviewForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    return render(request, 'main/create_review.html', {'form': form})


@login_required
def create_ticket_with_review(request):
    ticket_form = forms.CreateTicketForm()
    review_form = forms.CreateReviewForm()
    if request.method == 'POST':
        ticket_form = forms.CreateTicketForm(request.POST, request.FILES)
        review_form = forms.CreateReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket_form.save()
            review_form.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'main/create_review_with_ticket.html', context)
