from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image_url', models.URLField()),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(default='styles', max_length=60)),
                ('sort_order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['sort_order', 'id']},
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=120)),
                ('name_fr', models.CharField(max_length=120)),
                ('description_en', models.TextField(blank=True)),
                ('description_fr', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('featured', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['sort_order', 'id']},
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='+1 845 263 6492', max_length=40)),
                ('address', models.CharField(default='10 Harding Ave, Haverstraw, New York', max_length=220)),
                ('website', models.URLField(default='https://maystudio.shop')),
                ('special_price', models.DecimalField(decimal_places=2, default=80, max_digits=8)),
                ('home_service', models.BooleanField(default=True)),
                ('tagline_en', models.CharField(default='Your Hair, Our Passion', max_length=180)),
                ('tagline_fr', models.CharField(default='Vos cheveux, notre passion', max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('service', models.CharField(max_length=120)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.TimeField()),
                ('notes', models.TextField(blank=True)),
                ('home_service', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
