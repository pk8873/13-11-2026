# LPG Service Portal — Independent Demo

This is an independent LPG service UI/UX demo. It is not an official portal of IndianOil, Indane, Bharatgas, HP Gas, or any government/provider. It cannot look up real customer records, pause/restore real connections, issue real bills, or collect real payments.

## Demo connection lookup

- Admin creates fictional records under **Demo Gas Connections**.
- Test users enter the fictional Demo Connection ID and fictional Demo Owner Name.
- The page shows a clearly watermarked **DEMO BILL — NOT A REAL BILL**.
- The demo status can be changed from **ON HOLD** to **ACTIVE** only through a no-money payment simulation.
- Use only fictional IDs such as `DEMO-100001` and fictional names. Never enter real consumer details.

## Admin setup

Open /admin/ and:
1. Edit **Website Company Profile Switcher** for independent portal branding.
2. Add **Demo Gas Connections** with fictional IDs/names and a test due amount.
3. Use only original/authorized demo branding; do not use provider logos or official-looking payment details.

## Windows setup (Python 3.12)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/.

## Real-world integrations
Real LPG account lookup, connection status changes, billing, and payments require formal authorization and official provider APIs/partner access. A real payment gateway must be integrated in its authorized sandbox/live mode; this demo does not process payments.
