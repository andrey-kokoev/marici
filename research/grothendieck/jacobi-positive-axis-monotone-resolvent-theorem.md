# Positive-axis Jacobi resolvents converge monotonically

For a positive Jacobi compression `J_n`, define

\[
 R_n(h)=A_0\langle e_0,(I+hJ_n)^{-1}e_0\rangle,qquad h>0.
\]

When `J_n` is extended by one Jacobi row and column, block inversion replaces
the old positive block by its Schur complement, subtracting a positive rank-one
term. Inversion reverses Loewner order, hence

\[
 0<R_n(h)\le R_{n+1}(h)\le A_0.
\]

Therefore, if certified positive corners continue compatibly at every order,
`R_n(h)` converges for every positive `h` without any critical-line Euler
phase or zero input. Sizes one through five exhibit this monotone convergence
at `h=1,10,100,1000`; convergence is fastest near the expansion point and
slower toward the spectral boundary.

This gives the safe half of the infinite Weyl construction. The limiting
positive-axis function exists pointwise and inherits Stieltjes-type bounds.
What remains is to prove local uniform convergence/analytic continuation and
identify that limit with the completed source resolvent before approaching the
negative-axis phase.

## Scope

The theorem is conditional on compatible positive Jacobi extensions at every
order. Five numerical rows do not prove that hypothesis, local uniform
convergence, boundary phases, or RH.

## Durable verification

- Checker: `checkers/jacobi_positive_resolvent_monotonicity.py`
- Result: `results/jacobi-positive-resolvent-monotonicity.json`

Compact support and Hausdorff determinacy strengthen this: the Gaussian
measures converge weakly as a full sequence and their Weyl functions converge
locally uniformly off the fixed cut. See
`jacobi-gaussian-measure-to-weyl-limit-theorem.md`.
