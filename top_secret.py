"""You found it. Nobody told you to look in here. That is the best way to learn."""

import logging

import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
import re


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

"""You found it. Nobody told you to look in here. That is the best way to learn."""


# Hand-drawn template. Keep it next to this file (or the notebook).
TEMPLATE = "assets/certificate_template.png"
# Where the name goes, as fractions of the image (x = centre of the line, y = just above it, both from the top-left).
NAME_X, NAME_Y = 0.51, 0.655
NAME_MAX_WIDTH = 0.70           # the name is shrunk to fit within this fraction of the image width
NAME_SIZE = 42                  # biggest font size to try
NAME_COLOUR = "#1F2A44"         # same ink as the drawing
NAME_FONT = "Bradley Hand"                # e.g. "Segoe Script" or "Bradley Hand" for a handwritten look; None = the xkcd font


def secret_func(show=True):
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

    if show:
        plt.show()
        return None
    return fig


def certificate(name=None, show=True):
    """Ask for a name and make a certificate. Saved as certificate_<name>.png in the current folder."""
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

    if name is None:
        name = input("Your name for the certificate: ")
    name = " ".join(str(name).split())[:40] or "A Mysterious Plotter"   # tidy spaces, cap the length
    date = datetime.date.today().strftime("%d %B %Y")

    if os.path.exists(TEMPLATE):                                 # use the hand-drawn template
        img = plt.imread(TEMPLATE)
        h, w = img.shape[:2]
        fig = plt.figure(figsize=(8, 8 * h / w))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.imshow(img)
        ax.axis("off")
        with plt.xkcd():                                         # hand-written look to match the drawing
            t = ax.text(NAME_X * w, NAME_Y * h, name, ha="center", va="baseline",
                        fontsize=NAME_SIZE, color=NAME_COLOUR,
                        **({"fontfamily": NAME_FONT} if NAME_FONT else {}))
            fig.canvas.draw()
            box = t.get_window_extent()
            limit = NAME_MAX_WIDTH * fig.bbox.width
            if box.width > limit:                                # long names shrink to fit on the line
                t.set_fontsize(NAME_SIZE * limit / box.width)
    else:                                                        # otherwise, draw a default one
        with plt.xkcd():
            fig, ax = plt.subplots(figsize=(8, 5.6))
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            ax.add_patch(plt.Rectangle((0.03, 0.03), 0.94, 0.94, fill=False, lw=3))
            ax.text(0.5, 0.80, "Certificate of Plot Competence", ha="center", fontsize=24)
            ax.text(0.5, 0.65, "This certifies that", ha="center", fontsize=14)
            ax.text(0.5, 0.50, name, ha="center", fontsize=30)
            ax.text(0.5, 0.35, "can make plots that tell the truth,", ha="center", fontsize=14)
            ax.text(0.5, 0.28, "and checks them before trusting them.", ha="center", fontsize=14)
            ax.text(0.5, 0.12, date, ha="center", fontsize=12)

    filename = "certificate_" + re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_") + ".png"
    fig.savefig(filename, dpi=200)
    print(f"Saved {filename}")
    if show:
        plt.show()
    else:
        plt.close(fig)
    return None