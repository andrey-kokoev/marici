# 957 — Only Four Source Fitting Factors Are Direct Chamber Facets

## Frozen Betti carrier

Use the six ordered real disk chambers

\[
\gamma_\sigma:
0<z_{\sigma(2)}<z_{\sigma(3)}<z_{\sigma(4)}<1,
\qquad \sigma\in S_3,
\]

with cyclic words

\[
(1,\sigma(2),\sigma(3),\sigma(4),5,6).
\]

For each word, enumerate every cyclic contiguous partition with at least two
labels on each side.  Complementary subsets represent the same divisor.  The
result is exactly nine associahedral facets per chamber.

## Exact comparison lattice

Represent every channel by its vector in the fifteen pair variables
\(s_{ij}\).  Compare up to sign modulo:

1. the six momentum-conservation row sums;
2. the three and only three frozen branch normals
   \[
   s_{14},\qquad s_{23},\qquad s_{23}+s_{25}+s_{35}.
   \]

No additional kinematic relation is imposed.

## Result

Four factors of Entry 943's source Fitting minor match direct planar facets:

\[
\begin{aligned}
A_2&\longleftrightarrow s_{12},\\
A_3&\longleftrightarrow s_{13},\\
A_2B_{24}&\longleftrightarrow s_{124},\\
A_3B_{34}&\longleftrightarrow s_{134}.
\end{aligned}
\]

The four \(Z\)-dependent factors match no facet of any of the six chambers:

\[
ZA_2,qquad ZA_2B_{24},qquad A_3/Z,qquad A_3B_{34}/Z.
\]

Thus

\[
\boxed{
4\text{ direct chamber-wall factors}
+
4\text{ non-facet composite resonances}.
}
\]

## Correction to Entry 949

Entry 949 correctly observes that all eight factors are sine-type resonances
over already used kinematic variables.  It is too strong to treat all eight
as direct boundary monodromies of the six frozen chambers.

Only the first four admit the local loaded-boundary model

\[
\partial_\Phi\gamma
=(M_F-1)F
\]

with \(F\) an actual codimension-one chamber facet.  The remaining four may
belong to a transition determinant, an iterated/composite boundary operation,
or coefficient extension data.  They cannot be supplied with independent
facet cells after inspecting the Fitting factorization.

## Consequence

The direct chamber Gysin calculus can source at most the four matched wall
families without further derivation.  It does not by itself saturate the full
source branch lattice of Entry 943.

This is not evidence for a new carrier divisor.  It is a type separation
inside the comparison problem:

\[
\text{carrier facets}
\neq
\text{composite coefficient resonances}.
\]

## Next falsifier

Derive the four unmatched factors from the frozen chamber complex using only
pre-existing higher incidence operations:

- codimension-two iterated boundaries;
- transition between adjacent chamber charts;
- or a source-derived coefficient extension.

If none yields their additive channel vectors and multiplicities, they remain
comparison-support factors of the algebraic transition rather than Betti
boundary strata.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_branch_chamber_facets.rs`;
- packet:
  `research/benincasa/string-six-point-branch-chamber-facets.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_branch_chamber_facets`;
- allocator claim:
  `seqclaim-711ed02f8a84be8a362bc4e6`.
- epistemic event:
  `ev-000000000574-83fa16c2-c778-4cf2-b05b-753989efed0a`.
