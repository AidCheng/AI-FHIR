# Backend
This is a flask backend for the project. Its main functionality is to parse local FHIR json files
and extract key data from patients in order to improve prompts given to the AI. The AI will then create risk assessments of the patients using this data. The backend currently works with 'test_frontend' which displays a list of the extracted data.

## How to run

- To run first install necessary python packages globally or in a virtual environment:

```bash
pip install -r requirements.txt
```

- To run the backend:

```bash
flask run
```

- Also create a folder called 'data' containing the FHIR json files to process

## How to run without frontend

If you just want to print the results onto the console without connecting to a frontend, I added a comment at the end of app.py on how to do this.
