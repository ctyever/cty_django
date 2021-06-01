from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    driver_path = 'C:\\Program Files\\Google\\Chrome\\chromedriver'
    title_list = []
    dic = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': self.class_name})
        self.title_list = [ i.find('a').text for i in all_div]
        print(self.title_list)
        #print(i)
        driver.close()

    def scrap_to_dict(self):

        self.dic = dict(zip(range(1, 51), self.title_list))
        print(self.dic)

    def dict_to_dataframe(self):

        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self):

        self.df.to_csv('./data/navermovie.csv', sep='.', na_rep='NaN')


if __name__ == '__main__':
    naver = NaverMovie()
    # tit3
    naver.class_name = input('클래스 네임 입력')

    naver.scrap()
    naver.scrap_to_dict()
    naver.dict_to_dataframe()
    naver.dataframe_to_csv()

