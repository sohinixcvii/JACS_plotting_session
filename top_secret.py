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

def zen():
    """The plotting commandments."""
    print("\n".join([
        "1. Choose the plot for the question, not for the data.",
        "2. A colourbar without a label is a rumour.",
        "3. If it only works in colour, it doesn't work.",
        "4. Make the choice once, in a style file.",
        "5. If the code ran, you have learned nothing about whether it's right.",
        "6. Check the plot. Then check the checker.",
    ]))
