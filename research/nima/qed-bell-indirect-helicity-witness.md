# Continuous Compton modulation as an indirect QED helicity witness

The four-setting CHSH experiment is statistically wasteful when Compton polarimeters reduce the violation to \(2.014\). A more efficient, explicitly model-dependent readout uses the complete relative azimuth of the two Compton scatters.

For the selected incoming \(++\) channel, write

\[
C=
\frac{2|\Phi_1\Phi_2|}
{|\Phi_1|^2+|\Phi_2|^2+2|\Phi_5|^2}.
\]

The linear-polarization correlation is

\[
E(\alpha,\beta)=C\cos2(\alpha+\beta).
\]

Two Compton polarimeters turn this into the normalized azimuthal distribution

\[
p(\varphi)=\frac1{2\pi}
\left[1+V\cos2\varphi\right],
\qquad
V=\mu_A\mu_B C.
\]

At the exact transverse onset,

\[
\left|\frac{\Phi_2}{\Phi_1}\right|=0.41421534,
\qquad
C=\frac1{\sqrt2}+O(10^{-15}),
\]

while the mixed-helicity probability is only \(3.04\times10^{-6}\). With optimized single-Compton visibility,

\[
V=0.609561.
\]

The unbiased estimator

\[
\widehat V=2\left\langle\cos2\varphi\right\rangle
\]

has

\[
\operatorname{Var}(\widehat V)=\frac{2-V^2}{N}.
\]

Therefore only about \(110\) accepted events reject zero modulation at five standard deviations. A one-percent relative measurement of \(V\) requires approximately \(4.38\times10^4\) accepted events. This should be compared with roughly \(2.0\times10^6\) events for the analyzer-diluted CHSH violation.

Using a \(90^\circ\pm5^\circ\) light-by-light scattering bin retains approximately \(7.02\%\) of the leading cross section. Under ideal efficiency, a hypothetical luminosity of \(10^{32}\ {\rm cm}^{-2}{\rm s}^{-1}\) would produce a five-sigma modulation detection in about \(1.21\) days and a one-percent measurement in about \(1.32\) years.

This is not a Bell test. It assumes the QED source channel, the Compton POVM, and background calibration. Its advantage is precisely that it estimates the physically active helicity coherence without imposing the device-independent CHSH threshold. The remaining practical question is whether any polarized \(165\) keV photon source can approach the required \(\gamma\gamma\) luminosity.

## Source-luminosity audit

An optimistic upper-bound proxy can be built from the compact inverse-Compton design of [Deitrick et al.](https://arxiv.org/abs/1803.10326), which reports \(1.4\times10^{14}\) photons/s total flux at 100 MHz and a \(3.2\,\mu\mathrm m\) interaction spot, at 12 keV. Pretend—far more optimistically than demonstrated—that two such sources can instead deliver synchronized, perfectly polarized 165-keV beams and refocus every photon to the same gamma-beam spot.

For two equal Gaussian bunches,

\[
\mathcal L_{\gamma\gamma}
=\frac{fN_\gamma^2}{4\pi\sigma_x\sigma_y}.
\]

The total-flux proxy then gives only

\[
\mathcal L_{\gamma\gamma}\simeq1.52\times10^{26}
\ {\rm cm}^{-2}{\rm s}^{-1}.
\]

Even with perfect detection, the 110-event modulation signal would take approximately \(2.17\times10^3\) years. Using the design's \(0.1\%\)-bandwidth flux instead gives about \(9.63\times10^8\) years.

This closes the conventional inverse-Compton implementation. The indirect witness repairs the readout-statistics problem, but it does not repair the source luminosity by itself. A practical experiment requires genuinely new coherent gamma collision architecture, not incremental optimization of present ICLS parameters.

## Reproduction

```text
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_qed_bell_indirect_modulation.py
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_qed_bell_source_luminosity.py
```
