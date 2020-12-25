import csv

import scrapy


class UfcEventsSpider(scrapy.Spider):
    name = 'ufc_events'
    urls = []
    eventCounter = 0
    f = open("/ProfessorM.M.A/ufc_data/event_fights.csv")
    start_urls = [url for url in f.readlines()[1:]]
    # urls.append(url)
    # start_urls = [url[0]]
    f.close
    # start_urls = [urls[0][eventCounter]]
    # eventCounter = eventCounter+1

    def parse(self, response):
        # urls = []
        # f = open("/home/rotimi/Documents/FYP/ProfessorM.M.A/ufc_data/event_fight_copy.csv")
        # url = [url for url in f.readlines()[0:]]
        # urls.append(url)
        # f.close

        data = {}
        clean = []
        fighter_stats = response.css('div.l-page__container')
        fight_attribute = []

        for stats in fighter_stats:

            # for x in stats.css('span.b-content__title-highlight::text'):
            for x in stats.css('span.b-content__title-highlight::text'):
                data['NAME'] = x.getall()[0].strip()


            ###### player attributes sides #######################
            for x in stats.css('div.b-list__info-box_style_small-width'):

                for g in x.css('ul.b-list__box-list'):
                    # for i in g.css('li.b-list__box-list-item:first-child::text'):
                    #     data['HEIGHT'] = i.getall()[0].strip()

                    for x in g.css('li.b-list__box-list-item_type_block::text'):
                        fight_attribute.append(x.getall()[0].strip())

                        strip = fight_attribute

            ############# career staticstics side##########
            for x in stats.css('div.b-list__info-box_style_middle-width'):
                for g in x.css('ul.b-list__box-list_margin-top'):

                    for x in g.css('li.b-list__box-list-item_type_block::text'):
                        fight_attribute.append(x.getall()[0].strip())

                data['HEIGHT'] = fight_attribute[1]
                data['WEIGHT'] = fight_attribute[3]
                data['REACH'] = fight_attribute[5]
                data['STANCE'] = fight_attribute[7]
                data['DOB'] = fight_attribute[9]
                data['SLpM'] = fight_attribute[11]
                data['Str. Acc..'] = fight_attribute[13]
                data['SApM'] = fight_attribute[15]
                data['Str. Def'] = fight_attribute[17]
                data['TD Avg'] = fight_attribute[21]
                data['TD Acc'] = fight_attribute[23]
                data['TD Def.'] = fight_attribute[25]
                data['Sub. Avg'] = fight_attribute[27]
                yield data







        # for i in range(1,5):
        #
        #     eventCounter = eventCounter + 1
        #     print("#######################", i, urls[0][i])
        #     if eventCounter:
        #         yield scrapy.Request(urls[0][i], self.parse)
        #
        #     print(eventCounter)
        #
