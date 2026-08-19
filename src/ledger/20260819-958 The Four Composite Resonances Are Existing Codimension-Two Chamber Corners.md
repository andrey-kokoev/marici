# 958 — The Four Composite Resonances Are Existing Codimension-Two Chamber Corners

## Question from Entry 957

Entry 957 separated four direct chamber facets from four \(Z\)-dependent
source Fitting factors.  The first admissible provenance test for the latter
is whether each is the monodromy of two compatible facets meeting in an
existing associahedral corner.

Use the six frozen ordered chambers and the exact quotient lattice of Entry
957.  Two facet partitions are admitted only when they are compatible splits
and occur in a common chamber.  Test signed sums of their channel vectors
modulo momentum conservation and the three branch normals.

## Exact corner identities

All four composite factors are generated:

\[
\begin{aligned}
ZA_2&\longleftrightarrow s_{12}+s_{35},\\
ZA_2B_{24}&\longleftrightarrow s_{124}+s_{35},\\
A_3/Z&\longleftrightarrow s_{13}+s_{25},\\
A_3B_{34}/Z&\longleftrightarrow s_{134}+s_{25}.
\end{aligned}
\]

For the ratio factors, the frozen equations give

\[
s_{23}=0,qquad s_{235}=0
\quad\Longrightarrow\quad
s_{25}=-s_{35},
\]

so the last two identities are precisely the additive forms of
\(A_3/Z\) and \(A_3B_{34}/Z\).

## Labelled chamber occurrences

The compatible pairs occur in:

\[
\begin{array}{c|c|c}
\text{factor}&\text{ordered chambers}&\text{count}\\
\hline
ZA_2&(124356)&1\\
ZA_2B_{24}&(124356),(142356)&2\\
A_3/Z&(134256)&1\\
A_3B_{34}/Z&(134256),(143256)&2.
\end{array}
\]

These counts exactly reproduce their valuations in Entry 943's source
Fitting minor:

\[
\boxed{(1,2,1,2).}
\]

This agreement was not used to select the corners: the corner list was
generated from the six cyclic words before comparison with the Fitting
valuation.

## Narrow conclusion

The four factors left unmatched by the codimension-one census are not new
carrier walls.  They are supported on existing codimension-two chamber
incidences:

\[
\boxed{
\text{four direct facets}
+
\text{four existing two-facet corners}
=
\text{all eight source Fitting factors}.
}
\]

This materially strengthens the common-carrier interpretation of the
six-point source lattice.  It does not yet construct the integral twisted
boundary comparison: the ordered corner orientations and loaded iterated
boundary coefficients remain uncomputed.

## Next falsifier

For the four displayed pairs, derive the two ordered boundary routes

\[
\partial_{F_2}\partial_{F_1}\gamma,
\qquad
\partial_{F_1}\partial_{F_2}\gamma,
\]

including associahedral incidence signs and the loaded factors
\((M_{F_1}-1)(M_{F_2}-1)\).  Verify the Koszul anticommutation and compare the
resulting primitive corner columns with the corresponding source branch
blocks.  A multiplicity match without the signed matrix comparison is not yet
an integral de Rham--Betti theorem.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_branch_chamber_facets.rs`;
- packet:
  `research/benincasa/string-six-point-branch-chamber-facets.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_branch_chamber_facets`;
- allocator claim:
  `seqclaim-ee71554feb54966a928bb393`.
- epistemic event:
  `ev-000000000575-6b180142-52f9-4ae1-b792-50fa3691d465`.
