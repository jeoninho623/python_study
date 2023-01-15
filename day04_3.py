cafe_menu = []

# 카페 메뉴 이름
cafe_menu.append('아아')
cafe_menu.append('라떼')
cafe_menu.append('스무디')
cafe_menu.append('프라페')

print(cafe_menu)
print(cafe_menu[0])

# 데이터의 갯수 len
리스트의갯수 = len(cafe_menu)
print(리스트의갯수)

# 수정
cafe_menu[0] = '에소'

#전체 출력
for i in cafe_menu :
    print(i, end = ' ')
    
