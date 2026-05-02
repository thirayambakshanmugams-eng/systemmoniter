import os
import requests

BACKEND_URL = os.environ.get('BACKEND_URL', 'https://your-real-backend.onrender.com')

if BACKEND_URL == 'https://your-real-backend.onrender.com':
    print('WARNING: BACKEND_URL is still the placeholder value. Set BACKEND_URL to your real Render backend URL.')

try:
    r = requests.get(f'{BACKEND_URL}/api/report/pdf', timeout=120)
    print(f'Status: {r.status_code}')

    ct = r.headers.get('Content-Type', '')
    print(f'Content-Type: {ct}')

    if r.status_code != 200:
        print(f'Body: {r.text[:3000]}')
    else:
        print(f'PDF received OK, {len(r.content)} bytes')

except Exception as e:
    print(f'Request failed: {e}')