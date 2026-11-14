# Bharat LPG Demo (Independent Testing Project)

> स्पष्ट Demo/Testing portal. यह किसी सरकारी या निजी गैस कंपनी की आधिकारिक वेबसाइट नहीं है। कोई वास्तविक भुगतान न करें।

## Features
- Django 5.2 LTS + SQLite
- Public gas booking form
- Admin-managed products and prices
- Admin-uploadable/changeable payment QR image
- Booking status management
- Demo payment information page (no payment verification or collection)
- Responsive Hindi-friendly UI

## Windows setup (Python 3.12)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and admin at http://127.0.0.1:8000/admin/

## First admin setup
1. Sign in at /admin/.
2. Add one or more Gas Products and set test prices.
3. Open Payment QR Settings and upload an image QR that you own/control. You can replace it later from the same admin record.
4. Create a test booking from the home page.

## Public internet testing
For temporary testing, use a secure tunnel such as Cloudflare Tunnel or deploy to a test host. Never expose Django's development server as a production server. Before public deployment: set DEBUG=False, configure ALLOWED_HOSTS, use a strong SECRET_KEY from environment variables, HTTPS, secure cookies, backups, and a production database/server.

## Important
This project does not imitate IndianOil, Bharatgas, HP Gas, or any other real provider. It does not process UPI payments, verify transactions, or collect money. Use a licensed payment gateway's sandbox for integration testing.
