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

# plt.rc('font', family='AppleGothic')

# A = 4
# tau = 0.5
# T0 = 1
# n_values = np.arange(-10, 11)

# t = np.linspace(-1.5 * T0, 1.5 * T0, 1000)

# x_pulse = np.zeros_like(t, dtype=complex)

# for n in n_values:
#     if n != 0:
#         x_pulse += Bn(n, A, tau, T0) * np.exp(1j * 2 * np.pi * n / T0 * (t + T0/2))

# x_pulse += A0(A, tau, T0)

# plt.figure(figsize=(10, 6))
# plt.plot(t, x_pulse.real, color='blue')
# plt.xlabel('시간 t')
# plt.ylabel('주기 v(t)')
# plt.title('주기 펄스 구형파 신호 분석')
# plt.grid(True)
# plt.ylim(-5, 5)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')

def A0(n, A):
    return 0

def An(n, A):
    return (2 * A / (n * np.pi)) * (1 - np.cos(n * np.pi))

def Bn(n):
    return 0

def Vn(n, A):
    return (A / (n * np.pi * 1j)) * (1 - np.cos(n * np.pi))

A = 4
n_values = np.arange(-10, 11)

t = np.linspace(-3, 3, 1000)

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
