# Weil Gaussian first contact does not control sampled superpositions

## Question

Can the prior Gaussian smoothing-threshold and first-contact programme prove the sampled Hankel localizer cones?

## Diagonal versus matrix positivity

The two-variable smoothed Weil kernel

\[
U(\sigma,\xi)=(\widehat W*q_\sigma)(\xi)
\]

is the completed Weil form evaluated on one modulated Gaussian coherent test. Pointwise positivity

\[
U(\sigma,\xi)\ge0
\]

controls those diagonal tests.

A sampled localizer cone requires positivity for every polynomial superposition

\[
G_{t,h,c}(u)
=e^{-tu^2/2}q_h(u)p_c(e^{-hu^2}),
\]

including all cross pairings between distinct heat translates. Equivalently, it requires every finite matrix

\[
\bigl(H(t+(i+j)h)-H(t+(i+j+1)h)\bigr)_{i,j}
\]

to be PSD.

Nonnegativity of all individual kernel values does not imply positive definiteness of their Gram matrices. The missing polarization data are exactly the off-diagonal terms that produce the rank-two determinant.

## Why the heat maximum principle does not transfer

The smoothing semigroup propagates pointwise nonnegativity of `U` toward broader variance. It does not propagate positivity of arbitrary coherent-state superpositions backward, nor does it imply the Hausdorff localizer cones in the heat-scale index.

The first-contact equations

\[
U=0,
\qquad
\partial_\xi U=0
\]

therefore detect loss of diagonal Gaussian positivity. A sampled cone may fail through a negative eigenvector while every individual diagonal Gaussian value remains positive. Its boundary condition is instead

\[
Q_{t,h}(c)=0
\]

for a nontrivial polynomial coefficient vector, together with stationarity in that vector.

## Concrete rank-two obstruction

At rank two, diagonal positivity gives only `A_0>=0` and shifted scalar values. Matrix positivity additionally requires

\[
A_0A_2-A_1^2\ge0.
\]

The observed gamma--prime role reversal occurs in this polarization residual and is invisible to a theorem about `U(sigma,xi)` values alone.

## Surviving use of prior work

The character-coercivity theorem and finite-contact compactness remain useful for two-variable diagonal falsifier searches. They do not supply the missing source sign for `D_2` or higher exterior powers.

A viable transfer would require a stronger theorem that `U` is positive definite as a kernel in the relevant coherent-state labels, not merely pointwise nonnegative. That stronger statement is another presentation of Weil-form positivity and cannot be inferred from the maximum principle.

## Disposition

Do not import Gaussian first-contact rigidity as a proof of sampled Hankel cones. Retain it as an independent diagonal probe. The sampled programme must control polynomial superpositions and their off-diagonal Weil pairings directly.