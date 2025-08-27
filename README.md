# Student Information System

## Overview

This is a web-based Student Information System developed for the COS 202 Assignment. The application allows users to manage student records with the following features:

- **Add** new students with details (name, student ID, department).
- **View** existing student records with search functionality.
- **Update** student information.
- **Delete** student records.
- **User authentication** for secure access (default admin user: `username=admin`, `password=password`).
- **Data validation** to ensure accurate input (e.g., unique student IDs, required fields).
- **Search** functionality to find students by name or student ID.

The project is built using **Flask** (Python web framework), **SQLite** (via SQLAlchemy) for the database, **WTForms** for form handling, and **Flask-Login** for authentication. The front-end uses **HTML**, **CSS**, and minimal **JavaScript** for user interaction.

## Project Structure

```
student_info_system/
├── app.py               # Main Flask application
├── models.py            # Database models (User, Student)
├── forms.py             # Form definitions for input validation
├── templates/           # HTML templates
│   ├── base.html        # Base layout
│   ├── login.html       # Login page
│   ├── index.html       # Dashboard with student list and search
│   ├── add_student.html # Add student form
│   └── update_student.html # Update student form
├── static/              # Static files
│   └── style.css        # Basic CSS styling
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore file
└── database.db          # SQLite database (auto-created on first run)
```

## How It Was Made

The project was developed with the following approach:

1. **Planning**:
   - Defined the scope: CRUD operations, authentication, and search functionality.
   - Chose Flask for its simplicity and SQLite for lightweight database management.
   - Planned a modular structure to separate concerns (routes, models, forms, templates).
2. **Implementation**:
   - **Backend**: Used Flask to create routes for login, logout, and student management (`app.py`). SQLAlchemy models (`models.py`) handle database operations, and WTForms (`forms.py`) ensures data validation.
   - **Frontend**: Created HTML templates with a base layout (`base.html`) for consistency. Basic CSS (`style.css`) provides a clean, user-friendly interface.
   - **Authentication**: Implemented Flask-Login for secure user access with a default admin user.
   - **Database**: Used SQLite for simplicity, with a `Student` table (id, name, student_id, department) and a `User` table (id, username, password).
   - **Validation**: Ensured unique student IDs and required fields via WTForms validators.
   - **Search**: Added a search feature to filter students by name or student ID using SQLAlchemy queries.
3. **Version Control**: Designed with Git in mind, including a `.gitignore` to exclude temporary files (e.g., `database.db`, `__pycache__`).
4. **Testing**: Tested CRUD operations, authentication, and search functionality locally to ensure reliability.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Git** (optional, for version control)
- A modern web browser (e.g., Chrome, Firefox)

## Setup Instructions

1. **Clone or Create the Project**:
   - If using Git, clone the repository:
     ```bash
     git clone <repository-url>
     cd student_info_system
     ```
   - Alternatively, create a directory named `student_info_system` and add the project files as listed above.
2. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install the required packages from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
3. **Set Up the Environment**:
   - The app uses a SQLite database (`database.db`), which is auto-created on first run.
   - (Optional) Update the `SECRET_KEY` in `app.py` for production use:
     ```python
     app.config['SECRET_KEY'] = 'your_secret_key_here'
     ```
4. **Run the Application**:
   - Start the Flask server:
     ```bash
     python app.py
     ```
   - The app will run in debug mode at `http://127.0.0.1:5000/`.

## Usage Instructions

1. **Access the App**:
   - Open a browser and navigate to `http://127.0.0.1:5000/`.
2. **Login**:
   - Use the default admin credentials:
     - **Username**: `admin`
     - **Password**: `password`
   - If login fails, an error message will display.
3. **Manage Students**:
   - **View**: The dashboard (`/`) lists all students in a table. Use the search bar to filter by name or student ID.
   - **Add**: Click "Add New Student" to access the form. Enter name, student ID, and department (all required). Duplicate student IDs are rejected.
   - **Update**: Click "Update" next to a student to edit their details.
   - **Delete**: Click "Delete" next to a student and confirm to remove them.
4. **Logout**:
   - Click "Logout" in the header to end the session.
5. **Error Handling**:
   - Invalid inputs (e.g., empty fields) show error messages.
   - Flash messages display success or error feedback for actions.

## Notes for Collaboration

- **Group Work**: Divide tasks among group members (up to 5):
  - Backend: Routes and database logic (`app.py`, `models.py`, `forms.py`).
  - Frontend: HTML templates and CSS (`templates/`, `static/style.css`).
  - Testing: Verify CRUD operations, authentication, and search functionality.
  - Documentation: Maintain this README and add comments in code.
- **Version Control**: Use Git for collaboration:
  - Initialize: `git init`
  - Add files: `git add .`
  - Commit: `git commit -m "Initial commit"`
  - Push to a remote repository (e.g., GitHub) if needed.
- **Testing**: Test edge cases (e.g., duplicate student IDs, invalid inputs, empty search results).

## Troubleshooting

- **Dependency Issues**: Ensure all packages in `requirements.txt` are installed (`pip install -r requirements.txt`).
- **Database Issues**: If `database.db` is corrupted, delete it and restart the app to recreate it (note: this clears all data).
- **Port Conflicts**: If port 5000 is in use, change the port in `app.py`:
  ```python
  app.run(debug=True, port=5001)
  ```
- **Production**: Disable debug mode (`debug=False`) and set a secure `SECRET_KEY` for deployment.

## Future Improvements

- Add password hashing for new users and a user registration system.
- Enhance search with more filters (e.g., department).
- Improve styling with a CSS framework like Bootstrap.
- Add pagination for large student lists.
- Implement export functionality (e.g., CSV download).

## License

This project is for educational purposes as part of COS 202. Please follow your institution's guidelines for use and distribution.
