from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from .forms import ImageForm, PostForm
from .models import Images, Post, User

from django.views.generic import RedirectView


@login_required
def post(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponse("Успешно")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'gallery/uploadimg.html',
                  {'postForm': postForm, 'formset': formset})


def gallery(request):
    posts = Post.objects.all()
    images = Images.objects.all()
    return render(request, 'gallery/gallery.html', {"posts": posts, "images": images})


def like(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    user = request.user
    liked = False
    if user.is_authenticated:
        if request.method == 'POST':
            if posts.likes.filter(id=user.id).exists():
                posts.likes.remove(user)
                liked = False
            else:
                posts.likes.add(user)
                liked = True
            posts.save()
    data = {
        "likes": liked,
        "likes_count": posts.likes_count()
            }
    return JsonResponse(data)



