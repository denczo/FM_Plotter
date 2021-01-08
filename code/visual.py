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
fc = 500
fm = 100
c = 0.5
a = 0.5
fdelta = 100
# modulation index
beta = 0.1
#beta = fdelta / fm


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
    wave.minorticks_on()
    wave.grid(b=True, which='minor')
    wave.plot(x_plot[:chunk_size], y[:chunk_size], plot_color)
    wave.annotate(current_equation(wf_modulation.value_selected, title), xy=(0.5, 0.1), xycoords='axes fraction',
                  fontsize=9, bbox=dict(boxstyle="round", fc='white', ec="none", alpha=0.7), ha='center')


def plot_carrier_wave(y):
    carrier_wave.clear()
    carrier_wave.set_title('Carrier Signal')
    # carrier_wave.set_yticks([-1, 0, 1])
    carrier_wave.set_xticks([0, chunk_size, chunk_size * 2])
    carrier_wave.minorticks_on()
    carrier_wave.grid(b=True, which='minor')
    carrier_wave.plot(x_plot, y)
    carrier_wave.axvline(x=chunk_size, color='black', linestyle='--', alpha=0.5, lw=1.5)


def update_wf_fourier(val):
    global fourier_series, current_f_wf, fm
    fm = slider_freq_mod.val
    current_f_wf = current_fourier_wf(wf_modulation.value_selected, val, fm, x)
    plot_modulation_wave(current_f_wf[:chunk_size], fourier_series, 'Fourier Series')


def update_wf(label):
    global current_f_wf, current_t_wf
    update_wf_fourier(slider_iterations.val)
    apply_modulation(None)
    show_integral(None)


def update_wf_carrier(label, m=0):
    global current_m_wf, fc
    fc = slider_freq_carrier.val
    current_m_wf = current_trigon_wf(wf_carrier.value_selected, a, fc, x, c, m)
    plot_carrier_wave(current_m_wf)
    plt.draw()


def show_integral(label):
    global current_t_wf, fc
    annotation = False
    # c needs to be 0 (no shift on y axis)
    current_t_wf = current_trigon_wf(wf_modulation.value_selected, a, fm, x, 0)
    current_t_wf = normalize(running_sum(current_t_wf, 0))
    if check_integral.get_status()[0]:
        annotation = True
    else:
        current_t_wf = current_trigon_wf(wf_modulation.value_selected, a, fm, x, c)

    plot_modulation_wave(current_t_wf[:chunk_size], trigonometric, 'Trigonometric function', annotation)
    plt.draw()


def apply_modulation(label):
    global beta
    beta = slider_mod_index.val/fm
    if check_mod.get_status()[0]:
        update_wf_carrier(wf_carrier.value_selected, current_t_wf*beta)
    else:
        update_wf_carrier(wf_carrier.value_selected, 0)


def init():
    update_wf(wf_modulation.value_selected)
    show_integral(None)
    plot_carrier_wave(current_m_wf)


current_f_wf = current_fourier_wf('Triangle', 10, fm, x)
current_t_wf = current_trigon_wf('Triangle', a, fm, x, c)
current_m_wf = current_t_wf


plt.rcParams['toolbar'] = 'None'
fig, axes = plt.subplots(nrows=4, ncols=4)
fig.set_size_inches(15, 8)
style = ['seaborn']
plt.style.use(style)


fourier_series = plt.subplot(2, 2, 1)
trigonometric = plt.subplot(2, 2, 2)
carrier_wave = plt.subplot(2, 1, 2)

wf_labels = ['Triangle', 'Sawtooth', 'Square Wave']
wf_mod_pos = plt.axes([0.01, 0.8, 0.2, 0.2], frameon=False, aspect='equal')
wf_modulation = RadioButtons(wf_mod_pos, wf_labels, activecolor='#1f77b4')
wf_carrier_pos = plt.axes([0.01, 0.2, 0.2, 0.2], frameon=False, aspect='equal')
wf_carrier = RadioButtons(wf_carrier_pos, wf_labels, activecolor='#1f77b4')

slider_it_pos = plt.axes([0.1, 0.6, 0.2, 0.02])
slider_fm_pos = plt.axes([0.1, 0.55, 0.2, 0.02])
slider_fc_pos = plt.axes([0.1, 0.5, 0.2, 0.02])
slider_mod_pos = plt.axes([0.1, 0.45, 0.2, 0.02])
slider_iterations = Slider(slider_it_pos, 'Iteration (i)', 2, 100, valinit=10, valstep=1)
slider_freq_mod = Slider(slider_fm_pos, 'Mod. (Hz)', 1, 500, valinit=100, valstep=1)
slider_freq_carrier = Slider(slider_fc_pos, 'Carrier (Hz)', 1, 500, valinit=20, valstep=1)
slider_mod_index = Slider(slider_mod_pos, 'Mod. Index', 0.01, 1000)


check_i_pos = plt.axes([0.015, 0.65, 0.2, 0.2], frameon=False, aspect='equal')
check_integral = CheckButtons(check_i_pos, ['show Integral \n(trigonometric function)'])
check_integral.on_clicked(show_integral)

check_m_pos = plt.axes([0.015, 0.05, 0.2, 0.2], frameon=False, aspect='equal')
check_mod = CheckButtons(check_m_pos, ['apply modulation '])
check_mod.on_clicked(apply_modulation)


wf_modulation.on_clicked(update_wf)
slider_iterations.on_changed(update_wf_fourier)
slider_freq_mod.on_changed(update_wf)
slider_freq_carrier.on_changed(apply_modulation)
slider_mod_index.on_changed(apply_modulation)
wf_carrier.on_clicked(apply_modulation)
init()
#plt.title(r'$\sum_{i=0}^\infty x_i$', fontsize=20)

#plt.tight_layout()
plt.subplots_adjust(left=0.4)
plt.show()
