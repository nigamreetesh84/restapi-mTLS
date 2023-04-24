from fastapi import FastAPI
from pydantic import BaseModel
import ssl
from fastapi.responses import PlainTextResponse

# Define the models
class Item(BaseModel):
    name: str
    price: float

# Create the FastAPI applications
app2 = FastAPI()

# Configure mTLS for each application

app2_ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
app2_ssl_context.load_cert_chain(certfile="app2.crt", keyfile="app2.key")
app2_ssl_context.load_verify_locations(cafile="ca.crt"))

# Define the routes

@app2.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app2.get("/healthcheck")
async def healthcheck():
    return PlainTextResponse("OK")
