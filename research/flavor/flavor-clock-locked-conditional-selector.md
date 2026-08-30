# Clock-locked conditional selector: WP724

## Question

What is the strongest noncircular explanation possible if one independently
calibrated physical clock is admitted, while every dimensionless flavor datum
must still be source-derived?

## Candidate source principle

The surviving architecture is a clock-locked asymptotically safe
representation source. It combines five operations that earlier packets proved
cannot be substituted for one another:

1. representation theory fixes unequal Clebsch invariants;
2. an interacting gauge–Yukawa fixed point fixes their common normalization;
3. the full critical surface fixes the dimensionless RG basin;
4. a common-singlet relation locks the crossover and messenger scales to one
   independently calibrated clock; and
5. representation-labelled detector channels retain the contrast.

Let the electroweak norm \(v\) be the single calibrated dimensionful datum.
The common-singlet relations are

\[
v=\sqrt{2a}\,w,
\qquad
\Lambda_c=\kappa w,
\qquad
f=\sqrt6\,yw,
\qquad
M_A=z_Aw,
\qquad
M_B=z_Bw.
\]

If \(a,\kappa,y,z_A,z_B\) are fixed by the same source theory, then

\[
\frac{f}{v}=y\sqrt{\frac3a},
\qquad
\frac{M_A}{v}=\frac{z_A}{\sqrt{2a}},
\qquad
\frac{M_B}{v}=\frac{z_B}{\sqrt{2a}},
\qquad
\frac{v}{\Lambda_c}=\frac{\sqrt{2a}}{\kappa}.
\]

Every dimensionless threshold and RG argument is then independent of the
numerical value assigned to the clock.

## Portal sign and magnitude

Suppose the representation packet fixes

\[
C_n=C_m+\Delta_C,
\qquad
\Delta_C>0,
\]

and the interacting fixed trajectory fixes a positive normalization
\(\alpha_v\) at the source-determined argument \(v/\Lambda_c\). The portal
contrast becomes

\[
g_n-g_m=\alpha_v\Delta_C.
\]

Its sign and dimensionless magnitude are independent of the calibrated clock.
Changing either requires changing the representation or the fixed trajectory,
not retuning an independent portal coefficient.

## Threshold and readout gates

Fixed mass ratios do not by themselves prove threshold survival. The complete
finite matching map must preserve the contrast at those ratios, including
mixing, widths, decoupling, and uncertainty. WP720's condition remains the
linear acceptance test.

At readout, two representation-labelled channels preserve the contrast
direction. An unlabelled total channel annihilates it. With an independently
calibrated positive detector metric

\[
W=\begin{pmatrix}p&r\\r&q\end{pmatrix},
\]

the ideal labelled information Gram has determinant

\[
pq-r^2.
\]

This must remain strictly positive after the actual finite-width detector
model and uncertainty completion.

## Claim boundary

WP724 proves an exact conditional composition theorem. If all five source
operations exist, one measured clock suffices to convert the dimensionless
source prediction into masses in detector units without granting the detector
selection authority.

No current flavor theory realizes the antecedent. In particular:

- no anomaly-free matter packet fixes the required unequal Clebsches and all
  fixed-point coordinates;
- no completed beta system supplies the full attractive basin;
- no derived equality currently locks \(\Lambda_c\) to the common singlet;
- no exact finite matching calculation proves contrast survival; and
- no actual common-frame experiment realizes the labelled calibrated map.

The result is therefore an acceptance specification for the source principle,
not evidence that the principle already exists.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp724_clock_locked_conditional_selector.py`

Generated result: `results/wp724_clock_locked_conditional_selector.json`.
