# # 1부터 10까지 출력하기

# i = 1
# while i < 11 :
#     if i%2 == 1 :
#         i += 1
#         continue
#     print(i)
#     i += 1

# ################################

# lis = [100,77,-5,10]

# i = 0
# while i < 4 :
#     if lis[i] < 0 :
#         i += 1
#         continue
#     print(lis[i])
#     i += 1


##############################

# lis = [100,77,-5,10]

# i = 0
# while i < 4 :
#     if lis[i] == 77 :
#         break
#     print(lis[i])
#     i += 1



#####

# str = "hello"
# i = 0
# while i < 5 :
#     print(str[i])
#     i += 1

# print("------------------")

# num = [1,2,3,4,5,6,7]
# i = 0
# while i < 7 :
#     print(num[i])
#     i += 1

# print("-------------------")

# num1 = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i < 10 :
#     if num1[i] % 2 == 0 :
#         i += 1
#         continue
#     print(num1[i])
#     i += 1


# print("1--------------------")

# i = 11
# while i < 21 :
#     print(i)
#     i += 1

# print("2--------------------")

# lis = [1,2,3,4,5]
# i = 0
# sum = 0
# while i < 5 :
#     sum += lis[i]
#     i += 1
# print(sum)

# print("3--------------------")

# nums = [10,20,30]
# i = 0
# while i < 3 :
#     print(nums[i])
#     i += 1

# i = 1
# while i < 10 :
#     if i % 3 == 0 :
#         break 
#     print(i)
#     i += 1


# lis = ['aa', 'bbb', 'ccccc', 'dd']
# i = 0
# while i < 4 :
#     if len(lis[i]) > 4 :
#         break
#     print(lis[i])
#     i += 1


# i = 1
# while i < 11 :
#     if i % 2 == 0 :
#         i += 1
#         continue
#     print(i)
#     i += 1

lis = [10,'a',True,20,'b']
i = 0
while i < 5 :
    if type(lis[i]) == int :
        i += 1
        continue
    print(lis[i])
    i += 1


