from django.shortcuts import render

# Price estimation logic
def houseprice(beds, baths, sqft, location, floors):
    bedprice = 20000
    bathprice = 30000
    sqftprice = 1200
    baseprice = 100000
    floorprice = 25000

    # Location multiplier dictionary
    location_multipliers = {
        'downtown': 1.5,
        'suburb': 1.2,
        'rural': 1.0,
    }

    # Default multiplier is 1.0
    location_multiplier = location_multipliers.get(location.lower(), 1.0)

    # Total price calculation
    price = baseprice + (bedprice * beds) + (bathprice * baths) + (sqftprice * sqft) + (floorprice * floors)
    price *= location_multiplier

    return int(price)

# House price estimator view
def estimate_house_price(request):
    if request.method == "GET":
        beds = request.GET.get('beds', 0)
        baths = request.GET.get('baths', 0)
        sqft = request.GET.get('sqft', 0)
        floors = request.GET.get('floors', 0)
        location = request.GET.get('location', 'rural')  # Default to 'rural'

        # Convert to integers with fallback
        try:
            beds = int(beds)
            baths = int(baths)
            sqft = int(sqft)
            floors = int(floors)
        except ValueError:
            beds = baths = sqft = floors = 0

        # Only estimate if all fields are valid
        if beds > 0 and baths > 0 and sqft > 0 and floors > 0:
            estimated_cost = houseprice(beds, baths, sqft, location, floors)
        else:
            estimated_cost = None

        return render(request, 'House/House.html', {
            'estimated_cost': estimated_cost,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'floors': floors,
            'location': location,
        })

# Simple greeting page
def greek(request, name):
    return render(request, 'House/greek.html', {'name': name})
from django.shortcuts import render

def home(request):
    return render(request, 'House/home.html')

def estimate(request):
    # you can include your price estimation logic here
    return render(request, 'House/estimate.html')

def contact(request):
    return render(request, 'House/contact.html')
