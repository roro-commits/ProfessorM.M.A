import scrapy
# this is start1 events

class FightstatsLinkSpider(scrapy.Spider):
    name = 'fightStats_link'
    allowed_domains = ['www.ufcstats.com']
    start_urls = ['http://ufcstats.com/statistics/events/completed?page=all']

    def parse(self, response):
        data = {}
        link = []
        fight_events = response.css('tbody')

        ### limittign tripple link 
        for events in fight_events:

            for links in events.css('i.b-statistics__table-content a::attr(href)'):
                link.append(links.getall())

            print("##############", len(link), "############")

            for i in range(len(link)):
                data['Events Fight Link'] = link[i]

                yield data

        pass
