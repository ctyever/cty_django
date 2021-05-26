from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

class Melon2(object):

    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(urlopen(html), 'html.parser')
        for i in soup.find_all(name= 'div', attrs=({'class': self.class_name[0]})):
            print(i.find('a').text)
        for i in soup.find_all(name='div', attrs=({'class' : self.class_name[1]})):
            print(i.find('a').text)


    @staticmethod
    def main():

        melon = Melon2()

        while 1:
            menu = int(input('1.inpput_url 2.ranking'))

            if menu == 1:
                melon.set_url('2021052517')
            elif menu == 2:
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()

Melon2.main()
