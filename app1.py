from fastapi import FastAPI
from pydantic import BaseModel
import ssl
from fastapi.responses import PlainTextResponse

# Define the models
class Item(BaseModel):
    name: str
    price: float

# Create the FastAPI applications
app1 = FastAPI()

# Configure mTLS for each application
app1_ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
app1_ssl_context.load_cert_chain(certfile="app1.crt", keyfile="app1.key")
app1_ssl_context.load_verify_locations(cafile="ca.crt")



# Define the routes
@app1.post("/items/")
async def create_item(item: Item):
    return item

