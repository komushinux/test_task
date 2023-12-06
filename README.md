## Dependencies
Ensure that the following libraries and tools are installed:

- pymongo
- fastapi
- uvicorn

Install the required dependencies using:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Input data
#### Directory _input_ contains file examples for all tasks
- list_keys.txt
- list_version.txt
- task3_input.py
- text.txt

# Verify Data

## Description
The verify_data.py script provides a mechanism for verifying data in a given text using a list of keys.
It defines a custom exception class, VerifyError, to handle verification errors.

### Quick start
```bash
python3 app/task1.py
```

#### Parameters:
* test_text (str): The text to be verified.
* list_keys (list): List of keys to be used for verification.

#### Returns:
* str: The verified text.

#### Raises:
VerifyError: If verification errors are found, raises an exception with details.

# Group and Count

## Description
The group_and_count.py script processes a list of lists, grouping them and counting occurrences of unique lists.
It utilizes the Counter class from the collections module to achieve this.

### Quick Start
```bash
python3 app/task2.py
```

#### Parameters:
* list_version (list): A list of lists to be processed.

#### Returns:
* list: A list of lists, each containing the first and second elements of a unique list and their respective counts.

# Find JSON Diff

## Description
The find_json_diff.py script compares two JSON objects (json_old and json_new) based on
a specified list of keys (diff_list). It identifies and returns the differences between the old and new JSON objects.

### Quick Start
```bash
python3 app/task3.py
```

#### Parameters:
* json_old (dict): The old JSON object for comparison.
* json_new (dict): The new JSON object for comparison.
* diff_list (list): A list of keys to consider for detecting differences.

#### Returns:
* dict: A dictionary containing the differences between the old and new JSON objects,
where keys are the differing keys and values are the corresponding new values.

# MongoDB Log Events

## Description
The mongodb_log_events.py module provides functionality for working with MongoDB and managing the
'log_events' collection. It connects to the local MongoDB server, creates the 'log_events' collection,
and ensures the presence of a TTL (Time-To-Live) index on the 'createdAt' field.

### Quick Start
```bash
python3 app/task4.py
```

#### Dependencies
* pymongo: MongoDB driver for Python.

#### Notes
Ensure that a local MongoDB server is running.
The script inserts a sample document with a log message and 'createdAt' timestamp,
then waits for 20 seconds to demonstrate the TTL index functionality.
Modify the MongoDB connection details (MongoClient) according to your environment.

# FastAPI Webhook Handler

## Description
The webhook_handler.py module handles FastAPI requests, processes webhooks, and connects to MongoDB.
It registers functions to be called based on webhook data.

### Quick Start
```bash
uvicorn app.task5:app --reload
```
This command launches the FastAPI application with automatic reloading for development.
Then in other terminal run, for example:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"function": "function1", "key": "value"}' http://127.0.0.1:8000/Datalore
```
Then check MondoDB. A new document was created in the collection "log_events" of the "task" database as a result of the webhook

#### Notes
Ensure that a local MongoDB server is running.
