from datetime import datetime
from fastapi import FastAPI, HTTPException
from task4 import collection

app = FastAPI()
function_handlers = {}


def register_function(function_name):
    def decorator(func):
        function_handlers[function_name] = func
        return func

    return decorator


@app.post("/Datalore")
async def process_webhook(data: dict):
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
    current_time_utc = datetime.utcnow()
    doc = {"message": f"Handling function1",
           "createdAt": current_time_utc}
    collection.insert_one(doc)
    return {"message": "Handling function1", "data": data}


@register_function("function2")
def handle_function2(data):
    current_time_utc = datetime.utcnow()
    doc = {"message": f"Handling function2",
           "createdAt": current_time_utc}
    collection.insert_one(doc)
    return {"message": "Handling function2", "data": data}
