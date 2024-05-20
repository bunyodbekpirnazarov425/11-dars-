from django.shortcuts import render, get_object_or_404, redirect
from .models import Country, States, Airline
from .forms import CountryForm

def home(request):
    states = States.objects.all()
    country = Country.objects.all()
    airlines = Airline.objects.all()
    return render(request, template_name="home.html", context={"count":country, 'states': states, "airlines":airlines})

def batafsil(request, id):
    counts = get_object_or_404(Country, id=id)
    country = Country.objects.all()
    airlines = Airline.objects.all()
    states = States.objects.all()
    return render(request, template_name="batafsil.html", context={"count":country, "counts":counts, "states":states, "airlines":airlines})

def create_country(request):
    count = CountryForm()
    category = Country.objects.all()
    airlines = Airline.objects.all()
    states = States.objects.all()
    if request.method == 'POST':
        count = CountryForm(request.POST, request.FILES)
        if count.is_valid():
            count.save()
            return redirect('home_page')
    return render(request, template_name="create_country.html", context={"count": count, "cats":category, "states":states, "airlines":airlines})

def update_country(request, id):
    country = Country.objects.get(id=id)
    states = States.objects.all()
    airlines = Airline.objects.all()
    count = CountryForm(instance=country)
    
    if request.method == 'POST':
        count = CountryForm(request.POST, instance=country)
        if count.is_valid():
            count.save()
            return redirect('home_page')
    return render(request, template_name="create_country.html", context={"count":count, "states":states, "airlines":airlines})


def delete_country(request, id):
    country = Country.objects.get(id=id)
    country.delete()
    return redirect('home_page')

def contact(request):
    states = States.objects.all()
    airlines = Airline.objects.all()
    return render(request, template_name="contact.html", context={"states":states, "airlines":airlines})

# def states(request):
#     states = States.objects.all()
#     airlines = Airline.objects.all()
#     return render(request, template_name="home.html", context={"states":states, "airlines":airlines})

# def airlines(request, id):
#     airlines = Airline.objects.get(id=id)
#     states = States.objects.all()
#     return render(request, template_name="airline.html", context={"airlines":airlines, "states":states})

def airlines_list(request):
    airlines = Airline.objects.all()
    states = States.objects.all()
    return render(request, 'airlines.html', {'airlines': airlines, 'states': states})

def airline_detail(request, id):
    airlines = Airline.objects.all()
    states = States.objects.all()
    airline = get_object_or_404(Airline, id=id)
    return render(request, 'airline.html', {'airline': airline, 'airlines': airlines, 'states': states})

def states_page(request, id):
    state = get_object_or_404(States, id=id)
    airlines = Airline.objects.all()
    states = States.objects.all()
    return render(request, 'stets.html', {'state': state, 'airlines': airlines, 'states': states})