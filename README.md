# portfolio_django

# Dipti Dhavalikar's Portfolio Website

A personal portfolio website built using **Django** and **Bootstrap 5**. It showcases my skills, projects, resume, and provides a contact form with backend storage using Django models.

---



## Features

- **Home** – A clean landing page with carousel and navigation.
- **About** – A modern styled bio with profile photo, education, and skills.
- **Projects** – Project cards displaying your major work with descriptions.
- **Contact** – A functional contact form storing submissions via Django model.
- **Django Backend** – Handles dynamic form submissions and static files.
- Responsive – Optimized layout for mobile and desktop.

---

## 🛠️ Built With

- **Django 4+**
- **HTML5, CSS3**
- **Bootstrap 5**
- **Python**

---

## Project Structure

```bash
portfolio/
├── manage.py
├── db.sqlite3
├── portfolio_app/
│   ├── models.py        # Contact model
│   ├── views.py         # Views for each page
│   ├── urls.py          # App-specific routes
│   ├── templates/
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── projects.html
│   └── static/
│       └── images/
│           └── profile.jpg
├── portfolio_project/
│   ├── settings.py
│   └── urls.py
