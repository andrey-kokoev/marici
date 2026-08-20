# 949 — Every Source Fitting Wall Is a Twisted-Boundary Resonance

## Local comparison mechanism

For a loaded relative chamber chain (gamma) meeting a boundary component with
local-system monodromy (M), the twisted boundary has the rank-one form

\[
\partial\gamma=(M-1)e.
\]

Closing the chamber into a twisted cycle therefore requires a regularization
coefficient proportional to

\[
(M-1)^{-1}.
\]

The frozen string coordinates are square-root monodromy coordinates,

\[
A=e^{i\pi s},
\qquad M=A^2.
\]

## Comparison with Entry 943

After Laurent monomial units are removed, every zero factor in the source
Fitting minor is of the form

\[
U^2-1=M_U-1.
\]

The eight labelled monomials and their valuations are

\[
\begin{array}{c|cccccccc}
U&A_2&A_3&A_2B_{24}&A_3B_{34}&ZA_2&ZA_2B_{24}&A_3/Z&A_3B_{34}/Z\\
\hline
v&2&2&1&1&1&2&1&2.
\end{array}
\]

Their total valuation is twelve, agreeing with the exact maximal-minor
factorization.

Hence

\[
\boxed{
\text{source Fitting support}
=
\text{twisted-boundary resonance support}
}
\]

for the computed six-point branch lattice.

## Consequence

Entry 948's labelled chamber lattice is an integral relative-chain lattice.
It cannot be identified globally with closed twisted Betti cycles before
localizing the monodromy factors (M_U-1).  Away from those existing walls,
the standard chamber regularization is typed and the algebraic and twisted
lattices may be compared.

The nonunit source determinant is therefore explained by the de
Rham--Betti boundary operation.  It is neither an unexplained coefficient
singularity nor a new carrier divisor.

## Qualification

This entry identifies the support and local closure mechanism.  It does not
construct the full six-point regularized-cycle matrix or prove its global
normalization and intersection pairing.

## Next falsifier

Construct the full loaded-associahedron regularization matrix in the frozen
six-chamber order.  Its determinant must have exactly the displayed boundary
valuations, up to a source unit.  Any additional irreducible factor would be
a genuine comparison obstruction not seen by the branch Fitting audit.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_twisted_boundary_support.rs`;
- packet:
  `research/benincasa/string-six-point-twisted-boundary-support.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_twisted_boundary_support`;
- allocator claim:
  `seqclaim-972655775006fd061fd73c1f`.
- epistemic event:
  `ev-000000000566-ec02804e-ea67-47f6-b180-ffca64dc6c66`.
