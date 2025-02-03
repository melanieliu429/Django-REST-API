# 🌱 Sustainability Actions API - Django Backend

A simple Django REST API to **create, retrieve, update, and delete** sustainability actions.

## 🚀 Features
- **GET** `/api/actions/` - Get all actions.
- **POST** `/api/actions/` - Add a new action.
- **PUT/PATCH** `/api/actions/<id>/` - Update an action.
- **DELETE** `/api/actions/<id>/` - Delete an action.
- **GET** `/api/actions/json/` - Save and retrieve actions from a JSON file.

---

## 🛠️ Setup & Installation

### 1️⃣ Install Dependencies
git clone https://github.com/melanieliu429/Django-REST-API.git
cd Django-REST-API
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Apply Migrations
python manage.py migrate

3️⃣ Start the Server
python manage.py runserver

🌍 API Endpoints
GET /api/actions/
✅ Response Example:
[
  {
    "id": 1,
    "action": "Recycling",
    "date": "2025-01-08",
    "points": 25
  }
]

POST /api/actions/
✅ Payload Example:
{
  "action": "Planting Trees",
  "date": "2025-02-15",
  "points": 50
}

PUT /api/actions/1/
✅ Payload Example:
{
  "action": "Recycling Plastic",
  "points": 30
}

DELETE /api/actions/1/
✅ Response:
{
  "message": "Action deleted successfully"
}

🧪 Testing with Postman
Use http://127.0.0.1:8000/api/actions/ as the base URL.
Send GET, POST, PUT, DELETE requests.
Check JSON responses.

🚀 Deployment
For production:

Set DEBUG = False in settings.py.
Configure allowed hosts in settings.py.
Use Gunicorn for deployment:
pip install gunicorn
gunicorn sustainability_api.wsgi
