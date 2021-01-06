import numpy as np
from code.waveform import Triangle, Sawtooth, SquareWave


# discrete integration where s is your signal as array and l is your first entry
def running_sum(s, l):
    y = np.zeros(len(s))
    y[0] = s[0] + l
    for n in range(1, len(s)):
        y[n] = s[n] + y[n - 1]
    return y


def normalize(y):
    return (y - y.min(axis=0)) / (y.max(axis=0) - y.min(axis=0))


def current_fourier_wf(label, i, fm, x):
    if label == 'Triangle':
        return Triangle.fourier_series(int(i), fm, x)
    elif label == 'Sawtooth':
        return Sawtooth.fourier_series(int(i), fm, x)
    elif label == 'Square Wave':
        return SquareWave.fourier_series(int(i), fm, x)


def current_trigon_wf(label, a, fm, x, c):
    if label == 'Triangle':
        return Triangle.trigonometric(a, fm, x, c)
    elif label == 'Sawtooth':
        return Sawtooth.trigonometric(a, fm, x, c)
    elif label == 'Square Wave':
        return SquareWave.trigonometric(a, fm, x, c)


def current_equation(label):
    if label == 'Triangle':
        return Triangle.equation_string()
    elif label == 'Sawtooth':
        return Sawtooth.equation_string()
    elif label == 'Square Wave':
        return SquareWave.equation_string()