
mixed = [1,"apple",3.14,True]
for m in mixed :
    print(m)

print("\n")

fruits = ['apple','banana', 'cherry']
for f in fruits :
    print(f)

print("\n")

students = {'이름':'둘리','나이':20,'주소':'인천'}
# for s in students.keys() : --> 첫번째 방법
#     print(s)
for key in students :       # --> 두번째 방법
     print(key)

print("\n")

coffee_menu = {'아메리카노': '2500원', '라떼': '3000원', '케이크': '4500원'}
for c in coffee_menu.values() :
    print(c)
