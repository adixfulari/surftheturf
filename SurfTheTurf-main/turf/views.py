from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
import math
from datetime import date, datetime, timedelta

from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from pytz import timezone
import time
import razorpay
from django.views.decorators.csrf import csrf_exempt

def index(request):

    # days=[
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    # matrix = bookslot(week = days)
    # matrix.save()
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'mainpage_index.html', {'username':username})
    return render(request, 'mainpage_index.html')


def book_now(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'booking_index.html', {'username':username})
    return render(request, 'booking_index.html')


def turf_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    return render(request, 'turfblog.html', {'currentDate': currentDate, 'endDate': endDate})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('book_now')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'signIn.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already Taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signUp.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# Individual turf detail views
def turf1_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'JP Sports Arena',
        'location': 'Kothrud',
        'sports': 'Cricket, Football(7v7)',
        'address': 'Survey No. 25, Kothrud, Near COEP College, Pune, Maharashtra 411038',
        'map_link': 'https://goo.gl/maps/uPWKekGSQDH3jafW9',
        'images': ['image1.jpeg', 'image2.png', 'image3.png']
    }
    return render(request, 'turf1_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf2_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Baner Sports Club',
        'location': 'Baner',
        'sports': 'Cricket, Football(5v5)',
        'address': 'Plot No. 15, Baner Road, Near Aundh ITI, Baner, Pune, Maharashtra 411045',
        'map_link': '#',
        'images': ['turf2.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf3_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Wakad Champions Ground',
        'location': 'Wakad',
        'sports': 'Cricket, Football(6v6)',
        'address': 'Survey No. 45, Wakad Main Road, Near Bajaj Institute, Wakad, Pune, Maharashtra 411057',
        'map_link': '#',
        'images': ['turf3.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf4_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Hinjewadi Sports Arena',
        'location': 'Hinjewadi',
        'sports': 'Cricket, Football(6v6)',
        'address': 'Phase 2, Hinjewadi IT Park, Near Wipro Circle, Hinjewadi, Pune, Maharashtra 411057',
        'map_link': '#',
        'images': ['turf4.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf5_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Viman Nagar Sports Complex',
        'location': 'Viman Nagar',
        'sports': 'Cricket, Football(7v7)',
        'address': 'Survey No. 32, Viman Nagar, Near Phoenix Mall, Viman Nagar, Pune, Maharashtra 411014',
        'map_link': '#',
        'images': ['turf5.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf6_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Koregaon Park Sports Hub',
        'location': 'Koregaon Park',
        'sports': 'Cricket, Football(5v5), Badminton',
        'address': 'Lane 5, Koregaon Park, Near Osho Ashram, Koregaon Park, Pune, Maharashtra 411001',
        'map_link': '#',
        'images': ['turf6.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf7_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Magarpatta Sports City',
        'location': 'Magarpatta',
        'sports': 'Cricket, Football(8v8)',
        'address': 'Magarpatta City, Cybercity, Near Aditya Birla Memorial Hospital, Magarpatta, Pune, Maharashtra 411013',
        'map_link': '#',
        'images': ['turf7.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})

def turf8_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    turf_data = {
        'name': 'Aundh Sports Center',
        'location': 'Aundh',
        'sports': 'Cricket, Football(6v6)',
        'address': 'Survey No. 18, Aundh-Ravet Road, Near University of Pune, Aundh, Pune, Maharashtra 411007',
        'map_link': '#',
        'images': ['turf8.png', 'image2.png', 'image3.png']
    }
    return render(request, 'generic_turf_blog.html', {'currentDate': currentDate, 'endDate': endDate, 'turf': turf_data})
    
# def booking(request, id):
#     if request.method == 'POST':
#         username = request.POST['username']
#         lastName = request.POST['lastName']
#         fromCity = request.POST['fromCity']
#         toCity = request.POST['toCity']
#         depatureDate = request.POST['depatureDate']
#         days = request.POST['days']
#         noOfRooms = int(request.POST['noOfRooms'])
#         noOfAdults = int(request.POST['noOfAdults'])
#         noOfChildren = int(request.POST['noOfChildren'])
#         email = request.POST['email']
#         phoneNo = request.POST['phoneNo']
#         totalAmount = int(request.POST['totalAmount'])

#         request.session['fname'] = username
#         request.session['lname'] = lastName
#         request.session['to_city'] = toCity
#         request.session['from_city'] = fromCity
#         request.session['depature_date'] = depatureDate
#         request.session['arrival_date'] = days
#         request.session['no_of_rooms'] = noOfRooms
#         request.session['no_of_adults'] = noOfAdults
#         request.session['no_of_children'] = noOfChildren
#         request.session['email'] = email
#         request.session['phone_no'] = phoneNo
#         request.session['total_amount'] = totalAmount

#         requiredRooms = 1
#         if noOfAdults/3 > 1:
#             requiredRooms = math.ceil(noOfAdults/3)

#         if noOfRooms < requiredRooms:
#             noOfRooms = requiredRooms - noOfRooms
#             messages.info(
#                 request, 'For adding more travellers, Please add' + str(noOfRooms) + ' more rooms')
#             return redirect('booking', id)

#         if noOfRooms > noOfAdults:
#             messages.info(request, 'Minimum 1 Adult is required per Room')
#             return redirect('booking', id)

#         if (noOfAdults + noOfChildren)/4 > 1:
#             requiredRooms = math.ceil((noOfAdults + noOfChildren)/4)

#         if noOfRooms < requiredRooms:
#             noOfRooms = requiredRooms - noOfRooms
#             messages.info(
#                 request, 'For adding more travellers, Please add' + str(noOfRooms) + 'more rooms')
#             return redirect('booking', id)

#         noOfRooms = requiredRooms
#         request.session['no_of_rooms'] = noOfRooms
#         print("No of rooms = ", noOfRooms)
#         print("Working")
#         return redirect('receipt')
#     else:
#         return render(request, 'booking.html')


# @login_required(login_url='/accounts/login')
# def receipt(request):
    # first_name = request.session.get('fname')
    # print(first_name)
    # last_name = request.session.get('lname')
    # print(last_name)

    # tour_amount = int(request.session.get('total_amount'))  # Per person
    # print(tour_amount)
    # adults = int(request.session.get('no_of_adults'))
    # print(adults)
    # rooms = int(request.session.get('no_of_rooms'))
    # print(rooms)
    # children = int(request.session.get('no_of_children'))
    # print(adults)
    # if rooms > 1:
    #     totalCost = tour_amount*adults + tour_amount*children/2 + rooms*tour_amount/4
    # else:

    #     totalCost = tour_amount*adults + tour_amount*children/2

    # request.session['total_amount'] = str(totalCost)
    # print("Hello")

    # print(totalCost)
    # request.session['total_amount'] = tour_amount

    # today = date.today()

    # t = time.localtime()
    # currentTime = time.strftime("%H:%M:%S", t)
    # return render(request, 'receipt.html', {'totalCost': totalCost, 'date': today, 'currentTime': currentTime})


# def search(request):

    # # dests = Destination.objects.all()
    # query = request.GET['query']
    # # budget = request.GET['budget']
    # price = Destination.objects.all()
    # # print(price.price)
    # print(query)
    # # print("Price = ", budget)
    # dests = Destination.objects.filter(name__icontains=query)
    # print(dests)
    # # print(dests)

    # return render(request, 'search.html', {'dests': dests, 'query': query})
    # # return HttpResponse('This is search')


# def confirm_booking(request):
    # if request.method == 'POST':
    #     fullName = request.POST['fullName']
    #     fromCity = request.POST['fromCity']
    #     toCity = request.POST['toCity']
    #     depatureDate = request.POST['depatureDate']
    #     arrivalDate = request.POST['days']
    #     noOfRooms = int(request.POST['noOfRooms'])
    #     noOfAdults = int(request.POST['noOfAdults'])
    #     noOfChildren = int(request.POST['noOfChildren'])
    #     email = request.POST['email']
    #     phoneNo = request.POST['phoneNo']
    #     amountPerPerson = request.POST['amountPerPerson']
    #     totalAmount = float(request.POST['totalAmount'])
    #     userName = request.user.username

    #     books = ConfirmBooking(fullName=fullName, fromCity=fromCity, toCity=toCity,
    #                            depatureDate=depatureDate, days=arrivalDate, noOfRooms=noOfRooms, noOfAdults=noOfAdults,
    #                            noOfChildren=noOfChildren, email=email, phoneNo=phoneNo, amountPerPerson=amountPerPerson,
    #                            totalAmount=totalAmount, userName=userName)
    #     books.save()

    #     message = render_to_string('order_placed_body.html', {'fullName': fullName, 'fromCity': fromCity, 'toCity': toCity, 'depatureDate': depatureDate, 'arrivalDate': arrivalDate,
    #                                'noOfRooms': noOfRooms, 'noOfAdults': noOfAdults, 'noOfChildren': noOfChildren, 'email': email, 'phoneNo': phoneNo, 'amountPerPerson': amountPerPerson, 'totalAmount': totalAmount})
    #     msg = EmailMessage(
    #         'Tripology',
    #         message,
    #         settings.EMAIL_HOST_USER,
    #         [request.user.email]
    #     )
    #     msg.content_subtype = "html"  # Main content is now text/html
    #     msg.send()

    #     print("Mail successfully sent")

    #     print("User Added")

    #     return redirect('/')
    # else:
    #     return render(request, 'booking.html')


update = {"1"}

@login_required(login_url='login')
def slot_details(request):
    if request.method == 'POST':
        selectedDate = request.POST['selectedDate']
        request.session['selectedDate'] = selectedDate
    else:
        selectedDate = request.session.get('selectedDate', date.today().strftime("%Y-%m-%d"))
    slots = turfBooking.objects.all()
    
    # days=[
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    # matrix = bookslot(week = days)
    # matrix.save()
    matrix = bookslot.objects.get(id='1')
    print("Matrix Before")
    print(matrix.week)

    choosenDay = datetime.strptime(selectedDate, "%Y-%m-%d").strftime("%A")
    curentTime = datetime.now().strftime("%H:%M:%S")

    tomorrowDate = (datetime.now() + timedelta(days=1)
                    ).strftime("%Y-%m-%d")
    currentDate = datetime.now().strftime("%Y-%m-%d")
    # currentDate = tomorrowDate
    update.add(tomorrowDate)
    print("Array = ", update)
    for j in update.copy():
        if(currentDate == str(j)):
            dayTobeDeleated = (
                datetime.now() - timedelta(days=1)).strftime("%A")
            # dayTobeDeleated = "Wednesday"
            update.remove(currentDate)
            print(update)
            print("Day to be deleated: ", dayTobeDeleated)
            if dayTobeDeleated == "Monday":
                for i in range(1, 20):
                    matrix.week[0][i] = 0
            elif dayTobeDeleated == "Tuesday":
                for i in range(1, 20):
                    matrix.week[1][i] = 0
            elif dayTobeDeleated == "Wednesday":
                for i in range(1, 20):
                    matrix.week[2][i] = 0
            elif dayTobeDeleated == "Thursday":
                for i in range(1, 20):
                    matrix.week[3][i] = 0
            elif dayTobeDeleated == "Friday":
                for i in range(1, 20):
                    matrix.week[4][i] = 0
            elif dayTobeDeleated == "Saturday":
                for i in range(1, 20):
                    matrix.week[5][i] = 0
            elif dayTobeDeleated == "Sunday":
                for i in range(1, 20):
                    matrix.week[6][i] = 0

    ls = []
    if choosenDay == "Monday":
        for j in range(20):
            ls.append(str(matrix.week[0][j]))
    elif choosenDay == "Tuesday":
        for j in range(20):
            ls.append(str(matrix.week[1][j]))
    elif choosenDay == "Wednesday":
        for j in range(20):
            ls.append(str(matrix.week[2][j]))
    elif choosenDay == "Thursday":
        for j in range(20):
            ls.append(str(matrix.week[3][j]))
    elif choosenDay == "Friday":
        for j in range(20):
            ls.append(str(matrix.week[4][j]))
    elif choosenDay == "Saturday":
        for j in range(20):
            ls.append(str(matrix.week[5][j]))
    elif choosenDay == "Sunday":
        for j in range(20):
            ls.append(str(matrix.week[6][j]))

    print("Matrix After")
    print(matrix.week)
    return render(request, 'turfBooking.html', {'currentDate': currentDate, 'selectedDate': selectedDate,  'list': ls})


def turfDateSelection(request):

    if request.method == 'POST':
        selectedDate = request.POST['selectedDate']
        request.session['choosenDate'] = selectedDate
        return redirect('turf_bookings')
    else:
        currentDate = date.today().strftime("%Y-%m-%d")
        # print(currentDate)
        endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
        return render(request, 'turfDateSelection.html', {'currentDate': currentDate, 'endDate': endDate})


def turfBilling(request):
    if request.method == 'POST':
        currentDate = date.today().strftime("%Y-%m-%d")
        selectedDate = request.POST['date']
        list_of_input_ids = request.POST.getlist('id')
        print(list_of_input_ids)

        selectedTime = []
        # checkingTime = []
        bookedSlots = []
        for i in list_of_input_ids:
            if i == '1':
                bookedSlots.append('6-7 am')
                selectedTime.append('06:00:00')
            elif i == '2':
                bookedSlots.append('7-8 am')
                selectedTime.append('07:00:00')
            elif i == '3':
                bookedSlots.append('8-9 am')
                selectedTime.append('08:00:00')
            elif i == '4':
                bookedSlots.append('9-10 am')
                selectedTime.append('09:00:00')
            elif i == '5':
                bookedSlots.append('10-11 am')
                selectedTime.append('10:00:00')
            elif i == '6':
                bookedSlots.append('11-12 am')
                selectedTime.append('11:00:00')
            elif i == '7':
                bookedSlots.append('12-1 pm')
                selectedTime.append('12:00:00')
            elif i == '8':
                bookedSlots.append('1-2 pm')
                selectedTime.append('13:00:00')
            elif i == '9':
                bookedSlots.append('2-3 pm')
                selectedTime.append('14:00:00')
            elif i == '10':
                bookedSlots.append('3-4 pm')
                selectedTime.append('15:00:00')
            elif i == '11':
                bookedSlots.append('4-5 pm')
                selectedTime.append('16:00:00')
            elif i == '12':
                bookedSlots.append('5-6 pm')
                selectedTime.append('17:00:00')
            elif i == '13':
                bookedSlots.append('6-7 pm')
                selectedTime.append('18:00:00')
            elif i == '14':
                bookedSlots.append('7-8 pm')
                selectedTime.append('19:00:00')
            elif i == '15':
                bookedSlots.append('8-9 pm')
                selectedTime.append('20:00:00')
            elif i == '16':
                bookedSlots.append('9-10 pm')
                selectedTime.append('21:00:00')
            elif i == '17':
                bookedSlots.append('10-11 pm')
                selectedTime.append('22:00:00')
            elif i == '18':
                bookedSlots.append('11-12 pm')
                selectedTime.append('23:00:00')
            elif i == '19':
                bookedSlots.append('12-1 am')
                selectedTime.append('00:00:00')

        print("BookedSlots :")
        print(bookedSlots)
        totalAmount = len(bookedSlots) * 700

        # Prevent double booking: check for conflicts on same date and overlapping slots
        existing = TurfBooked.objects.filter(selected_date=selectedDate, paid=True)
        taken = set()
        for b in existing:
            taken.update(b.slots or [])
        if set(bookedSlots) & taken:
            messages.error(request, 'One or more selected time-slots are already booked. Please choose different slots.')
            request.session['selectedDate'] = selectedDate
            return redirect('slot_details')

        details = {
            'username': request.user.username,
            'email': request.user.email,
            'selectedDate': selectedDate,
            'currentDate': currentDate,
            'bookedSlots': bookedSlots,
            'totalAmount': totalAmount,
            'list_of_input_ids': list_of_input_ids
        }
        print("Turf Billing")
        print("Matrix in Billing")
        
        booking_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')
        keyId = 'rzp_test_9e8xrjzBFp5O7M'
        keySecret = 's4qIuVEiSi128ucHK9uAzoAU'

        client = razorpay.Client(auth=(keyId, keySecret))

        DATA = {
            # Amount will be in its smallest unit, that is Paisa (Therefore multiplying by 100 to convert amount in Rs to Paisa)
            "amount": int(totalAmount)* 100,
            "currency": "INR",
            "receipt": 'surftheturf',
            'notes': {
                'Name': request.user.username,
                'Payment_For': 'Turf Booking'
            },
            'payment_capture': '1'
        }

        payment = client.order.create(data=DATA)
        print(payment)
        turf = TurfBooked(name=request.user.username, email=request.user.email,
                           amount=totalAmount, selected_date=selectedDate,current_date=currentDate, booking_time=booking_time,slots=bookedSlots, payment_id=payment['id'])
        turf.save()
        return render(request, 'turfBilling.html', {'payment': payment, 'details': details})
    # return render(request, 'turfBilling.html', {'details': details})

@csrf_exempt
def success(request):
    if request.method == "POST":
        paymentDetails = request.POST   # Dictionary
        # {
        #     "razorpay_payment_id": "pay_29QQoUBi66xm2f",
        #     "razorpay_order_id": "order_9A33XWu170gUtm",
        #     "razorpay_signature": "9ef4dffbfd84f1318f6739a3ce19f9d85851857ae648f114332d8401e0949a3d"
        # }

        # Verify the Signature

        keyId = 'rzp_test_9e8xrjzBFp5O7M'
        keySecret = 's4qIuVEiSi128ucHK9uAzoAU'
        client = razorpay.Client(auth=(keyId, keySecret))
        params_dict = {
            'razorpay_order_id': paymentDetails['razorpay_order_id'],
            'razorpay_payment_id': paymentDetails['razorpay_payment_id'],
            'razorpay_signature': paymentDetails['razorpay_signature']
        }
        # If returns None, payment is successful, else some error occured
        check = client.utility.verify_payment_signature(params_dict)
        print(check)

        if check:
            return render(request, 'error.html')

        # If Payment is successfull done, the checkbox(Paid) is ticked in database of that user
        order_id = paymentDetails['razorpay_order_id']
        
        # Check if it's a regular turf booking or dynamic turf booking
        user = TurfBooked.objects.filter(payment_id=order_id).first()
        dynamic_user = DynamicTurfBooked.objects.filter(payment_id=order_id).first()
        
        if user:
            print("Regular turf booking found:", user)
            user.paid = True
            user.save()
            turf_name = 'JP Sports Arena'  # Default for regular bookings
            turf_address = 'Survey No. 25, Kothrud, Near COEP College, Pune, Maharashtra 411038'
            
            # Mark slots as unavailable in the shared matrix for static turf bookings
            try:
                matrix = bookslot.objects.get(id='1')
                choosenDay = datetime.strptime(user.selected_date, "%Y-%m-%d").strftime("%A")
                # Map slot labels to indices
                slot_to_idx = {
                    '6-7 am': 1, '7-8 am': 2, '8-9 am': 3, '9-10 am': 4,
                    '10-11 am': 5, '11-12 am': 6, '12-1 pm': 7, '1-2 pm': 8,
                    '2-3 pm': 9, '3-4 pm': 10, '4-5 pm': 11, '5-6 pm': 12,
                    '6-7 pm': 13, '7-8 pm': 14, '8-9 pm': 15, '9-10 pm': 16,
                    '10-11 pm': 17, '11-12 pm': 18, '12-1 am': 19
                }
                day_to_row = {
                    'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                    'Friday': 4, 'Saturday': 5, 'Sunday': 6
                }
                row = day_to_row.get(choosenDay)
                if row is not None:
                    for label in (user.slots or []):
                        idx = slot_to_idx.get(label)
                        if idx is not None and 0 <= idx < len(matrix.week[row]):
                            matrix.week[row][idx] = 1
                    matrix.save()
            except Exception as e:
                print(f"Failed to update availability matrix: {e}")
        elif dynamic_user:
            print("Dynamic turf booking found:", dynamic_user)
            dynamic_user.paid = True
            dynamic_user.save()
            user = dynamic_user  # Use dynamic_user as user for email
            turf_name = dynamic_user.turf.name
            turf_address = dynamic_user.turf.address
        else:
            print("No booking found for order_id:", order_id)
            return render(request, 'error.html')

        total_amount = request.POST.get('total_amount')
        username = request.POST.get('username')
        email = request.POST.get('email')
        selected_date = request.POST.get('selected_date')
        current_date = request.POST.get('current_date')
        slots = request.POST.getlist('slots')
        print(slots)
        booking_time = datetime.now(
            timezone("Asia/Kolkata")).strftime('%H:%M:%S')
        
        # bookedSlots = []
        # for i in slots:
        #     if i == '6-7 am':
        #         bookedSlots.append(1)
        #     elif i == '7-8 am':
        #         bookedSlots.append(2)
        #     elif i == '8-9 am':
        #         bookedSlots.append(3)
        #     elif i == '9-10 am':
        #         bookedSlots.append(4)
        #     elif i == '10-11 am':
        #         bookedSlots.append(5)
        #     elif i == '11-12 am':
        #         bookedSlots.append(6)
        #     elif i == '12-1 pm':
        #         bookedSlots.append(7)
        #     elif i == '1-2 pm':
        #         bookedSlots.append(8)
        #     elif i == '2-3 pm':
        #         bookedSlots.append(9)
        #     elif i == '3-4 pm':
        #         bookedSlots.append(10)
        #     elif i == '4-5 pm':
        #         bookedSlots.append(11)
        #     elif i == '5-6 pm':
        #         bookedSlots.append(12)
        #     elif i == '6-7 pm':
        #         bookedSlots.append(13)
        #     elif i == '7-8 pm':
        #         bookedSlots.append(14)
        #     elif i == '8-9 pm':
        #         bookedSlots.append(15)
        #     elif i == '9-10 pm':
        #         bookedSlots.append(16)
        #     elif i == '10-11 pm':
        #         bookedSlots.append(17)
        #     elif i == '11-12 pm':
        #         bookedSlots.append(18)
        #     elif i == '12-1 am':
        #         bookedSlots.append(19)

        # choosenDay = datetime.strptime(
        #     selected_date, "%Y-%m-%d").strftime("%A")
        # print(choosenDay)
        # matrix = bookslot.objects.get(id='1')
        # if choosenDay == "Monday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[0][int(i)] = 1
        #                 matrix.save()
        # elif choosenDay == "Tuesday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[1][int(i)] = 1
        #                 matrix.save()
        # elif choosenDay == "Wednesday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[2][int(i)] = 1
        #                 matrix.save()
        # elif choosenDay == "Thursday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[3][int(i)] = 1
        #                 matrix.save()
        # elif choosenDay == "Friday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[4][int(i)] = 1
        #                 matrix.save()
        # elif choosenDay == "Saturday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[5][int(i)] = 1
        #                 matrix.save()
        # elif choosenDay == "Sunday":
        #     for i in bookedSlots:
        #         for j in range(1, 20):
        #             if(int(i) == j):
        #                 matrix.week[6][int(i)] = 1
        #                 matrix.save()
        # book.save()


        # return redirect('book_now')

        # Sending Email
        try:
            # Prepare booking context for email template
            booking_context = {
                'customer_name': user.name,
                'booking_date': user.selected_date,
                'booking_slots': user.slots,
                'total_amount': user.amount,
                'turf_name': turf_name,
                'turf_address': turf_address,
                'booking_id': user.payment_id,
                'booking_time': user.booking_time,
                'contact_phone': '+91 9999999999',
                'contact_email': 'support@surftheturf.com'
            }
            
            # Render email template
            message_html = render_to_string('booking_confirmation_email.html', booking_context)
            message_plain = strip_tags(message_html)  # Create plain text version
            
            # Send email
            send_mail(
                'Booking Confirmed - SurfTheTurf',
                message_plain,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=message_html,
                fail_silently=False
            )
            print(f"Booking confirmation email sent to {user.email}")
        except Exception as e:
            print(f"Failed to send booking confirmation email: {str(e)}")

    return render(request, 'success.html')


def deleteRecord(dayTobeDeleated):
    matrix = bookslot.objects.get(id='1')
    if dayTobeDeleated == "Monday":
        for i in range(20):
            matrix.week[0][i] = 0
    elif dayTobeDeleated == "Tuesday":
        for i in range(20):
            matrix.week[1][i] = 0
    elif dayTobeDeleated == "Wednesday":
        for i in range(20):
            matrix.week[2][i] = 0
    elif dayTobeDeleated == "Thursday":
        for i in range(20):
            matrix.week[3][i] = 0
    elif dayTobeDeleated == "Friday":
        for i in range(20):
            matrix.week[4][i] = 0
    elif dayTobeDeleated == "Saturday":
        for i in range(20):
            matrix.week[5][i] = 0
    elif dayTobeDeleated == "Sunday":
        for i in range(20):
            matrix.week[6][i] = 0


# def Booked(request):
#     if request.method == 'POST':
        # total_amount = request.POST.get('total_amount')
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # selected_date = request.POST.get('selected_date')
        # current_date = request.POST.get('current_date')
        # slots = request.POST.getlist('slots')
        # print(slots)
        # booking_time = datetime.now(
        #     timezone("Asia/Kolkata")).strftime('%H:%M:%S')
        # print(username)
        # keyId = 'rzp_test_9e8xrjzBFp5O7M'
        # keySecret = 's4qIuVEiSi128ucHK9uAzoAU'

        # client = razorpay.Client(auth=(keyId, keySecret))

        # DATA = {
        #     # Amount will be in its smallest unit, that is Paisa (Therefore multiplying by 100 to convert amount in Rs to Paisa)
        #     "amount": int(total_amount)* 100,
        #     "currency": "INR",
        #     "receipt": 'surftheturf',
        #     'notes': {
        #         'Name': request.user.username,
        #         'Payment_For': 'Turf Booking'
        #     },
        #     'payment_capture': '1'
        # }

        # payment = client.order.create(data=DATA)
        # print(payment)
        # turf = TurfBooked(name=username, email=email,
        #                    amount=total_amount, selected_date=selected_date,current_date=current_date, booking_time=booking_time,slots=slots, payment_id=payment['id'])
        # turf.save()
        # return render(request, 'turfBilling.html', {'payment': payment})

        # book = TurfBooked(name=username, email=email, amount=total_amount, selected_date=selected_date,
        #                   current_date=current_date, booking_time=booking_time, slots=slots)

        


@login_required(login_url='login')
def orderHistory(request):

    # bookings = TurfBooked.objects.filter(paid=True)
    my_bookings = TurfBooked.objects.filter(paid=True).filter(email=request.user.email)
    # bookedSlots = []
    # for i in bookings.slots:
    #     if i == '1':
    #         bookedSlots.append('6-7 am')
    #     elif i == '2':
    #             bookedSlots.append('7-8 am')
    #     elif i == '3':
    #         bookedSlots.append('8-9 am')
    #     elif i == '4':
    #         bookedSlots.append('9-10 am')
    #     elif i == '5':
    #         bookedSlots.append('10-11 am')
    #     elif i == '6':
    #             bookedSlots.append('11-12 am')
    #     elif i == '7':
    #         bookedSlots.append('12-1 pm')
    #     elif i == '8':
    #         bookedSlots.append('1-2 pm')
    #     elif i == '9':
    #         bookedSlots.append('2-3 pm')
    #     elif i == '10':
    #         bookedSlots.append('3-4 pm')
    #     elif i == '11':
    #          bookedSlots.append('4-5 pm')
    #     elif i == '12':
    #         bookedSlots.append('5-6 pm')
    #     elif i == '13':
    #         bookedSlots.append('6-7 pm')
    #     elif i == '14':
    #         bookedSlots.append('7-8 pm')
    #     elif i == '15':
    #         bookedSlots.append('8-9 pm')
    #     elif i == '16':
    #         bookedSlots.append('9-10 pm')
    #     elif i == '17':
    #         bookedSlots.append('10-11 pm')
    #     elif i == '18':
    #         bookedSlots.append('11-12 pm')
    #     elif i == '19':
    #         bookedSlots.append('12-1 am')

    currentDate = date.today().strftime("%Y-%m-%d")
    # currentDate = '2021-08-18'
    return render(request, 'orderHistory.html', {'bookings': my_bookings, 'currentDate': currentDate})


def delete_booking(request, id):

    if request.method == 'POST':

        booking = TurfBooked.objects.get(id=id)
        selectedDate = booking.selected_date
        slots = booking.slots

        bookedSlots = []
        for i in slots:
            if i == '6-7 am':
                bookedSlots.append(1)
            elif i == '7-8 am':
                bookedSlots.append(2)
            elif i == '8-9 am':
                bookedSlots.append(3)
            elif i == '9-10 am':
                bookedSlots.append(4)
            elif i == '10-11 am':
                bookedSlots.append(5)
            elif i == '11-12 am':
                bookedSlots.append(6)
            elif i == '12-1 pm':
                bookedSlots.append(7)
            elif i == '1-2 pm':
                bookedSlots.append(8)
            elif i == '2-3 pm':
                bookedSlots.append(9)
            elif i == '3-4 pm':
                bookedSlots.append(10)
            elif i == '4-5 pm':
                bookedSlots.append(11)
            elif i == '5-6 pm':
                bookedSlots.append(12)
            elif i == '6-7 pm':
                bookedSlots.append(13)
            elif i == '7-8 pm':
                bookedSlots.append(14)
            elif i == '8-9 pm':
                bookedSlots.append(15)
            elif i == '9-10 pm':
                bookedSlots.append(16)
            elif i == '10-11 pm':
                bookedSlots.append(17)
            elif i == '11-12 pm':
                bookedSlots.append(18)
            elif i == '12-1 am':
                bookedSlots.append(19)

        choosenDay = datetime.strptime(selectedDate, "%Y-%m-%d").strftime("%A")
        print(choosenDay)
        matrix = bookslot.objects.get(id='1')
        if choosenDay == "Monday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[0][i] = 0
                        matrix.save()
        elif choosenDay == "Tuesday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[1][i] = 0
                        matrix.save()
        elif choosenDay == "Wednesday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[2][i] = 0
                        matrix.save()
        elif choosenDay == "Thursday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[3][i] = 0
                        matrix.save()
        elif choosenDay == "Friday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[4][i] = 0
                        matrix.save()
        elif choosenDay == "Saturday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[5][i] = 0
                        matrix.save()
        elif choosenDay == "Sunday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[6][i] = 0
                        matrix.save()

        TurfBooked.objects.filter(id=id).delete()

        return redirect('index')


def allBookings(request):
    datesInSortedOrder = []
    bookings = TurfBooked.objects.filter(paid = True).order_by('selected_date', 'booking_time')
    currentDate = date.today().strftime("%Y-%m-%d")
    # currentDate = '2021-08-19'
    return render(request, 'allBookings.html', {'bookings': bookings, 'dates': datesInSortedOrder, 'currentDate': currentDate})


# Owner Registration and Management Views
def owner_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        password = request.POST['password']
        business_name = request.POST['business_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('owner_signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already registered')
            return redirect('owner_signup')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
            owner = TurfOwner.objects.create(
                user=user,
                phone_number=phone_number,
                business_name=business_name,
                address=address
            )
            owner.save()
            messages.success(request, 'Owner account created successfully! Please login.')
            return redirect('owner_login')
    else:
        return render(request, 'owner_signup.html')


def owner_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                messages.error(request, 'Please provide both username and password')
                return render(request, 'owner_login.html')
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                # Check if user is a turf owner
                try:
                    owner = TurfOwner.objects.get(user=user)
                    auth.login(request, user)
                    messages.success(request, f'Welcome back, {owner.business_name}!')
                    return redirect('owner_dashboard')
                except TurfOwner.DoesNotExist:
                    messages.error(request, 'You are not registered as a turf owner. Please register first.')
                    return render(request, 'owner_login.html')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'owner_login.html')
        except Exception as e:
            messages.error(request, f'Login error: {str(e)}')
            return render(request, 'owner_login.html')
    else:
        return render(request, 'owner_login.html')


@login_required(login_url='owner_login')
def owner_dashboard(request):
    try:
        owner = TurfOwner.objects.get(user=request.user)
        turfs = Turf.objects.filter(owner=owner)
        return render(request, 'owner_dashboard.html', {'owner': owner, 'turfs': turfs})
    except TurfOwner.DoesNotExist:
        return redirect('owner_login')


@login_required(login_url='owner_login')
def add_turf(request):
    try:
        owner = TurfOwner.objects.get(user=request.user)
    except TurfOwner.DoesNotExist:
        return redirect('owner_login')
    
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        address = request.POST['address']
        sports_available = request.POST['sports_available']
        description = request.POST.get('description', '')
        price_per_hour = request.POST['price_per_hour']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        map_link = request.POST.get('map_link', '')
        
        # Amenities
        has_parking = 'has_parking' in request.POST
        has_washroom = 'has_washroom' in request.POST
        has_floodlights = 'has_floodlights' in request.POST
        has_drinking_water = 'has_drinking_water' in request.POST
        has_changing_room = 'has_changing_room' in request.POST
        
        turf = Turf.objects.create(
            owner=owner,
            name=name,
            location=location,
            address=address,
            sports_available=sports_available,
            description=description,
            price_per_hour=price_per_hour,
            contact_number=contact_number,
            email=email,
            map_link=map_link,
            has_parking=has_parking,
            has_washroom=has_washroom,
            has_floodlights=has_floodlights,
            has_drinking_water=has_drinking_water,
            has_changing_room=has_changing_room,
            is_verified=True,  # Auto-verify new turfs for immediate listing
        )
        
        # Handle image uploads
        if 'image1' in request.FILES:
            turf.image1 = request.FILES['image1']
        if 'image2' in request.FILES:
            turf.image2 = request.FILES['image2']
        if 'image3' in request.FILES:
            turf.image3 = request.FILES['image3']
        
        turf.save()
        messages.success(request, 'Turf added successfully! It will be reviewed and made live soon.')
        return redirect('owner_dashboard')
    
    return render(request, 'add_turf.html')


@login_required(login_url='owner_login')
def edit_turf(request, turf_id):
    try:
        owner = TurfOwner.objects.get(user=request.user)
        turf = Turf.objects.get(id=turf_id, owner=owner)
    except (TurfOwner.DoesNotExist, Turf.DoesNotExist):
        return redirect('owner_dashboard')
    
    if request.method == 'POST':
        turf.name = request.POST['name']
        turf.location = request.POST['location']
        turf.address = request.POST['address']
        turf.sports_available = request.POST['sports_available']
        turf.description = request.POST.get('description', '')
        turf.price_per_hour = request.POST['price_per_hour']
        turf.contact_number = request.POST['contact_number']
        turf.email = request.POST['email']
        turf.map_link = request.POST.get('map_link', '')
        
        # Amenities
        turf.has_parking = 'has_parking' in request.POST
        turf.has_washroom = 'has_washroom' in request.POST
        turf.has_floodlights = 'has_floodlights' in request.POST
        turf.has_drinking_water = 'has_drinking_water' in request.POST
        turf.has_changing_room = 'has_changing_room' in request.POST
        
        # Handle image uploads
        if 'image1' in request.FILES:
            turf.image1 = request.FILES['image1']
        if 'image2' in request.FILES:
            turf.image2 = request.FILES['image2']
        if 'image3' in request.FILES:
            turf.image3 = request.FILES['image3']
        
        turf.save()
        messages.success(request, 'Turf updated successfully!')
        return redirect('owner_dashboard')
    
    return render(request, 'edit_turf.html', {'turf': turf})


@login_required(login_url='owner_login')
def delete_turf(request, turf_id):
    try:
        owner = TurfOwner.objects.get(user=request.user)
        turf = Turf.objects.get(id=turf_id, owner=owner)
        turf.delete()
        messages.success(request, 'Turf deleted successfully!')
    except (TurfOwner.DoesNotExist, Turf.DoesNotExist):
        messages.error(request, 'Turf not found or access denied!')
    
    return redirect('owner_dashboard')


def explore_turfs(request):
    # Get all active turfs from database (verified or not) + existing hardcoded ones
    dynamic_turfs = Turf.objects.filter(is_active=True)
    
    # Create list of all turfs (both hardcoded and dynamic)
    all_turfs = []
    
    # Add hardcoded turfs
    hardcoded_turfs = [
        {'id': 'turf1', 'name': 'JP Sports Arena', 'location': 'Kothrud', 'sports': 'Cricket, Football(7v7)', 'type': 'static'},
        {'id': 'turf2', 'name': 'Baner Sports Club', 'location': 'Baner', 'sports': 'Cricket, Football(5v5)', 'type': 'static'},
        {'id': 'turf3', 'name': 'Wakad Champions Ground', 'location': 'Wakad', 'sports': 'Cricket, Football(6v6)', 'type': 'static'},
        {'id': 'turf4', 'name': 'Hinjewadi Sports Arena', 'location': 'Hinjewadi', 'sports': 'Cricket, Football(6v6)', 'type': 'static'},
        {'id': 'turf5', 'name': 'Viman Nagar Sports Complex', 'location': 'Viman Nagar', 'sports': 'Cricket, Football(7v7)', 'type': 'static'},
        {'id': 'turf6', 'name': 'Koregaon Park Sports Hub', 'location': 'Koregaon Park', 'sports': 'Cricket, Football(5v5), Badminton', 'type': 'static'},
        {'id': 'turf7', 'name': 'Magarpatta Sports City', 'location': 'Magarpatta', 'sports': 'Cricket, Football(8v8)', 'type': 'static'},
        {'id': 'turf8', 'name': 'Aundh Sports Center', 'location': 'Aundh', 'sports': 'Cricket, Football(6v6)', 'type': 'static'},
    ]
    
    all_turfs.extend(hardcoded_turfs)
    
    # Add dynamic turfs
    for turf in dynamic_turfs:
        all_turfs.append({
            'id': f'dynamic_{turf.id}',
            'name': turf.name,
            'location': turf.get_location_display(),
            'sports': turf.sports_available,
            'type': 'dynamic',
            'turf_obj': turf
        })
    
    return render(request, 'explore_turfs.html', {'turfs': all_turfs})


def dynamic_turf_details(request, turf_id):
    try:
        turf = Turf.objects.get(id=turf_id, is_active=True)
        currentDate = date.today().strftime("%Y-%m-%d")
        endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
        
        return render(request, 'dynamic_turf_details.html', {
            'currentDate': currentDate, 
            'endDate': endDate, 
            'turf': turf
        })
    except Turf.DoesNotExist:
        messages.error(request, 'Turf not found!')
        return redirect('explore_turfs')


@login_required(login_url='login')
def dynamic_turf_booking(request, turf_id):
    """Handle date selection for dynamic turf booking"""
    try:
        turf = Turf.objects.get(id=turf_id, is_active=True)
        
        if request.method == 'POST':
            selectedDate = request.POST['selectedDate']
            request.session['choosenDate'] = selectedDate
            request.session['turf_id'] = turf_id
            request.session['turf_type'] = 'dynamic'
            return redirect('dynamic_turf_slots')
        else:
            currentDate = date.today().strftime("%Y-%m-%d")
            endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
            return render(request, 'turfDateSelection.html', {
                'currentDate': currentDate, 
                'endDate': endDate,
                'turf': turf
            })
    except Turf.DoesNotExist:
        messages.error(request, 'Turf not found!')
        return redirect('explore_turfs')


@login_required(login_url='login')
def dynamic_turf_slots(request):
    """Show available slots for dynamic turf booking"""
    turf_id = request.session.get('turf_id')
    selectedDate = request.session.get('choosenDate')
    
    if not turf_id or not selectedDate:
        messages.error(request, 'Invalid booking session')
        return redirect('explore_turfs')
    
    try:
        turf = Turf.objects.get(id=turf_id, is_active=True)
        
        # Use the same slot logic as the existing system
        slots = turfBooking.objects.all()
        matrix = bookslot.objects.get(id='1')  # Use the same booking matrix
        
        choosenDay = datetime.strptime(selectedDate, "%Y-%m-%d").strftime("%A")
        currentDate = datetime.now().strftime("%Y-%m-%d")
        
        ls = []
        if choosenDay == "Monday":
            for j in range(20):
                ls.append(str(matrix.week[0][j]))
        elif choosenDay == "Tuesday":
            for j in range(20):
                ls.append(str(matrix.week[1][j]))
        elif choosenDay == "Wednesday":
            for j in range(20):
                ls.append(str(matrix.week[2][j]))
        elif choosenDay == "Thursday":
            for j in range(20):
                ls.append(str(matrix.week[3][j]))
        elif choosenDay == "Friday":
            for j in range(20):
                ls.append(str(matrix.week[4][j]))
        elif choosenDay == "Saturday":
            for j in range(20):
                ls.append(str(matrix.week[5][j]))
        elif choosenDay == "Sunday":
            for j in range(20):
                ls.append(str(matrix.week[6][j]))
        
        return render(request, 'turfBooking.html', {
            'currentDate': currentDate,
            'selectedDate': selectedDate,
            'list': ls,
            'turf': turf
        })
        
    except Turf.DoesNotExist:
        messages.error(request, 'Turf not found!')
        return redirect('explore_turfs')


@login_required(login_url='login')
def dynamic_turf_billing(request):
    """Handle billing for dynamic turf booking"""
    if request.method == 'POST':
        turf_id = request.session.get('turf_id')
        selectedDate = request.POST['date']
        list_of_input_ids = request.POST.getlist('id')
        
        try:
            turf = Turf.objects.get(id=turf_id, is_active=True)
            
            selectedTime = []
            bookedSlots = []
            for i in list_of_input_ids:
                if i == '1':
                    bookedSlots.append('6-7 am')
                    selectedTime.append('06:00:00')
                elif i == '2':
                    bookedSlots.append('7-8 am')
                    selectedTime.append('07:00:00')
                elif i == '3':
                    bookedSlots.append('8-9 am')
                    selectedTime.append('08:00:00')
                elif i == '4':
                    bookedSlots.append('9-10 am')
                    selectedTime.append('09:00:00')
                elif i == '5':
                    bookedSlots.append('10-11 am')
                    selectedTime.append('10:00:00')
                elif i == '6':
                    bookedSlots.append('11-12 am')
                    selectedTime.append('11:00:00')
                elif i == '7':
                    bookedSlots.append('12-1 pm')
                    selectedTime.append('12:00:00')
                elif i == '8':
                    bookedSlots.append('1-2 pm')
                    selectedTime.append('13:00:00')
                elif i == '9':
                    bookedSlots.append('2-3 pm')
                    selectedTime.append('14:00:00')
                elif i == '10':
                    bookedSlots.append('3-4 pm')
                    selectedTime.append('15:00:00')
                elif i == '11':
                    bookedSlots.append('4-5 pm')
                    selectedTime.append('16:00:00')
                elif i == '12':
                    bookedSlots.append('5-6 pm')
                    selectedTime.append('17:00:00')
                elif i == '13':
                    bookedSlots.append('6-7 pm')
                    selectedTime.append('18:00:00')
                elif i == '14':
                    bookedSlots.append('7-8 pm')
                    selectedTime.append('19:00:00')
                elif i == '15':
                    bookedSlots.append('8-9 pm')
                    selectedTime.append('20:00:00')
                elif i == '16':
                    bookedSlots.append('9-10 pm')
                    selectedTime.append('21:00:00')
                elif i == '17':
                    bookedSlots.append('10-11 pm')
                    selectedTime.append('22:00:00')
                elif i == '18':
                    bookedSlots.append('11-12 pm')
                    selectedTime.append('23:00:00')
                elif i == '19':
                    bookedSlots.append('12-1 am')
                    selectedTime.append('00:00:00')
            
            # Prevent double booking for this turf/date
            existing = DynamicTurfBooked.objects.filter(turf=turf, selected_date=selectedDate, paid=True)
            taken = set()
            for b in existing:
                taken.update(b.slots or [])
            if set(bookedSlots) & taken:
                messages.error(request, 'One or more selected time-slots have just been booked for this turf. Please choose different slots.')
                return redirect('dynamic_turf_booking', turf_id=turf.id)
            
            # Use dynamic turf pricing
            totalAmount = len(bookedSlots) * turf.price_per_hour
            currentDate = date.today().strftime("%Y-%m-%d")
            
            details = {
                'username': request.user.username,
                'email': request.user.email,
                'selectedDate': selectedDate,
                'currentDate': currentDate,
                'bookedSlots': bookedSlots,
                'totalAmount': totalAmount,
                'list_of_input_ids': list_of_input_ids,
                'turf': turf
            }
            
            booking_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')
            keyId = 'rzp_test_9e8xrjzBFp5O7M'
            keySecret = 's4qIuVEiSi128ucHK9uAzoAU'
            
            client = razorpay.Client(auth=(keyId, keySecret))
            
            DATA = {
                "amount": int(totalAmount) * 100,
                "currency": "INR",
                "receipt": f'surftheturf_{turf.name}',
                'notes': {
                    'Name': request.user.username,
                    'Payment_For': f'{turf.name} Turf Booking'
                },
                'payment_capture': '1'
            }
            
            payment = client.order.create(data=DATA)
            
            # Create booking record with turf info
            turf_booking = DynamicTurfBooked(
                name=request.user.username,
                email=request.user.email,
                amount=totalAmount,
                selected_date=selectedDate,
                current_date=currentDate,
                booking_time=booking_time,
                slots=bookedSlots,
                payment_id=payment['id'],
                turf=turf
            )
            turf_booking.save()
            
            return render(request, 'turfBilling.html', {'payment': payment, 'details': details})
            
        except Turf.DoesNotExist:
            messages.error(request, 'Turf not found!')
            return redirect('explore_turfs')
    
    return redirect('explore_turfs')


def searchBooking(request):

    query = request.POST['query']
    print(query)
    bookings = TurfBooked.objects.filter(name__icontains=query)
    print(bookings)
    return render(request, 'allBookings.html', {'bookings': bookings, 'query': query})
    # return HttpResponse('This is search')


#
# present = datetime.now()
# dayTobeDeleated = (datetime.now() - timedelta(days=1)).strftime("%A")
# print(dayTobeDeleated)
#
# schedule.every().day.at("00:00").do(deleteRecord, dayTobeDeleated)
