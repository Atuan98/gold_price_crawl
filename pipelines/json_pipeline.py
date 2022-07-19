import json


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
