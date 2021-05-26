class Member(object):

    id = ''
    name = ''
    pw = ''
    email = ''

    def join(self):
        self.id = input('id')
        self.name = input('name')
        self.pw = input('pw')
        self.email = input('email')

        return f'{self.id}{self.name}{self.pw}{self.email}'

    def login(self):
        loginid = input('id입력')
        loginpw = input('pw입력')
        if ord(self.id) == ord(loginid) & ord(self.pw) == ord(loginpw):
            print("로그인 성공")
        else:
            print("잘못된 아이디이거나 패스워드입니다")

    def mypage(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    '''
    def __init__(self, id, name, pw, email):
        self.id = id
        self.name = name
        self.pw = pw
        self.email = email
    '''

    '''
    def __str__(self):
        return f'{self.id}{self.name}{self.email}'
    '''

    @staticmethod
    def main():

        member = Member()

        ls = []

        while 1:
            menu = int(input('0.종료 1.회원가입 2.회원목록 3.로그인 4.MY PAGE 5.회원정보 수정 6.삭제'))

            if menu == 0:
                break
            elif menu == 1:
                a = member.join()
                ls.append(a)

                '''
                ls.append(Member(input('id'), input('name'), input('pw'), input('email')))
                '''

            elif menu == 2:
                for i in ls:
                    print(i)
            elif menu == 3:
                member.login()


            elif menu == 5:

                edit_id = input('id를 입력하세요')
                for i, j in enumerate(ls):
                    if j.id == edit_id:
                        ls[i] = Member(edit_id, j.name, input('pw'), input('email'))
                    else:
                        print('없는 id입니다')
            elif menu == 4:
                delete_id = input('id를 입력하세요')
                for i, j in enumerate(ls):
                    if j.id == delete_id:
                        del ls[i]

Member.main()

