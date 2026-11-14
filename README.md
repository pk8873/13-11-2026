# LPG Connection Service Demo (Independent Testing Project)

> स्पष्ट Demo/Testing portal. यह किसी सरकारी या निजी गैस कंपनी की आधिकारिक वेबसाइट नहीं है। कोई वास्तविक भुगतान न करें।

## Features
- Django 5.2 + SQLite
- Hindi-friendly responsive demo service portal
- Demo booking request
- Simulated "Connection Paused" status
- Test payment button (changes only the demo booking status in the database)
- Simulated "Demo Connection Restored" confirmation
- Django Admin for products, prices, and booking status

## Important safety design
- No real provider logos, names, or official affiliation.
- No real UPI QR or payment collection.
- The payment simulation does not open a UPI app, contact a bank, or verify a transaction.
- Use fictional customer details only.
- This demo does not disconnect or reconnect any real gas connection.

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
1. Sign in to /admin/ and add one or more Gas Products with fictional test prices.
2. Open the home page and submit a demo service request using fictional details.
3. The payment page displays a simulated paused-connection notice.
4. Click "Simulate Test Payment". No money is transferred.
5. The next page shows "Demo Connection Restored".
6. Admin can inspect the booking and its status.

## Temporary public internet testing (ngrok)
1. Run Django locally on port 8000.
2. In a second PowerShell window, run `ngrok http 8000`.
3. Copy the HTTPS forwarding hostname shown by ngrok.
4. Set that hostname in `DJANGO_ALLOWED_HOSTS` and the HTTPS origin in `DJANGO_CSRF_TRUSTED_ORIGINS`, then restart Django. Example:
```powershell
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost,example.ngrok-free.app"
$env:DJANGO_CSRF_TRUSTED_ORIGINS="https://example.ngrok-free.app"
python manage.py runserver
```
Replace the example hostname with the actual ngrok hostname. Keep Django and ngrok running while testing. A free tunnel URL may change after restart.

## Before any real production use
Do not use Django's development server as production hosting. Configure DEBUG=False, a strong environment-based SECRET_KEY, allowed hosts, HTTPS, secure cookies, backups, and a production database/server. For genuine payment testing, integrate a licensed payment provider's sandbox; never display a personal QR as if it were an official bill.
