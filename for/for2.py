# # range : 연속된 숫자를 만들어주는 함수
# # 반환값 : 숫자를 담고 있는 range 객체
# # 0 부터 9까지 연속된 숫자 10개가 반환됨
# nums = range(10) # 인자 : 개수
# print(nums)
# # 사용방법
# for n in nums : # 변수 n에 nums 의 요소를 차례로 담는다
#     print(n)

# # range 객체를 사용해 "안녕하세요" 10번 출력
# for n in nums :
#     print("안녕하세요")

# # 1부터 10까지
# num = range(1,11)
# print(num)
# for n in num :
#     print(n)

# # range 의 값이 필요하지 않은 경우
# for _ in nums :         # 언더바로 생략 가능
#     print("안녕하세요")

# input : 키보드를 통해 값을 입력받는 함수
# number = input()    # <-- 입력 대기 후 print 실행
# print('입력받은 값: ', number)

# 숫자 3개 입력받고 합 구하기
# num1 = input()
# num2 = input()
# num3 = input()
# # str -> int
# sum = int(num1) + int(num2) + int(num3)
# print('합계 : ', sum)

# 누적값으로 바꿔보자.
# sum = 0
# num1 = input()
# sum = sum + int(num1)

# num2 = input()
# sum = sum + int(num2)

# num3 = input()
# sum = sum + int(num3)

# # 반복문으로 바꿔보자.
# # 반복횟수가 명확할 때는 for 문
# for n in range(3) :
#     pass
# i = 0
# # 위와 동일한 코드
# # 반복횟수를 모를 때는 while 문
# while i < 3 :
#     pass
#     i += 1

sum = 0
for _ in range(3) :
    num = input()
    sum = sum + int(num)
print('합계: ', sum)