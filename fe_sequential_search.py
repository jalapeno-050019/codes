A = [55,11,77,33,66,44,22]

x = 44

length = len(A)

pos = -1
i = 0

#疑似言語の線形探索は探索条件を設定しているのでこの形
while i < length and pos == -1:
    if A[i] == x:
        pos = i
        print(pos)
    i += 1

# for i in range(length):
#     if A[i] == x:
#         print(i)
    