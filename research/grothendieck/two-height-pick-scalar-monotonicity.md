# The first coupled Xi Pick determinant is exactly one scalar monotonicity law

## Theta-axis data

Let

`B(y)=Xi(i y)=integral_0^infinity Phi(u) cosh(yu)du`

and

`a(y)=B'(y)/B(y)`.

The positive theta density makes `log B` convex, since

`a'(y)=Var_y(u)>=0`

under the exponentially tilted even theta measure.  Thus `a(y)>0` and both
`a(y)` and `y a(y)` are strictly increasing for `y>0`.

For two imaginary-axis points `i y_1,i y_2`, the Xi Pick matrix is

`P_jk=[a(y_j)+a(y_k)]/[y_j+y_k]`.

Its determinant is

`Delta_2
=a_1 a_2/(y_1 y_2)-(a_1+a_2)^2/(y_1+y_2)^2`.

## Exact factorization

Clearing the positive denominator gives

`y_1 y_2 (y_1+y_2)^2 Delta_2
=(y_1 a_2-y_2 a_1)(y_1 a_1-y_2 a_2)`.

Assume `0<y_1<y_2`.  Since `y a(y)` is strictly increasing,

`y_1 a_1-y_2 a_2<0`.

Therefore

`Delta_2>=0`

if and only if

`a(y_2)/y_2 <= a(y_1)/y_1`.

Hence all two-height imaginary-axis Pick matrices are positive semidefinite
exactly when

`y |-> a(y)/y`

is nonincreasing on `(0,infinity)`.

## Stieltjes identification

For

`R_Xi(x)=d/dx log B(sqrt(x))`,

we have

`R_Xi(y^2)=a(y)/(2y)`.

Thus the entire two-height Pick family is equivalent to the first
complete-monotonicity inequality

`R_Xi'(x)<=0`,  `x>0`.

This is substantially weaker than RH: RH requires the full Stieltjes property,
including all alternating derivatives, all moment matrices, and the correct
analytic continuation.  But it is the first genuinely coupled Pick gate and
is no longer a two-parameter problem.

## Source-side variance form

Differentiation gives

`d/dy[a(y)/y]=[y Var_y(u)-E_y(u)]/y^2`.

Consequently the target inequality is exactly

`y Var_y(u)<=E_y(u)`

for every positive tilt `y` of the even theta density.

This formulation contains no zeros, primes, or analytic continuation.  It asks
whether the variance of the tilted theta kernel decays relative to its mean at
the precise rate forced by a positive squared spectral measure.

## A sufficient structural route

A sufficient condition is that the tilted variance

`K''(y)=Var_y(u)`,  where `K(y)=log B(y)`,

is nonincreasing for `y>0`.  Indeed,

`E_y(u)=K'(y)=integral_0^y K''(t)dt`

and decreasing `K''` implies `y K''(y)<=K'(y)`.

Equivalently, it suffices to prove that the third cumulant of every positive
theta tilt is nonpositive:

`K'''(y)<=0`,  `y>0`.

This condition is not automatic for even positive or even log-concave
densities.  It must use the specific super-Gaussian theta potential and its
modular tail estimates.  It is nevertheless a one-variable source inequality
with a pointwise integral representation, making it a sharper analytic target
than full Weil positivity.

## Hostile numerical sweep

The source-moment checker

`checkers/theta_tilt_third_cumulant.py`

evaluates the first four tilted moments directly from the theta series using a
12,000-panel composite Simpson rule.  At

`y in {0.01,0.03,0.1,0.3,1,3,10,30,100}`

every sampled third cumulant was negative and every exact target residual

`E_y(u)-y Var_y(u)`

was positive.  The closest target residual was approximately

`1.49e-10` at `y=0.01`, as expected from its cubic vanishing at the origin.
The third cumulant ranged from approximately `-4.46e-6` at `y=0.01` to
`-4.65e-5` at `y=100`, reaching about `-1.66e-3` near `y=10` on this grid.

This sweep finds no falsifier and makes the third-cumulant route plausible. It
is not interval-certified and does not control unsampled heights.

## Unconditional large-tilt theorem

The sufficient third-cumulant inequality can be proved throughout the large
Euler region.  Put

`s=y+1/2`

and use

`B(y)=xi(s)
=(1/2)s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`.

For `s>1`, three differentiations give

