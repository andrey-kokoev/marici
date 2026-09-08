# Residue recursion for common-Jacobian affine pentagons

## Question

Is interval boundary recursion special to the reference slice, or does it hold across the common-Jacobian family?

## Claim boundary

The theorem applies to bounded simple affine pentagons whose cyclic facet-gradient determinants share one nonzero value. It does not derive those assumptions from scattering sources.

Let `a_i` be affine facet functions, positive in the interior, with cyclic incidence and

\[
\det(d a_i,d a_{i+1})=J\ne0.
\]

The logarithmic two-form

\[
\Omega=\sum_i d\log a_i\wedge d\log a_{i+1}
\]

has normal-first residue

\[
\operatorname{Res}_{a_i=0}\Omega
=d\log(a_{i+1}/a_{i-1}).
\]

On facet `i`, choose an affine coordinate `s=a_{i+1}`. Simplicity and positivity imply

\[
a_{i-1}=\lambda_i(L_i-s),\qquad \lambda_i,L_i>0,
\]

because the two adjacent facet functions vanish at opposite endpoints. The support-dependent scale disappears under `dlog`, giving

\[
\operatorname{Res}_{a_i=0}\Omega
=\left(\frac1s+\frac1{L_i-s}\right)ds.
\]

Thus every facet carries the interval canonical form with endpoint residues `+1,-1`. The sign of `J` identifies the normal-tangent frame with the ambient orientation. For `J>0`, increasing `s` is opposite the Stokes orientation determined by the outward conormal `-d a_i`; determinant-line transport retains this sign.

Exact checks cover every facet of the reference member and two non-reference rational members. Their endpoint separations and support scales differ, while the residue law does not.

## Disposition

Boundary recursion follows from simple affine incidence and orientation, not from selection of the reference fan or support constants. It therefore cannot distinguish the source-selected associahedron from positive common-Jacobian rivals.
