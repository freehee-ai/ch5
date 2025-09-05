
# nums = [5,9,3,8,2]
# # 리스트에서 가장 큰 값 구하기 => 9
# max = 0     # 가장 큰 값을 저장할 변수
# # 과정
# # 리스트의 요소와 현재 가장 큰 값을 비교

# for i in nums :
#     if max < i :
#         max = i
# print(max)

# 합이 100 을 넘으면 반복문 중단
# sum = 0
# for i in range(1, 21) :
#     if sum > 100 :
#         break
#     sum += i
#     print(sum)


# continue 사용해서 홀수 건너뛰기
for i in range(1, 11) :
    if i % 2 == 1 :
        continue
    print(i)

# 동일함.
for i in range(1, 11) :
    if i % 2 == 0 :
        print(i)