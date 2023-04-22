A = [34,78,56,90,12]

length = len(A)

ans = A[0]
i = 1

while i < length:
    if A[i] > ans:
        ans = A[i]
    i += 1
print(ans)

# for i in range(length):
#     if A[i] > ans:
#         ans = A[i]
# print(ans)