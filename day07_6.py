# 학생 클래스
# 속성(멤버변수) : 이름, 번호, 키
# 기능(메서드) : 학생정보보기, 학생정보입력, __init__

class 학생 :
    name = ''
    n = 0
    hei = 0.0
    def 학생정보보기(self):
        print('이름 :',self.name, '번호:', self.n, '키:',self.hei)

    def __init__(self,name,n,hei):
        self.학생정보입력(name, n, hei)

    def 학생정보입력(self,name,n,hei):
        self.name = name
        self.n = n
        self.hei = hei
    
        
# 사용 예시
철수 = 학생('김철수', 1, 177.7)
영희 = 학생('박영희', 2, 155.5)
짱구 = 학생('신짱구', 3, 173.3)

철수.학생정보보기()
영희.학생정보보기()
짱구.학생정보보기()

짱구.학생정보입력('짱구', 4, 174.0)
짱구.학생정보보기()



