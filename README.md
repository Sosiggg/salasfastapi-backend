# Full Stack To-Do List Application

This is a full-stack To-Do List application built with a **React + Vite** frontend and **FastAPI** backend. It uses **PostgreSQL** as the database.

- ✅ Frontend deployed on **Netlify**  
  🔗 [https://salastodolistfastapi.netlify.app/](https://salastodolistfastapi.netlify.app/)
- ⚙️ Backend deployed on **Render**  
  🔗 [https://salasfastapi-backend.onrender.com](https://salasfastapi-backend.onrender.com)
- 🗃️ PostgreSQL database also hosted on **Render**
- 📄 Documentation<br>
  🔗 [https://drive.google.com/file/d/1EwO5QYsCLjrDaZU03RXGjNnWcN9gb5YJ/view?usp=sharing](https://drive.google.com/file/d/1EwO5QYsCLjrDaZU03RXGjNnWcN9gb5YJ/view?usp=sharing)
  
---

### 🚀 Backend Setup Instructions (FastAPI)
The backend is built using FastAPI and connected to PostgreSQL for task management. Here's how to set it up.

#### 1. Clone the Backend Repository
```bash
git clone https://github.com/your-repository/salasfastapi-backend.git
cd salasfastapi-backend
```
#### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then, create a virtual environment and install the necessary dependencies.
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows

pip install -r requirements.txt
```

#### 3. Configure the Database
```bash
Go to the Render Dashboard.

Click on "New" in the top right corner and select "PostgreSQL".

Provide a name for your database (e.g., salas-todolist-db), choose a region, and create the database.

After the database is created, Render will give you a connection string that looks something like this:
  postgres://username:password@hostname:port/database_name
```
#### 4. Run the Backend Server
To start the backend, run:
```bash
uvicorn main:app --reload
```
---

## API Endpoints
1. GET /tasks/list/

    Description: Fetches all tasks in the system.

    Request:

        Method: GET

        Headers:

        json
        Copy
        Edit
        {
          "accept": "application/json"
        }

    Response:

        Status Code: 200 OK

        Response Body:

        json
        Copy
        Edit
        [
          {
            "id": 1,
            "text": "Eat",
            "completed": false
          },
          {
            "id": 2,
            "text": "Sleep",
            "completed": true
          }
        ]

2. POST /tasks/create/

    Description: Adds a new task.

    Request:

        Method: POST

        Headers:

        json
        Copy
        Edit
        {
          "Content-Type": "application/json",
          "accept": "application/json"
        }

        Request Body:

        json
        Copy
        Edit
        {
          "text": "New Task",
          "completed": false
        }

    Response:

        Status Code: 201 Created

        Response Body:

        json
        Copy
        Edit
        {
          "id": 3,
          "text": "New Task",
          "completed": false
        }

3. PATCH /tasks/update/{id}/

    Description: Updates a task (either the text or its completion status).

    Request:

        Method: PATCH

        Headers:

        json
        Copy
        Edit
        {
          "Content-Type": "application/json",
          "accept": "application/json"
        }

        Request Body (can update either text or completed):

        json
        Copy
        Edit
        {
          "text": "Updated Task",
          "completed": true
        }

    Response:

        Status Code: 200 OK

        Response Body:

        json
        Copy
        Edit
        {
          "id": 3,
          "text": "Updated Task",
          "completed": true
        }

4. DELETE /tasks/delete/{id}/

    Description: Deletes a task by ID.

    Request:

        Method: DELETE

        Headers:

        json
        Copy
        Edit
        {
          "accept": "application/json"
        }

    Response:

        Status Code: 204 No Content

        Response Body: None
---

### 🌐 Deployed Backend (Live)
Backend URL: 👉 [https://salastodolistfastapi.netlify.app](https://salasfastapi-backend.onrender.com)

