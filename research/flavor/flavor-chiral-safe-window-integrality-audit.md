# Chiral Safe-Window Integrality and Incidence Audit

## Question

Does a known anomaly-free chiral gauge--Yukawa theory repair WP802 by making
the safety-generating portal intrinsically chiral and physically realizable at
integer field multiplicity?

## Admitted source

The generalized Georgi--Glashow and Bars--Yankielowicz theories are chiral
(SU(N)) gauge theories. Normalize the cubic anomaly of a fundamental Weyl
fermion to one. Their gauge anomalies cancel exactly:

\[
\begin{aligned}
\mathcal A_{\rm GG}&=(N-4)-(N-4+p)+p=0,\\
\mathcal A_{\rm BY}&=(N+4)-(N+4+p)+p=0.
\end{aligned}
\]

This passes a gate that the vectorlike source in WP802 did not.

Adding a gauge-singlet meson (M) permits

\[
y_M\widetilde F_j M^j{}_k F^k+\text{h.c.}
\]

and can generate a perturbative ultraviolet fixed point after asymptotic
freedom is lost.

## Exact finite-SU(5) window

For the finite (SU(5)) Georgi--Glashow model, eliminating the meson Yukawa
along its fixed flow gives

\[
\beta_{a_g}^{\rm eff}=b_0a_g^2+b_1a_g^3,
\]

with

\[
b_0=\frac{4p}{3}-34,
\qquad
b_1=\frac{4(106p^2-1997p-19536)}{15(2p+11)}.
\]

Perturbative asymptotic safety requires (b_0>0) and (b_1<0). The exact
window is

\[
\frac{51}{2}<p<
\frac{1997+\sqrt{12271273}}{212}
\approx25.9436.
\]

It contains no integer. Thus the controlled finite-(SU(5)) fixed point exists
only after analytically continuing the number of vectorlike species. The exact
probe (p=103/4) lies in the window and yields

\[
a_g^*=\frac{625}{5393},
\qquad
a_M^*=\frac{288}{5393}.
\]

Both beta functions vanish exactly, so the obstruction is not failure of the
algebraic fixed point. It is failure to define a physical finite field packet
at an integer multiplicity.

## Chiral-incidence obstruction

The Yukawa interaction that creates the perturbative safe window couples
(F) and (widetilde F), the vectorlike fundamental--antifundamental pair.
The genuinely chiral two-index tensor (A) or (S) has zero incidence in this
vertex. Hence anomaly-free chiral matter is present in the source, but the
mechanism selecting the safe Yukawa ratio does not select a coupling of that
chiral sector.

Moreover, (a_M=y_M^2/(4\pi)^2) is sign-blind. A phase redefinition of (M)
changes the bare Yukawa phase without changing the fixed-point coordinate.
No rephasing-invariant orientation-odd loop is supplied.

## RG, threshold, and instrument gates

Even if the noninteger multiplicity were provisionally admitted, the fixed
point would select a dimensionless ratio rather than its crossover scale.
Relevant scalar masses choose distinct massive completions, and the source
contains no Standard Model embedding, threshold matching packet, or calibrated
physical16 instrument. Intrinsic fixed-point probes leave the crossover and
detector-calibration directions in their contextual kernel.

## Classification

- Anomaly cancellation: selected exactly.
- Chiral ultraviolet matter: present.
- Physical finite safe source at (SU(5)): absent in the controlled window.
- Safety-generating portal: vectorlike incidence, not chiral incidence.
- Portal sign: erased.
- Absolute magnitude and threshold: free relevant data.
- Physical readout: absent.

## Smallest exact falsifier

The open interval from (51/2) to
((1997+\sqrt{12271273})/212) contains no integer. This is the smallest
finite-source falsifier. Independently, the Yukawa incidence vector on
((F,\widetilde F,T)) is ((1,1,0)), so its chiral-tensor component vanishes.

## Disposition

Known chiral asymptotic safety does not yet provide the desired source
principle. The next constructor must satisfy a stronger incidence condition:
the orientation-sensitive portal itself must contain the anomaly-essential
chiral representation, rather than coupling only an added vectorlike sector.
Its safe window must contain an actual integer matter packet, and its
rephasing-invariant odd coupling must be irrelevant at the fixed point.

Verification:

- checker: research/flavor/checkers/wp803_chiral_safe_window_integrality_audit.py
- generated result: research/flavor/results/wp803_chiral_safe_window_integrality_audit.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp803_chiral_safe_window_integrality_audit.py
- primary source: [Mølgaard and Sannino](https://arxiv.org/abs/1610.03130)
