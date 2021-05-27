import pandas as pd

class Conversion(object):


    @staticmethod
    def create_tuple() -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @staticmethod
    def convert_list(tp) -> []:
        return list(tp)

    @staticmethod
    def convert_float_list(ls) -> []:
        return [float(i) for i in ls]

    @staticmethod
    def convert_int_list(ls) -> []:
        return [int(i) for i in ls]

    @staticmethod
    def list_convert_dictionary(ls) -> {}:
        return dict([str(i) for i in zip(ls, ls)])

    @staticmethod
    def str_convert_tuple(st) -> ():
        return tuple(list(st))

    @staticmethod
    def str_tuple_convert_list(tp) -> []:
        return list(tp)

    @staticmethod
    def dict_to_dataframe(dt) -> object:
        pass

    @staticmethod
    def main():
        tp = ()
        ls = []
        dt = {}
        df = pd.DataFrame({})

        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                tp = c.create_tuple()
                print(tp)
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                ls = c.convert_list(tp)
                print(ls)
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                ls = c.convert_float_list(ls)
                print(ls)
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                ls = c.convert_int_list()
                print(ls)
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                dt = c.convert_int_list(ls)
                print(dt)
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                tp = c.str_tuple_convert_list('hello')
                print(tp)
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                ls = c.str_tuple_convert_list(tp)
                print(ls)
            elif m == '8':
                pass
            else:
                continue
Conversion.main()