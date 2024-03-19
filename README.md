# FastAPI Course

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-005571?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

> This is a FastAPI course from Udemy. The course is created by Eric Roby and Chad Darby and can be found in the [following link](https://www.udemy.com/course/fastapi-the-complete-course/)

## Repository structure

The course is divided into different projects, where each project is intended to learn a specific topic about API development with FastAPI.

Each project could be followed by a specific branch in the repo while the main branch will contain all the projects together.

## Project 1: Bookstore API

### Description

This project is intended to learn all basic HTTP methods and how to use them with FastAPI.

We will create a bookstore where all the books will be stored in a list. This list will be used to simulate a database.
Each book will be represented by a dictionary with the following keys:
- `title`: The title of the book
- `author`: The author of the book
- `category`: The category of the book

### Learning objectives

We will be learning about CRUD operations, so we can:
- Create new books -> HTTP Post method
- Read all the books or specific books -> HTTP Get method
- Update the information of a book -> HTTP Put method
- Delete a book from our storage -> HTTP Delete method

### How to run the project

This project has been developed with Python 3.11.5 and FastAPI 0.110.0. You can install the dependencies with the following command:

```bash
pip install -r requirements.txt
```

Then, you can run the project with the following command

> [!IMPORTANT]
> You need to be inside the package folder to run the previous command. In this case you need to be inside _bookstore_ folder.

```bash
uvicorn bookstore:app --reload
```

Where:
- `bookstore` is the name of the file where the FastAPI app is defined
- `app` is the name of the FastAPI app
- `--reload` is a flag to reload automatically the server when the code changes

Running the previous command will start the server in the following address: `http://127.0.0.1:8000`

