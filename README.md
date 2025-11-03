# Geeks Andijan Courses API

A Django REST Framework API for managing Geeks Andijan courses, built with clean architecture principles.

## 🚀 Features

- RESTful API endpoints for courses and leads
- Nested serializers for related course info (audience, pluses, FAQs, legacy details)
- CORS enabled for frontend integration
- Production-ready configuration
- Clean code following PEP8 and Django best practices

## 📋 Requirements

- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+
- django-cors-headers 4.3+

## 🔧 Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd api-geeksandijan
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 📚 API Endpoints

### Courses

- **GET** `/api/courses/` - List all courses (with `for_who_list`, `pluses_list`, `faqs`, `details`)
- **GET** `/api/courses/<id>/` - Get single course with related info

### Leads

- **POST** `/api/leads/` - Create new course lead

### Example Requests

#### List All Courses
```bash
GET http://localhost:8000/api/courses/
```

Response:
```json
[
  {
    "id": 1,
    "title": "Python Fundamentals",
    "description": "Learn Python from scratch",
    "for_who_list": [ { "id": 10, "for_who": "Beginners" } ],
    "pluses_list": [ { "id": 5, "plus": "Mentor", "image": null, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z" } ],
    "faqs": [ { "id": 3, "question": "Duration?", "answer": "3 months", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z" } ],
    "details": {
      "pluses": ["mentor", "project", "team", "certificate"],
      "inthis_course": [ {"question": "What will I learn?", "answer": "Python basics"} ]
    },
    "created_at": "2025-01-01T10:00:00Z",
    "updated_at": "2025-01-01T10:00:00Z"
  }
]
```

#### Get Single Course
```bash
GET http://localhost:8000/api/courses/1/
```

#### Create Course Lead
```bash
POST http://localhost:8000/api/leads/
Content-Type: application/json

{
  "fullname": "John Doe",
  "age": 25,
  "phone": "+998901234567"
}
```

## 🌐 Deployment to PythonAnywhere

### Step 1: Push to GitHub

1. Initialize git repository (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create a new repository on GitHub and push:
   ```bash
   git remote add origin <your-github-repo-url>
   git branch -M main
   git push -u origin main
   ```

### Step 2: Create Web App on PythonAnywhere

1. Log in to [PythonAnywhere](https://www.pythonanywhere.com)
2. Go to **Web** tab
3. Click **Add a new web app**
4. Choose **Manual configuration** (not Flask)
5. Select Python version (3.10 recommended)
6. Click **Next** until web app is created

### Step 3: Configure Settings

1. **Update WSGI configuration file**:
   - Go to **Web** tab → **WSGI configuration file**
   - Replace the content with:
   ```python
   import sys
   import os
   
   # Add your project directory to the Python path
   path = '/home/yourusername/api-geeksandijan'
   if path not in sys.path:
       sys.path.insert(0, path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'geeks_api.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
   Replace `yourusername` with your PythonAnywhere username

2. **Update ALLOWED_HOSTS in settings.py**:
   ```python
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
   ```
   Replace `yourusername` with your PythonAnywhere username

3. **Update CORS_ALLOWED_ORIGINS**:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://your-frontend-domain.vercel.app",
   ]
   ```
   Replace with your actual Vercel frontend URL

4. **Update SECRET_KEY** (Important for production):
   - Use environment variable or set a secure key
   - Do NOT commit the secret key to GitHub

### Step 4: Clone and Setup

1. Open a **Bash console** on PythonAnywhere
2. Clone your repository:
   ```bash
   cd ~
   git clone https://github.com/yourusername/api-geeksandijan.git
   cd api-geeksandijan
   ```

3. Create virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install --user -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

### Step 5: Configure Web App Path

1. Go to **Web** tab
2. In **Source code** section, set:
   - Source code: `/home/yourusername/api-geeksandijan`
   - Working directory: `/home/yourusername/api-geeksandijan`

3. In **Virtualenv** section, set:
   - Virtualenv: `/home/yourusername/api-geeksandijan/venv`

### Step 6: Reload Web App

1. Click the green **Reload** button on the **Web** tab
2. Your API should now be live at: `https://yourusername.pythonanywhere.com`

### Step 7: Test Your API

Visit:
- `https://yourusername.pythonanywhere.com/api/courses/`
- Admin panel: `https://yourusername.pythonanywhere.com/admin/`

## 📝 Admin Panel

Access the Django admin panel at `/admin/` to:
- Create and manage courses
- Add course details
- View course leads

## 🔒 Security Notes

1. **Before deploying to production**:
   - Change `SECRET_KEY` in settings.py (use environment variable)
   - Set `DEBUG = False` in production
   - Update `ALLOWED_HOSTS` with your domain
   - Use environment variables for sensitive data

2. **Example production settings**:
   ```python
   import os
   
   SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   ```

## 🧪 Testing with Postman

### Import Collection

Create a Postman collection with these requests:

1. **Get All Courses**
   - Method: GET
   - URL: `http://localhost:8000/api/courses/`

2. **Get Single Course**
   - Method: GET
   - URL: `http://localhost:8000/api/courses/1/`

3. **Create Lead**
   - Method: POST
   - URL: `http://localhost:8000/api/leads/`
   - Headers: `Content-Type: application/json`
   - Body (JSON):
     ```json
     {
       "fullname": "John Doe",
       "age": 25,
       "phone": "+998901234567"
     }
     ```

## 📁 Project Structure

```
api-geeksandijan/
├── geeks_api/          # Main project directory
│   ├── __init__.py
│   ├── settings.py     # Django settings
│   ├── urls.py         # Root URL configuration
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── courses/            # Courses app
│   ├── __init__.py
│   ├── admin.py        # Admin configuration
│   ├── apps.py         # App configuration
│   ├── models.py       # Database models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # API views
│   └── urls.py         # App URL configuration
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 👨‍💻 Development

### Creating Sample Data

You can create sample data through the Django admin panel or Django shell:

```python
python manage.py shell

from courses.models import Course, CourseDetail, ForWho, CoursePluses, CourseFAQ

# Create a course
course = Course.objects.create(
    title="Python Fundamentals",
    description="Learn Python from scratch",
)

# Optional legacy details
CourseDetail.objects.create(
    course=course,
    pluses=["mentor", "project", "team", "certificate"],
    inthis_course=[
        {"question": "What will I learn?", "answer": "Python basics"},
        {"question": "Duration?", "answer": "3 months"}
    ]
)

# New related models
ForWho.objects.create(course=course, for_who="Beginners")
CoursePluses.objects.create(course=course, plus="Mentor")
CourseFAQ.objects.create(course=course, question="Duration?", answer="3 months")
```

## 📄 License

This project is proprietary software for Geeks Andijan.

## 🤝 Support

For issues or questions, please contact the development team.

