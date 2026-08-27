# The minimal SU(6) anomaly-free family permits only one positive-index bulk generation: WP775

## Question

Does anomaly cancellation independently require the \(SU(6)\) matter packet
needed by WP774 and simultaneously select its bulk localization?

## Minimal anomaly-free family

For \(SU(6)\), the cubic anomaly coefficients of the fundamental and
two-index antisymmetric representations obey

\[
A(6)=1,
\qquad
A(\overline6)=-1,
\qquad
A(15)=6-4=2.
\]

Therefore

\[
A(15)+2A(\overline6)=0.
\]

The minimal chiral family is \(15+2\overline6\), with degree

\[
15+2(6)=27.
\]

This is not a representation invented for the portal. An explicit \(SU(6)\)
model identifies \(15+2\overline6\) as the smallest anomaly-free chiral set
per generation: [Dutta et al.](https://arxiv.org/abs/1604.07838).

Under \(SU(4)\times SU(2)\times U(1)\), the dimensions branch as

\[
15=6+8+1,
\qquad
\overline6=4+2.
\]

Thus the anomaly packet is compatible with the subgroup chain used by WP774
at the level of exact representation dimensions.

## Spectral generation gate

With the \(SU(6)\) vector adjoint, \(N_V=35\). If \(n_f\) complete anomaly-free
families propagate in the bulk,

\[
\kappa(n_f)=2+35-27n_f.
\]

Hence

\[
\kappa(0)=37,
\qquad
\kappa(1)=10,
\qquad
\kappa(2)=-17,
\qquad
\kappa(3)=-44.
\]

The positive half-twist branch permits at most one bulk family. The second
complete family is the smallest exact sign falsifier.

## Localization obstruction

Anomaly cancellation derives the representation sum, not its localization.
Each \(15+2\overline6\) family is already four-dimensionally anomaly-free, so
the cubic anomaly equation does not require it to be bulk rather than
boundary. Placing all three observed families on boundaries preserves the
pure-vector index \(37\), but leaves the orbifold common kinetic modulus found
in WP772–WP774.

Thus anomaly cancellation supplies an independent reason for the \(SU(6)\)
matter grammar but does not supply the favorable source frame. A completion
must derive a localization and inflow law yielding three chiral generations,
a positive complete spectral measure, and a fixed common boundary kinetic
coefficient simultaneously.

The calibrated WP770 response still needs realization in actual physical16
production and decay channels.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp775_su6_anomaly_family_spectral_generation_gate.py

Generated result:
research/flavor/results/wp775_su6_anomaly_family_spectral_generation_gate.json
