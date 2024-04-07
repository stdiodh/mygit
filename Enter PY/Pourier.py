# import numpy as np
# import matplotlib.pyplot as plt

# def Vn(n, A, tau, T0):
#     return (A * tau / T0) * np.sinc(n * np.pi * tau / T0)
# def An(n):
#     return 0
# def Bn(n, A, tau, T0):
#     return (2 * A * tau / T0) * np.sinc(n * np.pi * tau / T0)
# def A0(A, tau, T0):
#     return A * tau / T0

# plt.rc('font', family='Malgun Gothic')

# A = 1
# tau = 0.5
# T0 = 1

# n_values = np.arange(-10, 11)

# Vn_values = [Vn(n, A, tau, T0) for n in n_values]
# An_values = [An(n) for n in n_values]
# Bn_values = [Bn(n, A, tau, T0) for n in n_values]
# A0_values = [A0(A, tau, T0) for n in n_values]

# plt.figure(figsize=(10, 6))

# plt.plot(n_values, Vn_values, label='$V_n$', linestyle='-', color='blue')
# plt.plot(n_values, An_values, label='$A_n$', linestyle='-', color='green')
# plt.plot(n_values, Bn_values, label='$B_n$', linestyle='-', color='red')
# plt.plot(n_values, A0_values, label='$A_0$', linestyle='-', color='orange')

# plt.xlabel('주파수 인덱스 $n$')
# plt.ylabel('주파수 구성 요소 값')
# plt.title('주기 구형파 신호의 주파수 스펙트럼')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# plt.rc('font', family='Malgun Gothic')

# def A0(n, A):
#     return 0

# def An(n, A):
#     return (2 * A / (n * np.pi)) * (1 - np.cos(n * np.pi))

# def Bn(n):
#     return 0

# def Vn(n, A):
#     return (A / (n * np.pi * 1j)) * (1 - np.cos(n * np.pi))

# A = 1

# n_values = np.arange(-10, 11) 

# An_odd_values = [An(n, A) for n in n_values if n % 2 != 0]
# An_even_values = [An(n, A) for n in n_values if n % 2 == 0]
# Vn_values = [Vn(n, A) for n in n_values if n % 2 != 0]

# plt.figure(figsize=(10, 6))

# plt.plot(n_values[n_values % 2 != 0], An_odd_values, marker='o', label='$A_n$ (홀수)', linestyle='-', color='blue')
# plt.plot(n_values[n_values % 2 == 0], An_even_values, marker='o', label='$A_n$ (짝수)', linestyle='-', color='green')
# plt.plot(n_values[n_values % 2 != 0], Vn_values, marker='o', label='$V_n$', linestyle='-', color='orange')

# plt.xlabel('주파수 인덱스 $n$')
# plt.ylabel('주파수 구성 요소 값')
# plt.title('주기 구형파 함수 분석')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# def Vn(n, A, tau, T0):
#     return (A * tau / T0) * np.sinc(n * np.pi * tau / T0)
# def An(n):
#     return 0
# def Bn(n, A, tau, T0):
#     return (2 * A * tau / T0) * np.sinc(n * np.pi * tau / T0)
# def A0(A, tau, T0):
#     return A * tau / T0

# plt.rc('font', family='Malgun Gothic')

# A = 1
# tau = 0.5
# T0 = 1
# n_values = np.arange(-10, 11)

# t = np.linspace(-3 * T0, 3 * T0, 1000)

# x_pulse = np.zeros_like(t, dtype=complex)

# for n in n_values:
#     if n != 0:
#         x_pulse += Bn(n, A, tau, T0) * np.exp(1j * 2 * np.pi * n / T0 * t)

# x_pulse += A0(A, tau, T0)

# plt.figure(figsize=(10, 6))
# plt.plot(t, x_pulse.real, color='blue')
# plt.xlabel('시간')
# plt.ylabel('주기')
# plt.title('주기 펄스 구형파 신호 분석')
# plt.grid(True)
# plt.ylim(-2, 2)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

def A0(n, A):
    return 0

def An(n, A):
    return (2 * A / (n * np.pi)) * (1 - np.cos(n * np.pi))

def Bn(n):
    return 0

def Vn(n, A):
    return (A / (n * np.pi * 1j)) * (1 - np.cos(n * np.pi))

A = 1
n_values = np.arange(-10, 11)

t = np.linspace(-5, 5, 1000)

x_pulse = np.zeros_like(t, dtype=complex)

for n in n_values[n_values % 2 == 0]:
    if n != 0:
        x_pulse += An(n, A) * np.exp(1j * 2 * np.pi * n * t * 0.5)

for n in n_values[n_values % 2 != 0]:
    x_pulse += Vn(n, A) * np.exp(1j * 2 * np.pi * n * t * 0.5)

plt.figure(figsize=(10, 6))
plt.plot(t, x_pulse.real, color='blue')
plt.xlabel('시간')
plt.ylabel('주기')
plt.title('주기 펄스 구형파 함수 분석')
plt.grid(True)
plt.show()