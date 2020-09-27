from django.shortcuts import render
import requests
# Create your views here.
from weatherapp.forms import CityForm
from weatherapp.models import City



def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    if request.method=="POST":
        form=CityForm(request.POST)
        form.save()
    #city='Las Vegas'
    form = CityForm()
    cities=City.objects.all()
    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={'city':city,'temperature':r['main']["temp"],'description':r["weather"][0]["description"],'icon':r["weather"][0]["icon"],}
        weather_data.append(city_weather)
        context={'weather_data':weather_data,'form':form}
    return render(request,'weather.html',context)

