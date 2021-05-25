from bs4 import BeautifulSoup
from urllib.request import urlopen

class Melon(object):

    url = ''

    def __str__(self):
        return self.url

    #https://www.melon.com/chart/index.htm
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
                # print({melon})

                soup = BeautifulSoup(urlopen(melon.url), 'html.parser')

                print('-------------------------ARTIST RANKING------------------------------')
                count = 0
                for i in soup.find_all(name='div', attrs=({"class" : "ellipsis rank01"})):
                    count += 1
                    print(f'{count} 위')
                    print(f'{i.find("a").text}')

                print('-------------------------TITLE RANKING------------------------------')
                count = 0
                for i in soup.find_all(name='div', attrs=({"class": "ellipsis rank02"})):
                    count += 1
                    print(f'{count} 위')
                    print(f'{i.find("a").text}')

            else:
                print('Wrong Number')
                continue

Melon.main()