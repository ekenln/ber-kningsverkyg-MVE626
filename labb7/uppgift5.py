import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

def myfunctionplot(f, a, b, dx=1e-4, N=100):
    x = np.linspace(a, b, N)

    y_f = f(x)

    y_fprim = (f(x + dx) - f(x - dx)) / (2 * dx)

    y_F = cumulative_trapezoid(y_f, x, initial=0)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))

    # Plottning
    axs[0].plot(x, y_F)
    axs[0].set_title('F (integral)')
    axs[0].grid(True)

    axs[1].plot(x, y_f)
    axs[1].set_title('f (funktion)')
    axs[1].grid(True)

    axs[2].plot(x, y_fprim)
    axs[2].set_title("f' (derivata)")
    axs[2].grid(True)

    plt.show()

f = lambda x: np.sin(x)/x

myfunctionplot(f, -10, 10)