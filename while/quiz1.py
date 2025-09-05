
i = 0
while i < 3 :
    print('하이')
    i += 1


i = 0
while i < 5 :
    print(i)
    i += 1

i = 1
while i < 6 :
    print(i)
    i += 1

i = 11
while i < 21 :
    print(i)
    i += 1

i = 0
lis = ['a','b','c','d','e']
while i < 5 :
    print(lis[i])
    i += 1

i = 0
nums = [10,20,30]
while i < 3 :
    print(nums[i])
    i += 1

# 조건 : 합이 100을 넘으면 while문 중단
i = 1
sum = 0
while i <= 20 :
    sum += i
    if sum > 100 :
        print('마지막 sum :', sum)
        print('마지막 i : ', i)
        break
    i += 1
print(sum)

# 짝수만 출력
# continue  를 만나면
# 더이상 아래 코드를 실행하지 않고
# 다시 반복문으로 돌아간다
i = 1
while i < 11 :
    if i % 2 == 1 :
        i += 1
        continue
    print(i)
    i += 1
