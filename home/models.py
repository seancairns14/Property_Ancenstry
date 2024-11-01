from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Plot(models.Model):
    address_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
    size_sq_ft = models.FloatField()
    zoning = models.CharField(max_length=50)
    current_owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, related_name="plots")
    x_postion = models.PositiveBigIntegerField()
    y_position = models.PositiveBigIntegerField()


    def __str__(self):
        return f"{self.address_name}, {self.city_name}"

class Building(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="buildings")
    name = models.CharField(max_length=100)
    construction_date = models.DateField()
    building_type = models.CharField(max_length=50)
    floors = models.IntegerField()
    square_footage = models.FloatField()
    current_status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('sale', 'Sale'),
        ('lease', 'Lease'),
        ('transfer', 'Transfer'),
    ]
    
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="transactions")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True, related_name="transactions")
    buyer = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="purchases")
    seller = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="sales")

    def __str__(self):
        return f"{self.transaction_type} on {self.date}"

class Permit(models.Model):
    PERMIT_TYPE_CHOICES = [
        ('construction', 'Construction'),
        ('renovation', 'Renovation'),
        ('demolition', 'Demolition'),
    ]
    
    permit_type = models.CharField(max_length=50, choices=PERMIT_TYPE_CHOICES)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="permits")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True, related_name="permits")
    description = models.TextField()
    approved_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.permit_type} Permit - {self.issue_date}"

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('renovation', 'Renovation'),
        ('fire', 'Fire'),
        ('flood', 'Flood'),
        ('zoning_change', 'Zoning Change'),
    ]
    
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    date = models.DateField()
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="events")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True, related_name="events")
    description = models.TextField()
    impact = models.TextField()

    def __str__(self):
        return f"{self.event_type} Event on {self.date}"
