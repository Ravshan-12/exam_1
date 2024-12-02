from django.shortcuts import render, redirect
from .models import Taxi


def taxi_list(request):
        name = request.GET.get('name')
        license_plate = request.GET.get('license_plate')
        driver_name = request.GET.get('driver_name')
        passenger_capacity = request.GET.get('passenger_capacity')
        car_model = request.GET.get('car_model')
        status = request.GET.get('status')
        if name and license_plate and driver_name and passenger_capacity and car_model and status:
            Taxi.objects.create(
                name=name,
                license_plate=license_plate,
                driver_name=driver_name,
                passenger_capacity=int(passenger_capacity),
                car_model=car_model,
                status=status
            )
        taxis = Taxi.objects.all()
        ctx = {'taxis': taxis}
        return render(request, 'taxi/taxi-list.html', ctx)
