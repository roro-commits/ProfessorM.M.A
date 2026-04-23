import logging
import scrapy
from scrapy.loader import ItemLoader
from typing import Generator

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

url = "http://ufcstats.com/statistics/fighters?char={}&page=all"


class fighter_spider(scrapy.Spider):
    name = "ultimate_fighter"

    async def start(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            yield scrapy.Request(url=url.format(char), callback=self.parse)

    def parse(self, response: scrapy.http.Response) -> Generator[list[str]]:
        """
        A function to iterate through the uc fighter
        """
        fighter_table = response.css("tr.b-statistics__table-row")
        for fighter_attribute in fighter_table:
            # logging.info(fighter)
            data = {}

            fighter_id = fighter_attribute.css(
                "td.b-statistics__table-col:nth-child(1) a::attr(href)"
            ).get()
            data["fighterID"] = fighter_id

            first_name = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(1) a::text")
                .get(default="")
                .strip()
            )
            data["firstName"] = first_name

            last_name = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(2) a::text")
                .get(default="")
                .strip()
            )

            data["lastName"] = last_name

            nick_name = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(3) a::text")
                .get(default="")
                .strip()
            )

            data["nickName"] = nick_name

            height = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(4) a::text")
                .get(default="")
                .strip()
            )

            data["height"] = height

            weight = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(5) a::text")
                .get(default="")
                .strip()
            )

            data["weight"] = weight

            reach = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(6) a::text")
                .get(default="")
                .strip()
            )

            data["reach"] = reach

            stance = (
                fighter_attribute.css("td.b-statistics__table-col:nth-child(7) a::text")
                .get(default="")
                .strip()
            )

            data["stance"] = stance

            win = (
                fighter_attribute.css(
                    "td.b-statistics__table-col_type_small:nth-child(8)::text "
                )
                .get(default="")
                .strip()
            )

            data["win"] = win

            loss = (
                fighter_attribute.css(
                    "td.b-statistics__table-col_type_small:nth-child(9)::text"
                )
                .get(default="")
                .strip()
            )

            data["loss"] = loss

            draw = (
                fighter_attribute.css(
                    "td.b-statistics__table-col_type_small:nth-child(10)::text"
                )
                .get(default="")
                .strip()
            )

            data["draw"] = draw

        logging.info(data)

        yield data
