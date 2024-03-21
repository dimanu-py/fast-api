# Project 2: Advanced Bookstore API

## Description

This project is intended to learn more advanced operations with FastAPI such as validation or error handling. Additionally, we will keep 
working with HTTP methods.

Instead of using a list of dictionaries to store the books, we will create a class `Book` to represent them.

## Learning objectives

We will be learning about:
- How to use pydantic to validate data
- How to handle errors
- What are the status codes
- How we can configure Swagger


In the [Following the code](#explanation) section you can find a direct link to each commit where you can see directly the API concept
with the corresponding code.

## How to run the project

This project has been developed with Python 3.11.5 and FastAPI 0.110.0. You can install the dependencies with the following command:

```bash
pip install -r requirements.txt
```

Then, you can run the project running the command below.

> [!IMPORTANT]
> You need to be inside the package folder to run the previous command. In this case you need to be inside *advanced_bookstore* folder.

```bash
uvicorn advanced_bookstore:app --reload
```

Where:
- `advanced_bookstore` is the name of the file where the FastAPI app is defined
- `app` is the name of the FastAPI app
- `--reload` is a flag to reload automatically the server when the code changes

To access the API and call its endpoints we can:

1. Access `http://127.0.0.1:8000` in our browser. By writing this URL and `/endpoint_name` we can access the different endpoints.
2. Access `http://127.0.0.1:8000/docs` in our browser. This will open the Swagger UI where we can see all the endpoints and interact with them.


<a name="explanation"></a>
## Following the code

> [!IMPORTANT]
> This is not a list of all the commits, but a selection of those that contain explanation and new concepts about API development.

1. [Creating a custom class to represent the books](https://github.com/dimanu-py/fast-api/commit/fa85474d86398bb7506609a36baf3d8f48dc1581)
2. [Creating GET endpoint returning a list of Books instead of a dictionary](https://github.com/dimanu-py/fast-api/commit/214a21b7c099219208402bdb0849e04c190ffdac)
3. [Creating a Book from a POST request](https://github.com/dimanu-py/fast-api/commit/dc720ac11b28172cd6b3e11dd827a04818ef550f)
4. [Introduction to Pydantic: defining validation of the request](https://github.com/dimanu-py/fast-api/commit/bdb4f2bc8dcf5d1474118905fff8792311d4bfc2)
5. [Validating a POST request with Pydantic and creating a Book](https://github.com/dimanu-py/fast-api/commit/16022445df71bc4218d525f4a3c94beca5d584d1)
6. [Making request data optional](https://github.com/dimanu-py/fast-api/commit/d703138a16dc80c544f950bcaf5b4eea5a45f829)
7. [Configuring Swagger examples from code](https://github.com/dimanu-py/fast-api/commit/7a5e0e8c1e4f85854e0d9ef91e3cae039c70c0ad)
8. [Defining validation of the response](https://github.com/dimanu-py/fast-api/commit/12736fd2a25d1d82f4a3b15eecca9fb07acad69a)
9. [Adding return type hint to endpoints combining domain objects and Pydantic](https://github.com/dimanu-py/fast-api/commit/e32bb3077e726f66176a83ab3ea5b2b4e662d8ba)
10. [Updating a book when we use Pydantic](https://github.com/dimanu-py/fast-api/commit/b2ed254d975f8f9a784df4b65472aa062ef719a5)
11. [Validating path parameters](https://github.com/dimanu-py/fast-api/commit/c8e47ad7d53317e3fbcf9cd998457683bcfd1c1f)
12. [Validating query parameters](https://github.com/dimanu-py/fast-api/commit/ee85ef9b6a27d53ecea027a784be667e201fcd5f)
13. [Handling HTTP errors with status codes](https://github.com/dimanu-py/fast-api/commit/860c6e03bd2e67fd5011b2618190f1e9e42f780a)
14. [Setting success status codes](https://github.com/dimanu-py/fast-api/commit/0569f93d33cfa366c0bcced61c64d3c71f210415)

