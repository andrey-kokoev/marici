# 1794 — The Five Physical Threshold Extensions Form a Regular \(C_5\) Orbit

## Question

Does Entry 1792's local logarithmic extension assemble naturally under cyclic
occurrence transport, or does its nilpotent attachment require a preferred
site?

## Frozen input

Entries 1787 and 1790 identify exactly one physically active free
\(C_5\)-orbit. At each occurrence \(i\in\mathbb Z/5\), Entry 1792 supplies a
two-dimensional local extension with basis

\[
(r_i,\ell_i),
\qquad
N\ell_i=r_i,
\qquad
Nr_i=0.
\]

The cyclic generator transports both labelled basis elements by

\[
\sigma r_i=r_{i+1},
\qquad
\sigma\ell_i=\ell_{i+1}.
\]

## Exact assembly

On the ten-dimensional assembled object,

\[
[N,\sigma]=0,
\qquad
\operatorname{rank}N=5,
\qquad
N^2=0.
\]

The total extension and its logarithmic-line subspace have characters

\[
\chi_{\rm total}=(10,0,0,0,0),
\qquad
\chi_{\log}=(5,0,0,0,0).
\]

Therefore

\[
\boxed{
\mathcal V_{\log}\simeq\mathbb Q[C_5],
\qquad
\mathcal V_{\rm total}\simeq\mathbb Q[C_5]\otimes\mathbb Q^2.
}
\]

## Consequence

The logarithmic attachment is occurrence-covariant and introduces no
preferred site, fitted normalization, or cyclic descent defect. It is a
sector-specific coefficient extension carried uniformly over an existing
free occurrence orbit.

This does not identify the deeper boundary specializations of the orbit.

## Next falsifier

Compactify one representative divisor and compute its intersections with
total-energy and soft support. Transport the resulting local comparison
through the regular \(C_5\)-orbit and test whether any boundary cone has a
non-regular character.

## Evidence

- research/benincasa/checkers/five_site_g5_logarithmic_orbit.py
- research/benincasa/results/five-site-g5-logarithmic-orbit.json
- allocator claim: seqclaim-e24876ca597141dc7ea32ae0
