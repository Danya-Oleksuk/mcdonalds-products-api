from fastapi import FastAPI

from fastapi_app import services


app = FastAPI()

@app.get("/all_products/")
def all_products():
    return services.load_all_products()

@app.get("/products/{product_name}")
def product_by_name(product_name: str):
    return services.get_product_by_name(product_name)

@app.get("/products/{product_name}/{product_field}")
def product_field(product_name: str, product_field: str):
    return services.get_product_field(product_name, product_field)