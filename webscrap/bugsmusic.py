from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def scrap(bugs):
        soup = BeautifulSoup(urlopen(bugs.url), 'html.parser')


        for i in soup.find_all(name='p', attrs=({"class": "left"})):
            count = 0
            count += 1
            print(f'{count} 위')
            print(f'{soup.find("a").text}')
        for i in soup.find_all(name='td', attrs=({"class": "left"})):
            count = 0
            count += 1
            print(f'{count} 위')
            print(f'{soup.find("a").text}')


    #'https://music.melon.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'

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
                #print({melon})

                soup = BeautifulSoup(urlopen(bugs.url), 'html.parser')
                melon.ranking(soup)


                ''' 
                print('-------------------------ARTIST RANKING------------------------------')
                count = 0
                for i in soup.find_all(name='p', attrs=({"class" : "artist"})):
                    count += 1
                    print(f'{count} 위')


                print('-------------------------TITLE RANKING------------------------------')
                '''


            else:
                print('Wrong Number')
                continue

melonMusic.main()