`K'''(y)
=2/s^3+2/(s-1)^3
 +(1/8) psi_2(s/2)
 +(log zeta)'''(s)`.

The Euler expansion has a favorable sign:

`(log zeta)'''(s)
=-sum_(p,k>=1) k^2 (log p)^3 p^(-ks)<0`.

Also

`psi_2(x)=-2 sum_(n>=0)(x+n)^(-3)`.

The `n=0` polygamma term contributes exactly `-2/s^3`, cancelling the
positive `2/s^3` endpoint term.  Hence

`K'''(y)
<2/(s-1)^3
 -(1/4)sum_(n>=1)(s/2+n)^(-3)`.

The integral bound

`sum_(n>=1)(s/2+n)^(-3)
>=integral_1^infinity (s/2+x)^(-3)dx
=2/(s+2)^2`

therefore yields

`K'''(y)<2/(s-1)^3-1/[2(s+2)^2]`.

The right side is negative when

`(s-1)^3>4(s+2)^2`.

This holds at `s=9` (`512>484`) and thereafter because the ratio of the two
sides is increasing.  We obtain:

**Large-tilt theorem.** `K'''(y)<0` for every `y>=17/2`.

Equivalently, the exact target residual

`Q(y)=K'(y)-y K''(y)`

is strictly increasing for `y>=17/2`, because `Q'(y)=-y K'''(y)>0`.
Therefore one certified nonnegative anchor value at `y=17/2` would prove the
target monotonicity throughout the large-tilt interval.  The numerical sweep
finds a comfortable positive value there, but that anchor is not yet an
analytic theorem.  No zero information enters the large-tilt sign proof.

The sufficient third-cumulant attack is now reduced to the compact tilt
interval `0<y<17/2`.  Near zero the leading term is the negative fourth theta
cumulant; a complete proof can therefore be organized as a local Taylor
certificate plus a compact-interval theta-tail inequality.  Proving that
compact sign would also supply the missing anchor automatically.

## Increasing-curvature diagnostic

Let the even theta density be written

`Phi(u)=exp(-V(u))`.

The checker

`checkers/theta_potential_increasing_curvature.py`

differentiates the full theta sum analytically term by term and combines the
logarithmic derivatives by normalized log-sum weights.  A 14,001-point sweep
on `0<=u<=5` found

`V'''(u)>0`

at every sampled `u>0`, with `V'''(0)` zero to floating-point error.  Sample
values grow from about `0.0143` at `u=10^(-4)` to `185.0` at `u=1` and
`5.54e5` at `u=5`.

This strongly suggests that the full modular theta potential has increasing
curvature on the positive half-line.  The property is not yet proved, and by
itself its implication for tilted skewness must not be assumed.

## Exact Stein-kernel reduction

Normalize the full-line tilted theta law as

`p_y(u)=B(y)^(-1) exp(yu) Phi(u)`

and write `m_y=E_y(U)`.  Its one-dimensional Stein kernel is

`tau_y(u)
=p_y(u)^(-1) integral_u^infinity (t-m_y)p_y(t)dt`.

It obeys

`E_y[(U-m_y)f(U)]=E_y[tau_y(U)f'(U)]`.

Taking `f(U)=(U-m_y)^2` gives the exact identity

`K'''(y)=E_y[(U-m_y)^3]
=2 E_y[(U-m_y)tau_y(U)]
=2 Cov_y(U,tau_y(U))`.

Therefore the source-explicit monotonicity

`tau_y'(u)<=0` for all real `u`

is sufficient for `K'''(y)<=0`.  The covariance sign follows from the
opposite monotonicities of `u` and `tau_y(u)`.

Differentiating the tail ratio yields the first-order equation

`tau_y'(u)=[V'(u)-y]tau_y(u)-(u-m_y)`.

The compact self-adjointness rung has consequently become a concrete Mills
ratio inequality:

`[V'(u)-y]tau_y(u)<=u-m_y`.

Every quantity is an integral or logarithmic derivative of the positive theta
source.  Increasing curvature of `V` is now useful because it gives tangent
and tail bounds for this ratio, but a proof still has to handle both sides of
the tilted mode and the point where `u=m_y`.

This Stein formulation is preferable to asserting a general theorem that
increasing potential curvature forces negative skewness: it states the exact
additional inequality needed and has pointwise falsifiers.

### Global Stein monotonicity is too strong

