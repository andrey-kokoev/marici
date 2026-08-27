# Reciprocal Euler transport has a unit current anomaly uniquely centered at one half

## Reciprocal scale sectors

The global scale coordinate carries the reciprocal involution

\[
r\longmapsto r^{-1}.
\]

It exchanges the regions \(0<r<1\) and \(r>1\), with common seam \(r=1\).
For the Euler potential

\[
E(r)=-\log(1-r),
\]

principal-branch continuation gives

\[
E(r^{-1})=E(r)+\log r-i\pi.
\]

The logarithmic term is the scale transition; the constant imaginary term is
the branch/seam phase.

## The unit current anomaly

Let

\[
J(r)=r\frac{d}{dr}E(r)=\frac{r}{1-r}.
\]

Reciprocity reverses the orientation of logarithmic scale. The oriented
transformation is therefore

\[
-J(r^{-1})=J(r)+1.
\]

The defect is exactly one. It is the derivative of the transition
\(\log r\); the branch phase disappears after differentiation.

## Unique half-centering

Seek an affine normalization \(C_a=J+a\) satisfying oriented reciprocal
invariance:

\[
-C_a(r^{-1})=C_a(r).
\]

The unit anomaly forces

\[
a=\frac12.
\]

Thus

\[
C(r)=J(r)+\frac12
=
\frac12\frac{1+r}{1-r}
\]

obeys

\[
-C(r^{-1})=C(r).
\]

The half-offset is again derived before examining zeros. Here it is the
unique affine center of the reciprocal Euler current.

## Typed interpretation

The transition separates two residuals:

- the unit real anomaly in the differentiated current;
- the constant branch phase \(-i\pi\) in the potential.

The first is a primitive boundary current. The second is seam monodromy.
They must not be collapsed into one scalar correction.

This also clarifies the two-sector picture. Each sector has an ordinary Euler
chart. Their centered currents agree only after orientation reversal, while
their potentials differ by a transition unit and a branch phase. The seam is
where neither ordinary chart is regular.

## Relation to Mellin centering

The exponential-coordinate pullback already derived \(z=s-1/2\) from the
unitary Jacobian. The present theorem derives the same half as the affine
center of the reciprocal scale current. These are compatible mechanisms on
the same logarithmic scale object, rather than an equality inferred from a
shared numeral.

The remaining gate is to prove their compatibility as a source naturality
square after the prime labels and archimedean theta channel are inserted.

## Scope

This theorem explains the reciprocal current and seam transition. It does
not constrain zeros. A scalar section can still vanish while the centered
current remains well-defined.

## Result

The two reciprocal Euler sectors differ by a logarithmic transition and a
branch phase. Their oriented currents differ by exactly one, and adding
one-half is the unique reciprocal centering. The primitive current and seam
phase are therefore forced boundary data of the global scale object.
