from django.db import models

# Create your models here.
# Using JSONField instead of Postgres-only ArrayField to support SQLite during local dev
from django.db.models.fields import AutoField
# Create your models here.


class Contact(models.Model):
    yourName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobilenumber = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.yourName



class turfBooking(models.Model):
    time_slot = models.CharField(max_length=12)
    isBooked = models.BooleanField(default=False)
    days = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.time_slot


class bookslot(models.Model):
    # week will be stored as a list of lists (7 lists each containing up to 20 integers)
    week = models.JSONField(default=list)


class Time(models.Model):
    name = models.CharField(max_length=200, default="")
    week = models.JSONField(default=list)

class TurfBooked(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    amount = models.IntegerField()
    selected_date = models.CharField(max_length=200)
    current_date = models.CharField(max_length=200)
    booking_time = models.CharField(max_length=200, default="")
    slots = models.JSONField(default=list)
    
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)


class TurfOwner(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    business_name = models.CharField(max_length=200)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.business_name


class Turf(models.Model):
    SPORT_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('badminton', 'Badminton'),
        ('tennis', 'Tennis'),
        ('basketball', 'Basketball'),
        ('volleyball', 'Volleyball'),
    ]
    
    PUNE_AREAS = [
        ('kothrud', 'Kothrud'),
        ('baner', 'Baner'),
        ('wakad', 'Wakad'),
        ('hinjewadi', 'Hinjewadi'),
        ('viman_nagar', 'Viman Nagar'),
        ('koregaon_park', 'Koregaon Park'),
        ('magarpatta', 'Magarpatta'),
        ('aundh', 'Aundh'),
        ('hadapsar', 'Hadapsar'),
        ('kharadi', 'Kharadi'),
        ('wagholi', 'Wagholi'),
        ('katraj', 'Katraj'),
        ('warje', 'Warje'),
        ('karve_nagar', 'Karve Nagar'),
        ('deccan', 'Deccan'),
        ('shivajinagar', 'Shivajinagar'),
        ('camp', 'Camp'),
        ('undri', 'Undri'),
        ('kondhwa', 'Kondhwa'),
        ('bibvewadi', 'Bibvewadi'),
    ]
    
    owner = models.ForeignKey(TurfOwner, on_delete=models.CASCADE, related_name='turfs')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=50, choices=PUNE_AREAS)
    address = models.TextField()
    sports_available = models.CharField(max_length=300, help_text="Comma-separated sports (e.g., Cricket, Football(7v7))")
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, default=700.00)
    
    # Amenities
    has_parking = models.BooleanField(default=True)
    has_washroom = models.BooleanField(default=True)
    has_floodlights = models.BooleanField(default=True)
    has_drinking_water = models.BooleanField(default=True)
    has_changing_room = models.BooleanField(default=False)
    
    # Contact and availability
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    map_link = models.URLField(blank=True, help_text="Google Maps link")
    
    # Admin fields
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Images
    image1 = models.ImageField(upload_to='turf_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='turf_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='turf_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_location_display()}"
    
    def get_amenities_list(self):
        amenities = []
        if self.has_parking:
            amenities.append('Parking')
        if self.has_washroom:
            amenities.append('Washroom')
        if self.has_floodlights:
            amenities.append('Floodlights')
        if self.has_drinking_water:
            amenities.append('Drinking Water')
        if self.has_changing_room:
            amenities.append('Changing Room')
        return amenities
    
    class Meta:
        ordering = ['-created_at']


class DynamicTurfBooked(models.Model):
    """Model for booking dynamic turfs created by owners"""
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    selected_date = models.DateField()
    current_date = models.DateField()
    booking_time = models.TimeField()
    slots = models.JSONField()  # Store list of booked time slots
    payment_id = models.CharField(max_length=200)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.turf.name} - {self.selected_date}"
    
    def get_total_slots(self):
        return len(self.slots) if self.slots else 0
    
    class Meta:
        ordering = ['-created_at']
