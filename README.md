# LPG Connection Service Demo (Independent Testing Project)

> स्पष्ट Demo/Testing portal. यह किसी सरकारी या निजी गैस कंपनी की आधिकारिक वेबसाइट नहीं है। कोई वास्तविक भुगतान न करें।

## Features
- Django 5.2 + SQLite
- Responsive Hindi-friendly Indian utility-style portal UI
- Admin-managed website title, tagline, demo support text and announcement
- Four independent visual themes: Indigo Corporate, Saffron Service, Green Energy, Blue Utility
- Demo booking request, simulated connection pause, test payment and restored status
- Admin management for products, prices and booking statuses

## Theme customisation in Admin
1. Sign in at /admin/.
2. Open **Website Appearance Settings**.
3. Edit portal name, tagline, theme style, demo support phone text and announcement.
4. Save; the public website immediately uses the selected theme.
5. Only one appearance settings record is allowed; edit the existing record to switch styles.

These are original generic demo themes. They do not reproduce IndianOil, Bharatgas, HP Gas or another provider's logos, exact brand identity, official notices, or payment flows.

## Important safety design
- This is an independent demo, not an official provider portal.
- No real UPI payment, QR payment, payment collection or transaction verification.
- The simulated payment only changes a demo booking status in the local database.
- Use fictional customer details only.
- No real gas connection is paused or restored.

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

## Test the workflow
1. In Admin, add Demo Gas Products.
2. Open the home page and create a demo service request using fictional details.
3. See the simulated paused connection page.
4. Click **Simulate Test Payment**; no money is transferred.
5. See the Demo Connection Restored page.
6. In Admin, inspect the booking status.

## Temporary public internet testing (ngrok)
1. Run Django locally on port 8000.
2. In a second PowerShell window, run ngrok http 8000.
3. Copy the HTTPS forwarding hostname shown by ngrok.
4. Set that hostname in DJANGO_ALLOWED_HOSTS and the HTTPS origin in DJANGO_CSRF_TRUSTED_ORIGINS, then restart Django. Example:
```powershell
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost,example.ngrok-free.app"
$env:DJANGO_CSRF_TRUSTED_ORIGINS="https://example.ngrok-free.app"
python manage.py runserver
```
Replace the example hostname with the actual ngrok hostname. Keep Django and ngrok running while testing. A free tunnel URL may change after restart.

## Before production
Do not use Django's development server as production hosting. Configure DEBUG=False, a strong environment-based SECRET_KEY, allowed hosts, HTTPS, secure cookies, backups, and a production database/server. Genuine payment testing requires a licensed payment provider's sandbox.