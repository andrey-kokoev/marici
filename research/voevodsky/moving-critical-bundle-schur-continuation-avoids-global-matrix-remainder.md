# Moving-critical-bundle Schur continuation avoids the global matrix remainder

Let `H(t)` be a Hermitian analytic family on `[-1,1]`.  Suppose an analytic
rank-one orthogonal projection `P(t)` and `Q(t)=1-P(t)` are given, and write

\[
a=PHP,\qquad b=QHP,\qquad C=QHQ.
\]

After identifying `P(t)C^m` with `C`, assume directed bounds

\[
a(t)\ge a_0>0,\quad C(t)\ge \beta I,\quad \|b(t)\|\le\eta,
\quad a_0-\eta^2/\beta>0.                 \tag{1}
\]

Then `H(t)>0` uniformly.  Indeed, completing the square gives, for
`x=Px+Qx`,

\[
\langle Hx,x\rangle
\ge (a_0-\eta^2/\beta)\|Px\|^2
 +\beta\|Qx+ C^{-1}bPx\|^2.
\]

This formulation is useful even when `P` is only an approximate spectral
bundle.  If `H=\widetilde H+E`, and the three components of `E` satisfy

\[
\|PEP\|\le\epsilon_a,\quad
\|QEP\|\le\epsilon_b,\quad
\|QEQ\|\le\epsilon_C<\beta,
\]

then the certified lower bound is

\[
 a_0-\epsilon_a-
 { (\eta+\epsilon_b)^2\over \beta-\epsilon_C}.       \tag{2}
\]

No global bound on `||E||` is required.

## Analytic construction of the bundle

If a contour `Gamma` separates one simple eigenvalue of `H(t)` from the
remaining spectrum, set

\[
P(t)={1\over2\pi i}\int_\Gamma(z-H(t))^{-1}\,dz.
\]

A directed resolvent bound on a complex Bernstein ellipse proves both
analyticity and a tail estimate for a Chebyshev interpolant of `P`.  On the
real interval the differential estimate

\[
\|P'(t)\|\le {\|QH'(t)P\|\over
 \operatorname{dist}(\sigma(PHP),\sigma(QHQ))}
                                                        \tag{3}
\]
provides a consistency check and a subdivision criterion.  Formula (3) is
obtained by differentiating `HP=PH` and solving the off-diagonal Sylvester
equation.

For the complete continuum-corrected degree-8 interpolant on
`L in [0.649,0.65]`, the current floating scouts give

\[
\inf\lambda_1=2.0002667\,10^{-11},\qquad
\inf\lambda_2=9.2830125\,10^{-9},
\]

and `sup ||P'|| = 0.4703` in the scaled coordinate.  Following this moving
bundle reduces the observed post-degree-8 scalar tails to `3.08e-22` on the
critical branch and `2.08e-15` on the first robust branch.  In contrast, a
fixed-center splitting sees a useless `6.30e-6` robust matrix tail.

## Certificate contract for one slab

A slab certificate therefore consists of:

1. interval Chebyshev coefficients for an approximate frame `p(t)`;
2. a directed normalization bound for `p^*p-1`;
3. directed component bounds for `p^*Hp`, `(1-pp^*)Hp`, and
   `(1-pp^*)H(1-pp^*)`;
4. a positive evaluation of (2);
5. a complex resolvent or interval-LDL proof that the robust block remains
   above `beta`.

This is the continuation contract to implement for each threshold-free
slab.  It replaces the invalid demand that a global matrix interpolation
remainder be smaller than the critical margin.
