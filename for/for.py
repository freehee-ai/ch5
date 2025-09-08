scores = {'철수': 80, '영희': 95, '민수':70, '지연': 100}
sum = 0
cnt = len(scores)

for a in scores.values() :
    sum += a
print(sum/cnt)

cnt = 0
for a in scores.values() :
    if a >= 90 :
        cnt += 1
print(cnt)

print('\n')

# nums = [1,2,3,4]
# new_nums = []
# for n in nums :
#     new_nums.append(n * 3)
#     print(new_nums)

# # 리스트 컴프리헨션
# new_nums = [ n * 3 for n in nums ]

nums = [1,2,3,4,5,6,7,8,9,10]
new_nums = []
new_nums = [n for n in nums if n % 2 == 0]
print(new_nums)

print('\n')

strings = ['a','bb','ccc','dddd','e']
new_str = []
new_str = [s.upper() for s in strings if len(s) > 2]
print(new_str)