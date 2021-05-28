import pandas as pd
from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all('p', {'class' : self.class_name[1]})
        ls2 = soup.find_all('p', {'class': self.class_name[0]})
        for i in ls1:
            self.title_ls.append(i.find('a').text)
        for i in ls2:
            self.artist_ls.append(i.find('a').text)

    def insert_title_dict(self):

        self.dict = dict(zip(self.title_ls, self.artist_ls))

    def dict_to_dataframe(self):

        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

        print(self.df)

    def save_as_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3-print dict 4-dict_to_dataframe')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('wl_ref=M_contents_03_01')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()

            elif menu == '4':
                bugs.dict_to_dataframe()
            elif menu == '5':
                bugs.save_as_csv()
            else:
                print('Wrong Number')
                continue

BugsMusic.main()