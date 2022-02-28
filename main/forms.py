from django import forms

from . import models


class FollowUserForm(forms.Form):
    follow_user = forms.CharField(
        max_length=30,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )


class TicketForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={'hidden': 'hidden'}
        ),
    )

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    CHOICES = [('0', '- 0'), ('1', '- 1'), ('2', '- 2'),
               ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
