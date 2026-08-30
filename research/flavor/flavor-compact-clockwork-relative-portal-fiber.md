# Compact Clockwork Relative Portal and Source Fiber

## Question

Can a compact clockwork incidence replace WP795's continuous localization
geometry by quantized source data and thereby fix the asymmetric flavor portal,
its basin, thresholds, and readout?

## Claim boundary

The admitted source is a four-site compact \(U(1)^4\) chain with three
oriented Higgs links of charges \((1,-q)\), integer \(q>1\). Its incidence
matrix is

\[
C=
\begin{pmatrix}
1&-q&0&0\\
0&1&-q&0\\
0&0&1&-q
\end{pmatrix}.
\]

The gauge-boson Gram operator is \(K=C^\mathsf TC\). It is positive
semidefinite and has the unique normalized zero-mode profile

\[
v_0\propto
\begin{pmatrix}
1&q^{-1}&q^{-2}&q^{-3}
\end{pmatrix}^{\mathsf T}.
\]

Matter localized at site \(j\) therefore couples to the unbroken mode with a
relative factor \(q^{-j}\). Once the integer incidence, orientation, and
endpoint assignment are fixed, the hierarchy is a kernel theorem rather than
a fitted overlap.

For \(q=3\), the three nonzero eigenvalues of \(K/m^2\) are

\[
10-3\sqrt2,\qquad 10,\qquad 10+3\sqrt2.
\]

The strict gap rigidifies the zero-mode direction against small deformations
that preserve the exact gauge incidence.

## Source fibers

Compactness quantizes charges but does not select which integer occurs. Both
\(q=2\) and \(q=3\) are admitted charge packets and give endpoint ratios
\(1/8\) and \(1/27\). The chain length is also source data.

Let \(J\) reverse the site order. The reversed Gram operator \(JKJ\) has the
same spectrum, while its normalized kernel is \(Jv_0\). With fixed species
labels at the two laboratory endpoints, reversal changes

\[
g_{\mathrm L}-g_{\mathrm R}
\longmapsto
-(g_{\mathrm L}-g_{\mathrm R}).
\]

Thus the oriented charge incidence selects a relative sign only after its
orientation and endpoint species map are supplied. The mirror chain remains
an equally valid compact source.

The absolute zero-mode coupling retains the gauge coupling \(g\), and the gear
thresholds retain the link scale \(m\). Quantized relative charges do not fix
either dimensionful normalization.

## RG, threshold, and instrument typing

The exact unbroken \(U(1)\) protects the kernel charge profile. The positive
gear spectrum supplies a gapped neighborhood of that profile. This is stronger
than the continuous wall-overlap construction.

It is not yet a complete RG theorem. Matter-dependent wavefunction
renormalization, gauge running, and finite gear thresholds require a declared
anomaly-free matter completion. Their absolute locations depend on \(g\) and
\(m\).

Localized couplings and gear resonances are physical channels in principle.
No source-derived map currently identifies those channels with perturbations
of the faithful physical16 flavor coordinate, and no detector calibration is
provided.

## Classification

- The incidence matrix is a relative-coupling selector.
- Its Gram operator is a gapped presentation and basin rigidifier.
- Compactness quantizes but does not select \(q\), chain length, or orientation.
- Endpoint assignment controls the portal sign.
- \(g\) and \(m\) control absolute coupling and thresholds.
- The physical16 instrument remains absent.

Clockwork therefore converts a continuous overlap fiber into a discrete
incidence fiber plus two continuous normalizations. It is substantial
progress, but not the required single source constructor.

## Smallest exact falsifier

The \(q=2\) and \(q=3\) chains satisfy the same compactness and locality rules
while producing different endpoint ratios. Reversing either chain preserves
all gear masses and reverses the endpoint contrast. This falsifies both
integer uniqueness and sign uniqueness.

## Disposition

Retain compact clockwork incidence as the strongest relative-magnitude
selector in the boundary-history branch. The positive successor must derive
the integer charge pattern, chain orientation, endpoint species assignment,
and the scales \(g,m\) from one non-mirror-completable source. Only then should
the anomaly-complete RG flow, finite gear thresholds, and physical16 detector
Jacobian be computed.

Verification:

- checker:
  research/flavor/checkers/wp796_compact_clockwork_relative_portal_fiber.py
- generated result:
  research/flavor/results/wp796_compact_clockwork_relative_portal_fiber.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp796_compact_clockwork_relative_portal_fiber.py
- general clockwork source:
  [Giudice and McCullough](https://arxiv.org/abs/1610.07962)
- compact gauged source:
  [Lee](https://arxiv.org/abs/1708.03564)
- UV charge constraint:
  [Ibáñez and Montero](https://arxiv.org/abs/1709.02392)
