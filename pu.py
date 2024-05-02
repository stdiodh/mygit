import numpy as np
import matplotlib.pyplot as plt

def square_pulse(t, A, T0, tau):
    result = 0.0
    for n in range(1, 11): # 임의의 횟수
        result += Bn[n-1] * np.cos(2 * np.pi * n * t / T0)
    return result

# 파라미터 설정
A = 4.0  # 진폭
T0 = 2.0 # 주기
tau = T0 / 10 # 펄스 너비

# 주파수 배열 생성
n_values = np.arange(1, 11) # 임의의 횟수

# Bn 계산
Bn_values = np.array([2 * A * tau / T0 * np.sinc(n * tau / T0) for n in n_values])

# 시간 배열 생성
t = np.linspace(0, 5 * T0, 1000) # 0에서 5T0 사이를 1000등분

# 사각 펄스 구형파의 시간 영역에서의 표현 생성
v_t = square_pulse(t, A, T0, tau)

# 그래프 그리기
plt.plot(t, v_t * A, label='Square Pulse Waveform')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Square Pulse Waveform')
plt.legend()
plt.grid(True)
plt.show()
