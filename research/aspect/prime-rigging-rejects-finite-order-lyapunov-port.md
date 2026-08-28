# Prime rigging rejects the finite-order Lyapunov port

## The test

Use the rapid-decay prime test space with seminorms

`q_N(x)=sup_p p^N |x_p|`.

Its continuous dual contains the primitive current

`b_p=(log p)/sqrt(p)`

and the augmentation current with coefficients of constant order.

The theta scale derivative acts diagonally by `log p`; Newman heat acts by a
quadratic logarithmic multiplier.  Thus the natural positive generator on
the prime labels has order

`L_p=(log p)^2`.

The Lyapunov solution for a diagonal real generator is

`G_p=1/(2 (log p)^2)`.

## Exact obstruction

Applied to the primitive current, this gives

`(G b)_p=1/(2 sqrt(p) log p)`.

For every `N>1/2`, its test seminorm contains

`p^(N-1/2)/(2 log p)`,

which diverges.  Applied to augmentation it gives

`(G a)_p=1/(2 (log p)^2)`,

whose `q_N` diverges for every `N>0`.

Therefore the source heat Green operator does not map either completed
current from `E'` into `E`.  Its finite covariance selector is correct, but
it does not repair the completed variance defect.

The obstruction survives every finite differential order: division by any
fixed power of `log p` cannot produce rapid decay in `p`.

## Required next constructor

A successful source map must be infinitely smoothing in the arithmetic
label.  Its multiplier must decay faster than every inverse power of `p`.
Candidates such as `exp(-tau (log p)^2)` have the required mapping property
for every `tau>0`, but introduce the same positive time parameter that the
selector gate forbids us to fit.

This exposes the sharper target: derive a nonzero arithmetic smoothing time
from a source composition law, or derive a parameter-free projector whose
range already lies in the rapid test grade.  Ordinary Newman heat inversion
cannot do it.

## Optical meaning

A finite-bandwidth Gaussian filter can reproduce any fixed cutoff and still
miss this obstruction.  The apparatus must sweep the prime-label bandwidth
and test super-polynomial suppression.  A response that merely follows a
power of `log p` is a failed variance-changing port even when every finite
covariance matrix is positive and Fourier invariant.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_prime_rigging_lyapunov_obstruction.py
```
