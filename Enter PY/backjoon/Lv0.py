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
A, B = input("").split()
C = int(input(""))
A = int(A)
B = int(B)

CHour = int(C // 60)
CTime = int(C % 60)
if B + CTime > 60:
    CHour += 1
    B -= 60

print(A+CHour, B+CTime, sep=" ")
