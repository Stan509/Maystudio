import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','maystudio_api.settings')
import django
django.setup()
from core.models import Service, GalleryItem, SiteSetting

services=[
('African braids','Tresses africaines'),('Box braids','Tresses box'),('Cornrows','Nattes collées'),
('Senegalese twists','Torsades sénégalaises'),('Twists & braids','Torsades et tresses'),
('Weaves & wigs','Tissages et perruques'),("Men’s hairstyles",'Coiffures pour hommes')]
for i,(en,fr) in enumerate(services):
    Service.objects.update_or_create(name_en=en,defaults={'name_fr':fr,'sort_order':i,'featured':True})

source='/assets/maystudio-banner-source.jpeg'
for i in range(6):
    GalleryItem.objects.update_or_create(title=f'MAY STUDIO style {i+1}',defaults={'image_url':source,'alt_text':'MAY STUDIO African hairstyle','sort_order':i})
SiteSetting.objects.get_or_create(id=1,defaults={'phone':'+1 845 263 6492','address':'10 Harding Ave, Haverstraw, New York','website':'https://maystudio.shop','special_price':80,'home_service':True})
print('Seeded MAY STUDIO data.')
