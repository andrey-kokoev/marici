# Experimental gate for the sub-threshold QED Bell signal

## Typed protocol

Use two counter-propagating photon beams with center-of-mass energy

\[
\sqrt{s}=0.6481956562\,m_e,
\qquad
E_\gamma=165.614\ {\rm keV}
\]

per beam. Select elastic \(\gamma\gamma\to\gamma\gamma\) events in a forward cone and analyze the two outgoing linear polarizations with independent Compton polarimeters. The four analyzer settings are the fixed CHSH settings used by the source Bell functional.

The source channel is not unpolarized. Both counter-propagating photons must be prepared in positive circular helicity relative to their own momenta. In the circular-helicity qubit basis, the selected outgoing state is

\[
|\psi_{\rm out}\rangle\propto
\Phi_1|00\rangle+\Phi_2|11\rangle
\]

up to the small mixed-helicity component included by the exact readout. The preparation contract therefore requires narrow-band, synchronized, counter-propagating \(165.6\) keV beams with the \(++\) occurrence channel retained and helicity-independent collision/acceptance support.

The scattering-state Bell construction follows the framework of [Sinha and Zahed](https://arxiv.org/abs/2212.10213). A practical two-arm Compton-polarimeter architecture has been demonstrated at 511 keV by [Abdurashitov et al.](https://arxiv.org/abs/2204.04692), although that experiment did not supply the light-by-light source required here.

## Polarimeter gate

At \(165.6\) keV, the polarized Klein--Nishina kernel has maximum single-arm visibility

\[
\mu=0.928466
\]

at a Compton scatter angle of \(88.12^\circ\). Two independent arms therefore reduce the ideal correlation by

\[
\mu^2=0.862049.
\]

Consequently, an ideal scattering-state value must exceed

\[
\frac{2}{\mu^2}=2.32005
\]

before a single-scatter Compton implementation can violate CHSH. The transverse onset itself has ideal value \(2\), so it is not directly visible with this analyzer.

In a common transverse linear-polarization frame, the four required analyzer axes are

\[
\begin{array}{c|cc}
 & 1 & 2\\
\hline
\text{Alice} & 90^\circ & 45^\circ\\
\text{Bob} & 67.5^\circ & 112.5^\circ
\end{array}
\]

corresponding to

\[
A_1=-\sigma_x,quad A_2=\sigma_y,quad
B_1=\frac{-\sigma_x+\sigma_y}{\sqrt2},quad
B_2=\frac{-\sigma_x-\sigma_y}{\sqrt2}.
\]

Each physical setting is implemented by rotating the Compton azimuthal reference and assigning calibrated parallel/perpendicular scatter sectors to the two outcomes. The measured effects are unsharp,

\[
E_\pm(\alpha)=\frac12\bigl(1\pm\mu O(\alpha)\bigr),
\]

not ideal projectors.

The exact QED state does exceed the instrumental threshold in the forward region. At the onset energy the surviving cone is

\[
x=\sin^2\frac{\theta}{2}<0.0279165,
\qquad
\theta<19.2365^\circ.
\]

After averaging with the leading Euler--Heisenberg angular weight, the ideal and analyzer-diluted values are

\[
B_{\rm ideal}=2.33644,
\qquad
B_{\rm observed}=2.01412.
\]

Thus the protocol is typed and nonzero, but its margin is small.

That margin imposes an unusually severe preparation/background gate. After the calculated Compton dilution, every additional imperfection must retain visibility

\[
\eta_{\rm residual}>\frac{2}{2.014122}=0.992988.
\]

Thus the aggregate additional visibility loss must stay below \(0.701\%\). If this factor is modeled only as the product of equal incoming circular-polarization purities, each beam requires

\[
P_\gamma>0.996488.
\]

This is a necessary idealized bound, not a complete systematic-error budget.

## Rate gate

The leading low-energy total cross-section estimate at this energy is

\[
\sigma_{\gamma\gamma}\simeq1.50\times10^{-38}\ {\rm m}^2.
\]

Only about \(3.88\%\) lies in one accepted forward cone. With the conservative balanced-CHSH bound

\[
\sigma_S\le \frac4{\sqrt N},
\]

a five-standard-deviation observation of the \(0.0141\) excess requires approximately

\[
N_{\rm accepted}\simeq2.0\times10^6
\]

events, before detector losses or backgrounds. The corresponding ideal integrated luminosity is approximately

\[
3.45\times10^{41}\ {\rm cm}^{-2}.
\]

This excludes a credible near-term single-Compton experiment. Detector efficiency, finite beam phase space, backgrounds, setting switching, and loophole closure only strengthen that conclusion.

For scale, even granting perfect efficiency and the ideal accepted cross section, the five-sigma live time would be approximately

\[
\begin{array}{c|c}
\mathcal L\ ({\rm cm}^{-2}{\rm s}^{-1}) & \text{live time}\\
\hline
10^{30} & 1.09\times10^4\ {\rm yr}\\
10^{32} & 1.09\times10^2\ {\rm yr}\\
10^{34} & 1.09\ {\rm yr}
\end{array}
\]

These are luminosity benchmarks, not claims that a \(165\) keV polarized photon collider can attain them.

Repeated Compton interactions may sharpen the polarization POVM, as proposed by [Clarke et al.](https://arxiv.org/abs/2604.25034), and would widen the angular acceptance. But the elastic light-by-light event rate remains the primary bottleneck, while repeated interactions introduce additional efficiency costs.

## Theory uncertainty

The central energy is the exact one-loop value. No explicit two-loop helicity amplitude has been inserted. The measured Bell normalization removes a common radiative rescaling, so the relevant uncertainty is the differential correction to \(\Phi_2/\Phi_1\).

Using one \(\alpha/\pi\) unit in that direction as a sensitivity benchmark gives

\[
|\delta y_*|\simeq0.07274,
\]

or the per-beam energy interval

\[
150.6\ {\rm keV}\lesssim E_\gamma\lesssim179.4\ {\rm keV}.
\]

This is not a confidence interval. It is the theory-systematics envelope to use for beam-energy scans until the two-loop relative helicity correction is calculated.

## Scientific conclusion

The Bell threshold is a valid amplitude-level and conditional-state prediction. It is not presently an experimentally accessible fundamental-physics Bell test with ordinary gamma-ray technology. The correct experimental frontier is therefore either:

1. a radically higher-luminosity coherent gamma--gamma source with efficient polarization analysis; or
2. an indirect witness/readout that accesses the same helicity ratio without requiring millions of detected elastic light-by-light events.

## Reproduction

```text
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_qed_bell_experimental_gate.py
```
