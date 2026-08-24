# Prime-two level 44 reduces to an odd weighted inequality and one even rank-one gate

Status: analytic reduction with numerical discovery evidence; no continuum
positivity claim yet

On the interval of length `L=log(2)`, Nima's level-44 operator is

\[
T_{44}=d_{44}I+K_{44}(|x-y|),
\qquad
d_{44}=2.6337834936719723\ldots,
\]

where

\[
K_{44}(t)=e^{t/2}
\left(1-\sum_{n=1}^{43}e^{-(2n+1)t}\right).
\]

The kernel is increasing and has exactly one zero.  Setting

\[
B(t)=K_{44}(L)-K_{44}(t)
\]

gives the exact rank-one decomposition

\[
T_{44}=d_{44}I-B_{\rm op}
+K_{44}(L)|1\rangle\langle1|.
\]

The unweighted Schur shortcut genuinely fails:

\[
\sup_x\int_0^L|K_{44}(|x-y|)|dy
\approx2.8648497365>d_{44}.
\]

Thus cancellation and the constant-channel repair cannot be discarded.

Reflection about the interval center folds the odd sector to `[0,L/2]` with
positive candidate kernel

\[
B_{\rm odd}(x,y)=B(|x-y|)-B(x+y)
=K_{44}(x+y)-K_{44}(|x-y|).
\]

Plain Schur remains insufficient (`2.802858728>d44`).  An initial weighted
Schur scout with

\[
w(x)=\sin(kx),
\qquad
k=\frac{39\pi}{25L},
\]

is sharply successful in a 2400-point midpoint scout:

\[
\sup_{0<x\le L/2}
\frac{(B_{\rm odd}w)(x)}{w(x)}
\approx2.59530<d_{44},
\]

leaving reserve about `0.03848`.  Because `K44` is a finite exponential
sum, `(B_odd w)(x)` has an elementary closed form.  The robust spectral gate
is therefore reduced to the directed scalar inequality

\[
(B_{\rm odd}w)(x)<d_{44}w(x),
\qquad0<x\le L/2.
\]

Nima subsequently found the more certificate-friendly integer weight

\[
\phi(x)=x\exp(-7x^2-32x^4).
\]

An independent 2400-point midpoint scout gives maximum quotient
`2.5946381`, reserve `0.0391454`, near `x=0.2673671`.  This is now the
canonical candidate.

The apparent division by `phi(0)=0` is removable before interval
quadrature.  Split the integral at `y=x`.  On the upper triangle use

\[
\frac{K(y+x)-K(y-x)}x
=\int_{-1}^{1}K'(y+xz)\,dz,
\]

On the lower triangle the centered interval is instead around `x`:

\[
K(x+y)-K(x-y)
=y\int_{-1}^{1}K'(x+yz)\,dz.
\]

Putting `y=xv` both cancels the external `1/x` through the Jacobian and
retains the required correlated factor `xv` in the kernel difference.
After also writing `y=x+(L/2-x)v` on the upper triangle, the target is one
smooth fixed-cube inequality on the closed interval `0<=x<=L/2`:

\[
d_{44}e^{-7x^2-32x^4}-I(x)/x>0.
\]

Thus directed quadrature need not exclude or separately extrapolate the
reflection center.

The integer weight is a comparison barrier, not the center-jet truncation of
the true principal odd eigenfunction.  Midpoint Nyström eigenvectors at 400,
800, and 1200 points stabilize instead at

\[
\log(u(x)/x)
=-8.00707\,x^2-15.5506\,x^4-64.34\,x^6+\cdots.
\]

Thus the tempting identity `6*(-7)=K44(0)=-42` is coincidental.  The barrier
is flatter than the eigenfunction at the center and steeper toward the
boundary; its role is to equalize the weighted Schur quotient, not reproduce
the eigenfunction jets.

To infer the full second-eigenvalue separation one must still prove the
positivity/oscillation statement that orders the nonprincipal spectrum by
the top odd mode.  After that, only Nima's near-saturated even rank-one
secular inequality remains.

## The first secular crossing is numerically level 44

For level `N`, retain rates `a_n=2n+1/2`, `0<=n<N`, and define the exact
source quantities

\[
d_N=h_\infty(0)+\sum_{n=0}^{N-1}\frac2{a_n},
\qquad
c_N=K_N(\log2)
=\frac{5+4^{-(N-1)}}{3\sqrt2}.
\]

Writing `A_N=d_N I-B_N`, the even repair is governed, once the one-defect
inertia hypotheses hold, by

\[
S_N=1+c_N\langle1,A_N^{-1}1\rangle.
\]

Independent Gauss--Legendre Nyström calculations at orders 512, 768, 1024,
and 1280, extrapolated against the observed diagonal-cusp `N^-2` error, give

\[
S_{43}\approx+9.03\times10^{-5},
\qquad
S_{44}\approx-4.07\times10^{-6},
\qquad
S_{45}\approx-9.22\times10^{-5}.
\]

Thus level 44 is numerically the first secular crossing, not merely the first
positive eigenvalue in a discretized census.  The level-44 value agrees with
Nima's independent extrapolation `-4.15e-6`.  This remains discovery evidence:
every raw quadrature value is positive because its cusp error exceeds the
true margin, so a directed proof must analytically subtract or enclose that
error rather than certify a raw matrix sign.

Sharp falsifiers are: failure of positivity or oscillation ordering for
`B_op`; a directed point where the weighted inequality reverses; or failure
of the even secular inequality.  None is presently excluded by numerical
evidence alone.

Discovery checkers:

- `checkers/prime_two_t44_schur_scout.py`
- `checkers/prime_two_t44_odd_weight_scout.py`
- `checkers/prime_two_t44_odd_eigenfunction_jets.py`
- `checkers/prime_two_secular_crossing_scout.py`
