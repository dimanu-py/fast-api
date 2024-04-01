# Project 3: Todo List API

## Description

In this project we will be developing a Todo List application, being able to create, read, update and delete tasks.

We will be implementing a connection to different SQL databases and learning advanced concepts like authentication. As we do on the 
previous projects, we will be gaining a deeper understanding of FastAPI and its features.

## Learning objectives

We will be learning about:
- Working with SQL Database
- Authentication
- Authorization
- Hashing passwords

In the [Following the code](#explanation) section you can find a direct link to each commit where you can see directly the API concept
with the corresponding code.

## How to run the project

This project has been developed with Python 3.11.8 and FastAPI 0.110.0. To install the dependencies follow these steps:

1. Create a virtual environment with Python 3.11.8. You can do this running the command below:
    
    ```bash
    python3.11 -m venv venv
    ```
2. Install `pipenv` if you don't have it yet:

    ```bash
    pip install pipenv
    ```
3. Install the dependencies with the following command:
     
    ```bash
    pipenv install
    ```

Then, you can run the project running `uvicorn advanced_bookstore:app --reload` or `pipenv run uvicorn advanced_bookstore:app --reload`.

> [!IMPORTANT]
> You need to be inside the package folder to run the previous command. In this case you need to be inside *todo_list* folder.


Where:
- `todo_list` is the name of the file where the FastAPI app is defined
- `app` is the name of the FastAPI app
- `--reload` is a flag to reload automatically the server when the code changes

To access the API and call its endpoints we can:

1. Access `http://127.0.0.1:8000` in our browser. By writing this URL and `/endpoint_name` we can access the different endpoints.
2. Access `http://127.0.0.1:8000/docs` in our browser. This will open the Swagger UI where we can see all the endpoints and interact with them.


<a name="explanation"></a>
## Following the code

> [!IMPORTANT]
> This is not a list of all the commits, but a selection of those that contain explanation and new concepts about API development.

1. 