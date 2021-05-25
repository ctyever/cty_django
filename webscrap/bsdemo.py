from bs4 import BeautifulSoup

class Bsdemo(object):

    html_doc = ''

    def __str__(self):
        return self.html_doc

    @staticmethod
    def main():

        bs = Bsdemo()

        while 1:

            menu = int(input('0.exit\n1.InputHtml_doc\n2.OutputHtml_doc\n3.print title'))

            if menu == 0:
                break
            elif menu == 1:
                bs.html_doc = '''<html><head><title>The Dormouse's story</title></head>
                                <body>
                                <p class="title"><b>The Dormouse's story</b></p>
                                
                                <p class="story">Once upon a time there were three little sisters; and their names were
                                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                and they lived at the bottom of a well.</p>
                                
                                <p class="story">Test value</p>
                                '''
            elif menu == 2:
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.prettify())
            elif menu == 3:
                print(soup.title.name)
                print(soup.p['class'])

            else:
                print('WrongNumber')
                continue

Bsdemo.main()

