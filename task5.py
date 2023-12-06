"""
Module for handling FastAPI requests and processing webhooks.
Connects to MongoDB and registers functions to be called based on webhook data.
"""

from datetime import datetime

from fastapi import FastAPI, HTTPException

from task4 import collection

app = FastAPI()
function_handlers = {}


def register_function(function_name):
    def decorator(func):
        """
        Register Function as a Webhook Handler.
        This decorator allows you to register a function to be used as a handler for a specific webhook function.
        It associates the provided `function_name` with the decorated function in the `function_handlers` dictionary.
        """
        function_handlers[function_name] = func
        return func

    return decorator


@app.post("/Datalore")
async def process_webhook(data: dict):
    """
    This function is designed to handle incoming webhook data from a Datalore service.
    It expects a JSON payload with a 'function' field specifying the function to be executed.

    Parameters:
        data (dict): A dictionary containing the webhook data.

    Raises:
        HTTPException: If the 'function' field is missing in the webhook data (status_code=400)
        or if the specified function is not found (status_code=404).

    Returns:
        dict: A dictionary containing the result of the executed function.
    """
    function_name = data.get("function")

    if function_name is None:
        raise HTTPException(status_code=400, detail="Missing 'function' field in the webhook data")
    handler = function_handlers.get(function_name)
    if handler is None:
        raise HTTPException(status_code=404, detail=f"Function '{function_name}' not found")

    result = handler(data)
    return {"result": result}


@register_function("function1")
def handle_function1(data):
    """
    Handle function1 by inserting a document into the MongoDB collection.

    Args:
        data (dict): Input data from the webhook.

    Returns:
        dict: Result message and processed data.
    """
    current_time_utc = datetime.utcnow()
    doc = {"message": f"Handling function1",
           "createdAt": current_time_utc}
    collection.insert_one(doc)
    return {"message": "Handling function1", "data": data}


@register_function("function2")
def handle_function2(data):
    """
   Handle function2 by inserting a document into the MongoDB collection.
   Args:
       data (dict): Input data from the webhook.

   Returns:
       dict: Result message and processed data.
   """
    current_time_utc = datetime.utcnow()
    doc = {"message": f"Handling function2",
           "createdAt": current_time_utc}
    collection.insert_one(doc)
    return {"message": "Handling function2", "data": data}
