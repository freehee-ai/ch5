# for 문으로 리스트 요소를 하나씩 출력하기

lis = ['a','b','c','d','e'] 
for ch in lis :     # ch에 덮어쓰기?교체?
    print(ch)

# while 문과 for 문의 차이
# while : 조건을 만족하는 동안 실행
# for : 자료구조(리스트, 튜플 등)을 순회

# 딕셔너리 생성
# key : value
# 키는 과일이고 값은 가격인 과일 목록 생성
dic = {'apple': 1200, 'banana': 800, 'orange' : 1500}

# for 문으로 딕셔너리의 요소를 하나씩 출력
for key in dic : 
    print(key)

print(dic.items())
print(dic.keys())
print(dic.values())

# for 문 구조
# for 변수 in 자료구조 or 딕셔너리에서 반환된 객체
                    # dic.items(),dic.keys(),dic.values()

# for 문으로 딕셔너리의 키와 값 모두 꺼내기
items = dic.items()

for key, value in items :
    print(key, value)

# 아이템 안의 요소 하나씩 꺼내기
# 튜플 형태로 반환된다.
for t in items :
    print(t)

# # 튜플 만들기
# t = ('apple', 12000)
# # 튜플 분해하기
# # 요소 순서대로 변수에 할당됨
# a, b = t
# print(a, b)

values = dic.values()
print(values)

for value in values :
    print(value)


# iterable : 순회가 가능한 객체

# for 문의 구조
# for 변수 in 자료구조 또는 iterable