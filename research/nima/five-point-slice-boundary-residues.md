# Five-point slice boundary residues

## Question

Do all facets of the declared affine pentagon carry the expected oriented interval residue?

## Claim boundary

This is a conditional canonical-form recursion theorem for the explicit slice. It does not supply source authority for that slice or an analytic contour prescription.

Let

\[
\Omega_5=\sum_{i\bmod 5}d\log a_i\wedge d\log a_{i+1}.
\]

On the reference slice every cyclic determinant `det(d a_i,d a_{i+1})` is one. Define the normal-first Poincare residue by

\[
\Omega_5=d\log a_i\wedge\operatorname{Res}_i\Omega_5
 +\text{terms regular in }a_i.
\]

Only the two terms incident to facet `i` contribute, giving

\[
\operatorname{Res}_i\Omega_5
=d\log a_{i+1}-d\log a_{i-1}
=d\log\frac{a_{i+1}}{a_{i-1}}.
\]

Along each edge, `a_{i-1}+a_{i+1}=L_i`, where the exact lengths in the `a_{i+1}` coordinate are `1,1,1/2,1/2,1/2`. Hence the residue is the interval logarithmic form

\[
\left(\frac1{s}+\frac1{L_i-s}\right)ds,
\]

with endpoint residues `+1,-1` as `s` increases.

For the positive region `a_i>=0`, the outward conormal is `-d a_i`. Since `d a_i wedge d a_{i+1}` has positive ambient orientation, increasing `a_{i+1}` is opposite the Stokes boundary orientation. The resulting minus sign is not discarded: normal-first residue and outward-boundary orientation are distinct orientation-line conventions.

## Disposition

All five facets satisfy interval factorization with explicit signs. The determinant-line convention resolves the apparent residue-sign ambiguity. The result remains conditional on selection of the affine slice and its support constants.
