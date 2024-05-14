# 1000
# A, B = input("")
# A = int(A)
# B = int(B)

# print(A+B)

#1001
# A,B = input("").split()
# A = int(A)
# B = int(B)

# print(A-B)

#10998
# A,B = input("").split()
# A = int(A)
# B = int(B)

# print(A*B)

#1008
# A,B = input("").split()
# A = int(A)
# B = int(B)

# print(A/B)

# 10869
# A, B = input("").split()
# A = int(A)
# B = int(B)
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

#10430
# A,B,C = input("").split()
# A = int(A)
# B = int(B)
# C = int(C)

# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)
       

#2558
# A = input("")
# B = input("")
# A = int(A)
# B = int(B)

# print(A+B)

#2588
# A = int(input(""))
# B = input("")

# print(A*int(B[-1]))
# print(A*int(B[-2]))
# print(A*int(B[-3]))
# print(A*int(B))

#3046
# R1,S = input("").split()
# R1 = int(R1)
# S = int(S)

# print(S * 2 - R1)

#2163
# N,M = input("").split()
# print(int(N)*int(M) - 1)

#10699
# import time
# print(time.strftime("%Y-%m-%d"))

#7287
# print("32")
# print("mekazon")

#2525
# A, B = map(int, input().split())
# C = int(input())

# A += C // 60
# B += C % 60

# if B >= 60:
#     A += 1
#     B -= 60
# if A >= 24:
#     A -= 24

# print(A, B)

#2530
# H, M, S = map(int, input().split())
# C = int(input())

# S += C

# while S >= 60:
#     M += 1
#     S -= 60
#     if M >= 60:
#         H += 1
#         M -= 60
#     if H >= 24:
#         H -= 24

# print(H, M, S)

#2914
# A, I = map(int, input().split())

# print(A*(I-1)+1)

#5355
# A = int(input())
# for i in range(A):
#     j = list(map(str, input().split()))
#     result = 0
#     for x in range(len(j)):
#         if x == 0:
#             result += float(j[x])
#         else:
#             if j[x] == '#':
#                 result -= 7
#             elif j[x] == '%':
#                 result += 5
#             elif j[x] == '@':
#                 result *= 3
#     print(f'{result:.2f}')
    

#2675
