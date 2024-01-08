# if(a == 10) {
#
# }

a = None

#if 조건문 :
if a is None:
    print("a is None")

# if a is None:
#     print("second a is None")
#
# elif a is not None:
#     print(" a is None")

# for (int i = 0; i < 10 ; i++)
for i in range(10):
    print(f"i:{i}")

a = [1,2,3,4,5]
arr = [1, 2,'3','4',5.5,"Hello World", True, False, None]

# append = ejgksek
arr.append(6)

a.insert(1, 1.5)
print(arr)
print("a is" + str(a))

for aa in a:
    print(aa)

a= [[1,2,3],[4,5,6]]