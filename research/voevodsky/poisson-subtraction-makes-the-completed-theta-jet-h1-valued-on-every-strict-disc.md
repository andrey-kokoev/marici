# Poisson subtraction makes the completed-theta jet H1-valued on every strict disc

Put `u=e^(2x)`, `c=1-t`, and

\[
F(c,u)=\sum_{n\ge1}e^{-\pi c u n^2}
=\frac12\bigl(\vartheta(cu)-1\bigr).
\]

The summed jet is exactly

\[
\Phi_x(t)=e^{x/2}(4\partial_c^2+6\partial_c)F(c,u).
\]

Poisson summation gives

\[
F(c,u)=\frac12\left((cu)^{-1/2}-1\right)
 +(cu)^{-1/2}\sum_{m\ge1}e^{-\pi m^2/(cu)}.
\]

Applying `e^(x/2)(4 partial_c^2+6 partial_c)` to the zero-mode term gives

\[
E_x(t)=\frac32\,t(1-t)^{-5/2}e^{-x/2}.
\]

Hence the renormalized bulk has the exact dual-mode formula

\[
\Phi_x^{\rm bulk}(t)
=e^{x/2}(4\partial_c^2+6\partial_c)
\left[(cu)^{-1/2}\sum_{m\ge1}e^{-\pi m^2/(cu)}\right].
\]

Fix `r<1`. For `|t|<=r`, both `Re(c)>0` and `Re(1/c)>0` have positive
lower bounds depending only on `r`. As `x -> -infinity`, every dual-mode term
and every finite `x,t` derivative is bounded by a polynomial in `e^(-2x)` and
`m` times

\[
\exp(-C_r m^2e^{-2x}).
\]

As `x -> +infinity`, the original direct-mode expression gives the analogous
bound

\[
\exp(-C_r n^2e^{2x}).
\]

The Gaussian sums absorb all polynomial factors. Therefore, uniformly on every
closed strict disc `|t|<=r<1`,

\[
\Phi^{\rm bulk}(\cdot,t)\in H^k(\mathbb R_x)
\]

for every finite `k`, and the map

\[
t\longmapsto\Phi^{\rm bulk}(\cdot,t)
\]

is holomorphic into every `H^k(R)` graph topology. In particular it is a
holomorphic `H1`-valued section.

The complete jet carrier is consequently the direct sum of the holomorphic
modular boundary line spanned by `e^(-x/2)` and the renormalized `H1` bulk.
This proves the whole-line graph estimate. It does not yet identify the
boundary line with an admitted G4 endpoint coordinate or construct the
prime-labelled forward incidence columns.
