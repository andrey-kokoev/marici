# A common Kummer parameter exists on the total-energy specialization

## Question

Can the common relative parameter \(Y\), which separates the two active point restrictions, be compared to the two conductor square-root discriminants without inserting an arbitrary equality?

## Claim boundary

This derives the exact equalizer of the two audited conductor discriminants and a formal Kummer-coordinate match on its total-energy component. It does not identify the relative hyperplanes with the conductor walls or construct a physical contour.

## Source inputs

The relative model uses the factors

\[
X_1\pm Y,
\qquad
X_2\pm Y,
\]

and its connection contains logarithmic ratios of these factors. The conductor audit gives quadratic wall denominators

\[
D_i(r)=a_i r^2+b_i r+c_i
\]

and the identity

\[
\frac{dr}{a r^2+br+c}
=
\Delta^{-1/2}d\log
\frac{2ar+b-\sqrt\Delta}{2ar+b+\sqrt\Delta}.
\]

Thus a common relative \(Y\) can model both Kummer square roots only on a locus where \(\Delta_1=\Delta_2\).

## Exact discriminant equalizer

For the audited conductor walls,

\[
\Delta_1=4x\bigl(xy^2+2Exy-E^2(x+2y-E)\bigr),
\]

\[
\Delta_2=4y\bigl(x^2y+2Exy-E^2(2x+y-E)\bigr).
\]

Their difference factors as

\[
\Delta_1-\Delta_2
=
4E(x-y)\bigl(E^2-E(x+y)+2xy\bigr).
\]

Therefore the equalizer has three components:

\[
E=0,
\qquad x=y,
\qquad E^2-E(x+y)+2xy=0.
\]

The audited total-energy component is \(E=0\). There

\[
\Delta_1|_{E=0}=
\Delta_2|_{E=0}=4x^2y^2.
\]

After choosing the orientation branch

\[
Y_{\rm rel}=2xy,
\]

the two Kummer square roots become one common relative parameter.

## Degenerate affine Kummer coordinates

At \(E=0\), the quadratic coefficients vanish and

\[
b_1=2xy,
\qquad b_2=-2xy.
\]

Hence the affine Kummer coordinates \(2a_i r+b_i\) reduce to

\[
X_{1,\rm rel}=Y_{\rm rel},
\qquad
X_{2,\rm rel}=-Y_{\rm rel}.
\]

One factor in each pair vanishes:

\[
X_{1,\rm rel}-Y_{\rm rel}=0,
\qquad
X_{2,\rm rel}+Y_{\rm rel}=0.
\]

This algebraically distinguishes the two moving-wall endpoints \(r=1\) and \(r=-1\) found in the conductor specialization. Reversing the square-root orientation interchanges the vanishing factors.

## Relation to the factor-two residual

The relative point-stratum separation is \(2Y_{\rm rel}\). On the total-energy component this becomes

\[
2Y_{\rm rel}=4xy.
\]

Thus the integer factor two in the normalized ambient obstruction is compatible with normalization by the common square-root scale \(2xy\). This does not derive that normalization or prove that the obstruction is a relative restriction matrix.

## Strongest falsification attempt

Away from the discriminant equalizer, one common \(Y\) cannot represent both conductor square roots. Even on \(E=0\), the quadratic walls degenerate to linear factors, so the comparison is a specialization and not a generic Gauss–Manin identification. The other equalizer components provide rival specializations and must not be conflated with total energy.

## Disposition

The previously missing parameter comparison exists algebraically on the source-audited component \(E=0\): \(Y_{\rm rel}=\pm2xy\). The remaining blocker is a geometric map from the conductor walls and occurrence points to the relative surfaces and point strata, with orientation and normalization derived rather than chosen.
