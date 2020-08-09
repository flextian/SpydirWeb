from typing import Union

from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import Profile
from myplace.forms import ProfileCommentForm


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return HttpResponseRedirect(reverse('user-profile', kwargs={'username_or_id': request.user.username}))


def user(request, username_or_id: Union[int, str]):
    try:
        profile = _get_profile(username_or_id)
    except Profile.DoesNotExist:
        messages.error(request, 'That user profile does not exist.')
        return render(request, 'users/home.html')

    if request.method == 'POST':
        return add_profile_comment(request, profile)
    else:
        context = {
            'profile': profile,
            'title': profile,
            'custom_css': profile.profile_css,
            'new_comment_form': ProfileCommentForm()
        }
        return render(request, 'myplace/profile.html', context)


def _get_profile(username_or_id: Union[int, str]) -> Profile:
    """
    Tries to get Profile model object based on user id or username.

    :return: Profile object
    """
    if isinstance(username_or_id, int):
        return Profile.objects.get(id=username_or_id)
    else:
        return Profile.objects.get(user__username=username_or_id)


def add_profile_comment(request, profile: Profile):
    comment_form = ProfileCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user_profile = profile
        comment.author = request.user.profile
        comment.save()

        messages.success(request, 'Comment added.')
        return redirect(request.build_absolute_uri())
    else:
        messages.error(request, 'Comment is invalid-')
        return redirect(request.build_absolute_uri())


def blog(request, username_or_id: Union[int, str]):
    try:
        profile = _get_profile(username_or_id)
    except Profile.DoesNotExist:
        messages.error(request, 'That user profile does not exist.')
        return render(request, 'users/home.html')

    context = {
        'profile': profile,
        'title': profile,
        'custom_css': profile.profile_css,
    }
    return render(request, 'myplace/blog.html', context)
