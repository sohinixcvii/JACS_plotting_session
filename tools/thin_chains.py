"""Make data/chains_thinned.npz from data/chains/b-sys.npy (not shared with participants).

b-sys.npy holds ONE Gibbs run: 250000 samples x 12 complex parameters, no names stored.
The output keeps every THIN-th sample (burn-in included), splits Re and Im into separate
float32 columns, and cuts the run into 4 consecutive segments that are used as 4 "chains".
"""
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "chains" / "b-sys.npy"
OUT = ROOT / "data" / "chains_thinned.npz"
N_CHAINS = 4
MAX_BYTES = 10 * 1024**2

raw = np.load(SRC, allow_pickle=False)                     # (n_samples, n_params), complex
n_par = raw.shape[1]
names = np.array([f"Re theta_{k}" for k in range(n_par)] + [f"Im theta_{k}" for k in range(n_par)])

thin = 10
while True:
    x = np.concatenate([raw.real, raw.imag], axis=1)[::thin].astype(np.float32)
    n = (len(x) // N_CHAINS) * N_CHAINS                    # equal-length segments
    chains = x[:n].reshape(N_CHAINS, n // N_CHAINS, x.shape[1])
    np.savez_compressed(OUT, chains=chains, names=names, thin=thin,
                        note="4 chains = 4 consecutive segments of a single run; burn-in not removed")
    if OUT.stat().st_size < MAX_BYTES:
        break
    thin *= 2

print(f"{OUT.name}: chains {chains.shape} float32, thin={thin}, {OUT.stat().st_size / 1024**2:.2f} MB")
