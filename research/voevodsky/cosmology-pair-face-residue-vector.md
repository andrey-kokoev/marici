# Ordered pair-face residue vector for the denominator obstruction

## Question

Where does the logarithmic denominator obstruction live after resolving the single double-residue test across all ordered pair-wall faces?

## Claim boundary

This packet computes residues of the denominator form on the three marked-wall pair faces. It does not construct the relative face module that would cancel them, a resolved/Rees exceptional generator, a Cayley--Menger face cone, a global contour, or a physical period.

## Disposition

For

\[
q_3=q_1+q_2+p
\]

and

\[
p\eta=\frac{p\,dq_1\wedge dq_2}{q_1q_2q_3},
\]

the ordered pair-face residues are computed in the basis

\[
(q_1q_2,
q_1q_3,
q_2q_3).
\]

At \(q_1=q_2=0\), the remaining wall is \(q_3=p\), and the residue is \(+1\). At \(q_1=q_3=0\), the remaining wall is \(q_2=-p\), and the residue is \(-1\). At \(q_2=q_3=0\), the remaining wall is \(q_1=-p\), while the ordered coordinate wedge reverses \(dq_1\wedge dq_2\); the residue is \(+1\).

Thus the residue vector is

\[
(1,-1,1),
\]

matching the logarithmic circuit vector. Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), this vector is nonzero. A relative cone that cancels the denominator obstruction must therefore supply a non-tautological face term with boundary residue vector

\[
(-1,1,-1)
\]

in this ordered pair-face basis.

This sharpens the previous obstruction: the generic Cayley--Menger face remains empty and cannot cancel the class. The required enlargement is an ordered pair-wall Čech or resolved/Rees face module carrying exactly the opposite residue vector and a stable differential. Enlarging ordinary Laurent pole depth cannot change this residue.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_pair_face_residue_vector.py`

Result:

- `research/voevodsky/results/cosmology_pair_face_residue_vector.json`

Command:

- `python research/voevodsky/check_cosmology_pair_face_residue_vector.py`
