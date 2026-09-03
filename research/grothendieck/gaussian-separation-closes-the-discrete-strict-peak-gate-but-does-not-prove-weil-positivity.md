# Gaussian separation closes the discrete strict-peak gate but does not prove Weil positivity

## Setup

Assume a hypothetical off-seam nontrivial zero

`rho=beta+i gamma`,

with reciprocal partner

`rho^vee=1-beta+i gamma`.

Let

`c=1/2+i gamma`, `d=beta-1/2`,

and define

`Q(s)=(s-rho)(s-rho^vee)=(s-c)^2-d^2`.

For `s=sigma+i t` in the critical strip,

`Re Q(s)=(sigma-1/2)^2-(t-gamma)^2-d^2`.

Since `0<=sigma<=1`, the set where `Re Q(s)>=0` lies in the bounded horizontal band

`|t-gamma|<=sqrt(1/4-d^2)`.

The nontrivial zero divisor is discrete, so only finitely many zeros lie in that band.

## Finite hostile interpolation

Choose a polynomial `P` satisfying

`P(rho)=1`, `P(rho^vee)=-1`,

and vanishing at every other zero for which `Re Q>=0`, including boundary points where `Re Q=0`.

For `R>0`, set

`F_R(s)=P(s) exp(Q(s)/R^2)`.

The exponential equals one at the target pair. At every interpolated competing zero, `F_R` vanishes.

For every remaining zero, `Re Q<0`. Discreteness supplies a negative margin on bounded height ranges after the boundary zeros have been removed. At large height, `Re Q` decreases quadratically while `P` grows polynomially. Therefore, for sufficiently small `R`,

`sup_(z != rho,rho^vee) |F_R(z)| = q < 1`.

Thus a vertically Schwartz entire strict peak exists.

## Return to compactly supported Mellin packets

A polynomial times `exp(Q/R^2)` is the bilateral Laplace transform of a Gaussian-type Schwartz source with polynomial derivatives. Smooth compact truncations of that source converge in exponentially weighted `L^1` uniformly for `0<=Re s<=1`; their transforms therefore converge uniformly on the full closed strip.

The truncation perturbs the two target values. Correct them using two fixed compactly supported smooth packets whose two-point evaluation matrix at `rho,rho^vee` is invertible. The correction coefficients tend to zero. Since the original strict-peak margin `1-q` is positive, a sufficiently accurate truncation plus correction preserves

`Phi(rho)=1`, `Phi(rho^vee)=-1`,

and

`sup_(z != rho,rho^vee)|Phi(z)|<1`.

This gives the compactly supported strict peak required by convolution amplification, subject to writing the weighted truncation and two-point correction estimates with directed constants.

## What this does and does not close

Convolution powers of this packet isolate the negative reciprocal swap block if an off-seam pair exists. This closes the completion-localization issue in the zero-side Weil criterion.

It does not prove that the source-side Weil form is nonnegative. It proves only that any off-seam pair is visible to the authorized compact test class. Without an independent prime/archimedean positivity theorem, the argument reconstructs the implication

`off-seam zero => negative Weil test`,

which is part of the classical Weil equivalence, not a proof of RH.

## Correction to route ranking

Strict-peak interpolation is a completion theorem and hostile-test constructor, not an independent positivity constructor. The compact weighted source operator remains the only currently live route aimed at proving positivity itself. Canonical-system or arithmetic Li-kernel constructions would become additional routes only after source-derived positive energy is materialized.

## Disposition

The strict-peak gate appears analytically closable by Gaussian separation and compact approximation. The next proof task is a directed weighted-truncation lemma. This result should be used to validate test-space completeness and to falsify proposed positive constructors, not reported as RH positivity.
