from webscrap import melon4

class Vectortest(object):

    ls = []
    tinyls = [123, 'john']

    def list_CRUD_Example(self, menu):

        if menu == 0:
            melon4.Melon.main()

        elif menu == 1:
            self.ls.append(100)
            print(f'Create: ls 에 100을 추가 : {self.ls}')

        elif menu == 2:
            for i in self.ls:
                print(f'Read: ls 의 목록을 출력 : {i}')

        elif menu == 3:
            self.ls.extend(self.tinyls)
            print(f'Update: ls와 tinyls 의 결합 : {self.ls}')

        elif menu == 4:
            self.ls.remove(786)
            print(f'Delete: ls 에서 786을 제거 : {self.ls}')

    def tuple_CRUD_Example(self, menu):
        tp = ('abcd', 786, 2.23, 'john', 70.2)
        tinytp = (123, 'john')

        if menu == 5:
            tp += (100,)
            print(f'Create: tp 에 100을 추가 : {tp}')

        elif menu == 6:
            for i in tp:
                print(f'Read: tp 의 목록을 출력 : {i}')


        elif menu == 7:
            tp += (tinytp)
            print(f'Update: tp와 tinytp 의 결합 : {tp}')


    def dictionary_CRUD_Example(self, menu):
        dt = {'abcd': 786, 'john': 70.2}
        tinydt = {'홍' : 123, '30세' : 456}

        if menu == 9:
            dt['tom'] = 100
            print(f'Create: dt 에 키값으로 tom, 밸류로 100을 추가 : {dt}')

        elif menu == 10:
            for i in dt:
                print(f'Read: dt 의 목록을 출력 : {i}')

        elif menu == 11:
            dt.update(tinydt)
            print(f'Update: dt와 tinydt 의 결합 : {dt}')

        elif menu == 12:
            del dt['abcd']
            print(f'Delete: dt 에서 abcd 제거 : {dt}')


    @staticmethod
    def main():


        vectortest = Vectortest()

        while 1:
            menu = int(input('List_CRUD_Example : 1.Create 2.Read 3.Update 4.Delete\n'
                             'Tuple_CRUD_Example : 5.Create 6.Read 7.Merge 8.Delete\n'
                             'Dictionary_CRUD_Example : 9.Create 10.Read 11.Update 12.Delete'))

            if menu in range(0,5):

                vectortest.list_CRUD_Example(menu)

            elif menu in range(5,9):
                vectortest.tuple_CRUD_Example(menu)

            elif menu in range(9,13):
                vectortest.dictionary_CRUD_Example(menu)

Vectortest.main()
