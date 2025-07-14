import json


PRODUCTS_MENU_PATH = "data/menu.json"

def load_all_products():
    with open(PRODUCTS_MENU_PATH, encoding="utf-8") as file:
        return json.load(file)

def get_product_by_name(name: str):
    menu = load_all_products()

    for product in menu:
        if product.get("name", "").lower() == name.lower():
            return product

    return {"error": "Product not found"}

def get_product_field(name: str, field: str):
    product = get_product_by_name(name)

    if "error" in product:
        return product

    return {field: product.get(field, "Field not found")}