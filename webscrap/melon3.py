from bs4 import BeautifulSoup
import requests

class Melon3(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_list = []
    artist_list = []
    dict = {}

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        #print('----------제목---------')
        artist = ''
        for i in soup.find_all(name='div', attrs=({'class' : self.class_name[0]})):
            print(f'{i.find("a").text}')
            self.title_list.append(i.find("a").text)

        #print('----------가수---------')

        for i in soup.find_all(name='div', attrs=({'class' : self.class_name[1]})):
            print(f'{i.find("a").text}')
            self.artist_list.append(i.find("a").text)

    def insert_title_dict(self):

        print('----------제목---------')
        dict = self.dict
        for i, j in enumerate(self.title_list):
            self.dict[j] = self.artist_list[i]
        print(dict)

    @staticmethod
    def main():

        melon = Melon3()

        while 1:

            menu = int(input('1.Time 2.Output 3.title'))

            if menu == 1:
                melon.set_url(input('Inputtime')) #2021052608
            elif menu == 2:
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            elif menu == 3:
                melon.insert_title_dict()


Melon3.main()


