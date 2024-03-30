# plt.rc('font', family='Malgun Gothic')

# import numpy as np
# import matplotlib.pyplot as plt

# def Vn(n, A, tau, T0):
#     """
#     Vn을 계산합니다.
    
#     Parameters:
#         n (int): 주파수 인덱스
#         A (float): 직류성분
#         tau (float): 주기성분
#         T0 (float): 주기
        
#     Returns:
#         float: Vn
#     """
#     return (A * tau / T0) * np.sinc(n * np.pi * tau / T0)

# def An(n):
#     """
#     An을 계산합니다. (주어진 조건에 따라 0입니다.)
    
#     Parameters:
#         n (int): 주파수 인덱스
        
#     Returns:
#         float: An
#     """
#     return 0

# def Bn(n, A, tau, T0):
#     """
#     Bn을 계산합니다.
    
#     Parameters:
#         n (int): 주파수 인덱스
#         A (float): 직류성분
#         tau (float): 주기성분
#         T0 (float): 주기
        
#     Returns:
#         float: Bn
#     """
#     return (2 * A * tau / T0) * np.sinc(n * np.pi * tau / T0)

# plt.rc('font', family='Malgun Gothic')
# # 파라미터 설정
# A = 1  # 직류성분
# tau = 0.5  # 주기성분
# T0 = 1  # 주기

# # 주파수 범위 설정
# n_values = np.arange(-10, 11)  # -10부터 10까지의 주파수 인덱스

# # 각 주파수 구성 요소 계산
# Vn_values = [Vn(n, A, tau, T0) for n in n_values]
# An_values = [An(n) for n in n_values]
# Bn_values = [Bn(n, A, tau, T0) for n in n_values]

# # 그래프로 표시
# plt.figure(figsize=(10, 6))

# # 주파수 구성 요소를 선으로 연결하여 그래프로 그립니다.
# plt.plot(n_values, Vn_values, marker='o', label='$V_n$', linestyle='-')
# plt.plot(n_values, An_values, marker='o', label='$A_n$', linestyle='-')
# plt.plot(n_values, Bn_values, marker='o', label='$B_n$', linestyle='-')

# plt.xlabel('주파수 인덱스 $n$')
# plt.ylabel('주파수 구성 요소 값')
# plt.title('주파수 구성 요소')
# plt.legend()
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

def An(n, A):
    """
    홀수 주파수 인덱스에 대한 An을 계산합니다.
    
    Parameters:
        n (int): 주파수 인덱스
        A (float): 직류성분
        
    Returns:
        float: 홀수 주파수 인덱스에 대한 An
    """
    return (2 * A / (n * np.pi)) * (1 - np.cos(n * np.pi))

def Bn(n):
    """
    Bn을 계산합니다. (주어진 조건에 따라 0입니다.)
    
    Parameters:
        n (int): 주파수 인덱스
        
    Returns:
        float: Bn
    """
    return 0

def Vn(n, A):
    """
    홀수 주파수 인덱스에 대한 Vn을 계산합니다.
    
    Parameters:
        n (int): 주파수 인덱스
        A (float): 직류성분
        
    Returns:
        complex: 홀수 주파수 인덱스에 대한 Vn
    """
    return (A / (n * np.pi * 1j)) * (1 - np.cos(n * np.pi))

# 파라미터 설정
A = 1  # 직류성분

# 주파수 범위 설정
n_values = np.arange(-10, 11)  # -10부터 10까지의 주파수 인덱스

# 각 주파수 구성 요소 계산
An_odd_values = [An(n, A) for n in n_values if n % 2 != 0]
An_even_values = [An(n, A) for n in n_values if n % 2 == 0]
Bn_values = [Bn(n) for n in n_values if n % 2 != 0]  # 홀수에 대해서만 계산

# 그래프로 표시
plt.figure(figsize=(10, 6))

# 홀수 주파수 구성 요소를 선으로 연결하여 그래프로 그립니다.
plt.plot(n_values[n_values % 2 != 0], An_odd_values, marker='o', label='$A_n$ (홀수)', linestyle='-', color='blue')

# 짝수 주파수 구성 요소를 선으로 연결하여 그래프로 그립니다.
plt.plot(n_values[n_values % 2 == 0], An_even_values, marker='o', label='$A_n$ (짝수)', linestyle='-', color='green')

plt.xlabel('주파수 인덱스 $n$')
plt.ylabel('주파수 구성 요소 값')
plt.title('주파수 구성 요소')
plt.legend()
plt.grid(True)
plt.show()