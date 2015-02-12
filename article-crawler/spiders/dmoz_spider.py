import scrapy
import HTMLParser

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        #"https://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"https://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        #"http://finance.yahoo.com/news/cisco-earnings-53-cents-per-210559266.html",
        "http://finance.yahoo.com/news/can-tim-cook-grow-apple-to-a-trillion-174014745.html",
        "http://finance.yahoo.com/news/icahn-values-apple-more-1-013021347.html",
        "http://finance.yahoo.com/news/irs-apologizes-seizing-bank-accounts-172627143.html"
    ]

    def parse(self, response):

        name = ''
        body = ''

        for sel in response.xpath('/html/head/meta[@property = "og:title"]'):
            title = sel.xpath('@content').extract()
            h = HTMLParser.HTMLParser()
            name = ''.join(h.unescape(title)).encode("utf-8")
            print"\n"
            print title


        for paragraph in response.xpath('//p'):
                text = paragraph.xpath('text()').extract()
                h = HTMLParser.HTMLParser()
                decoding = ''.join(h.unescape(text)).encode("utf-8")
                body += ''.join(h.unescape(text)).encode("utf-8")
                print "\n"
                print decoding

        with open(name, 'w') as f:
            f.write(body)
        print "\n\n\n\n"
