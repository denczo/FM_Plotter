import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider, CheckButtons
from code.tools import running_sum, normalize, current_fourier_wf, current_trigon_wf, current_equation
from code.waveform import *

rate = 44100
chunk_size = 1024
start = 0
end = chunk_size * 2
x_plot = np.arange(start, end)
x = x_plot / rate
fc = 12
fm = 240
c = 0.5
a = 0.5


def plot_modulation_wave(y, wave, title, legend=False):
    wave.clear()
    wave.set_title(title)
    wave.set_xticks([0, chunk_size])
    wave.set_yticks([0, 1])
    plot_color = '#1f77b4'
    if legend:
        plot_color = '#d62728'
        wave.annotate("F(x)", xy=(0.03, 0.94), xycoords='axes fraction',
                      fontsize=8, bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none", alpha=0.7))
    else:
        wave.annotate("f(x)", xy=(0.03, 0.94), xycoords='axes fraction',
                      fontsize=8, bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none", alpha=0.7))

    wave.plot(x_plot[:chunk_size], y[:chunk_size], plot_color)
    wave.annotate(current_equation(selection.value_selected, title), xy=(0.5, 0.03), xycoords='axes fraction',
                  fontsize=8, bbox=dict(boxstyle="round", fc=(0.9, 0.9, 0.9), ec="none", alpha=0.7), ha='center')


def plot_carrier_wave(y):
    carrier_wave.clear()
    carrier_wave.set_title('Modulated Signal')
    # carrier_wave.set_yticks([-1, 0, 1])
    carrier_wave.set_xticks([0, chunk_size, chunk_size * 2])
    carrier_wave.plot(x_plot, y)
    carrier_wave.axvline(x=chunk_size, color='black', linestyle='--', alpha=0.5, lw=1.5)


def update_wf_fourier(val):
    global fourier_series, current_f_wf
    current_f_wf = current_fourier_wf(selection.value_selected, val, fm, x)
    plot_modulation_wave(current_f_wf[:chunk_size], fourier_series, 'Fourier Series')


def update_wf(label):
    global current_f_wf, current_t_wf
    current_f_wf = current_fourier_wf(label, f_iterations.val, fm, x)
    plot_modulation_wave(current_f_wf[:chunk_size], fourier_series, 'Fourier Series')
    show_integral(None)


def show_integral(label):
    global current_t_wf
    annotation = False
    # c needs to be 0 (no shift on y axis)
    current_t_wf = current_trigon_wf(selection.value_selected, a, fm, x, 0)
    current_t_wf = normalize(running_sum(current_t_wf, 0))
    if check_integral.get_status()[0]:
        annotation = True
    else:
        current_t_wf = current_trigon_wf(selection.value_selected, a, fm, x, c)

    plot_modulation_wave(current_t_wf[:chunk_size], trigonometric, 'Trigonometric function', annotation)
    plt.draw()


current_f_wf = current_fourier_wf('Triangle', 10, fm, x)
current_t_wf = current_trigon_wf('Triangle', a, fm, x, c)

fig, axes = plt.subplots(nrows=4, ncols=4)
fig.set_size_inches(10, 7)
plt.tight_layout()

fourier_series = plt.subplot(2, 2, 1)
trigonometric = plt.subplot(2, 2, 2)
carrier_wave = plt.subplot(2, 1, 2)

wf_lables = ['Triangle', 'Sawtooth', 'Square Wave']
radio_pos = plt.axes([0.01, 0.8, 0.2, 0.2], frameon=False, aspect='equal')
selection = RadioButtons(radio_pos, wf_lables)
plt.subplots_adjust(left=0.4)

slider_pos = plt.axes([0.05, 0.6, 0.13, 0.02])
f_iterations = Slider(slider_pos, '', 0, 200, valinit=10, valstep=5)

check_pos = plt.axes([0.015, 0.65, 0.2, 0.2], frameon=False, aspect='equal')
check_integral = CheckButtons(check_pos, ['show Integral \n(trigonometric function)'])
check_integral.on_clicked(show_integral)

selection.on_clicked(update_wf)
f_iterations.on_changed(update_wf_fourier)
plot_carrier_wave(current_t_wf)

plt.show()
