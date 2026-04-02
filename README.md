🚀 SaaS Task Manager API

A scalable backend system for task management, inspired by tools like Trello and Notion.
Built with Django and Django REST Framework, focusing on clean architecture, performance, and real-world backend practices.

⸻

🎯 Features
 • 🔐 JWT Authentication (Access & Refresh)
 • 👥 Team management (Owner / Member roles)
 • 📁 Project management
 • ✅ Task management with statuses and priorities
 • 💬 Task comments
 • 🔍 Filtering, search, pagination
 • ⚡ Asynchronous tasks (Celery + Redis)
 • 📊 Logging & permissions system
 • 📘 Swagger API documentation

⸻

🧱 Tech Stack
 • Python
 • Django
 • Django REST Framework
 • PostgreSQL
 • Redis
 • Celery
 • Docker
 • drf-spectacular / drf-yasg

⸻

🏗️ Architecture

The project follows a modular and scalable architecture:
 • apps/
 • users/
 • teams/
 • projects/
 • tasks/
 • core/
 • config/

Key principles:
 • Separation of concerns
 • Scalable app structure
 • Clean API design
 • Reusable components

⸻

🔐 Authentication
 • JWT-based authentication
 • Access & Refresh tokens
 • Role-based permissions

⸻

📁 API Endpoints (example)

Auth
 • POST /api/auth/register/
 • POST /api/auth/login/
 • POST /api/auth/refresh/

Teams
 • GET /api/teams/
 • POST /api/teams/
 • POST /api/teams/{id}/invite/

Projects
 • GET /api/projects/
 • POST /api/projects/

Tasks
 • GET /api/tasks/
 • POST /api/tasks/
 • PATCH /api/tasks/{id}/
 • DELETE /api/tasks/{id}/

⸻

⚡ Asynchronous Tasks

Using Celery + Redis:
 • Send notifications on task creation
 • Background processing
