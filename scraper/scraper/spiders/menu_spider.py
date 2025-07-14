import scrapy
import json
from scraper.items import ProductItem


class MenuSpider(scrapy.Spider):
    name = 'Menu'
    allowed_domains = ['www.mcdonalds.com']
    start_urls = ['https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html']

    def parse(self, response):
        products = response.css("li.cmp-category__item")

        for product in products:
            product_id = product.css("::attr(data-product-id)").get()

            if product_id:
                api_url = (
                    f"https://www.mcdonalds.com/dnaapp/itemDetails"
                    f"?country=UA&language=uk&showLiveData=true&item={product_id}"
                )
                yield scrapy.Request(api_url, callback=self.parse_product, dont_filter=True)

    def parse_product(self, response):
        data = json.loads(response.text)
        item_data = data.get("item", {})

        product = ProductItem()

        product["name"] = item_data.get("item_name")
        product["description"] = item_data.get("description")


        nutrients = {n["name"]: n["value"] for n in item_data.get("nutrient_facts", {}).get("nutrient", [])}
        print(f"----------------------nutrients: {nutrients}")

        product["calories"] = nutrients.get("Калорійність")
        product["fats"] = nutrients.get("Жири")
        product["carbs"] = nutrients.get("Вуглеводи")
        product["proteins"] = nutrients.get("Білки")
        product["sugar"] = nutrients.get("Цукор")
        product["salt"] = nutrients.get("Сіль")
        product["portion"] = nutrients.get("Вага порції")
        product["unsaturated_fats"] = nutrients.get("НЖК")

        yield product
