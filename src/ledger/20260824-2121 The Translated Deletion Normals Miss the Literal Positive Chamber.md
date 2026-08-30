# 2121 — The Translated Deletion Normals Miss the Literal Positive Chamber

## Hard-to-vary claim

At physical positive kinematics, none of the eight translated total-energy normals from Entry 2119 meets the literal Cayley--Menger loop contour.

## Proof

The source chamber has

\[
E_T>0,
\qquad
y_{12},y_{23},y_{31}\ge0.
\]

For every deletion subset `S`,

\[
E_T^{(S)}=E_T+2\sum_{e\in S}y_e
\ge E_T>0.
\]

Therefore

\[
\boxed{
\Gamma_{m CM}^{+}
\cap
\{E_T^{(S)}=0\}
=\varnothing
\quad\text{for all }S.
}
\]

No subdivision term introduces a finite physical pole or contour pinch through these normals on the undeformed positive chamber.

## Verification

`research/benincasa/checkers/deletion_normals_positive_chamber.rs` enumerates all eight labelled sectors over three exact positive loci and verifies the inequality. The general result is the displayed order argument.

## Consequence

The translated-normal pushforward cannot make \(\mathcal Q\), or any successor polynomial, into a singularity of the literal positive correlator merely by adding deletion sectors.

Any nontrivial discriminant from this mechanism requires analytic continuation in external energies and a genuine Landau pinch involving:

- a translated normal;
- the Cayley--Menger boundary or another frozen integration boundary;
- the stationary/tangency equations of the loop pushforward.

Thus the admissible problem is not the unconstrained resultant of the eight linear normals. It is their **relative Landau discriminant with the source contour boundary**.

## Next falsifier

For one cyclic representative, solve

\[
E_T+2y_{12}=0,
\qquad
CM(y,P)=0,
\]

together with tangency of the two hypersurfaces in loop-edge space. Eliminate the loop variables and classify every factor against existing soft, Gram, signed-energy, and Landau support before comparing with \(\mathcal Q\).

