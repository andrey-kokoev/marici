# D Cayley positive-real pair

## Question

Does the bounded-real ratio `S=R/P` admit a stable Cayley pair suitable for an algebraic positive-real certificate?

## Claim boundary

The Cayley transform is

\[
F=\frac{1+S}{1-S}=\frac{P+R}{P-R}.
\]

Exact Routh arrays show that both `P-R=H D_n` and `P+R` are Hurwitz for all 21 tested depth/shift pairs through `n=8`; `R/P` has unit feedthrough because P and R have equal leading coefficient. This supplies stable numerator and denominator data but does not prove `Re F>=0`: stable pairs need not be positive real. The governing DPC case remains `rh-quarter-D-imaginary-axis-dominance.md`.

## Disposition

The bounded-real backend passes its stable-pair gate. The next nonredundant object is the positive-real Bezoutian or KYP matrix of `(P+R)/(P-R)`; proving that matrix positive semidefinite would certify the required boundary inequality without shell matching.
