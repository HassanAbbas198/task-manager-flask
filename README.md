# Task Manager API

Task Manager API is a Flask-based application that allows users to create, update, delete, and retrieve tasks. It utilizes Flask's "Blueprints" to create modular applications, enabling clear separation between different functional areas of the application, making it easier to maintain and scale.

# Prerequisites

Make sure you have the following dependencies installed on your machine:

- PostgreSQL: [Install PostgreSQL](https://www.postgresql.org/download/)

# Setup

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```sh
    git clone https://github.com/HassanAbbas198/task-manager-flask.git

    cd task-manager-flask
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create an `.env` file at the root level of the project and add the following environment variables. Alternatively, you can copy them from the provided `.env.example` file:

   ```sh
   SECRET_KEY=a-more-secure-and-complex-key
   DEBUG=True
   DATABASE_URI=postgresql://username:password@localhost:5432/db_name
   ```

   Make sure to replace **username**, **password** and **db_name** with your actual PostgreSQL credentials

5. **Running the Application**:

   ```sh
   flask run
   ```

## API Endpoints

Here are some of the sample API endpoints provided by the application:

- `GET /api/v1/tasks`: Retrieve all tasks
- `GET /api/v1/tasks/<task_id>`: Retrieve a specific task by id
- `POST /api/v1/tasks` Create a new task record to the database.
- `PUT /api/v1/tasks/<task_id>:` Update data for a specific task.
- `DELETE /api/v1/tasks/<task_id>:` Delete a task record.

## Usage

Below are examples of how to interact with the API using its endpoints, along with a Postman collection for easier testing:

- Create a task

```
POST /api/v1/tasks
{
    "title": "New Task",
    "description": "Task details"
}

```

- Update a task

```
PUT /api/v1/tasks/<task_id>
{
    "title": "Completed my task!!",
    "description": "Task details",
    "completed": true
}

```

**Postman Collection**:

For a more comprehensive guide to all API functionalities, including additional endpoints and detailed examples, feel free to import the Postman collection:
[Task Manager API Collection](https://elements.getpostman.com/redirect?entityId=15081635-c8ab4a3d-3160-416e-8e24-8e7955472a07&entityType=collection)