The sufficient condition above fails already at the symmetric endpoint.  At
`y=0`, the theta law is even, so its canonical Stein kernel is even.  It is
nonconstant for a non-Gaussian density and therefore cannot be nonincreasing
on the whole real line.  Continuity in `y` preserves an increasing portion on
the negative half-line for all sufficiently small positive tilts.

Thus increasing curvature of the theta potential does **not** close the proof
through global Stein-kernel monotonicity.  The exact identity remains useful,
but the surviving target is the weaker weighted inequality

`Cov_y(U,tau_y(U))<=0`.

Equivalently, using an independent copy `U'`, one must prove

`E[(U-U')(tau_y(U)-tau_y(U'))]<=0`.

This allows a unimodal Stein kernel: the positive contribution from pairs on
its increasing left branch must be dominated by the negative contribution
from pairs crossing or lying to the right of its maximum.  A viable use of
`V'''>=0` must establish that weighted single-crossing dominance, rather than
the false pointwise monotonicity shortcut.

## Increasing curvature does imply negative tilted skewness: the paired proof

The missing implication can nevertheless be proved without the false global
Stein monotonicity.

Let `X_1,X_2` be independent with tilted density

`p_y(x) proportional exp(yx-V(x))`,

where `V` is even.  Put

`R=(X_1+X_2)/2`, `D=(X_1-X_2)/2`.

Their joint density is proportional to

`exp(2yR-V(R+D)-V(R-D))`.

Conditional on `R`, the law of `D` is independent of `y`.  For `R,d>=0`, its
log-density has mixed derivative

`partial_R partial_d[-V(R+d)-V(R-d)]
=-V''(R+d)+V''(R-d)`.

If `V''` is even and nondecreasing on `[0,infinity)`, then

`R+d>=|R-d|`

implies that this mixed derivative is nonpositive.  Thus the conditional law
of `|D|` decreases in monotone-likelihood-ratio order as `R>=0` increases.
In particular,

`g(R)=E[D^2 | R]`

is even and nonincreasing as a function of `|R|`.

The marginal law of `R` is an exponential tilt by `exp(2yR)` of an even base
law.  Conditional on `T=|R|`,

`E[R | T]=T tanh(2yT)`,

which is increasing in `T`, while `g(T)` is decreasing.  The rearrangement
covariance inequality gives

`Cov_y(R,D^2)=Cov_y(T tanh(2yT),g(T))<=0`.

Finally,

`Var_y(X)=2 E_y[D^2]`

and differentiation of the paired tilted law gives

`K'''(y)=d/dy Var_y(X)=4 Cov_y(R,D^2)<=0`.

We obtain the following source-independent lemma.

**Increasing-curvature tilt lemma.** If an even positive density is
`exp(-V)` with `V''` nondecreasing on the positive half-line, then every
positive exponential tilt has nonpositive third central moment.

For the Riemann theta density, proving

`V'''(u)>=0`, `u>0`,

would therefore prove `K'''(y)<=0` for every `y>0`, the monotonicity of
`a(y)/y`, and all two-height imaginary-axis Xi Pick inequalities.  The dense
source sweep above supports exactly this remaining pointwise inequality.

This is a genuine positivity mechanism: the functional equation supplies an
even base law, and increasing theta curvature makes two-copy relative
fluctuations contract as their midpoint moves into the tilted tail.

## Two-zone proof program for theta increasing curvature

Write the positive-half-line theta kernel as

`Phi=sum_(n>=1) phi_n`,

where

`phi_n(u)
=2 pi n^2 exp(5u/2)
 [2 pi n^2 exp(2u)-3]
 exp[-pi n^2 exp(2u)]`.

For the dominant term put

`a=2 pi exp(2u)`, `h=a-3`, `V_1=-log phi_1`.

Direct differentiation gives

`V_1'''(u)
=4a[1-6/h^2-36/h^3]`.

Its sign is the sign of

`h^3-6h-36`.

The unique positive root is approximately

`h_*=3.9020426740606684`,

corresponding to

`u_*=0.046970170550847214`.

Thus the leading potential already has increasing curvature for `u>=u_*`.
The relative theta tail

`r(u)=sum_(n>=2)phi_n(u)/phi_1(u)`

is approximately `8.05e-4` at `u_*`, `2.37e-4` at `u=0.1`, and
`1.39e-10` at `u=0.5` in direct source evaluation.  Its exponential factors
make it rapidly decreasing.  The outer-zone task is therefore to prove a
derivative-aware perturbation bound

