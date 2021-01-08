import numpy as np
# for mathematical symbols
# https://matplotlib.org/3.1.1/tutorials/text/mathtext.html

class Sawtooth:

    # a = amplitude, f = frequency, x = samples, c = constant
    @staticmethod
    def trigonometric(a, f, x, c=0, m=0):
        return -2 * a / np.pi * np.arctan(1 / np.tan(2 * np.pi * f/2 * x + m)) + c

    # a = amplitude, f = frequency, x = samples
    @staticmethod
    def fourier_series(a, f, x):
        result = 0
        for n in range(1, a):
            result += (np.sin(2 * np.pi * f * n * x) / n)
        return 0.5 + (1 / np.pi) * result

    @staticmethod
    def equation_fourier():
        #return "0.5a + 1/\u03C0  \u03A3 sin(2\u03C0 f n x)/n"
        return r'$\dfrac{1}{2}a + \dfrac{1}{\pi} \sum_{n=0}^i \dfrac{\sin(2\pi\/f\/n\/x)}{n}$'

    @staticmethod
    def equation_trigon():
        #return "-2a/\u03C0 arctan(1/tan(2\u03C0 f/2 x)) + 0.5)"
        return r'$\dfrac{-2a}{\pi} + \dfrac{1}{\pi} \arctan(\dfrac{1}{\tan(2\pi \dfrac{f}{2} x)}) + C $'

class SquareWave:

    # a = amplitude, f = frequency, x = samples, c = constant
    @staticmethod
    def trigonometric(a, f, x, c=0, m=0):
        return a * np.sign(np.sin(2*np.pi * f * x + m) + c)

    # a = amplitude, f = frequency, x = samples
    @staticmethod
    def fourier_series(a, f, x):
        result = 0
        for n in range(1, a):
            result += (np.sin(2 * np.pi * f * (2*n - 1) * x) / (2 * n - 1))
        return 0.5 + 2 / np.pi * result

    @staticmethod
    def equation_fourier():
        #return "0.5a + 2/\u03C0  \u03A3 sin(2\u03C0 f (2n-1) x)/(2n-1)"
        return r'$\dfrac{1}{2}a + \dfrac{2}{\pi} \sum_{n=0}^i \dfrac{\sin(\dfrac{2}{\pi}\/f\/(2n - 1)\/x)}{2n - 1}$'


    @staticmethod
    def equation_trigon():
        #return "a\u03C0 sign(sin(2\u03C0 f x) + 0.5)"
        return r'$a\/\/ \mathrm{\mathsf{sign}}(\sin(2\pi\/f\/x) + C)$'


class Triangle:

    # a = amplitude, f = frequency, x = samples, c = constant
    @staticmethod
    def trigonometric(a, f, x, c, m):
        return 2 * a / np.pi * np.arcsin(np.sin(2 * np.pi * f * x - np.pi/2 + m)) + c

    # a = amplitude, f = frequency, x = samples
    @staticmethod
    def fourier_series(a, f, x):
        result = 0
        for n in range(1, a):
            result += (np.cos(2 * np.pi * f * (2*n - 1) * x) / (2 * n - 1) ** 2)
        return 0.5 - 4 / np.pi ** 2 * result

    @staticmethod
    def equation_fourier():
        #return "0.5a - 4/\u03C0\u00B2  \u03A3 cos(2\u03C0 f (2n - 1) x)/(2n - 1)\u00B2"
        return r'$\dfrac{1}{2}a - \dfrac{4}{\pi^{2}} \sum_{n=0}^i \dfrac{\cos(2\pi\/f\/(2n - 1)\/x)}{(2n - 1)^{2}}$'

    @staticmethod
    def equation_trigon():
        #return "2a/\u03C0 arcsin(sin(2\u03C0 f x - \u03C0/2)) + 0.5"
        return r'$\dfrac{2a}{\pi}\/\arcsin(\sin(2\pi\/f\/x - \dfrac{\pi}{2})) + C $'
