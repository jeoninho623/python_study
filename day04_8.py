# 튜플! tuple
# tuple = ()
# 튜플 : 추가 못행

menu = ('돈까스','순두부','김밥')           # 추가 안됑
print(menu[0])
print(menu[1])
print(menu[2])

name1 = ''
name2 = ''
name3 = ''

name1, name2, name3 = menu
name1, name2, name3 = ('안녕하세요','hello', '반갑습니다')
print(name1, name2, name3)

# 전체 조회
print('전체 메뉴를 출력합니다.')
for i in menu : 
    print(i)