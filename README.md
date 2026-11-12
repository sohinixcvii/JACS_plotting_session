# Plotting without tears : a guide to making pretty plots in python
![alt text](assets/image-2.png)
## Before the session (15 minutes, please do this beforehand)

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. In a terminal, from this repo folder:
   ```bash
   conda env create -f environment.yml
   conda activate jacs-plotting
   python -m ipykernel install --user --name jacs-plotting --display-name "JACS plotting"
   ```
3. Open `jacs_participant.ipynb` in `Jupyter` or `VS Code` and pick the **JACS plotting** kernel.
4. Run the first code cell (the setup check). If it prints **"🎉 All good! Kernel ready, packages found, data in place. Grab your keyboards, it's time to lock in."**, you're ready.

## If something goes wrong

- Restart your kernel 
- Windows: if healpy fails to install, use WSL or pair up.

![alt text](assets/image-1.png)
## What's in this folder

- `jacs_participant.ipynb`: the notebook we'll work through together.
- `environment.yml`: the conda environment (`jacs-plotting`) with everything the notebook needs.
- `data/`: the data files the notebook loads. The setup check confirms they're in place.
- `README.md`: This README file

## What we'll cover

- Houston, we need a kernel: Setup, and how to choose the right plot for your data.
- Choose your fighter: How to pick the appropriate kind of plot
- Bad plot, good plot: spotting and fixing plot crimes on real astronomy data.
- Time for a makeover: colour, palettes, text, and a style file that restyles everything at once.
- Seems legit: a cautionary tale about AI-made plots that look right but aren't.
- A short bonus on interactive plots.

## Data credits

- **Haslam 408 MHz all-sky map:** Haslam et al. 1982; reprocessed (destriped) in Remazeilles et al. 2015; used at Nside 256, from [LAMBDA](https://lambda.gsfc.nasa.gov/).
- **Horsehead Nebula image:** a UK Schmidt Telescope photographic plate (SERC-ER survey), distributed by STScI/MAST. from Digitized Sky Survey (DSS), via the Astropy tutorial data (HorseHead.fits), accessed through Astropy.

## After the session

A solutions notebook and the cheat sheet will be released after the session.

---

Happy plotting! 🔭

_Sohini_

> _Questions are welcome any time by any format (except courier pigeons or other avian methods, sadly my windows don't open wide enough to let them in)._