`|(log(1+r))'''| <= V_1'''`.

The bound must be sharp at `u_*`, where `V_1'''=0`; in practice one should
start the perturbative region slightly to the right and let the fixed-point
certificate overlap it.

On the inner interval `0<=u<=u_*+delta`, modular symmetry makes `Phi` and
`V=-log Phi` even, so `V'''(0)=0`.  The diagnostic slope is positive.  It is
enough to certify

`V''''(u)>0`

on this short interval.  All theta summands and their first four derivatives
have explicit exponential-polynomial forms, while the `n>=2` tail at zero is
only about `2.18e-3` of the leading value.  A Taylor remainder bound at the
modular fixed point is therefore finite and source-explicit.

This gives a concrete proof architecture:

1. exact modular-fixed-point derivatives and a fourth-derivative lower bound
   on a short interval;
2. an overlapping dominant-summand inequality beyond `u_*`; and
3. the increasing-curvature tilt lemma to obtain all two-height Pick minors.

## The dominant `n=2` tail correction has the favorable sign

The first tail ratio can be handled globally.  Put `t=exp(2u)`,

`q(u)=phi_2(u)/phi_1(u)
=4 [8 pi t-3]/[2 pi t-3] exp(-3 pi t)`,

and `F(u)=log(1+q(u))`.  Write

`A=-(log q)'`, `B=-(log q)''`, `C=-(log q)'''`,

and `p=q/(1+q)`.  Direct differentiation gives

`F'''
=-p{C+(1-p)A[(1-2p)A^2-3B]}`.

All three quantities `A,B,C` are positive.  Indeed, with

`h_1=2 pi t-3`, `h_2=8 pi t-3`,

one has

`A=6 pi t+6(1/h_1-1/h_2)>6 pi t`.

Also

`B=12 pi t+12[(h_2+3)/h_2^2-(h_1+3)/h_1^2]`.

Since `h_1>3` and `h_2>21`, this is positive and satisfies

`B<12 pi t+2/3`.

For the third derivative, the non-linear part is

`24(h+3)(h+6)/h^3`,

which decreases with `h`; subtracting its values at `h_2>h_1` reinforces the
negative dominant term in `(log q)'''`.  Hence `C>0`.

The elementary bounds

`h_2/h_1<7`, `pi t>3`, `exp(9)>84`

give

`q<28 exp(-9)<1/3`,

so `p<1/4` and `1-2p>1/2`.  Finally,

`A^2>36 pi^2 t^2>6(12 pi t+2/3)>6B`.

It follows that

`(1-2p)A^2-3B>0`

and therefore

`F'''(u)<0` for every `u>=0`.

Thus adding the `n=2` theta summand to the dominant term always contributes

`-F'''(u)>0`

to the full potential curvature `V'''`.  This explains the modular repair of
the negative `V_1'''` near zero rather than treating it as accidental
cancellation.

The unresolved tail now begins at `n=3`.  At `u=0` its total value relative to
the `n=2` ratio is about `8.21e-7`, and this ratio decays with the additional
factor `exp(-5 pi exp(2u))`.  A derivative-weighted bound on this remainder is
the last outer-zone estimate.

## Full-tail logarithmic third derivative is negative

The remainder can be bounded uniformly.  For `n>=2`, put

`q_n=phi_n/phi_1`,

and define its positive logarithmic derivative magnitudes

`A_n=-(log q_n)'`, `B_n=-(log q_n)''`, `C_n=-(log q_n)'''`.

For `n>=3`, comparison with `q_2` gives

`epsilon_n=q_n/q_2
< [n^4/14] exp[-3(n^2-4)t]`, `t=exp(2u)>=1`.

The derivative magnitudes admit the elementary upper bounds

`A_n < (44/7)(n^2-1)t+2`,

`B_n < (88/7)(n^2-1)t+16`,

while `C_n` has the same linear-in-`(n^2-1)t` growth up to a fixed constant.
Every product of `epsilon_n` with a derivative polynomial of degree at most
three is decreasing in `t>=1`; its worst value is therefore at `t=1`.

Termwise comparison, with the `n=3` term separated and the rest bounded by a
geometric tail, gives

`sum_(n>=3) epsilon_n < 1.8e-6`,

`sum_(n>=3) epsilon_n A_n B_n < 0.011`,

