# 🧠 SmartNotes – A Django Notes App

SmartNotes is a full-stack web app built with Django that lets users sign up, log in, and manage their personal notes. It supports CRUD operations, user authentication, and a simple UI — all deployed live on Render.

## 🌐 Live Demo

👉 [smartnotes-x8r1.onrender.com](https://smartnotes-x8r1.onrender.com)

---

## 🚀 Features

- User Registration, Login, Logout
- Create, Read, Update, Delete Notes
- Like/Unlike Notes
- Dynamic Home Page with Current Date
- Admin Panel for Superuser
- Responsive Template using Django Templates + Bootstrap
- Deployed to Render with PostgreSQL + Whitenoise for static files

---

## 🛠 Tech Stack

- **Backend**: Django 4.x
- **Database**: PostgreSQL (Render-hosted)
- **Frontend**: HTML, CSS (Bootstrap), Django Templates
- **Deployment**: Render.com
- **Static Files**: Whitenoise
- **Server**: Gunicorn

---

## 🧑‍💻 Getting Started Locally

### 📦 Clone the repo

```bash
git clone https://github.com/your-username/smartnotes.git
cd smartnotes

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 🔧 Setup the environmental variables

SECRET_KEY=your-local-secret
DEBUG=True
ALLOWED_HOSTS=localhost

### 🗄️ Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```


Developed with 💙 by Shine Titus

---

Let me know if you'd like a shorter one for portfolios or a version with step-by-step screenshots or badges (`build passing`, `deployed to render`, etc.). I can also help auto-generate the screenshots using Playwright or Selenium if you're into that.

