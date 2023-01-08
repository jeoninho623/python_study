# 20이상은 성인
# 14이상은 청소년
# 14미만은 어린이



# 나이 = int(input('나이를 입력하세요.'))
# if 나이 >= 20 :
#     print('성인입니다.')
# elif 나이 >=14 :          #위에 있는 if가 틀렸다는 가정하에 실행
#     print('청소년입니다.')
# elif 나이 >= 0 :                          
#     print('어린이입니다.')
# else :
#     print('?')


age = int(input('나이를 입력하세요.'))
if age >= 23:
    print('회사원')
elif age >=20 :
    print('대학교')
elif age >= 17 :
    print('고등학교')
elif age >= 14 :
    print('중학교')
elif age >= 8 :
    print('초등학교')
elif age >= 0 :
    print('유치원')
else :
    print('?')