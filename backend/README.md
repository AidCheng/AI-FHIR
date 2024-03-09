# Backend

- To run first install necessary python packages globally or in a virtual environment:

```bash
pip install -r requirements.txt
```

- To run the backend server:

```bash
flask run
```

- Also create a folder called 'data' containing the FHIR json files to process

Was originally testing using a simple react frontend so not integrated with new frontend yet.

## How to run without frontend

If you just want to print the results onto the console and not use backend server or a frontend, I added a comment at the end of app.py on how to do this.
