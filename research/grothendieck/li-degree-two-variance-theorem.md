# The first coupled Li determinant is a spectral variance

## Universal measure theorem

Let `mu` be a finite positive symmetric measure on the unit circle and put

`c_k=integral cos(k theta) d mu(theta)`.

The two degree-two reflection channels satisfy

`A_2=c_0-c_2=2 integral sin(theta)^2 d mu(theta)`,

and

`D_2=c_0(c_0+c_2)-2c_1^2`

`   =2[(integral 1 dmu)(integral cos(theta)^2 dmu)
        -(integral cos(theta) dmu)^2]`

`   =2 mu(T)^2 Var_(mu/mu(T))(cos(theta))`.

Thus the first irreducibly coupled determinant is exactly a variance. Its
positivity is Cauchy--Schwarz, not an accidental cancellation.

## Equality and hostile cases

`A_2=0` exactly when `sin(theta)=0` almost everywhere, so the measure is
supported on the real phases `{1,-1}`.

`D_2=0` exactly when `cos(theta)` is constant almost everywhere. For a
symmetric circle measure this means support is confined to one conjugate
phase pair (with the possible real-phase degeneracies).

Therefore strict degree-two positivity measures two kinds of spectral
spread: departure from the real phases and dispersion among distinct real
parts of phases.

## Meaning of the small observed margins

The small values of `A_2` and `D_2` are now interpretable. The
inverse-square-weighted phases `u_rho=1-1/rho` are strongly concentrated near
`1`, and their cosines have small weighted variance. Near-singularity of the
finite Toeplitz matrices is therefore expected geometry, not necessarily a
numerical pathology.

## Source-side burden

This theorem proves positivity only after a positive measure exists. The RH
problem remains the construction of the moment functional from arithmetic
source data. Its benefit is diagnostic: a candidate source functional must
turn `A_2` into a sine-square energy and `D_2` into a genuine variance through
one degree-independent rule. If it cannot, it has not explained the coupled
completion.
