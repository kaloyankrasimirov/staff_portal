# Staff Portal App

An internal Human Resources Information System built with Django for managing company structure, employees, cross-functional projects, and performance tracking.

## Core Features
- **Departments:** Organize company units and locations.
- **Employees:** Manage staff profiles linked to departments.
- **Projects:** Track company initiatives with cross-departmental collaboration (Many-to-Many).
- **Records:** Manage employees, departments and projects records as budget, milestones, targets, paid leave tracking, etc.

## Setup Instructions
1. Clone the repository
2. Create and activate a virtual environment (`python -m venv venv`)
3. Install dependencies (`pip install -r requirements.txt`)
4. Configure your `.env` file based on `.env.example`
5. Run migrations (`python manage.py migrate`)
6. Start the server (`python manage.py runserver`)