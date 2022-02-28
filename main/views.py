from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

from. import forms, models


# redirect to Homepage
def index(request):
    return redirect("/home")


@login_required    # redirect to login-page if not logged in
def home(request):
    # get tickets created by followed users or the user
    tickets = models.Ticket.objects.filter(
        Q(user__in=request.user.follows.all()) | Q(user=request.user)
    )
    # get reviews created by followed users or the user
    reviews = models.Review.objects.filter(
        Q(user__in=request.user.follows.all()) | Q(user=request.user)
    )
    # sort all items in feed, newest first
    feed = sorted(
        chain(tickets, reviews), key=lambda i: i.time_created, reverse=True
    )
    paginator = Paginator(feed, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "main/home.html", {'feed': page_obj})


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
                name = form.cleaned_data['follow_user'].capitalize()
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
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'main/create_ticket.html', {'form': form})


@login_required
def create_review(request, ticket_id):
    form = forms.ReviewForm()
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'form': form,
        'post': ticket,
    }
    return render(request, 'main/create_review.html', context)


@login_required
def create_ticket_with_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'main/create_review_with_ticket.html', context)


@login_required
def posts(request):
    # get tickets created by followed users or the user
    tickets = models.Ticket.objects.filter(
        Q(user__in=request.user.follows.all()) | Q(user=request.user)
    )
    # get reviews created by only the user
    reviews = models.Review.objects.filter(user=request.user)
    # sort all items in feed, newest first
    feed = sorted(
        chain(tickets, reviews), key=lambda i: i.time_created, reverse=True
    )
    paginator = Paginator(feed, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'feed': page_obj,
    }
    return render(request, "main/posts.html", context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    image_url = ''
    if ticket.image:
        image_url = ticket.image.url
    form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        form = forms.TicketForm(
            request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('posts')

    if request.method == 'GET':
        if image_url:
            form.fields["image"].widget.attrs[
                'data-text'] = 'Upload New File'

    context = {'form': form, 'image': image_url}
    return render(request, 'main/edit_ticket.html', context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket_id = review.ticket.id
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.ReviewForm(instance=review)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {'form': form, 'post': ticket}
    return render(request, 'main/edit_review.html', context)


@login_required
def delete_post(request, post_type, post_id):
    if post_type == 'Ticket':
        post = models.Ticket.objects.get(id=post_id)
    else:
        post = models.Review.objects.get(id=post_id)
    post.delete()
    return redirect('posts')
