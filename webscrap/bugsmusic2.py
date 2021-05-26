from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugsmusic2(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():

        melon = Bugsmusic2()

        while 1:
            menu = input('1.extract')

            melon.url = 'https://music.melon.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'

            if menu == '1':
                soup = BeautifulSoup(urlopen(melon.url), 'html.parser')
                n_title = 0
                for link1 in soup.find_all(name='p', attrs=({"class" : "title"})):
                    n_title += 1
                    print(f'{n_title} 위')
                    print(f'{link1.find("a").text}')

Bugsmusic2.main()

