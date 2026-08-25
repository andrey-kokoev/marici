# The global grade-three operator is a paired spin-four spectral multiplier

## 1. Covariant operator

Write the two shear helicities as spin-weighted sections

\[
 C_+\in\Gamma(L^{2}),\qquad C_-\in\Gamma(L^{-2}).
\]

The globally typed grade-three transport is

\[
 \boxed{
 \mathcal A_3(C_+,C_-)=
 \left(\bar\eth\,\eth^3C_+,\;
       \eth\,\bar\eth^3C_-\right)
 \in\Gamma(L^4)\oplus\Gamma(L^{-4}).}
\]

The coordinate expression
`partial_zbar D_z^3 C_zz` is a trivialization of the first component. Its
conjugate is the second component. Subtracting the two as raw scalar functions
before transporting them into a common parity frame produces the local
`p^4-q^4` expression, but that subtraction is not the unprojected global
bundle map.

## 2. Spin-harmonic multiplier

Use

\[
 \eth,{}_sY_{lm}=\sqrt{(l-s)(l+s+1)},{}_{s+1}Y_{lm},
\]

\[
 \bar\eth,{}_sY_{lm}=-\sqrt{(l+s)(l-s+1)},{}_{s-1}Y_{lm}.
\]

Both helicity branches have the same real multiplier

\[
 \boxed{
 \lambda_l=-(l-4)(l+5)
 \sqrt{(l-2)(l+3)(l-3)(l+4)}.}
\]

Thus

\[
 \mathcal A_3: {}_{\pm2}Y_{lm}
 \longmapsto\lambda_l,{}_{\pm4}Y_{lm}.
\]

The multiplier vanishes precisely at `l=2,3,4` and is nonzero for every
`l>=5`. Each helicity kernel has complex dimension

\[
 5+7+9=21.
\]

These are smooth low multipoles, not characteristic high-frequency waves.

## 3. Scalar-source multiplier

If a scalar potential `Phi` generates shear by

\[
 C_+=\eth^2\Phi,
 \]

and `Phi=Delta^{-1}T` on the nonconstant modes, the additional multiplier is

\[
 \frac{\sqrt{(l-1)l(l+1)(l+2)}}{l(l+1)}.
\]

The composite source-to-grade-three map therefore kills scalar harmonics
`l=0,1,2,3,4` and is nonzero for every `l>=5`. The `l=0` Green mode and `l=1`
spin-two-constructor modes are already declared quotients; `l=2,3,4` are new
low-multipole blind modes of the grade-three transport.

## 4. Sobolev and distributional extension

Since `|lambda_l|` grows like `l^4`,

\[
 \mathcal A_3:H^s(L^{\pm2})\longrightarrow H^{s-4}(L^{\pm4})
\]

is bounded. On the orthogonal complement of `l=2,3,4`, it has a bounded
pseudodifferential inverse of order `-4`.

The same coefficient law extends to distributions. If a distributional shear
is in the kernel, all of its `l>=5` coefficients vanish. Therefore

\[
 \boxed{\ker_{\mathcal D'}\mathcal A_3
 =\bigoplus_{l=2}^{4}\mathcal H_l^{(+2)}
  \oplus\bigoplus_{l=2}^{4}\mathcal H_l^{(-2)}.}
\]

No new singular kernel is created by passing from Sobolev sections to the full
distribution carrier for the paired covariant operator.

## 5. Relation to the local characteristic polynomial

The polynomial `p^4-q^4` belongs to the coordinate magnetic projection after
identifying opposite spin frames. Its characteristic lines remain relevant to
that projected scalar presentation, but they are not characteristic zeros of
either covariant helicity branch, whose principal symbols are nonzero fourth
powers in the appropriate complex spin line.

The next step must transport the parity/helicity involution into the harmonic
basis and determine which part of the 42-complex-dimensional paired low-mode
kernel lies in the real electric and magnetic sectors.

## Evidence

`checkers/global_grade_three_spin_spectrum_checks.py` derives the multiplier
from the eth ladder, verifies its zeros and dimensions, checks the scalar
source composite, and proves the order-four Sobolev bounds by exact polynomial
comparison through hostile angular momentum.
