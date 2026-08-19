# 948 — The Rank-Twelve Chamber Lattice Has a Unimodular Discrete Atlas

## Correct transport category

Entry 930 excludes a rational differential connection in exponent space: an
exponent derivative produces digamma/logarithmic insertion data.  Integer
exponent changes instead define discrete contiguity maps.

After Entry 946 restores the full six-chamber lattice, test those discrete
maps directly.

## Source lattice action

In the frozen word order

\[
(234,243,324,342,423,432),
\]

the cyclic and reflection maps are the permutations

\[
c=(3,2,5,4,0,1),
\qquad
r=(2,3,0,1,5,4),
\]

in zero-based image notation.  They satisfy

\[
c^3=1,qquad r^2=1,qquad rcr=c^{-1}.
\]

The two pair shifts act diagonally by

\[
B_{24}=\operatorname{diag}(-1,-1,-1,1,1,1),
\]

\[
B_{34}=\operatorname{diag}(-1,1,-1,-1,1,1),
\]

and commute.  Pivot shifts act as (-I_6).  Every matrix is a signed
permutation matrix and therefore has determinant (pm1).

## Target factor and rank twelve

Entry 941's target sheet transition is the integral shear

\[
\begin{pmatrix}1&0\\2&1\end{pmatrix},
\qquad \det=1.
\]

Tensoring the six-dimensional chamber lattice with the two-dimensional target
lattice therefore gives a source-derived rank-twelve integral discrete atlas:

\[
\boxed{
L_{12}=L_{\rm target}\otimes L_{\rm chamber},
\qquad
\text{all frozen discrete transitions lie in }GL_{12}(\mathbb Z).
}
\]

## Qualification

This does not construct the missing differential parameter connection, nor
does it prove that (L_{12}) is the physical twisted-Betti local system.
It proves that the natural finite-difference category is integrally closed on
the frozen labelled chamber lattice.

Thus the earlier two-primary quotient was a defect of the two-seed orbit
presentation, not of the full discrete atlas.

## Next falsifier

Construct the de Rham--Betti comparison for one convergence chamber and test
whether analytic continuation intertwines these integral discrete matrices.
Failure would place the remaining obstruction in the comparison functor;
success would promote (L_{12}) from an algebraic chamber lattice to the
integral twisted-cycle lattice.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_integral_discrete_atlas.rs`;
- packet:
  `research/benincasa/string-six-point-integral-discrete-atlas.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_integral_discrete_atlas`;
- allocator claim:
  `seqclaim-1fedbee1cec7c7ec2c951394`.
- epistemic event:
  `ev-000000000565-d2a9539f-3df1-49cc-980c-fc79c7f10148`.
