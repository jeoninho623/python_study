# 문자열을 저장하는 리스트 
lst = []
num = 0
# 사용자에게 입력을 받아 리스트를 구성
# 1 : 추가하기 2 : 수정하기 3 : 삭제하기 4 : 전체보기

while True :
    num = int(input('1:추가, 2:수정 3: 삭제 4:조회'))
    if num == 1:
        add = input('추가할 값을 입력하세요>>')
        lst.append(add)
                    # 값을 추가
    elif num == 2:
        수정 = input('수정하고자하는 값을 입력하세요>>')
        ktx = lst.index(수정)
        값 = input('수정할 값을 입력하세요>>')
        lst[ktx] = 값
                   # 값을 수정 (수정하고자하는 값, 수정할 값)
    elif num == 3:
        삭제 = input('삭제할 값을 입력하세요>>')
        lst.remove(삭제)
                    # 삭제할 값을 입력
    elif num == 4:
            print(lst)            #전체조회
    elif num == 0:
        print('프로그램을 종료합니다.')
        break
    else :
        print('없는 번호입니다.')
