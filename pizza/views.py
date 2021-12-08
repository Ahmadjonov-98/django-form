from django.shortcuts import render, redirect
from django.contrib import messages

from pizza.forms import PizzaForm


def home(request):
    return render(request, "pizza/home.html")


def order(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            note = "Thanks for ordering, your {0} {1} and {2} pizza on the way".format(data["size"], data["topping1"],
                                                                                       data["topping2"])
            # messages.success(request,"Your order was successfully added")
            form = PizzaForm()
            return render(request, "pizza/order.html", context={"form": form, "note": note})
        else:
            messages.error(request, "Error saving form")
        return redirect("home")
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', context={"form": form})
