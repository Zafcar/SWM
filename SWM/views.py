from django.shortcuts import render
from django.shortcuts import render
import matplotlib.pyplot as plt

from io import StringIO
import folium
import datetime
from .models import static_route, collection_location, realtime_location

def maps(request):

    points = static_route.objects.all()
    f = folium.Figure(width = 900, height = 800)
    
    m = folium.Map(location= [12.972442, 77.580643], tiles="openstreetmap",
    zoom_start=-12, min_zoom = 11).add_to(f)
    
    all_points = []

    for pin_points in points:
        coordinates = (pin_points.Latitude, pin_points.Longitude)
        all_points.append(coordinates)
        folium.Marker(coordinates).add_to(m)

    folium.PolyLine(all_points, color='red', weight=2, opacity=0.8).add_to(m)


    if request.method == "POST":
        lat = float(request.POST.get("lat"))
        lon = float(request.POST.get("lon"))
        time = request.POST.get("time")
        stud = static_route.objects.all()

        static_route.objects.create(Time = time, Latitude = lat, Longitude = lon)
        
    return render(request, "maps.html", {'maps' : m._repr_html_()})

def collection(request):
    if request.method == "POST":
        name = request.POST.get("user")

        lat = float(request.POST.get("lat"))
        lon = float(request.POST.get("lon"))

        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")


        phone = int(request.POST.get("phone"))
        garbage = request.POST.get("type")
        # print(lat, lon, phone, garbage)
        collection_location.objects.create(Name = name,  Phone = phone, Start_date = start_date, End_date = end_date, Start_time = start_time, End_time = end_time, Latitude = lat, Longitude = lon, Garbage_type = garbage)
        
    return render(request, "collection.html")

def index(request):
    return render(request, "index.html")

def display(request):
    data = collection_location.objects.all()
    name = []
    phone = []
    start_date = []
    end_date = []
    start_time = []
    end_time = []
    lat = []
    lon = []
    garbage = []

    for i in data:
        name.append(i.Name)
        phone.append(i.Phone)
        start_date.append(i.Start_date)
        end_date.append(i.End_date)
        start_time.append(i.Start_time)
        end_time.append(i.End_time)
        lat.append(i.Latitude)
        lon.append(i.Longitude)
        garbage.append(i.Garbage_type)

    data1 = zip(name, phone, start_date, end_date, start_time, end_time, lat, lon, garbage)
    print(data1)

    return render(request, "display.html", {'data1': data1})

def return_graph(x, y):

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data



def live_dashboard(request):
    real = realtime_location.objects.all()
    static = static_route.objects.all()

    count = 0
    Time = 0

    current_weight = 0
    weight = []
    time = []
    real_location = []
    static_location = []
    current_location = []

    for i in real:
        weight.append(i.Weight)


    for i in real:
        real_location.append([i.Latitude, i.Longitude, i.Time, i.Weight])
        time.append(str(i.Time))
        
    for j in static:
        static_location.append([j.Latitude, j.Latitude, j.Time])

    total_no_of_stops = len(static_location)

    for i in real_location:
        for j in static_location:
            if((i[0] - j[0] >= 0 and i[0] - j[0] < 5) or (i[1] - j[1] >= 0 and i[1] - j[1] < 5)):
                count += 1
                Time = int(datetime.timedelta(hours=i[2].hour, minutes=i[2].minute, seconds=i[2].second).total_seconds()) - int(datetime.timedelta(hours=j[2].hour, minutes=j[2].minute, seconds=j[2].second).total_seconds())
                current_location = [i[0], i[1]]
                # print(int(datetime.timedelta(hours=i[2].hour, minutes=i[2].minute, seconds=i[2].second).total_seconds()))
                current_weight = i[3]
    
                # print(weight)
                static_location.remove(j)

    print(time, weight)

    # print(count, total_no_of_stops)
    percentage = count/total_no_of_stops
    graph = return_graph(time, weight)
    # print(percentage)
    return render(request, "Live_information.html", {"pecen" : percentage, 'Time' : Time/60, 'Location' : current_location, 'weight' : current_weight, 'graph' : graph })

# Create your views here.
