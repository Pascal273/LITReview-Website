from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from. import forms


# redirect to Homepage
def index(request):
    return redirect("/home")


@login_required    # redirect to login-page if not logged in
def home(request):
    return render(request, "main/home.html", {})


@login_required
def following(request):
    form = forms.FollowUserForm()
    current_user = request.user
    follows = current_user.following.all()
    if request.method == 'POST':
        form = forms.FollowUserForm(request.POST)
        # follow users
        if form.is_valid():
            if form.cleaned_data:
                name = form.cleaned_data['follow_user']
                User = get_user_model()
                users = User.objects.all()
                # check if user exists
                if name in [user.username for user in users]:
                    # check if user is yourself
                    if name == current_user.username:
                        messages.info(request, "You cant Follow yourself!")
                    else:
                        # follow the user
                        user_to_follow = User.objects.get(username=name)
                        current_user.follows.add(user_to_follow)
                        return redirect('following')
                else:
                    messages.info(request, "User not found!")
        # unfollow users
        elif request.POST.get("unfollow"):
            user_to_unfollow = request.POST["unfollow"]
            current_user.follows.remove(user_to_unfollow)
            return redirect('following')
    return render(request, "main/following.html",
                  {'form': form, 'follows': follows})


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
