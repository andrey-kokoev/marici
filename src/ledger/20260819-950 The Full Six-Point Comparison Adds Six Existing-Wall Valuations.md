# 950 — The Full Six-Point Comparison Adds Six Existing-Wall Valuations

## Falsifier from Entry 949

Entry 949 proposed that the full loaded-associahedron comparison determinant
should reproduce the branch Fitting valuation twelve.  The already frozen
dense six-point momentum-kernel certificate provides the relevant full-rank
determinant test.

It returns

\[
v_{\rm branch}=12,
\qquad
v_{\rm dense}=18.
\]

Therefore

\[
\boxed{
\text{the branch minor does not determine the full comparison determinant.}
}
\]

The additional total valuation is six.

## Support classification

The full determinant factors only through the eleven source channel
monomials

\[
\begin{gathered}
x_2,x_3,x_4,y_{23},y_{24},y_{34},
y_{23}y_{24}y_{34},\\
x_2x_3y_{23},
x_2x_4y_{24},
x_3x_4y_{34},
x_2x_3x_4y_{23}y_{24}y_{34},
\end{gathered}
\]

each entering through its sine factor (M-M^{-1}).  The exact valuations
sum to eighteen, with quotient (-1) in the independent two-prime
certificate.

Thus the failed valuation prediction does not expose new support:

\[
\boxed{
\text{six additional comparison orders}
\subset
\text{existing source-channel incidence walls}.
}
\]

## Interpretation

The branch lattice sees only the boundary components meeting that resolved
normal sector.  The full twisted comparison sees all loaded chamber
boundaries.  This is expected support enlargement under global assembly, not
a new carrier divisor or unexplained coefficient singularity.

Entry 949 remains valid for the branch Fitting support, but its proposed
equality with the complete determinant is rejected.

## Next falsifier

Construct the occurrence map from the branch wall factors into the eleven
full source-channel factors.  Test whether the branch valuations are the
restriction/Gysin pullback of the dense determinant divisor.  Any unmatched
branch factor would obstruct the common loaded-associahedron comparison;
matching factors would close the support-level de Rham--Betti test.

## Durable verification

- source certificate:
  `research/benincasa/string-six-point-dense-momentum-kernel.json`;
- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_full_comparison_support.rs`;
- packet:
  `research/benincasa/string-six-point-full-comparison-support.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_full_comparison_support`;
- allocator claim:
  `seqclaim-095a48b04f88d240b750796c`.
- epistemic event:
  `ev-000000000567-21c9a87b-0396-45db-b0c9-a77d11305103`.
