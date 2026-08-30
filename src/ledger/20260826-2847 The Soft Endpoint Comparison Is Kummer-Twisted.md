# 2847 — The Soft Endpoint Comparison Is Kummer-Twisted

> **Partially retracted by the complete-source normalization audit.** The
> claimed \(p\)-weight \(+3\) is an artifact of stripping the rational source
> coefficient from the positive endpoint. The full endpoint ratio has weight
> zero. Its nontrivial square-root/deck dependence remains, but must be treated
> on the occurrence-resolved packets of Entries 2851--2855.

## Question

Entry 2844 showed that a comparison between the marked negative endpoint and the unmarked positive endpoint must carry (p)-weight (+3). The stronger question is whether an ordinary base-rational restriction or Gysin map can provide it.

## Required scalar in the displayed period frames

Write

\[
r_-^2=5-4\kappa,
\qquad
r_+^2=5+4\kappa.
\]

The source-normalized local entries are

\[
c_+=\frac{\pi i}{p r_+},
\]

and

\[
c_-=
\frac{\pi i(r_-+1)}
{2p^4r_-(r_--1)^2(r_-+3)}.
\]

The unique scalar identifying these displayed frames would be

\[
J=\frac{c_+}{c_-}
=
\frac{2p^3r_-(r_--1)^2(r_-+3)}
{(r_-+1)r_+}.
\]

It has the required (p)-weight (+3).

## Deck-character obstruction

Under the positive-endpoint deck involution

\[
r_+\longmapsto-r_+,
\]

one has

\[
J\longmapsto-J.
\]

Every rational function on the base (mathbb Q(p,\kappa)) is invariant under this involution. Therefore (J) is not a base-rational scalar.

Ordinary restriction, residue, and algebraic Gysin morphisms over the frozen base cannot identify these two displayed period frames by a scalar rational over that base. Multiplying by a convenient homogeneous cubic would repair only the weight and would miss the Kummer character.

## Narrow conclusion

The ordinary scalar-covector route is closed. The surviving typed possibility is a morphism valued in the nontrivial Kummer-twisted line

\[
\operatorname{Hom}(E_-,E_+).
\]

Its existence, horizontality, and source normalization are not established. They must be derived from the marked-relative local-system geometry, not inferred from the desired endpoint sum.

This result does not exclude a source-derived morphism in the twisted local-system category. It excludes only an ordinary base-rational scalar or Gysin adapter.

## Next falsifier

Compute the Gauss–Manin connection on

\[
\operatorname{Hom}(E_-,E_+)
\]

and test whether the frozen marked-relative source supplies a horizontal section with the deck character and (p)-weight of (J). If no such section is source-derived, retire the endpoint-combination hypothesis completely while retaining the two local periods separately.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_rational_comparison_obstruction.py`
- `research/benincasa/soft-endpoint-rational-comparison-obstruction.json`
