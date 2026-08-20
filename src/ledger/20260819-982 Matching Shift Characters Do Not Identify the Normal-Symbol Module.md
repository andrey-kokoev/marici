# 982 — Matching Shift Characters Do Not Identify the Normal-Symbol Module

## Basis alignment before comparison

Entry 981 identifies the exceptional cochain with its loaded occurrence image

\[
r_{\rm occ}=\lambda C.
\]

This vector is occurrence-indexed, whereas Entry 931's normal-symbol row
\(r_{\rm norm}\) is indexed by the six dense words. Before comparing them,
apply Entry 974's source-derived permutation

\[
p=(4,1,0,5,3,2)
\]

to place (r_{\rm occ}) in the frozen dense order

\[
(123456,124356,132456,134256,142356,143256).
\]

No further basis transformation is allowed.

## Characterwise proportionality test

Project both rows to the four characters of the pair-shift group. Exact
projective-minor reduction gives

\[
\begin{array}{c|c|c}
\text{character}&\text{combined generic rank}&\text{proportional}\\ \hline
(++)&2&\text{no}\\
(-+)&1&\text{yes}\\
(+-)&1&\text{yes}\\
(--)&2&\text{no}.
\end{array}
\]

The two proportional scalars, with loaded image divided by normal symbol,
are

\[
c_{-+}
=
\frac{2((A_2ZB_{24})^2-1)}
{(Z^2-1)((A_2B_{24})^2-1)},
\]

\[
c_{+-}
=
-\frac{2(Z^2-(A_3B_{34})^2)}
{(Z^2-1)((A_3B_{34})^2-1)}.
\]

The first nonzero minors in the two rank-two characters are, up to the
displayed invertible constants and monomials,

\[
m_{++}
\sim
(A_2^2-1)(A_3^2-1)((A_2A_3)^2-1),
\]

\[
m_{--}
\sim
((A_2B_{24})^2-1)
((A_3B_{34})^2-1)
((A_2A_3B_{24}B_{34})^2-1).
\]

They are nonzero at generic kinematics.

## Narrow conclusion

\[
\boxed{
\text{equal deck-character multiplicities do not identify the loaded
occurrence image with the normal-symbol module.}
}
\]

The mixed characters agree projectively, but the invariant and doubly odd
characters each contain two independent coefficient directions. Therefore
the two rank-four regular representations are not the same embedded
submodule in the source-derived common word frame.

This is a coefficient distinction, not evidence for a new carrier stratum.
No intertwiner between the two rank-two character planes has been derived.

## Next falsifier

Project Entry 979's twisted chamber-edge coboundary to the ((++)) and
((--)) characters. Test whether its image supplies exactly the second
direction detected by (m_{++}) and (m_{--}). If yes, the mismatch is a
derived edge extension inside the existing Pochhammer calculus. If not, the
normal-symbol and exceptional modules remain independent coefficient
objects.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_normal_symbol_comparison.rs;
- packet:
  research/benincasa/string-six-point-normal-symbol-comparison.json;
- verified command:
  cargo run --quiet --bin string_six_point_normal_symbol_comparison;
- allocator claim:
  seqclaim-d08d3f57a2b13409df24f6ba.
- epistemic event:
  ev-000000000599-31d45981-8b88-4ae1-aedd-a6d9f0db1c37.
