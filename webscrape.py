from bs4 import BeautifulSoup
import requests
import locale
locale.setlocale(locale.LC_ALL,'')


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(url="https://www.myproperty.ph/pampanga/buy/price:750000-2000000/?sorting=newest", headers=header)

context = response.text


class WebCrawler(BeautifulSoup):
    def __init__(self):
        super(WebCrawler, self).__init__()
        self.soup = BeautifulSoup(context, 'html.parser')
        self.raw_items = self.soup.find_all(name='div', class_='ListingCell-AllInfo ListingUnit')
        self.all_address = self.soup.find_all(name='span', class_='ListingCell-KeyInfo-address-text')
        self.links = self.soup.select('.js-listing-link')
        self.all_links = [item['href'] for item in self.links]
        self.all_links = self.all_links[::2]

    def generate_all_details(self, raw_items, all_address):
        sorted_details = {'address': [],
                          'prices': [],
                          'links': [],
                          'coordinates': []}

        for i in range(len(raw_items)):
            raw_price = float(raw_items[i]['data-price'])
            price = f'{raw_price:,}'
            address = "".join(all_address[i].stripped_strings)
            coor = raw_items[i]['data-geo-point']
            coor = coor.split(',')
            x = coor[1].strip(']')
            y = coor[0].strip('[')
            coordinate = f"x= {x}, y= {y}"
            link = self.all_links[i]

            sorted_details['address'].append(address)
            sorted_details['prices'].append(f'PHP {price}')
            sorted_details['links'].append(link)
            sorted_details['coordinates'].append(coordinate)

        return sorted_details





