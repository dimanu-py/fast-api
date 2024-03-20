# Project 1: Bookstore API

## Description

This project is intended to learn all basic HTTP methods and how to use them with FastAPI.

We will create a bookstore where all the books will be stored in a list. This list will be used to simulate a database.
Each book will be represented by a dictionary with the following keys:
- `title`: The title of the book
- `author`: The author of the book
- `category`: The category of the book

## Learning objectives

We will be learning about CRUD operations, so we can:
- Create new books -> HTTP Post method
- Read all the books or specific books -> HTTP Get method
- Update the information of a book -> HTTP Put method
- Delete a book from our storage -> HTTP Delete method

In the [Following the code](#explanation) section you can find a direct link to each commit where you can see directly the API concept
with the corresponding code.

## How to run the project

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

To access the API and call its endpoints we can:

1. Access `http://127.0.0.1:8000` in our browser. By writing this URL and `/endpoint_name` we can access the different endpoints.
2. Access `http://127.0.0.1:8000/docs` in our browser. This will open the Swagger UI where we can see all the endpoints and interact with them.


<a name="explanation"></a>
## Following the code

1. [Creating a basic GET endpoint](https://github.com/dimanu-py/fast-api/commit/09bb81b0a76da1f430a13668f18f1a14c62380d2)
2. [Creating a functional GET endpoint to get all books](https://github.com/dimanu-py/fast-api/commit/678135dfe029ca2723847b4a65995be4a4b30270)
3. [Understanding and using path parameters in GET endpoint](https://github.com/dimanu-py/fast-api/commit/acf04b5063f19eef6321e110b0b42354ef0a30b4)
4. [Understanding and using query parameters in GET endpoint](https://github.com/dimanu-py/fast-api/commit/6d92fa1d2f93688674c469f171f7a6574fdf7797)
5. [How to combine path and query parameters in a GET endpoint](https://github.com/dimanu-py/fast-api/commit/5c5f4ec3967584d76738c7cd0298434f5a6c28ff)
6. [Creating a POST endpoint to add new books](https://github.com/dimanu-py/fast-api/commit/337c69216eb20a9d4cd5c44564dead9f6924b2a5)
7. [Creating a PUT endpoint to update a book](https://github.com/dimanu-py/fast-api/commit/ba42f0e5b41c89804f4defe8a60cba6487f7762f)
8. [Creating a DELETE endpoint to remove a book](https://github.com/dimanu-py/fast-api/commit/2345c6242a11ef3b53eb56c053507c30be9ef8ab)
9. [Understanding why the order of the endpoints matters](https://github.com/dimanu-py/fast-api/commit/ee400ec5b7d8d39a9d48745545fad4257a39fccb)

