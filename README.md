# Social-Media-API

API for creating social media account where users can create posts

## Installing using GitHub:

```shell
  git clone https://github.com/DavidGlusch/Social-Media-API.git
  cd social_media_api
  python -m venv venv
  venv\Scripts\activate (on Windows)
  source venv/bin/activate (on macOS)
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
```

## Setting env variables
```shell
SECRET_KEY=your_secret_key
```

## Features:

- Authenticate with JWT
- Admin panel (/admin/)
- SWAGGER documentation (/api/doc/swagger/) 
- Create and update your profile, including profile picture, bio, and other details
- Create new posts with text content and optional media attachments

## Access:
- creating user (/api/user/register/) 
- get a JWT token to use (/api/user/token/)