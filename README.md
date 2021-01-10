# FM Plotter
FM Plotter is a tool which demonstrates and visualizes the basics of frequency modulation with waveforms like Sawtooth, Square Wave and Triangle.
Parameters like the amount of iterations, the frequency or the modulation index can be adjusted interactively. The result is displayed immediately.
It's easy to use and helps you to understand how frequency modulation actually works. 

<img src="http://denicz.info/wp-content/uploads/2021/01/fm_plotter1.png" width="600" />
<img src="http://denicz.info/wp-content/uploads/2021/01/fm_plotter2.png
" width="600" />

## Features
- Modulation signal (Triangle, Sawtooth, Square Wave)
    - Fourier series (with formula)
    - Trigonomic function (with formula)
- Discrete integration of the modulating signal
- Carrier signal (Sine, Triangle, Sawtooth, Square Wave)
- Adjustable parameters:
    - amount of iterations to calculate fourier series
    - frequency of modulating signal
    - frequency of carrier signal
    - modulation index

## Quickstart Guide
- simply run `/code/visuals.py`
- choose your modulation signal
- set frequency of modulating signal
- calculate Integral
- choose carrier signal
- set frequency of carrier signal
- apply modulation
- increase/decrease modulation index

## Why is the Integral needed?

A basic formula for frequency modulation is (source Wikipedia):

<img src="http://denicz.info/wp-content/uploads/2021/01/basic_formula_fm.png" width="200" />

The second part of this formula in the brackets (with the Integral) is our modulation signal. So for example if
we want to modulate a Cosine carrier signal with a Square Waveform, we first will need to calculate the Integral
of the Square Waveform. The Integral of the Square Waveform results into the Triangle waveform.
