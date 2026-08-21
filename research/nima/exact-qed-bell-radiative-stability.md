# Radiative stability of the exact QED Bell crossing

At the exact one-loop transverse crossing,

\[
y_* = 0.4201576087546\ldots,
\qquad
\frac{dB}{dy}\bigg|_{y_*}=0.0451598073372\ldots.
\]

Write the real below-threshold helicity amplitudes as \((\Phi_1,\Phi_2,\Phi_5)\). Their logarithmic Bell sensitivities are

\[
(-1.4141989030,\;1.4142110472,\;-0.0000121442).
\]

Their sum vanishes to the numerical enclosure scale, as required because the normalized Bell readout is invariant under a common amplitude rescaling. The physical radiative direction is therefore almost purely the relative correction

\[
\delta\log\left|\frac{\Phi_2}{\Phi_1}\right|.
\]

To first order,

\[
\delta y_*\simeq
-31.315\,
\delta\log\left|\frac{\Phi_2}{\Phi_1}\right|.
\]

A differential correction of size \(\alpha/\pi\) moves the onset by about \(0.0727\) in \(y=s/m_e^2\). This is phenomenologically material, so an explicit two-loop calculation is needed for a precision threshold. But moving the crossing all the way to the pair-production threshold \(y=4\) would require a relative logarithmic correction of about

\[
0.1143\simeq49.2\,\frac{\alpha}{\pi}.
\]

Thus higher loops can plausibly shift the numerical onset appreciably, but ordinary perturbative corrections are not expected to erase its sub-threshold character. This is a local first-order condition-number statement, not a substitute for the two-loop helicity amplitudes.

## Reproduction

```text
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_exact_qed_bell_radiative_sensitivity.py
```

