# print('안녕하세요 제 이름은' , 이름 , '입니다.')
# print('나이는' , 나이 , '살이고 성별은' , 성별 , '입니다.')
# print('키는' , 키 , 'cm입니다.')

#input 과 print를 활용해서 만들어보기
#이름은 무엇인가요?
#나이는 몇살인가요?   int()
#성별은 무엇인가요?
#키는 몇인가요?    float()


'''
안녕하세요 제 이름은 ***입니다.
나이는 **살이고 성별은 **입니다.
키는 ***.*cm입니다.
'''

# 이름 = input('이름은 무엇인가요?')
# 나이 = input('나이는 몇살인가요?')
# 성별 = input('성별은 무엇인가요?')
# 키 = input('키은 얼마인가요?')
# print('안녕하세요 제 이름은',이름,'입니다.','나이는 ',int(나이), '살이고 성별은 ',성별,'입니다.','제 키는', float(키),'cm입니다.')
# print('====================================================')



#2
'''
10~99 사이 숫자를 입력 받아서
십의 자리와 일의 자리를 알려주시오
'''


숫자 = input('10~99 사이의 숫자를 입력하세요 :')
print('십의자리 :',int(int(숫자)/10))
print('일의자리 :',int(숫자)%10)
