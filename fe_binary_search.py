A = [11,22,33,44,55,66,77]

x = 22

length = len(A) #7

pos = -1
left = 0
right = length - 1 #lengthは7なのでマイナス1にしておかないとリスト右端A[6]が取得できない

while pos == -1 and left <= right: #リストの二分割を繰り返すと最後がleft == rightになる。逆転してleft > rightはあり得ない
    mid = (left + right) // 2
    
    if A[mid] == x:
        pos = mid
    elif A[mid] > x:
        right = mid - 1 #midから右を削除してrightをmidの左のインデックスに定義
    elif A[mid] < x:
        left = mid + 1 #midから左を削除してleftをmidの右のイデックスに定義

print(pos)

