# Flavor-Gram portal threshold: WP688

## Full flavor pairing

Lift the WP687 threshold to the ordinary quark Yukawa matrix (Y_q) and exit
tensor (Y_X). The flavor factor is

\[
P=\operatorname{Tr}
\left[(Y_q^\dagger Y_q)(Y_X^\dagger Y_X)\right].
\]

In the quark-mass basis,

\[
P=\sum_{i,j}q_j^2|(Y_X)_{ij}|^2.
\]

It is a positive pairing with no intergeneration sign cancellations. If all
ordinary quark Yukawas are positive, (P=0) exactly when (Y_X=0). For the
canonical exit shape (Y_X=I),

\[
P=q_1^2+q_2^2+q_3^2>0.
\]

At a common heavy matching scale on the WP687 slice,

\[
\delta\lambda_p=\frac{N_cP}{4\pi^2}.
\]

## Domain-relative faithfulness

The positivity is relative to the admitted nonzero-quark-Yukawa domain. If one
ordinary Yukawa vanishes exactly, exit support confined to that column lies in
the pairing kernel. This is the smallest boundary falsifier.

For the physical massive-quark domain and nonzero canonical exit tensor, the
threshold support is strictly positive. This is a source-defined positive
pairing and a genuine portal rigidifier. It still does not select the total
renormalized portal because the UV boundary coupling can shift it.

## Remaining gate

Nondegenerate messenger thresholds must be summed with their actual masses,
and the UV boundary coupling must be transported in the same scheme. Only then
can a calibrated lower bound at the interference scale be tested.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp688_flavor_gram_portal_threshold.py

Generated result: results/wp688_flavor_gram_portal_threshold.json.
