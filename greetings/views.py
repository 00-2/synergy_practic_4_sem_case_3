from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import GreetingForm
from .models import Greeting


@require_http_methods(["GET", "POST"])
def home(request):
    form = GreetingForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        request.session["greeting_id"] = form.save().pk
        return redirect("home")

    greeting = Greeting.objects.filter(pk=request.session.get("greeting_id")).first()
    return render(request, "greetings/home.html", {"form": form, "greeting": greeting})
