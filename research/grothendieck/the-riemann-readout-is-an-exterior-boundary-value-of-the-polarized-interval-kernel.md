# The Riemann readout is an exterior boundary value of the polarized interval kernel

## Canonical polarization

For spectral parameters with

\[
\Re s>\frac12,
\qquad
\Re w>\frac12,
\]

define the coefficient vectors

\[
c_s=(n^{-s})_{n\ge1}.
\]

Their Gram kernel is

\[
K(s,w)
=
\langle c_w,c_s\rangle
=
\sum_{n\ge1}n^{-s-\bar w}
=
\zeta(s+\bar w).
\]

It is positive definite on this parameter domain because, for every finite
packet of parameters and coefficients,

\[
\sum_{i,j}a_i\overline{a_j}K(s_i,s_j)
=
\sum_{n\ge1}
\left|
\sum_i a_in^{-s_i}
\right|^2
\ge0.
\]

## Polarized interval energy

Insert the full logarithmic interval operator:

\[
Q(s,w)
=
2\sum_{n\ge1}(\log n)n^{-s-\bar w}
=-2\zeta'(s+\bar w).
\]

This is also positive definite, with vacuum kernel, because its Gram weights
are \(2\log n\ge0\). On the diagonal,

\[
Q(s,s)
=
2\sum_n(\log n)n^{-2\Re s},
\]

which is exactly the previously derived full interval energy.

Thus the mixed kernel was not missing algebraically. It is the canonical
polarization of the source-state energy.

## Where the Riemann readout sits

Formally,

\[
K(s,0)=\sum_{n\ge1}n^{-s}=\zeta(s).
\]

But \(w=0\) is not in the positive-kernel parameter domain. The vector

\[
c_0=(1,1,1,\ldots)
\]

is not in the coefficient Hilbert space. For \(1/2<\Re s\le1\), the series
defining \(K(s,0)\) does not converge ordinarily.

Therefore the analytically continued Riemann readout is not an interior
matrix coefficient of the positive kernel. It is a relative boundary value
against an exterior distributional observer.

This explains why diagonal positivity does not constrain its zeros. Positive
kernels control overlaps between admitted interior states; they do not
control a continuation to an observer outside the state space.

## Five-wall interpretation

The exterior observer is precisely where the boundary-bearing construction
must act. The constant carrier represents the formal vector \(c_0\), while
the delta wall is its Fourier incidence. Primitive and square scale currents
describe how finite states approach this observer, and the archimedean heat
term supplies a relative extension.

The missing theorem is not construction of another kernel. It is construction
of a source-authorized boundary morphism

\[
\partial_0K(s,\cdot)
\]

whose scalar value is the completed theta section and whose Green current is
compatible with the positive interior kernel \(Q\).

## A precise no-go

Analytic continuation from the Euler chamber is unique, but uniqueness alone
supplies neither positivity nor a source-level boundary morphism. Hostile
sources can preserve the visible functional symmetry while changing the
interior kernel and its divisor. To distinguish them before scalar
continuation, the boundary morphism must retain:

- the scale pullback;
- the constant–delta overlap;
- primitive and square conormal grades;
- reciprocal Fourier–Tate sewing;
- the theta heat boundary current.

Only then can its divisor be attributed to the source rather than to a chosen
continuation.

## Remaining gate

Derive the boundary Green formula obtained by letting \(w\) approach the
exterior observer through the boundary-bearing five-cell, not through the
Hilbert half-plane. The target is an identity whose interior term is
\(Q(s,w)\) and whose boundary value is the completed Riemann section.

The sharp falsifier is path dependence: if two source-authorized approaches
to \(w=0\) yield different boundary currents after all five walls are
retained, the relative observer is not canonical.

## Result

The canonical polarized interval kernel is \(K(s,w)=\zeta(s+\bar w)\), and
its positive logarithmic derivative is the full interval energy. The Riemann
readout is the exterior boundary value \(K(s,0)\), not an admitted interior
overlap. RH-bearing content is concentrated in construction and orientation
of that relative boundary observer.
