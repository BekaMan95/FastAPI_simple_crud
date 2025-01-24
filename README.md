## The Minimalist FastAPI

#### Simple crud api with [FastAPI](https://fastapi.tiangolo.com/)
*implemented with database dependency injection for each route.*

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
    pip install fastapi uvicorn sqlalchemy pymysql
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

### Have Fun!!
