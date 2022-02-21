from django import forms
from django.contrib.auth import get_user_model

from . import models


class FollowUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['follows']
        labels = {
            'follows': '',
        }


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
