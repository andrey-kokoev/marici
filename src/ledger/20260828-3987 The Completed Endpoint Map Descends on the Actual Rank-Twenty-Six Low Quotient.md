# 3987 — The Completed Endpoint Map Descends on the Actual Rank-Twenty-Six Low Quotient

## Correction

Entries 3979 and 3983 are retracted.

Their endpoint non-descent result was caused by an unauthorized projection in the checker, not by the physical quotient.

The old implementation:

1. reduced a low monomial in the full ambient presentation;
2. retained only coordinates in the declared twenty-six-dimensional low basis;
3. silently discarded every surviving ambient coordinate.

That operation was not proved to be a quotient map. Its augmented inconsistency measured projection loss.

## Repaired quotient

The low simple-pole sector contains thirty-six monomials of total degree at most seven.

The ambient presentation induces ten relations that close entirely inside this low sector. Quotienting by these ten internal relations gives
\[
36-10=26.
\]

The repaired checker reduces only by these ten relations. It does not reduce ambiently and then truncate.

## Exact result

At both primes
\[
p=32009,\qquad p=32003,
\]
at
\[
(x,y,z)=(2,3,4),
\]
all three completed endpoint functionals descend uniquely through the repaired rank-twenty-six quotient.

Each constraint matrix has rank twenty-six and solution nullity zero.

The source-derived finite parts remain nonzero:

\[
\begin{array}{c|ccc}
&5&6&7\\
\hline
t=0&2&3&4\\
t=-1&6&7&8\\
t=\infty&2&3&4
\end{array}
\]

The degree-five normalization guard still reproduces the independently derived direct residues.

## Retraction of false witnesses

Entry 3983's normalized combinations were kernels only after the unauthorized ambient-coordinate projection. They are not relations in the actual low quotient.

The ten genuine low relations all carry zero completed endpoint boundary.

Thus there is presently no evidence that the absolute rank-twenty-six quotient kills relative endpoint information.

## Surviving conclusions

Entry 3981's deck-character decomposition remains valid:
\[
(\dim H^1_+,\dim H^1_-)=(2,5).
\]

The physical source still lies in the anti-invariant sector.

But the endpoint part of that anti-invariant target is now well-defined on the rank-twenty-six quotient. Compact coordinates are required to complete the anti-invariant Leray readout, not to repair endpoint descent.

## Revised frontier

Construct the two compact elliptic coordinate functionals in the same repaired low quotient convention.

Then test:

1. compact descent;
2. the complete rank-five anti-invariant map;
3. occurrence inversion;
4. source-character preservation;
5. comparison of its dual image with the transported seven-plane.

The rank-two invariant sector remains unavailable unless independently sourced.

## Defect provenance

The defect was a violation of projection typing:

\[
\text{ambient reduction}
\longrightarrow
\text{discard ambient remainder}
\]

was treated as though it were

\[
\text{quotient by internal low relations}.
\]

These operations are not equivalent.

## Artifacts

- \`research/benincasa/checkers/check_rank26_infinity_order2_endpoint_descent.py\`
- \`research/benincasa/checkers/check_rank26_low_pivot_relative_boundary.py\`
- \`research/benincasa/results/rank26-infinity-order2-endpoint-descent-p32009.json\`
- \`research/benincasa/results/rank26-infinity-order2-endpoint-descent-p32003.json\`
- \`research/benincasa/results/rank26-low-pivot-relative-boundary-p32009.json\`

Sequence claim: \`seqclaim-613f83c2cbe09303b9185d55\`.
