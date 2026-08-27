# Reciprocal doubling closes incidence only in an indefinite metric

## Question

The direct theta tail supplies a forward triangular incidence and its
Fourier--Tate dual supplies the reverse arrow. Does placing both on one doubled
carrier produce the positive skew-adjoint system required by the weighted seam
theorem?

## Minimal doubled incidence

Let

\[
N=\begin{pmatrix}0&p\\0&0\end{pmatrix},
\qquad p\ne0,
\]

and form the canonical direct--dual double

\[
K=\begin{pmatrix}N&0\\0&-N^*\end{pmatrix}.
\]

This retains the forward arrow in one sector and its adjoint reverse arrow in
the other. It also satisfies

\[
K^2=0,
\qquad K\ne0.
\]

## Positive-metric no-go

There is no positive-definite inner product in which (K) is skew-adjoint.
If such an inner product existed, (K) would be similar to an ordinary
skew-adjoint matrix. It would therefore be normal and diagonalizable with
imaginary eigenvalues. A nilpotent operator has only the eigenvalue zero, so a
nilpotent skew-adjoint operator must vanish. This contradicts (K\ne0).

Thus reciprocal doubling supplies both incidence directions but does not, by
itself, supply a positive conservation law.

## What doubling does supply

Let

\[
J=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]

Then

\[
K^*J+JK=0.
\]

So the doubled generator is exactly skew with respect to the exchange form.
But (J) has both positive and negative directions. The construction is a
Krein-space conservation law, not a Hilbert-space one. Its zero flux can arise
from cancellation between sector energies and therefore does not confine the
spectral parameter.

## Consequence

The missing reverse arrow has been located, but transporting it from the dual
sector produces only indefinite conservation. Something else must convert the
exchange form into the positive Gram trace previously obtained from the two
Clark sheets.

That conversion cannot be an invertible change of metric on the nilpotent
incidence block. It must involve additional dynamics or boundary incidence:

- the differential transport term and its endpoint Green form;
- primitive and square boundary currents;
- or a source-derived off-diagonal seam actuator that destroys nilpotency.

This agrees with the controllability lesson: possessing both arrows is not
enough when they remain separated by a symmetry-preserving commutant. A
nontrivial composite path or independent reference is required.

## Next falsifier

For each proposed boundary augmentation (B), form (K+B). Reject it if:

1. (B) is not derived before the scalar readout;
2. (K+B) remains nonzero nilpotent on an invariant source subspace;
3. skewness holds only for an indefinite exchange form;
4. the positive Gram trace appears only after scalar compression;
5. finite-cutoff compatibility fails.

The next live calculation is therefore not another sewing identity. It is the
smallest primitive or square-current augmentation that breaks the nilpotent
Jordan chain while preserving the exact source equations after projection.

