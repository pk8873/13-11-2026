# LPG Service Portal — Independent Demo

This project is an independent LPG-service UI/UX demo. It is not an official portal of any gas provider. It does not pause or restore real connections and does not collect real payments.

## Admin Company Profile Switcher

Open /admin/ and edit **Website Company Profile Switcher**. Only one settings row is allowed; edit that row to switch profiles.

Profiles:
- Indian-style LPG Demo Profile
- Bharat-style LPG Demo Profile
- Green Energy Utility Demo Profile
- Custom Independent Demo Profile

Switching the profile changes the page composition, header treatment, hero layout, service-card treatment, and palette. Admin can also edit:
- Independent portal name and tagline
- Text logo or upload an original/authorized demo logo
- Homepage heading and description
- Navigation labels
- Demo announcement and support label

Do not upload another company's official logo or create a page that could be mistaken for its official service/payment portal. The public site always displays a DEMO / TESTING notice.

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

## Demo workflow
1. Add Demo Gas Products in Admin.
2. Create a service request with fictional test details.
3. View the simulated paused status.
4. Click Simulate Test Payment. No money is moved.
5. View the simulated restored status.

## Media uploads
The uploaded logo is stored under MEDIA_ROOT/demo_branding/. Configure persistent media storage and backups before deploying.

## Deployment
Do not use Django's development server in production. Set DEBUG=False, a strong secret key, allowed hosts, HTTPS, secure cookies, production database, and persistent media storage. Real payment testing requires an authorized payment provider's sandbox.
