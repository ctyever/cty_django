from selenium import webdriver
from bs4 import BeautifulSoup


class Samsung(object):

    url = 'https://finance.naver.com/item/frgn.nhn?code=005930'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    price = []
    day = []
    dic = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        ls1 = soup.find_all('td', {'class': 'tc'})
        ls2 = soup.find_all('td', {'class': 'num'})
        for i in ls1:
            self.day.append(i.find('span').text)
        for i in ls2:
            self.price.append(i.find('span').text)

    def scrap_to_dict(self):
        dic = dict(zip(self.day, self.price))
        print(dic)


Samsung().scrap()
Samsung().scrap_to_dict()
