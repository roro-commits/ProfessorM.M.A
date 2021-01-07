import scrapy


class EventdatasSpider(scrapy.Spider):
    name = 'eventDatas'

    f = open("/home/lol/Desktop/scrapy /eventLinks/eventLinks.csv")
    start_urls = [url.strip() for url in f.readlines()[2:]]
    f.close

    def parse(self, response):

        data = {}
        link = []
        fight_events = response.css('tbody')

        ### limittign tripple link
        for events in fight_events:

            for fights in events.css('td.b-fight-details__table-col.l-page_align_left'):
                for links in fights.css('p.b-fight-details__table-text a::attr(href)'):
                    # 'p.b-fight-details__table-text a::attr(href)'

                    link.append(links.getall())

            print("##############", len(link), "############")

            for i in range(0, len(link)):  # removes the fight detail and leave fighter details

                data['Events Fighter Link'] = link[i]

                yield data

        pass