from django.template import Library
from django.utils import timezone

register = Library()


@register.filter
def model_type(value):
    """filter that returns the name of the model of an instance"""
    return type(value).__name__


@register.simple_tag(takes_context=True)
def display_poster(context, user):
    """displays 'You' if the logged in created the post"""
    if context['user'] == user:
        return 'You'
    return user.username


@register.filter
def get_posted_at_display(post_time):
    timedelta = timezone.now() - post_time
    minutes = round(int(timedelta.total_seconds()) / 60)
    hours = round(minutes / 60)
    if minutes <= 60:
        return f'{minutes} minutes ago.'
    elif hours <= 24:
        return f'{hours} hours ago'
    return post_time.strftime('%I:%M %p, %a %d, %Y')
