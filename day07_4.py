# 생성자 : 클래스는 초보자를 위해서 만듦, 근데 얘가 제대로 사용을 못함
# 함수는 def, 클래스는 class
class 회사프로그램:
    n1 = 0              # 멤버변수 : 클래스 안에 있는 변수
    n2 = 0
    # 메서드 : 클래스 안에 있는 함수(매개변수 가장 앞에 self라는 매개변수를 만들어놓아야함)
    def AbsSum(self, n1, n2):           # self : 메서드 고정 매개변수로 사용할 때 채우지 않음(사용 X)
        result = 0              # 지역변수 : 함수 안에 있는 변수
        if n1 < 0:
            n1 = n1 * -1
        if n2 < 0:
            n2 = n2 * -1
        self.n1= n1             # self.n1 : 매개변수의 n1
        self.n2= n2             # n2 : 지역변수의 n2
        result = n1 + n2
        return result
    def Last(self):             # 사실상 매개변수가 없는 매서드 (self)는 함수가 아니라 매서드
        print(self.n1 + self.n2)
    # 생성자 __init__ : 객체화하는 순간에 사용될 메서드
    def __init__(self):
        # 생성자
        # 객체화를 하는 순간에 실행될 코드
        # 객체화하는 순간에 클래스명 앞에 있는 ()
        print('회사프로그램 객체화를 성공했습니다!!')
    def __init__(self, 수1, 수2):
        self.AbsSum(수1, 수2)
        #필요한 사전작업은 다 하고 들어간다!


a = 회사프로그램(3, 5)
# 생성자라는 문법을 추가해서 사전 작업을 사람이 하지 않아도 자동사용되게끔 처리
a.Last()
# 클래스 이름 옆에 있는 ()는 __init__를 사용하는 코드
b = 회사프로그램(5, -2)
b.Last()
