# Endpoint-annihilating packets reduce any diagonal Poisson contraction to a pointwise density test

## Candidate contraction

The Poisson decomposition suggests a finite-stage inequality

\[
\|C_Sg\|^2
\le
Q_{\infty+end+baseline,S}(g),
\qquad
C_Sg=
\sqrt{\rho_S}\widehat g.
\]

Suppose the endpoint-free part of the proposed right side is diagonal in the same real spectral variable:

\[
Q_{\infty+baseline,S}(g)
=
\int_\mathbb R
w_{\infty,S}(t)
|\widehat g(t)|^2dt.
\]

Then the completed difference has the form

\[
Q_S(g)
=
\int
k_S(t)|\widehat g(t)|^2dt
+
Q_{end}(g),
\]

where

\[
k_S=w_{\infty,S}-\rho_S.
\]

The exact sign and constants in `w_infinity,S` must be inherited from the chosen explicit-formula normalization.

## Killing both endpoint coordinates

Let `h` be an entire spectral packet and set

\[
\widehat g(z)
=
(z^2+\tfrac14)h(z).
\]

Then

\[
\widehat g(i/2)
=
\widehat g(-i/2)
=0.
\]

Therefore

\[
Q_{end}(g)=0
\]

for the complete swap-polarized endpoint form, independently of its sign.

This construction is source-compatible: multiplication by `z^2+1/4` corresponds in physical coordinates to applying the shifted differential operator associated with the endpoint complex.

## Localized entire packets

Fix `t_0 in R`. For `epsilon>0`, choose

\[
h_\epsilon(z)
=
\exp\left(
-\frac{(z-t_0)^2}{2\epsilon^2}
\right).
\]

On the real axis, `|h_epsilon|^2` localizes near `t_0`. Put

\[
\widehat g_\epsilon(z)
=
(z^2+\tfrac14)h_\epsilon(z).
\]

After normalization in real-axis `L2`, the measures

\[
|\widehat g_\epsilon(t)|^2dt
\]

converge weakly to a point mass at `t_0`, because

\[
t_0^2+\frac14>0.
\]

Both endpoint evaluations vanish for every `epsilon`.

If the observer class requires compact physical support rather than Gaussian decay, analogous endpoint-annihilating approximants can be constructed in increasing Paley--Wiener spaces. Passing to that class requires a standard density argument but does not alter the obstruction.

## Necessary pointwise condition

Assume `k_S` is continuous at `t_0`. Then

\[
\lim_{\epsilon\downarrow0}
Q_S(g_\epsilon)
=
k_S(t_0)
\]

after normalization. Hence positivity for all endpoint-annihilating analytic packets implies

\[
\boxed{
k_S(t)\ge0
\quad\text{for every real }t.}
\]

Equivalently, a diagonal gamma--baseline carrier can dominate the Poisson prime feature only if

\[
\boxed{
w_{\infty,S}(t)
\ge
\rho_S(t)
\quad\text{pointwise}.}
\]

A finite-rank endpoint correction cannot repair failure of this inequality on an open real interval.

## Resonant prime test

At `t=0`, every prime phase is aligned. The Poisson density is

\[
\rho_S(0)
=
\frac12
\sum_{p\in S}
(\log p)
\frac{1+p^{-1/2}}
     {1-p^{-1/2}},
\]

and

\[
V_S(0)
=
\rho_S(0)-c_S
=
\sum_{p\in S}
(\log p)
\frac{p^{-1/2}}
     {1-p^{-1/2}}.
\]

Thus the hostile prime peak grows monotonically as places are added. Any proposed diagonal domination must pass the explicit test

\[
w_{\infty,S}(0)
\ge
\rho_S(0).
\]

If `w_infinity,S` consists only of a fixed archimedean density plus the baseline `c_S`, this reduces to

\[
w_\infty(0)
\ge
V_S(0),
\]

which fails for sufficiently large `S` because the right side grows without bound.

Therefore no fixed diagonal archimedean density plus endpoint rank two can uniformly dominate all finite prime stages.

## Consequence for the common bulk

The desired positive realization cannot have the form

\[
\text{diagonal gamma density}
-
\text{diagonal Poisson density}
+
\text{finite-rank endpoint repair}.
\]

It must contain an infinite-rank **noncommuting or nonlocal** gamma--prime coupling. Such a coupling must act nontrivially even on the codimension-two subspace

\[
\widehat g(i/2)=
\widehat g(-i/2)=0.
\]

This agrees with the first-prime-crossing result: prime translations must enter the same positive bulk operator, not merely be compared against a fixed diagonal archimedean weight.

## Relation to the contour kernel

The scalar boundary differential `Omega_S` records the correct completed functional but diagonalizes it too early. Passing to its real-axis density loses the analytic cross-boundary coupling needed for positivity. A successful strip-kernel realization must therefore be genuinely two-variable:

\[
K_S(z,w),
\]

not multiplication by a one-variable density `k_S(t)`.

Endpoint-annihilating packets remain a decisive test for any proposed `K_S`: after restriction to the kernel of the two endpoint evaluations, the resulting bulk kernel must already be positive.

## Disposition

The Poisson common-density factorization is exact, but the naive contraction into a diagonal gamma--baseline carrier cannot work uniformly over primes. The endpoint can be annihilated while concentrating at any real spectral point, forcing pointwise domination; aligned prime phases at `t=0` violate any fixed archimedean bound.

The next viable target is a nonlocal two-variable strip kernel whose gamma and prime translations are coupled before diagonal restriction.
