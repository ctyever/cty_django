from bs4 import BeautifulSoup
import requests


class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        ls = []
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all('div', {'class': self.class_name[0]}):
            #print(i.find('a').text)
            ls.append(i.find('a').text)

        #for i in soup.find_all('div', {'class': self.class_name[1]}):
            #print(i.find('a').text)



    @staticmethod
    def main():

         melon = Melon()

         while 1:

             menu = int(input('0.Exit 1.InputTime 2.GetRanking'))

             if menu == 0:
                 break

             elif menu == 1:

                 #2021052608
                 melon.set_url(input('Time'))

             elif menu == 2:

                 melon.class_name.append('ellipsis rank01')
                 melon.class_name.append('ellipsis rank02')
                 melon.get_ranking()

             else:
                 print('Wrong Number')

Melon.main()







