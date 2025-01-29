## The Minimalist FastAPI

#### Simple crud api with [FastAPI](https://fastapi.tiangolo.com/)
*implemented with database dependency injection for each route.*

---

#### Follow up
* setup the environment

    ```bash
    git clone https://github.com/BekaMan95/FastAPI_simple_crud.git project

    cd project

    ```
* setup the environment

    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

    ```
* install required libraries
    ```bash
    pip install -r requirements.txt
    ```
* create and set configurations (configure the database info in config.py)
    ```bash
    touch config.py && cp config.example.py config.py
    ```
* run the uvicorn server
    ```bash
    uvicorn main:app --reload
    ```
* test routes with the prefix http://localhost:8000/api

---

# API Documentation

### Base URL http://localhost:8000/api


---

### **2. Endpoints Overview**

#### Auth

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| POST   | `/auth/login`       | Get auth tokens         | 

#### Users

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| GET    | `/users`       | Get a list of all users |
| POST   | `/users`       | Create a new user       |
| GET    | `/users/{id}`  | Get details of a user   |
| PUT    | `/users/{id}`  | Update user details |
| DELETE | `/users/{id}`  | Delete user           |

#### Posts

| Method | Endpoint         | Description                |
|--------|------------------|----------------------------|
| GET    | `/posts`      | Get a list of all posts |
| POST (auth)  | `/posts`      | Create a new post       |
| GET    | `/posts/{id}` | Get details of a post   |
| PUT    | `/posts/{id}` | Update post details |
| DELETE | `/posts/{id}` | Delete post           |

---

### Have Fun!!
