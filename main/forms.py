from django import forms
from django.contrib.auth import get_user_model
from django.forms import RadioSelect

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
    CHOICES = [('0', '- 0'), ('1', '- 1'), ('2', '- 2'),
               ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
