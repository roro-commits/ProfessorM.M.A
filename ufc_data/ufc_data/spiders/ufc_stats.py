import scrapy


class UfcStatsSpider(scrapy.Spider):
    name = 'ufc_stats'
    start_urls = ['http://www.ufcstats.com/statistics/fighters?char={}&page=all']

    def parse(self, response):
        data = {}
        link =[]
        fighter_names = response.css('tbody')
        
        ### limittign tripple link 
        for stats in fighter_names:

            for names in stats.css('td.b-statistics__table-col a::attr(href)'):

                link.append(names.getall())
            
            print("##############",len(link),"############")
              
            for i in range(len(link)):



                data['Figter stats Link'] = link[i*3]

                    

                yield data

           
    

        pass
