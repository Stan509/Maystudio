# MAY STUDIO — Django + React + PostgreSQL

Luxury bilingual website for MAY STUDIO (English / Français), built around the visual identity from the provided flyer.

## Included
- Django + Django REST Framework backend
- PostgreSQL database (Docker Compose)
- React + Vite frontend
- Bilingual EN/FR interface
- Services, gallery, site settings and booking requests in PostgreSQL
- Django Admin for content management
- $80 hairstyle special
- Home-service availability
- Haverstraw, New York location + phone
- QR code to `https://maystudio.shop`
- Responsive premium black / cream / gold styling

## Quick start

### 1. Backend
```bash
cd backend
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2. Frontend
```bash
cd frontend
npm install
npm run dev
```

Set `VITE_API_URL` if the Django API is not running at `http://127.0.0.1:8000/api`.

### PostgreSQL
The project is configured for PostgreSQL by default. Create a `.env` based on `.env.example` and set your PostgreSQL credentials:

`USE_POSTGRES=True`

Start PostgreSQL first, then run migrations.

## Production notes
- Put Django behind Gunicorn/Uvicorn + Nginx/Cloudflare.
- Set `DJANGO_DEBUG=False`, a strong `DJANGO_SECRET_KEY`, and allowed hosts.
- Set the frontend API URL to the production API.
- Keep PostgreSQL backups enabled.
