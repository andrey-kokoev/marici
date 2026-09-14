# Finite-Blaschke Suzuki intersection has the degree-difference dimension

## Finite model

Assume

\[
\Theta=S/B
\]

with coprime finite Blaschke products `S` and `B`. Write

\[
m=\deg S,
\qquad
n=\deg B.
\]

The linearized Suzuki leakage is

\[
L=T_{\bar S}T_B=T_{\bar S B}.
\]

Its kernel is the incidence space

\[
V\simeq T_B^{-1}(BH^2\cap K_S).
\]

## Toeplitz index

The unimodular symbol

\[
\bar S B
\]

has winding number `n-m`. Therefore the Fredholm index is

\[
\operatorname{ind}T_{\bar S B}=m-n.
\]

Coburn's alternative for nonzero Toeplitz symbols says that at least one of

\[
\ker T_{\bar S B},
\qquad
\ker T_{\bar S B}^*
\]

is trivial. Combining this with the index gives

\[
\boxed{
\dim\ker T_{\bar S B}=\max(m-n,0),
}
\]

and

\[
\boxed{
\dim\ker T_{\bar S B}^*=\max(n-m,0).
}
\]

Since finite-Blaschke Toeplitz operators are Fredholm, their ranges are closed.

## Incidence dimension

Multiplication by `B` is injective and isometric, so

\[
\dim(BH^2\cap K_S)
=
\dim V.
\]

Consequently

\[
\boxed{
\dim(BH^2\cap K_S)=\max(\deg S-\deg B,0).
}
\]

Each denominator Blaschke zero removes one dimension from the numerator model space until the intersection collapses.

## Direct monomial check

For

\[
S(z)=z^m,
\qquad
B(z)=z^n
\]

in the disk model,

\[
T_{\bar S}T_B=(S^*)^mS^n.
\]

If `m>n`, its kernel is spanned by

\[
1,z,\ldots,z^{m-n-1}.
\]

If `m<=n`, the kernel is zero. This exactly matches the index formula and confirms the orientation of the factors.

## Consequence for forbidden divisors

In a finite spectral truncation, the positive numerator divisor supplies `m` model directions, while the forbidden pole divisor consumes `n` of them. The unconditional Suzuki projection retains only the excess

\[
m-n.
\]

Thus nontriviality of `V` does not imply absence of forbidden poles. It only implies that the numerator model has larger degree than the denominator defect in the finite model.

Likewise, a large intersection can coexist with an off-axis defect. This reinforces Proposition 5.8: interpolation faithfulness, not mere dimension, is needed to expose every hostile orbit.

## Defect appears as cokernel after degree reversal

When `n>m`, the kernel vanishes but the adjoint kernel has dimension `n-m`. The forbidden divisor is then visible as a cokernel rather than a negative vector inside `V`. A quotient construction that studies only `ker L` would report total collapse while missing a finite residual obstruction in

\[
\operatorname{coker}L.
\]

Therefore a source Green identity must track both kernel and cokernel indices. Discarding the cokernel loses the signed divisor information.

## Infinite numerator limit

For zeta, the numerator inner factor is expected to carry infinitely many boundary/model directions. A finite forbidden `B` would not force `V` to be finite or zero by dimension counting alone. Conversely, if the forbidden denominator has infinite degree, Fredholm index no longer applies directly and closed range may fail.

The finite theorem therefore supplies a truncation law, not a conclusion about the full completed symbol.

## Rung filtration interpretation

At a finite rational/model truncation, adding a numerator zero raises the available model dimension by one; adding a forbidden denominator zero lowers it by one. The running index

\[
\deg S_N-\deg B_N
\]

is the algebraic Euler characteristic of the truncated Suzuki incidence complex.

But positivity is not determined by this integer. It records net dimension, while each off-axis pair still carries an indefinite `(1,1)` polarization. Index coherence can therefore coexist with failure of Weil cone admission.

## Disposition

The finite generalized-inner model is completely classified:

\[
\boxed{
\dim V=\max(\deg S-\deg B,0),
\qquad
\dim\operatorname{coker}L=\max(\deg B-\deg S,0).
}
\]

This validates the Toeplitz orientation and shows exactly why intersection nontriviality is too weak: it measures only the excess model dimension after divisor cancellation, not positivity or faithful interpolation.
