"""You found it. Nobody told you to look in here. That is the best way to learn."""

import logging

import matplotlib.pyplot as plt
import numpy as np


def secret_func(show=False):
    """Draw a small xkcd-style plot. Runs in its own style context, so it leaves your settings alone."""
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)  # hides harmless findfont warnings

    rng = np.random.default_rng(0)
    x = np.linspace(0, 10, 20)
    y = 2 * x + rng.normal(0, 2, x.size)

    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, "o-")
        ax.set_xlabel("Hours of plotting")
        ax.set_ylabel("Confidence in the plot")
        ax.set_title("Seems legit")

    # if show:
    #     plt.show()