`sum_(n>=3) epsilon_n A_n^3 < 0.253`,

and

`sum_(n>=3) epsilon_n B_n < 2.1e-4`.

Now set

`r=sum_(n>=2)q_n`, `L=log r`,

and let the weights be `w_n=q_n/r`.  Then

`A=-L'=E_w[A_n]`,

`B=-L''=E_w[B_n]-Var_w(A_n)`,

`C=-L'''=E_w[C_n]-3 Cov_w(A_n,B_n)+kappa_(3,w)(A_n)`.

Using the bounds above, the covariance and third-cumulant perturbations from
the `n=2` atom have total absolute size less than `2.16`.  On the other hand,

`B_2>28`, `C_2>24 pi t>72`.

Consequently

`B>0`, `C>0`, `A^2>6B`.

The full ratio also satisfies `r<1/3`.  Applying the same identity as for the
single `q_2` ratio, now with `p=r/(1+r)`, yields

`[log(1+r)]'''<0` for every `u>=0`.

Therefore

`V'''=V_1'''-[log(1+r)]''' > V_1'''`.

Since `V_1'''>=0` for `u>=u_*`, this proves the full source inequality

`V'''(u)>0`, `u>=0.046970170550847214`.

The increasing-curvature problem is now confined rigorously to the modular
fixed-point interval `0<u<u_*`.  The dense diagnostic indicates no interior
sign change there; the remaining task is the fourth-derivative/Taylor
certificate described above.

## The inner interval has a large fourth-derivative margin

The exact summand calculation can be extended one derivative further.  If
`a=2 pi n^2 exp(2u)`, `h=a-3`, and `ell_n=log phi_n`, then

`ell_n''''=-48a/h^2+288a^2/h^3-288a^3/h^4-8a`.

Combining these with the fourth complete Bell polynomial for `Phi''''/Phi`
and the fourth logarithmic derivative gives a direct source evaluation of
`V''''`.  A 10,001-point sweep on the entire unresolved interval found

`min_[0,u_*] V'''' = 141.3552319365...`,

with the minimum at the right endpoint; at the modular fixed point,

`V''''(0)=143.0149377615...`.

The diagnostic has now been replaced by a directed-rounding certificate.
Partitioning `[0,u_*]` into 4,096 cells, enclosing the first 50 theta summands
and their first four derivatives at 70 decimal digits, and evaluating the
logarithmic Bell combination interval-wise gives

`V''''(u) >= 140.3261324093189301276413787`.

The worst enclosure is the final cell.  The omitted derivative tails are each
enclosed by `10^-1000`.  This allowance is extremely conservative: on this
interval `t=exp(2u)<1.1`; for `n>=51`, a direct Bell-polynomial majorant is
bounded by `10^15 n^20 exp(-3n^2)`, whose first term is below `10^-3300`, and
successive terms decrease by more than `exp(-300)`.  The directed operations
include the stated enclosure of pi and downward/upward rounding of arithmetic
and exponentials.

It follows from evenness, `V'''(0)=0`, and the certified bound that

`V'''(u)>0` for `0<u<=u_*`.

Together with the outer theorem, this proves the increasing-curvature
condition on the whole half-line.  By the tilt lemma,

`K'''(y)<=0` for all `y>=0`,

and therefore every two-height imaginary-axis Pick minor is positive
semidefinite.  This remains only a rank-two shadow of the full
self-adjointness problem.

## Smallest falsifiers

Any of the following kills the two-height Pick route:

1. one `y>0` with `y Var_y(u)>E_y(u)`;
2. one `x>0` with `R_Xi'(x)>0`; or
3. one pair `0<y_1<y_2` with `Delta_2(y_1,y_2)<0`.

The third-cumulant sufficient condition may fail without falsifying the target
monotonicity, so it must be reported separately from the exact equivalence.

## Consequence for self-adjointness

The scalar monotonicity establishes the first coupled positive minor of the
source-derived Weyl kernel for every imaginary-axis pair.  It does not prove
self-adjointness, but it is the first analytic advance beyond automatic
one-point positivity and identifies tilted-theta variance control as a viable
positivity mechanism.

## Scope

The theta-potential argument proves the scalar monotonicity and the associated
two-height Pick positivity.  It does not prove positivity of higher Pick
matrices, a self-adjoint realization, RH, or the physical coefficient--Betti
pushforward.
