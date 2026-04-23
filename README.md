# Railway_System (Django)

A simple Django project for managing railway ticketing and user accounts.

## Summary

This project includes two main apps:

- `myapp`: core ticketing functionality (tickets, ticket images, purchase flow, views/templates).
- `users`: custom user handling (authentication, forms, backends).

It's configured to use SQLite (`db.sqlite3`) and stores uploaded media under `media/`.

## Features

- User signup / login
- Profile pictures and ticket image uploads
- Ticket creation, listing, details, and deletion
- Templates in `template/` and static assets in `static/`

## Requirements

- Python 3.8+ (recommend 3.10+)
- pip
- Virtual environment (venv / virtualenv)

Dependencies are listed in `requirements.txt`.

## Setup (local)

1. Create and activate a virtualenv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or
.\.venv\Scripts\activate.bat   # cmd
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. (Optional) Collect static files for production-like tests:

```powershell
python manage.py collectstatic
```

5. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Media & Static

- Uploaded files are stored in `media/` (profile pictures, ticket images).
- Static assets are under `static/`.

If deploying, ensure `MEDIA_ROOT`, `MEDIA_URL`, `STATIC_ROOT`, and `STATIC_URL` are correctly set and served by your web server.

## Environment / Settings

- The project currently uses `db.sqlite3` for development.
- For production, configure `DATABASES` in `MyProject/settings.py` and set `DEBUG = False`.
- Use environment variables for sensitive settings (secret key, DB credentials, allowed hosts).

## Running Tests

```powershell
python manage.py test
```

## Project Structure (key files)

- `manage.py` — Django CLI
- `MyProject/settings.py` — project settings
- `myapp/` — main app (models, views, forms, templates under `template/myapp`)
- `users/` — user app (custom backends/forms)
- `template/` — HTML templates
- `static/` — static files
- `media/` — uploaded user files

## Notes

- Templates are in `template/` with subfolders for `myapp` and `Auth`.
- If you add new model fields, remember to run `makemigrations` and `migrate`.

## Contributing

Feel free to open issues or submit pull requests. Describe changes clearly and ensure tests pass.

## License

Add a license of your choice (e.g., MIT) — update this section accordingly.
