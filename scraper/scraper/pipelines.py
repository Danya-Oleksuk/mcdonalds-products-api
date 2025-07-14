import json
import os


class JsonWriterPipeline:
    def __init__(self):
        self.items = []

    def open_spider(self, spider):
        if os.path.exists('../data/menu.json'):
            os.remove('../data/menu.json')

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        with open('../data/menu.json', 'w', encoding='utf-8') as file:
            json.dump(self.items, file, ensure_ascii=False, indent=4)
