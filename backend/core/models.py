from django.db import models

class Service(models.Model):
    name_en = models.CharField(max_length=120)
    name_fr = models.CharField(max_length=120)
    description_en = models.TextField(blank=True)
    description_fr = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return self.name_en

class GalleryItem(models.Model):
    title = models.CharField(max_length=120)
    image_url = models.URLField()
    alt_text = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=60, default='styles')
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return self.title

class SiteSetting(models.Model):
    phone = models.CharField(max_length=40, default='+1 845 263 6492')
    address = models.CharField(max_length=220, default='10 Harding Ave, Haverstraw, New York')
    website = models.URLField(default='https://maystudio.shop')
    special_price = models.DecimalField(max_digits=8, decimal_places=2, default=80)
    home_service = models.BooleanField(default=True)
    tagline_en = models.CharField(max_length=180, default='Your Hair, Our Passion')
    tagline_fr = models.CharField(max_length=180, default='Vos cheveux, notre passion')

    def __str__(self):
        return 'MAY STUDIO settings'

class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    service = models.CharField(max_length=120)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    notes = models.TextField(blank=True)
    home_service = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.service} — {self.preferred_date}'
