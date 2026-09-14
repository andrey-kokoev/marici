# The known orientation sign does not determine the return bit

## Question

Can the last kernel-orientation bit be fixed from the known Jacobian sign

\[
da\wedge db\mapsto-db\wedge da
\]

of site exchange?

## Exact test

The return map on the primitive complement is an integral isometry of

\[
A_1^2,
\qquad G=-2I_2.
\]

There are eight such maps: the signed permutation matrices. Split them by determinant.

For both determinant classes \(\det=+1\) and \(\det=-1\), pulling back the wall covector \((-1,+1)\) produces representatives of both unoriented types

\[
(1,1)
\quad\text{and}\quad
(1,-1).
\]

Consequently both candidate kernel lines

\[
\mathbb Z\langle\alpha_{13}-\alpha_{14}\rangle,
\qquad
\mathbb Z\langle\alpha_{13}+\alpha_{14}\rangle
\]

occur among orientation-preserving return isometries and among orientation-reversing return isometries.

## Meaning

The sign of the two-dimensional coordinate Jacobian is not the same datum as the relative signs of the two integral Picard route axes. Likewise, the fact that \(W\) and the ordered component labels are preserved by cross-pencil site exchange does not determine the return path through parameter space.

Thus none of the following fixes the last bit:

- \(da\wedge db\) orientation reversal;
- determinant of the return isometry;
- preservation of the \(W=\pm Q\) labels;
- primitivity or saturated image;
- the already-known opposite one-wall tails.

## Minimal decisive datum

One oriented column suffices only if its axis label is retained. Concretely, transport the positive generator of the \(a\)-wall route and compute whether its fixed-pencil coordinates are

\[
\pm\alpha_{13}
\quad\text{or}\quad
\pm\alpha_{14},
\]

together with the sign relative to the already anchored \(b\)-wall route. Equivalently, record one signed intersection with either \(\alpha_{13}\) or \(\alpha_{14}\).

The final obstruction is therefore not an unspecified orientation convention; it is one labelled signed Picard incidence.

Verification:

- `research/voevodsky/checkers/check_orientation_sign_does_not_fix_return_bit.py`
- `research/voevodsky/results/orientation_sign_does_not_fix_return_bit.json`
