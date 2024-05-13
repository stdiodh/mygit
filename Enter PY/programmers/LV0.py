# def solution(numbers):
#     numbers.sort()
#     return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])


# def solution(my_string, num1, num2):
#     my_string = list(my_string)
#     my_string[num1],my_string[num2] = my_string[num2],my_string[num1]
#     return "".join(my_string)

# print(solution("hello", 1, 2))

# def solution(num, n):
#     answer = 0
#     if num%n == 0:
#         answer = 1
#     else:
#         answer = 0
#     return answer

# def solution(myString):
#     return myString.lower()

# print(solution("aBcDe"))

# def solution(number, n, m):
#     answer = 0
#     if number % n == 0:
#         if number % m == 0:
#             answer = 1
#     return answer

# print(solution(60, 2, 3))

# def solution(myString):
#     return myString.split()

# print(solution('i love you'))

# def solution(num_list:list, n):
#     answer = 0
#     if n in num_list:
#         answer = 1
#     return answer

# print(solution([1,2,3], 3))

# def solution(a, b, flag:int):
#     answer = 0
#     if flag == 1:
#         answer = a+b
#     elif flag == 0:
#         answer = a-b
#     return answer

# print(solution(-4, 7, True))

# def solution(a, b):
#     sum1 = str(a)+str(b)
#     sum2 = str(a)+str(b)
#     answer = 0
#     if sum1 > sum2:
#         answer = sum1
#     else:
#         answer = sum2
#     return answer


# def solution(str_list, ex):
#     answer = ''
#     for x in range(0, len(str_list)):
#         if ex not in str_list[x]:
#             answer += str_list[x]
#     return answer

# print(solution(["abc", "def", "ghi"], "ef"))

# import math

# def solution(flo):
#     return math.floor(flo)

# print(solution(1.42))

# def solution(my_string, n):
#     return my_string[0:n]

# print(solution("ProgrammerS123", 11))

# def solution(arr1, arr2):
#     x, y = len(arr1), len(arr2)
#     if x != y:
#         return 1 if x > y else -1
#     elif x == y:
#         sum_x, sum_y = sum(arr1), sum(arr2)
#         if sum_x > sum_y:
#             return 1 
#         elif sum_x < sum_y: 
#             return -1 
#         else:
#             return 0

# print(solution([49, 13], [70, 11, 2]))

# str1, str2 = input().strip().split(' ')
# totalStr = str1+str2

# print(totalStr.replace(" ", ""))

# def solution(num_list, n):
#     return num_list[::n]

# def solution(n):
#     answer = 0
#     if n % 2 == 0:
#         for x in range(0, n+1, 2):
#             answer+=x**2
#     else:
#         for x in range(1, n+1, 2):
#             answer+=x
#     return answer

# print(solution(7))

# n = int(input())

# print(f"{n} is odd" if n % 2 else f"{n} is even")

# def solution(num_list):
#     odd_list = []
#     even_list = []
#     for x in num_list:
#         if x % 2 == 0:
#             even_list.append(x)
#         else:
#             odd_list.append(x)
#     str_list1 =  "".join(map(str, odd_list))
#     str_list2 =  "".join(map(str, even_list))
    
#     total = int(str_list1)+ int(str_list2)
#     return total

# print(solution([3, 4, 5, 2, 1]))


# def solution(my_string, target):
#     answer = 0
#     if target in my_string:
#         answer = 1
#     return answer

# def solution(num_list, n):
#     result_list = []
#     for x in range(n):
#         result_list.append(num_list[x])
#     return result_list

# def solution(my_string, index_list):
#     answer = ''
#     for x in index_list:
#         answer += my_string[x]
#     return answer

# print(solution("cvsgiorszzzmrpaqpe" ,[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))

# def solution(n, control):
#     list_cont = list(control)
#     for x in list_cont:
#         if x == 'w':
#             n += 1
#         elif x == 's':
#             n -= 1
#         elif x == 'd':
#             n += 10
#         elif x == 'a':
#             n -= 10
#     return n

# print(solution(0, "wsdawsdassw"))

# def solution(arr):
#     conArr = []
#     for x in arr:
#         if x < 50:
#             if x % 2 == 1:
#                 conArr.append(x * 2)
#         if 50 <= x:
#             if x % 2 == 0:
#                 conArr.append(x / 2)
#         else:
#             conArr.append(x)
#     return conArr

# print(solution([1, 2, 3, 100, 99, 98]))

# def solution(a, b):
#     re1 = str(a)+str(b)
#     re2 = 2 * a * b
#     answer = 0
#     if int(re1) > re2:
#         answer = re1
#     elif re2 > int(re1):
#         answer = re2
#     else:
#         answer = int(re1)
#     return answer

# def solution(a, b):
#     return max(int(str(a) + str(b)), 2 * a * b)

# print(solution(91, 2))

# def solution(num_list):
#     re1=sum(num_list) ** 2
#     re2=1
#     for x in num_list:
#         re2 *= x
#     print(re1, re2)
#     return 1 if re1 > re2 else 0

# print(solution([5, 7, 8, 3]))

# def solution(num_list):
#     return type(num_list)

# print(solution([3, 4, 5, 2, 1]))

# def solution(n):
#     answer = []
#     for x in range(1, n+1):
#         if n % x == 0:
#             answer.append(x)
#     return answer

# print(solution(24))

# def solution(num, k):
#     a = str(num).find(str(k))
#     return (a if a == -1 else a+1)

# print(solution(29183, 1))

# def solution(order):
#     answer = 0
#     order = list(str(order))
#     for i in order:
#         if i in "369":
#             answer += 1
#     return answer

# print(solution(29423))

# def solution(rny_string):
#     return rny_string.replace('m', 'rn')

# print(solution('masterpiece'))

# def solution(num_list):
#     answer = 0
#     for x in range(len(num_list)):
#         if num_list[x] < 0:
#             return x
#         else:
#             answer = -1
#     return answer

# print(solution([13, 22, 53, 24, 15, 6]))


# def solution(arr, k):
#     answer = []
#     for x in range(len(arr)):
#         if k % 2 == 0:
#             answer.append(arr[x] + k)
#         else:
#             answer.append(arr[x] * k)
#     return answer

# print(solution([1, 2, 3, 100, 99, 98], 3))

# def solution(start, end_num):
#     answer = []
#     for x in range(start, end_num-1, -1):
#         print(x)
#         answer.append(x)
#     return answer

# print(solution(10,3))

# def solution(num_list):
#     add = 0
#     mul = 1
#     answer = 0
#     if len(num_list) >= 11:
#         for x in range(len(num_list)):
#             add += num_list[x]
#             answer = add
#     elif 10 >= len(num_list):
#         for x in range(len(num_list)):
#             mul *= num_list[x]
#             answer = mul
#     return answer

# print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))


# def solution(n):
#     answer = 0
#     for i in range(n+1):
#         c = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 c += 1
#         if c >= 3:
#             answer += 1
        
#     return answer
