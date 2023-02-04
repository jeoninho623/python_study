# 클래스를 만들어보세요
# 속성(멤버변수) : 차주인, 색상, 차종
# 기능 (메서드) : 차정보, 차운전

class 자동차:
    info1 = ''
    info2 = ''
    info3 = ''
    def 차정보(self):
        print('차주:',self.info1, '색상:',self.info2,'차종:', self.info3)
    def 차운전(self):
        print(self.info1,"가(이) 운전합니다.")
    def __init__(self,info1,info2, info3) :
        self.info1 = info1
        self.info2 = info2
        self.info3 = info3      
    

# 클래스 사용예시
아빠차 = 자동차('아빠','black','x7')                # 클래스명 옆에 있는 () : __init__ 생성자
엄마차 = 자동차('엄마','white','x5')
내차 = 자동차('홍길동','white','530i')

아빠차.차정보() # 차주인, 차색장, 차종을 print
엄마차.차정보()
내차.차정보()

아빠차.차운전()     # 아빠가 차를 운전합니다
내차.차운전()     # 홍길동이 차를 운전합니다


# 메서드가 같아도 객체가 다르면 그 객체에 해당하는 메서드와 멤버변수로 사용됨