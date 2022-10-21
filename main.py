from webscrape import WebCrawler
from selenium_automation import AutoFill

crawler = WebCrawler()

listings_details = crawler.generate_all_details(crawler.raw_items, crawler.all_address)

client = AutoFill()


for index in range(len(listings_details['address'])):
    client.input_address(listings_details['address'][index])
    client.input_price(listings_details['prices'][index])
    client.input_link(listings_details['links'][index])
    client.input_coor(listings_details['coordinates'][index])
    client.submit_button()
    if index < len(listings_details['address']) - 1:
        client.resubmit_button()


client.browser.quit()






