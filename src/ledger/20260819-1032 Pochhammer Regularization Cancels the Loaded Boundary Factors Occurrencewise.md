# 1032 — Pochhammer Regularization Cancels the Loaded Boundary Factors Occurrencewise

## Question

Entries 1030–1031 identify the six loaded columns as source-derived
occurrence paths and show that their four host columns saturate the primitive
orbit lattice.  Does this already make the loaded boundary complex a genuine
twisted-Betti comparison?

## First loaded boundary grade

Entry 969 gives the exact integral normal form

\[
C=S\operatorname{diag}(q_1,\ldots,q_6),
\qquad S\in GL_6(\mathbb Z),
\]

where each occurrence factor is

\[
q_i=M_i-1
\]

and the repeated labels retain the two distinct occurrences on each
rank-two wall.  The incidence skeleton is

\[
S=
\begin{pmatrix}
0&0&0&0&-1&0\\
1&0&0&0&1&0\\
0&-1&0&0&0&0\\
0&1&0&1&0&0\\
0&0&1&0&0&0\\
0&0&0&0&0&1
\end{pmatrix},
\qquad |\det S|=1.
\]

Entry 949's local Pochhammer regularization divides a relative path by its
twisted-boundary factor.  Hence the occurrencewise primal regularization gives

\[
\boxed{
C\operatorname{diag}(q_i^{-1})=S.
}
\]

Entry 1010 fixes the dual local coefficient

\[
\frac1{M_i^{-1}-1}=-\frac{M_i}{M_i-1}.
\]

Therefore the corresponding dual occurrencewise composition is

\[
\boxed{
C\operatorname{diag}\!\left(-\frac{M_i}{q_i}\right)
=S\operatorname{diag}(-M_i).
}
\]

Both resulting matrices are unimodular over the Laurent monodromy ring,
because the entries (M_i) are units and (|\det S|=1).

## Narrow result

\[
\boxed{
\text{Pochhammer regularization removes the complete loaded Fitting divisor
on the first occurrencewise boundary grade.}
}
\]

Thus no rational factor, integral index, or extra support survives after
localizing the six declared monodromy walls.  The index-(32) primitive-orbit
defect of Entry 944 is not a generic obstruction in this loaded grade: Entry
1031 supplies the missing host columns, and regularization removes precisely
their boundary factors.

## Qualification

This is a chain-side, occurrencewise statement.  It does **not** construct:

- the full loaded-associahedron regularized cycle;
- the source-normalized twisted period pairing;
- its adjoint on chamber cochains;
- the global intersection normalization.

Accordingly it does not overturn Entries 1007 and 1009.  It removes the last
possible determinant or lattice-index obstruction at the local loaded
boundary grade, while leaving the global Betti comparison morphism untyped.

## Next falsifier

Assemble the six local regularizations across the native hexagon two-cell and
compare the resulting chain map with the already derived complete dual
cellular intertwiner of Entries 1013–1016.  The acceptance condition is a
source-normalized global regularization whose restriction to every occurrence
is the matrix above.  A nontrivial Čech defect would be a genuine global Betti
extension; vanishing would close the static six-point comparison.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_pochhammer_cancellation.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-pochhammer-cancellation.json`;
- allocator claim:
  `seqclaim-11575927ed6b033a4b65b77b`.
- epistemic event:
  `ev-000000000651-1d813679-ab7b-4fbb-a3b7-696f74c5082f`.
