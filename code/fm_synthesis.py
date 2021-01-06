import numpy as np
import matplotlib.pylab as plt
from scipy import signal, integrate

chunk_size = 1024
rate = 44100
start = 0
end = start + chunk_size
x = np.arange(start, end) / rate
x1 = np.arange(start, end) / rate
start = end
end = start + chunk_size
x2 = np.arange(start, end) / rate
start = end
end = start + chunk_size
x3 = np.arange(start, end) / rate
print(start, end)
max = 0
min = 0
x = np.linspace(0, 1, 5000)
# x2 = np.linspace(1, 2, 5000)
# x3 = np.linspace(2, 3, 5000)
# x_sum = np.linspace(0,3, 100000)

# fm = 7.381012301
fm = 410
amount = int(rate / chunk_size) / fm
x_test = np.arange(0, amount * chunk_size) / rate
fdelta = 100
# modulation index


fm = 4
beta = fdelta / fm
fc = 10
amp = 1
setup = 2 * np.pi * fm * x

square_scipy = signal.square(setup)
saw_scipy = signal.sawtooth(setup, 1)
tri_scipy = signal.sawtooth(setup, 0.5)

triangle_fm = 2 * amp / np.pi * np.arcsin(np.sin(setup))
square_fm = amp * np.sign(np.sin(setup))
saw_fm = -2 * amp / np.pi * np.arctan(1 / np.tan(setup))

lfo = integrate.cumtrapz(square_scipy, initial=0) * beta

triangle_fc = 2 / np.pi * np.arcsin(np.sin(2 * np.pi * fc * x + lfo))
saw_fc = -2 * amp / np.pi * np.arctan(1 / np.tan(setup + lfo))
square_fc = amp * np.sign(np.sin(setup + lfo))
sin_fc = amp * np.sin(setup + 0.5 * lfo)

# plt.plot(x, lfo1)
# plt.plot(x, saw_scipy)
plt.plot(x, saw_scipy)
plt.plot(x, saw_fm)
# plt.plot(x, sin_fc)
# plt.plot(x, triangle_fm)
# plt.plot(x, saw_fm)
# plt.plot(x, square_fm)

# lfo2 = integrate.cumtrapz(square2, dx=0.0002, initial=0)*beta
# lfo3 = integrate.cumtrapz(square3, dx=0.0002, initial=0)*beta
# print(t1)
# #
# def create_sawtooth(a, x, fc):
#     result = 0
#     for n in range(1, a):
#         # result += (np.sin(2*np.pi*fc*n*x+10*(np.sin(2*np.pi*2*x)))/n)
#         result += (np.sin(2 * np.pi * fc * n * x) / n)
#     return 0.5 + (1 / np.pi) * result
#
#
# def create_fw_rectified(a, x, fc):
#     result = 0
#     for n in range(1, a):
#         result += (np.cos(2 * np.pi * fc * n * x) / (4 * n**2 - 1))
#     return 2/np.pi - 4/np.pi * result
#
#
# def create_triangle(a, x, fc):
#     result = 0
#     for n in range(1, a):
#         result += (np.cos(2 * np.pi * fc * (2*n - 1) * x) / (2 * n - 1) ** 2)
#     return 0.5 - 4 / np.pi ** 2 * result
#
#
# def create_square(a, x, fc):
#     result = 0
#     for n in range(1, a):
#         result += (np.sin(2 * np.pi * fc * (2*n - 1) * x) / (2 * n - 1))
#     return 0.5 + 2 / np.pi * result
#
#
# #
# #saw = create_sawtooth(3000, x1, fm)
# #fwr = create_fw_rectified(200, x1, fm)
# #tri = create_triangle(10, x1, fm)
# #square = create_square(5000, x1, fm)
#
#

#
#
# def sawtooth_simple(freq, rate, chunk_size):
#     # 0.5 to round to next bigger number
#     period = int(rate / freq + 0.5)
#     # amount of samples to get a complete set of periods
#     samples = int(chunk_size / period + 1) * period
#     result = np.zeros(samples)
#     for i in range(samples):
#         # calc ramp and amplitude between 0 and 1
#         result[i] = i % period / period
#     return result
#
#
# def triangle_simple(freq, rate, chunk_size):
#     # 0.5 to round to next bigger number
#     period = int(rate / freq + 0.5)
#     # amount of samples to get a complete set of periods
#     samples = int(chunk_size / period + 1) * period
#     result = np.zeros(samples)
#     for i in range(samples):
#         # amplitude between 0 and 1
#         result[i] = i % period / period
#     return result
#
#
# y = sawtooth_simple(120, 44100, 1024)
# y = abs(y)

# y = test(200, 44100, x1)
# plt.plot(t1, saw)
# plt.plot(x1, y[:1024])
# plt.plot(t1, tri)
# plt.plot(t1, square)
# y = np.sin(2*np.pi*fc*x1+80*lfo1)
# y = 0.5*create_sawtooth(100, x1, 10)
# y = np.sin(2*np.pi*fc*x1 + 10 * triangle)
# plt.plot(x1, y)
# plt.plot(x, y, label="Sine waveform with frequency modulation")
# plt.plot(x, 20*lfo, label="LFO at 4 hz")
# plt.legend(loc="upper left")
# plt.ylim(-1.5, 2.0)
# #plt.axis('off')
# plt.plot(x1, square1)
# y_test = running_sum(y_test, 0)
# y_min = y_test.min(axis=0)
# y_max = y_test.max(axis=0)
#
#
# y1 = running_sum(y1, 0)
# y2 = running_sum(y2, y1[-1])
# y3 = running_sum(y3, y2[-1])
#
# y1 = (y1 - y_min) / (y_max - y_min)
# y2 = (y2 - y_min) / (y_max - y_min)
# y3 = (y3 - y_min) / (y_max - y_min)
#


# print(y_min, y_max)
# plt.plot(t1, y_test)
# integral_sum = running_sum(square_sum, 0)
# max_val = max(integral)
# min_val = min(integral)
# y = integrate - min_val / max_val - min_val
# y1 = (integral1 - integral1.min(axis=0)) / (integral1.max(axis=0) - integral1.min(axis=0))
# y2 = (integral2 - integral2.min(axis=0)) / (integral2.max(axis=0) - integral2.min(axis=0))
# y3 = (integral3 - integral3.min(axis=0)) / (integral3.max(axis=0) - integral3.min(axis=0))
# y_sum = integral_sum / integral_sum.max(axis=0)

# plt.plot(x_sum, y_sum)

# chunks = []
# chunks = np.append(chunks, y1)
# chunks = np.append(chunks, y2)
# chunks = np.append(chunks, y3)

# print('ended')
# wavfile.write('recorded_test.wav', 44100, chunks)

# plt.plot(t1, saw)
#
# plt.plot(t1, y1)
# plt.plot(t2, y2)
# plt.plot(t3, y3)
# plt.plot(x1, lfo1)
# plt.plot(x1, square1)
#
# plt.plot(x2, sine2)
# plt.plot(x2, lfo2)
# plt.plot(x2, square2)
#
# plt.plot(x3, sine3)
# plt.plot(x3, lfo3)
# plt.plot(x3, square3)

# plt.plot(x1,y)

plt.show()
