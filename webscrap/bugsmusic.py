from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''
    class_name = []

    def __str__(self):
        return self.url


    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), "lxml")

        count = 0
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[0]})):

            count += 1
            print(f'{count} 위')
            print(f'{i.find("a").text}')

        count = 0
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            count += 1
            print(f'{count} 위')
            print(f'{i.find("a").text}')


    #'https://music.bugs.co.kr/chart'

    @staticmethod
    def main():

        bugs = BugsMusic()

        while 1:
            menu = int(input('0.exit 1.Input Url 2.Get Ranking '))

            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input Url')
            elif menu == 2:
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.scrap()

            else:
                print('Wrong Number')
                continue

BugsMusic.main()