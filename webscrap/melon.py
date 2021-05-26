from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

class Melon(object):

    url = ''
    class_name = []
    hdr = { 'User-Agent' : 'Mozilla/5.0'}


    def __str__(self):
        return self.url

    def scrap(self):

        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'lxml')

        print('-------------------------ARTIST RANKING------------------------------')
        count = 0
        for i in soup.find_all(name='div', attrs=({"class": self.class_name[0]})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{i.find("a").text}')

        print('-------------------------TITLE RANKING------------------------------')
        count = 0
        for i in soup.find_all(name='div', attrs=({"class": self.class_name[1]})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{i.find("a").text}')


    # https://www.melon.com/chart/index.htm
    @staticmethod
    def main():

        melon = Melon()

        while 1:
            menu = int(input('0.exit 1.Input Url 2.Get Ranking '))

            if menu == 0:
                break
            elif menu == 1:
                melon.url = input('Input Url')
            elif menu == 2:

                melon.class_name.append("ellipsis rank02")
                melon.class_name.append("ellipsis rank01")

                melon.scrap()

            else:
                print('Wrong Number')
                continue

Melon.main()