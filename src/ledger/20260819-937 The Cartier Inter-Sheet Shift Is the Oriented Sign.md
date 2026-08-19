# 937 — The Cartier Inter-Sheet Shift Is the Oriented Sign

## Frozen comparison

Entry 935 proves that a unit normal exponent shift exchanges the two Cartier
sheets. The remaining question is whether the source six-point transition
induces only the forced normal-line sign or mixes the coefficient fibers.

Use the unspecialized twelve-component dense-to-sparse transition and retain
the other two maximal-flag specializations. Define the native first grades

\[
G_+
=
\left.
\frac{T(A_4)}{A_4-1}
\right|_{A_4=1},
\qquad
G_-
=
\left.
\frac{T(A_4)}{A_4+1}
\right|_{A_4=-1}.
\]

No basis or normalization is changed between the calculations.

## Exact sheet comparison

Symbolic reduction gives equality in every component:

\[
\boxed{
G_-=G_+.
}
\]

All twelve entries are nonzero in the generic source field. There is no
componentwise mismatch and no off-diagonal mixing.

## Oriented shift map

The unit shift acts by \(A_4\mapsto-A_4\). On local parameters,

\[
A_4-1\longmapsto-(A_4+1).
\]

Therefore the shift-induced map between the native sheet frames includes the
normal-line orientation:

\[
\boxed{
T_{A_4}:G_+\longrightarrow G_-,
\qquad
T_{A_4}=-I.
}
\]

Applying the shift twice returns identity:

\[
T_{A_4}^2=I.
\]

Thus the two-sheet atlas carries the sign representation forced by the
resolved normal coordinate, and nothing else.

## Consequence

The rank-eight tangential shift module extends across the two Cartier sheets
without rank growth:

\[
\boxed{
\mathcal N_{m shift}^{(+)}
\xleftrightarrow{-I_8}
\mathcal N_{m shift}^{(-)}.
}
\]

No new extension class, carrier cell, or fitted sheet identification is
needed. The distinction between the linear resolved normal and the quadratic
coarse invariant is exact:

\[
N\mapsto-N
\quad\text{acts nontrivially on the resolved sheets, while}\quad
N^2\text{ is fixed}.
\]

This is the same structural pattern already seen in the cosmological
total-energy square-root coordinate, but the present statement is derived
independently in the string coefficient system.

## Next falsifier

Assemble the three normal coordinates of the maximal flag into the full
\((\mathbf Z/2)^3\) sheet cube. Compute all edge signs and every square
commutator. A nontrivial square sign would be a genuine discrete gerbe or
higher-coherence class; complete commutation would establish the full
resolved-sheet difference atlas.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_cartier_sheet_transition.rs;
- packet:
  research/benincasa/string-six-point-cartier-sheet-transition.json;
- allocator claim:
  seqclaim-8f515cd16cb3363f976cc169.
- epistemic event:
  ev-000000000554-6cf331ec-688b-496b-9e12-cf8299c6af20.
