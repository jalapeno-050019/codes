A = [55,11,44,33,22]

###自分で書いたコード###
# for i in range(len(A)):
#      if i < len(A) - 1:
#          for j in reversed(range(len(A))):
#              if j > 0:
#                 if A[j] < A[j - 1]:
#                     temp = A[j]
#                     A[j] = A[j - 1]
#                     A[j - 1] = temp
#                 print('i:'+ str(i), 'j:' + str(j), A)

###FE 試験B的コード　インクリメント、デクリメントは「+=」「-=」で処理###
# length = len(A) #5
# num = 0

# while num < length - 1:
#     pos = length - 1 #4

#     #右端から隣の値と比較し位置を入れ替えていく処理
#     while pos > num: #posが0になってしまうとA[pos-1]が右端の値に定義され左端と右端の比較になるため避ける
#         if A[pos] < A[pos -1]:
#             temp = A[pos]
#             A[pos] = A[pos -1]
#             A[pos -1] = temp
#         print('num:' + str(num), 'pos:' + str(pos), A)
#         #末端をひとつずつ左にずらしながら比較するためのデクリメント
#         pos -= 1
#     #左端から値を決めていく（決まったらそこはスキップする）ためのインクリメント
#     num += 1

###Chat GPTが書いたコード###
length = len(A)

#FEの疑似言語と違い左側から比較していっている
while length > 1:
    i = 0
    while i < length - 1: #マイナス1にしないとA[i]が右端、A[i-1]が左端になってしまう
        #FEの疑似言語のようtempに逃がさなくてもPythonは一気に入れ替え可能（いけてる）
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
        print('length:' + str(length),'i:'+ str(i), A)
        i += 1
    length -= 1
'''
このコードでは、まずリストの長さnを取得し、lengthが1未満になるまでwhileループを続けます。
内側のループでは、リストを前から順に比較し、隣り合う要素の値が逆になっていた場合、それらを交換します。
内側のループが終了すると、lengthを1減らして、リストの末尾に最大値が移動することを示します。
内側のループが終了すると、lengthを1減らして、リストの末尾に最大値が移動することを示します。
'''
    