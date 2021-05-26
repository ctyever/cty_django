class Gugudan(object):

    number = 0
    dict = {}

    def print_selected_dan(self):
        for i in range(1, 10):
            print(f'{self.number} * {i} = {self.number * i}')

    def print_all_dan(self):
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i} * {j} = { i * j }')

    def print_dict_dan(self):
        d = self.dict
        for i in range(1, 10):
            d[i] = self.number * i
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.number} * {k} = {d.get(k)}')

    @staticmethod
    def main():

        dan = Gugudan()

        while 1:

            menu = int(input('1.개별 단수 출력 2.전체 구구단 출력 3.input dan with dict' ))

            if menu == 1:
                dan.number = int(input('숫자 입력'))
                dan.print_selected_dan()

            if menu == 2:
                dan.print_all_dan()

            if menu == 3:
                dan.number = int(input('숫자 입력'))
                dan.print_dict_dan()

Gugudan.main()

