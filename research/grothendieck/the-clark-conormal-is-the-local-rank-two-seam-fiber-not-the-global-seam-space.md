# The Clark Conormal Is the Local Rank-Two Seam Fiber, Not the Global Seam Space

## Source-derived normal coordinate

For a completed scalar section \(F\), the Clark sheets are

\[
H_+=F+iaF',
\qquad
H_-=F-iaF'.
\]

Their difference is the source-defined conormal current

\[
C=H_+-H_-=2iaF'.
\]

At a simple zero \(s_0\), the value channel vanishes while the conormal
survives:

\[
F(s_0)=0,
\qquad
C(s_0)\ne0.
\]

The divisor of a complex scalar section has a one-complex-dimensional
conormal fiber. After realification, this is rank two. It is exactly the
linear normal rank required by the local Lagrangian seam model.

## Local quadratic normal form

Near a simple zero, the value and conormal coordinates provide the local
splitting

\[
W=L\oplus N,
\qquad
\dim_{\mathbb R}L=dim_{\mathbb R}N=2.
\]

Its quadratic controls therefore have the `3+4+3` decomposition:

- three value/tangent quadratics;
- four value–conormal comparisons;
- three conormal quadratics.

This identifies the local source carrier of the finite `sp4` normal form. No
new fitted seam coordinate is needed: Clark differentiation supplies it
before the zero condition is imposed.

## Why the completed seam is larger

The local fiber must not be confused with the global seam state.

First, the moving-endpoint seam is a boundary field over the continuous scale
variable, not one complex number. Evaluation at a spectral point compresses
that field to the conormal line.

Second, at a zero of multiplicity \(m\),

\[
F'=\cdots=F^{(m-1)}=0,
\qquad
F^{(m)}\ne0.
\]

The first Clark conormal then vanishes and the first surviving normal datum is
an order-\(m\) jet. No uniform finite jet truncation is authorized without an
independent multiplicity bound.

Third, the endpoint `sp4` action itself requires a common unbounded domain.
The polynomial normal form does not establish closedness or completion of the
theta boundary operators.

Hence:

```text
simple spectral fiber -> real rank-two normal -> local sp4 model
completed seam field  -> infinite-dimensional boundary object
multiple zero         -> higher normal-jet filtration.
```

## Explanatory consequence

A scalar zero does not destroy the state. It transfers the first nonzero datum
from the value coordinate into the normal-jet filtration. “Loss of meaning”
in the scalar channel is therefore a change of grade in a relative boundary
object, not annihilation of the full source relation.

## Remaining RH gate

This construction explains what the missing normal state is locally. It does
not orient it. Hostile positive sources also possess nonzero conormals at
off-seam zeros.

The unresolved theorem remains global: completed modular sewing must constrain
the conormal or first surviving normal jet so that its total boundary current
cannot close off the reciprocal seam.
