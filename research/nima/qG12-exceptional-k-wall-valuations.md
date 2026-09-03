# Exceptional Cayley–Menger wall valuations at `X1` soft

## Question

What square-root valuations do the three sewn wall forms acquire from the exceptional Cayley–Menger kernel, and what are their final algebraic soft grades before relative reduction?

## Exact restrictions

The bulk strict transform has

\[
K_0=x^2K_{\rm exc}+O(x^3).
\]

Execution `structured_command_execution:e_30844_1788299704320249600_6` restricts `K_exc` to the three leading wall loci and obtains exact squares:

\[
K_{\rm exc}|_{q_{g1}}=
\left(a^2+4\kappa p^2-5p^2\right)^2,
\]

\[
K_{\rm exc}|_{q_{g2}}=16p^4(\kappa+\xi)^2,
\qquad
K_{\rm exc}|_{q_{g3}}=16p^4(\kappa-\xi)^2.
\]

Thus, away from the displayed reduced-factor zeros, every wall square root contributes one additional factor of `x` from the bulk soft degeneration and no fractional `x` valuation.

## Combined valuations

The previously computed rational-plus-differential valuations are

\[
(0,-1,0)
\]

for `(q_g1,q_g2,q_g3)`. Dividing by the wall square root shifts each by `-1`, giving final algebraic soft valuations

\[
(-1,-2,-1).
\]

Therefore `q_g2` remains one grade more singular than `q_g1` and `q_g3`. The discrepancy is not caused by the Cayley–Menger square root: all three wall restrictions have the same bulk `x` order. It is caused by the extra simultaneous marked collision in the rational denominator.

## Branch factors

The reduced square roots are, up to signs,

\[
a^2+4\kappa p^2-5p^2,
\qquad 4p^2(\kappa+\xi),
\qquad 4p^2(\kappa-\xi).
\]

Their zeros define additional supported subloci where higher normal analysis is required. The generic valuations above exclude those loci.

## Strongest falsification attempt

Attribute the `q_g2` extra pole to a special square-root degeneration. Exact restriction disproves this: its exceptional kernel is a nonzero square generically, with the same bulk `x^2` order as the other walls. The excess pole survives after square-root accounting.

## Remaining normalization gate

These are algebraic form valuations. Analytic epsilon normalization may cancel a common conductor pole, and relative reduction may kill or move leading terms. Neither operation is encoded by the exceptional square identities.

## Acceptance test

1. compute relative leading classes at grades `-1,-2,-1`;
2. apply the source analytic normalization and record grade shifts;
3. test whether the `q_g2` grade `-2` coefficient is exact or supported;
4. compare surviving classes with the positive-cut generator;
5. evaluate on a reduced-factor zero as a deliberate nongeneric failure.

## Disposition

All three exceptional wall kernels are exact squares. Final generic algebraic soft grades are `(-1,-2,-1)`, with a genuine extra `q_g2` singular grade awaiting relative and analytic normalization.

## Evidence

- `research/nima/checkers/check_qG12_exceptional_k_wall_restrictions.py`
- `research/nima/checkers/check_qG12_sewn_wall_x1_soft.py`
- `research/benincasa/check_x1_soft_physical_strict_transform.py`
