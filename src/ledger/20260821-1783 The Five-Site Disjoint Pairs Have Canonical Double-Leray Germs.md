# 1783 — The Five-Site Disjoint Pairs Have Canonical Double-Leray Germs

## Question

Entry 1781 proves that the literal positive chain misses the six new
disjoint-cut pinches. Does the frozen Bunch–Davies boundary value nevertheless
determine their local analytically continued residue germs, or would choosing
such a germ require extra contour data?

## Frozen source continuation

The source prescription sends every external and internal energy into the
negative-imaginary tube

\[
T_-:
\qquad
\operatorname{Im}X_i<0,
\qquad
\operatorname{Im}y_e<0.
\]

This tube is convex. For a disjoint-cut mixed pair,

\[
q_e=5t+2y_e,
\qquad
q_A=mt+y_i+y_j,
\qquad e\notin\{i,j\},
\]

both wall coordinates inherit the same negative boundary-value side.

Choose the source internal coordinates ((y_e,y_i)), retaining (y_j) as a
coordinate on the double-residue surface. Then

\[
\frac{\partial(q_e,q_A)}{\partial(y_e,y_i)}
=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
\det=2.
\]

Thus every labelled pair has the same source-fixed double-Leray
normalization

\[
\boxed{
\operatorname{Disc}_{q_e}\operatorname{Disc}_{q_A}
\frac{dy_e\wedge dy_i}{q_e q_A}
=
\frac{(2\pi i)^2}{2}\,
\delta(q_e)\delta(q_A),dy_e\wedge dy_i,
}
\]

with orientation inherited from the ordered source measure. The overall sign
changes only with an explicitly changed residue order; it is not fitted after
seeing the Landau divisor.

## Uniqueness

Two continuations in (T_-) with the same endpoint are homotopic. The positive
Cayley–Menger sheet, signed-minor inequalities, source orientation, and the
double-residue multiplicity therefore continue uniquely on a generic
transverse patch. Adding an absolute cycle would change the source period germ
and is not admissible.

Hence

\[
\boxed{
\text{each of the thirty labelled occurrences has a canonical local
boundary-value double-Leray germ.}
}
\]

The construction is (C_5)-natural: cyclic relabelling preserves the negative
tube, the ordered pair type, the determinant (2), and the positive
Cayley–Menger sheet. It therefore acts on the regular occurrence module of
Entry 1782 without identifying its five labels.

## Corrected physical status

Entry 1781 remains valid: the uncontinued positive chain has no literal wall
intersection. The stronger combined classification is now:

- literal positive-chain intersection: zero;
- local analytically continued double-residue germ: canonical;
- local algebraic Morse line: rank one per occurrence;
- global Picard–Lefschetz variation around each degree-six divisor: not yet
  computed.

Thus “no literal support” does not mean “physically unselected.” The remaining
physical falsifier is transport of this canonical germ around a generic point
of one degree-six divisor.

## Provenance

- Entry 180: boundary-value Leray uniqueness theorem
- Entry 1782: rank-30 occurrence-resolved Morse assembly
- allocator claim: `seqclaim-22eca0e0996eece0a5207150`
