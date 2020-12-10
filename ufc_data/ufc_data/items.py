# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import MapCompose
import scrapy

def replace_quotes(text):
    for c in ['“', '”']:
        if c in text:
            text = text.replace(c, "")

class UfcDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field(output_processor= MapCompose(replace_quotes))
    pass
