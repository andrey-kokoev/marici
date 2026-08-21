# One-loop QED Bell-energy onset

## Result

Substituting the published one-loop QED coefficients into the source-typed photon helicity basis changes the interpretation of the zero-energy near miss.

With (y=s/m_e^2), the relevant exact coefficient ratios are

\[
\left|\frac{f_2}{g_2}\right|=\frac3{11},\quad
m_e^2\frac{g_3}{g_2}=\frac4{77},\quad
m_e^2\left|\frac{f_3}{g_2}\right|=\frac{10}{77},\quad
m_e^2\frac{h_3}{g_2}=-\frac1{77}.
\]

At dimension twelve, the transverse combinations additionally give

\[
m_e^4\frac{g_{4,1}+\frac32g_{4,2}}{g_2}=\frac{157}{9240},
\qquad
m_e^4\frac{\frac94|f_4|}{g_2}=\frac3{308}.
\]

The exact normalized readout formed from each truncated amplitude reaches (I=2) at

\[
y_{10}=0.4680304499\ldots,
\qquad
y_{12}=0.4236925577\ldots.
\]

If the normalized observable itself is consistently expanded and truncated at the corresponding EFT order, the onsets are

\[
y_{10}^{\rm series}=0.4539354698\ldots,
\qquad
y_{12}^{\rm series}=0.4215196030\ldots.
\]

The dimension-twelve correction shifts the observable-series onset by about seven percent. All four values lie far below the electron-pair threshold (y=4).

Therefore consecutive EFT orders agree qualitatively: one-loop QED begins below the fixed-analyzer Bell threshold at zero energy but moves into the violating region at a finite sub-threshold energy. This remains controlled EFT evidence rather than a theorem about the exact one-loop amplitude. The decisive next calculation is to evaluate the exact Karplus–Neuman helicity amplitudes and test whether the crossing survives the full analytic function.

## Reproduction

```text
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_qed_bell_energy_onset.py
```

The durable result is `research/nima/results/qed-bell-energy-onset.json`.
