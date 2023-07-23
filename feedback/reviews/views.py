from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        ###example if you want to update and existing review
        # existing_data = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_data)

        if form.is_valid():
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating'])
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })

def thank_you(request):
    return render(request, "reviews/thank_you.html")