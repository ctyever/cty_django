import pandas as pd
from bs4 import BeautifulSoup
import requests
import pandas

class Melon3(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_list = []
    artist_list = []
    dict = {}
    df = None

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

    def dict_to_dataframe(self):

        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

    def dataframe_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


    @staticmethod
    def main():

        melon = Melon3()

        while 1:

            menu = int(input('1.Time\n2.Output\n3.insert_title_dict\n4.OutDataFrame\n5.dataframe_to_csv'))

            if menu == 1:
                melon.set_url(input('Inputtime')) #2021052608
            elif menu == 2:
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            elif menu == 3:
                melon.insert_title_dict()
            elif menu == 4:
                melon.dict_to_dataframe()
            elif menu == 5:
                melon.dataframe_to_csv()


Melon3.main()


