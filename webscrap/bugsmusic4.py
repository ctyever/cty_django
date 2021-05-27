from bs4 import BeautifulSoup
import requests
import pandas as pd

class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_list = []
    artist_list = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all('p', {'class' : self.class_name[0]}):
            self.title_list.append(i.find('a').text)
        for i in soup.find_all('p', {'class' : self.class_name[1]}):
            self.artist_list.append(i.find('a').text)

    def dict_ranking(self):
        self.dict = dict(zip(self.title_list, self.artist_list))

    def dict_to_dataframe(self):

        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def dataframe_to_csv(self):

        self.df.to_csv('./data/bugs2.csv', sep=',', na_rep='NaN')


    @staticmethod
    def main():

        bugs = Bugsmusic()

        while 1:

            menu = int(input('1.inputurl\n2.get_ranking\n3.dict_ranking\n4.dict_to_dataframe\n5.dataframe_to_csv'))

            if menu == 1:
                bugs.set_url('wl_ref=M_contents_03_01')
            elif menu == 2:
                bugs.class_name.append('title')
                bugs.class_name.append('artist')
                bugs.get_ranking()
            elif menu == 3:
                bugs.dict_ranking()
            elif menu == 4:
                bugs.dict_to_dataframe()
            elif menu == 5:
                bugs.dataframe_to_csv()
            else:
                continue

Bugsmusic.main()



