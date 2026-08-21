# The three-height Xi gate is a correlation-triangle obstruction

This is Gate A of
`deutschian-prime-spectral-explanation-charter.md`: the first separated
finite-rank falsifier for the proposed prime--spectral explanation.

## Exact normalization

Let `a(y)=B'(y)/B(y)` and `f(y)=a(y)/y`.  The imaginary-axis Pick matrix is

`P_ij=(a_i+a_j)/(y_i+y_j)=(y_i f_i+y_j f_j)/(y_i+y_j)`,

with diagonal `P_ii=f_i`.  Define

`rho_ij=P_ij/sqrt(f_i f_j)`.

The proved two-height theorem says exactly `0<rho_ij<=1` for every pair.
For three distinct heights, direct expansion gives

`det(P)/(f_1 f_2 f_3)
 =1+2 rho_12 rho_13 rho_23-rho_12^2-rho_13^2-rho_23^2`.

Thus rank three contains genuinely new information.  Pairwise positivity does
not imply it: three numbers can each lie in `[0,1]` and still fail this
correlation-determinant inequality.

Equivalently, writing `rho_ij=cos(theta_ij)`, the determinant is nonnegative
exactly when the three angles can be side lengths of a spherical correlation
triangle.  The next source theorem must control the compatibility of three
tilts, not merely the monotonicity of one scalar function.

## Lyapunov--Cauchy form

Let `C_ij=1/(y_i+y_j)` and `D=diag(a_i)`.  Then

`P=DC+CD`.

The Cauchy matrix `C` is positive, but a Lyapunov sum with a positive diagonal
matrix need not be positive in dimensions at least three.  Consequently
positivity cannot be inferred formally from positivity of the theta density,
nor from the two-height theorem.  A source-derived Gram factorization or a
three-tilt inequality is required.

## Hostile diagnostic

A direct theta-source sweep used the heights

`0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100`

and tested all 286 triples.  No determinant was negative beyond `10^-10` in
diagonal-product normalization.  The only negative floating values were of
order `10^-17`, for nearly coalescing small heights where the determinant
vanishes to high order and double precision loses the sign.  This is evidence
for rank-three positivity, not a proof.

## Smallest falsifier and next attack

The smallest falsifier is a triple `0<y_1<y_2<y_3` for which

`1+2 rho_12 rho_13 rho_23
 <rho_12^2+rho_13^2+rho_23^2`.

The sharp next attack is the confluent limit `y_1,y_2,y_3 -> y`.  Dividing by
the squared Vandermonde produces a local differential inequality involving
derivatives of `a`.  If that inequality fails, arbitrarily close triples
falsify the construction.  If it is positive, it supplies the local anchor
for an interval proof over ordered triples.

## Exact confluent factorization

Put `d=2y`.  The confluent jet matrix is the coefficient matrix of

`[a(y+h)+a(y+k)]/[2y+h+k]`

in `h^i k^j`, `0<=i,j<=2`.  Its entries are

`J_00=2a/d`,

`J_01=-2a/d^2+a'/d`,

`J_02=2a/d^3-a'/d^2+a''/(2d)`,

`J_11=4a/d^3-2a'/d^2`,

`J_12=-6a/d^4+3a'/d^3-a''/(2d^2)`,

`J_22=12a/d^5-6a'/d^4+a''/d^3`.

No derivatives beyond `a''` survive.  Clearing the positive factor `d^-9`
and defining

`q=a-y a'`, `r=-y^2 a''`,

gives the complete factorization

`d^9 det(J)=8(q+r)[q(3a-2q)-a r]`.

The rank-two theorem gives `q>=0`.  The proved theta-curvature theorem gives
`r>=0`.  Hence the local rank-three condition reduces exactly to

`a r <= q(3a-2q)`.

Equivalently,

`-y^2 a'' <= [(a-y a')/a][a+2y a']`.

This is the first quantitative curvature gate.  Rank two controls the sign of
the variance-decay reserve `q`; confluent rank three controls how rapidly that
reserve itself may be consumed by the negative third cumulant.

Direct theta evaluation makes the cleared determinant positive from moderate
heights onward.  Near `y=0` it vanishes to high order, so double precision
cannot decide the sign.  The next rigorous attack is therefore a modular
Taylor expansion of `q(3a-2q)-ar` at zero, followed by an interval enclosure
away from zero.

## Modular fixed-point leading coefficient is positive

Write the even cumulant expansion

`a(y)=kappa_2 y+kappa_4 y^3/6+kappa_6 y^5/120+O(y^7)`.

Substitution into the local gate shows cancellation through order four and
gives

`q(3a-2q)-ar
 =[kappa_2 kappa_6/15-2 kappa_4^2/9]y^6+O(y^8)`.

Thus the first fixed-point obstruction is the sixth-cumulant inequality

`3 kappa_2 kappa_6-10 kappa_4^2>=0`.

Direct theta moments give

`kappa_2=0.046209986230838...`,

`kappa_4=-0.000446071191423270...`,

`kappa_6=0.0000346017435362564...`,

and therefore

`3 kappa_2 kappa_6-10 kappa_4^2
 =2.80704319894... 10^-6>0`.

The leading coefficient of the local gate is

`6.23787377543... 10^-8`.

This is diagnostic until the three fixed-point moments receive directed
enclosures, but it shows that the confluent rank-three gate opens rather than
fails at the modular point.  The remaining hostile region is at positive,
noncoincident height.

## Logistic form of the confluent gate

The two defect variables are not independent:

`q'=d/dy(a-y a')=-y a''`,

so `r=y q'`.  Put

`p=q/a=1-y a'/a`.

Since `a>0` and the rank-two theorem gives `0<=p<=1`, the confluent
rank-three inequality is equivalent to

`y p' <= p(2-p)`.

Equivalently,

`y |-> p(y)/[(2-p(y))y^2]`

is nonincreasing.  Thus the third coupled gate is another scalar monotonicity
law: the normalized rank-two positivity reserve may grow at most logistically
with logarithmic height.

This form explains the high-order cancellation at zero.  Since
`p(y)=O(y^2)`, the leading relation is the saturated Euler law `y p'=2p`;
the sixth-cumulant inequality decides the first correction.

A 121-point logarithmic sweep on `0.1<=y<=100` found the unnormalized margin

`S=q(3a-2q)-ar`

positive at every point.  It grows from approximately `6.24e-14` at `y=0.1`
to `1.52` at `y=100`.  The normalized quantity `S/y^6` decays at large
height, as expected from saddle scaling, but this does not threaten the raw
determinant sign.

The logistic reduction is the preferred analytic target.  It replaces a
three-point determinant by a one-variable differential inequality and makes
the exact local falsifier `y p'>p(2-p)`.

## Source-statistical and propagation forms

Under the positive theta tilt, write

`m=E_y[U]=a`, `v=Var_y(U)=a'`, `c_3=kappa_3,y(U)=a''`.

Then the local rank-three margin is exactly

`S=m^2+y m v-2y^2 v^2+m y^2 c_3`.

This involves no zeros or analytic continuation.  It is a three-cumulant
inequality for a one-parameter exponential family.

Differentiating, with `c_4=a'''` the tilted fourth cumulant, gives the compact
propagation identity

`S'=3q(v+y c_3)+m y^2 c_4`, `q=m-yv`.

Therefore a sufficient global strategy is:

1. certify the positive sixth-order germ at `y=0`;
2. prove `3q(v+y c_3)+m y^2 c_4>=0` until `c_4` changes sign; and
3. beyond that sign change, use `c_4>=0` together with `v+y c_3>=0`.

The diagnostic supports exactly this architecture.  At heights
`0.1,0.3,1,3,10,30,100`, the derivative `S'` is positive.  The fourth
cumulant is negative at least through `y=3` and positive by `y=10`; the first
term compensates it in the inner zone.  The quantity `v+y c_3=(yv)'` is
positive at every sampled height.

This identifies the next two source lemmas sharply:

`(yv)'>=0`,

and, while `c_4<0`,

`-m y^2 c_4 <=3q(yv)'`.

Either violated inequality is a smaller falsifier than a full three-height
determinant.

The sign transition is numerically sharp:

`c_4(y)=0` at `y=7.23535828446...`.

On a logarithmic sweep from `10^-3` to `10^3`, `(yv)'` remained positive.
Its smallest sampled value was `1.75e-6` at the largest height, consistent
with decay toward zero from above.  The margin derivative `S'` was positive
whenever it was larger than the cancellation floor; the apparent signs below
`y=0.01` are unresolved by double precision because `S'=O(y^5)`.

The two-zone conjecture can now be made precise:

1. `c_4<0` on `(0,7.235358...)` and the compensation inequality holds there;
2. `c_4>=0` afterwards; and
3. `(yv)'>0` on the whole positive axis.

Only the first sign change is currently diagnostic.  A proof must exclude
later recrossings rather than inferring them from the sweep.

## The fourth cumulant is rigorously positive beyond height 12.5

Let `s=y+1/2`.  From the completed-zeta formula,

`c_4=K''''(y)
 =-6/s^4-6/(s-1)^4+(1/16)psi_3(s/2)+(log zeta)''''(s)`.

The polygamma series gives

`(1/16)psi_3(s/2)=6 sum_(n>=0)(s+2n)^-4`.

Its `n=0` term cancels `-6/s^4`.  The prime-power expansion gives

`(log zeta)''''(s)
 =sum_(p,k) k^3(log p)^4 p^(-ks)>0`.

Finally,

`6 sum_(n>=1)(s+2n)^-4
 >=6 integral_1^infinity (s+2x)^-4 dx
 =1/(s+2)^3`.

Therefore

`c_4>1/(s+2)^3-6/(s-1)^4`.

The right side is positive for every `s>=13`, because

`(s-1)^4>6(s+2)^3`.

Hence

`c_4(y)>0` for every `y>=12.5`.

This rigorously excludes all later fourth-cumulant recrossings in the outer
zone.  The diagnostic zero near `7.23536` now leaves only the compact interval
`7.23536<=y<=12.5` to certify before the positive-fourth-cumulant half of the
propagation argument is complete.

## Finite prime--gamma retention shrinks the bridge to 0.0047

The coarse `12.5` threshold throws away almost all positive terms.  Retain the
gamma summands `1<=n<=20`, bound the remaining convex tail by the trapezoidal
lower estimate

`sum_(n>=21)(s+2n)^-4
 >= integral_21^infinity (s+2x)^-4 dx
   +(1/2)(s+42)^-4`,

and retain the positive prime-power terms `m<=20` in

`(log zeta)''''(s)=sum_(m>=2)Lambda(m)(log m)^3 m^-s`.

At `s=7.74` the gamma-minus-pole lower bound is

`-0.00144716273477...`,

while the retained prime-power sum is

`0.00144737639772...`.

Their difference is `2.1366e-7>0`.  Each omitted term is positive.  A
70-decimal directed-rounding certificate with adaptive subdivision evaluates
the explicit lower bound on all of `7.74<=s<=13`.  Its certified lower endpoint
is

`1.10908203429... 10^-9>0`.

The earlier coarse theorem takes over at `s=13`.  Therefore the rigorous outer
threshold improves to

`c_4(y)>0` for `y>=7.24`.

Only the interval from the observed zero `7.235358...` to `7.24` remains.
Direct fifth-cumulant evaluation gives

`c_5(y)=c_4'(y) approximately 5.0e-5`

throughout that window.  The directed enclosure is now complete.  Retaining
100 gamma terms and all prime powers through 100, with explicit all-integer
integral bounds for the omitted Dirichlet tails, gives

`c_5(y)>4.99548771767... 10^-5`

for every `7.235<=y<=7.24`.  The same enclosure proves

`c_4(7.235)<-1.63859443130... 10^-8`,

while the outer certificate proves `c_4(7.24)>0`.  Hence `c_4` has exactly one
zero in `(7.235,7.24)`, is negative immediately before it, and is positive at
every later height.  The fourth-cumulant sign-transition component of the
rank-three propagation program is closed.

## Variance elasticity is positive in the outer zone

The completed-zeta expansion also gives an elementary lower bound for

`(yv)'=v+y c_3`.

With `s=y+1/2`, cancel the `n=0` polygamma term and write the remaining gamma
sum as

`sum_(n>=1)[(s+2n)^-2-(2s-1)(s+2n)^-3]`.

Lower-bound the square sum by its integral and upper-bound the cube sum by its
first term plus integral.  For the prime contribution, use
`Lambda(m)<=log m` and dominate the decreasing all-integer series by its
`m=2` term plus integral.  This gives the explicit lower function

`s/(s-1)^3 +1/[2(s+2)]
 -(2s-1){1/(s+2)^3+1/[4(s+2)^2]}
 -(s-1/2){(log 2)^3 2^-s
   +integral_2^infinity (log x)^3 x^-s dx}`.

A 70-decimal directed certificate on `8<=s<=100` gives the lower endpoint

`3.34312277465... 10^-5>0`.

For `s>=100`, clearing denominators gives a rational gamma margin greater than
`1/(5s^2)`.  The elementary bounds `log x<=x` and monotonicity give the prime
majorant less than `7*2^-s`, which is smaller than `1/(5s^2)` there and decays
faster thereafter.  Hence

`(yv)'>0` for every `y>=7.5`.

Since the unique fourth-cumulant crossing occurs below `7.24`, both terms in

`S'=3q(yv)'+m y^2 c_4`

are positive for every `y>=7.5`.  Thus the confluent rank-three margin is
strictly increasing throughout the whole outer zone.  The remaining
propagation problem is compact: `0<y<7.5`.

## The compact compensation margin is positive after removing its forced zero

Near the modular point, the propagation margin has the expansion

`S'(y)=[2 kappa_2 kappa_6/5-4 kappa_4^2/3]y^5+O(y^7)`.

The leading coefficient is approximately

`3.742724265... 10^-7>0`.

Thus direct evaluation of `S'` is ill-conditioned near zero, while `S'/y^5`
is regular.  A 181-point source sweep on `0.01<=y<=7.22` found

`1.4684e-7 <= S'(y)/y^5 <=3.7423e-7`.

The smallest compensation *ratio* occurs at the left endpoint and exceeds
one by only `1.82e-6`, reflecting the forced leading cancellation.  The
normalized additive margin, however, remains robust throughout the interval.

This dictates a two-chart certificate:

1. enclose the cumulant Taylor series of `S'/y^5` on a short modular interval;
2. interval-evaluate the unnormalized source moments on an overlapping compact
   interval bounded away from zero.

If both charts retain a positive lower endpoint, then `S'>0` on `(0,7.5)`.
Together with the outer theorem, this proves the confluent rank-three Pick
condition at every height.  It still does not prove the determinant for three
separated heights.

## The normalized modular reserve has a Stieltjes-like jet

The fixed-point cumulants through order 16 alternate:

`kappa_2>0, kappa_4<0, ..., kappa_16<0`.

Propagating them through the exact formula gives

`S'(y)/y^5
 =3.74272426526e-7
 -7.64929737847e-9 y^2
 +9.89478169841e-11 y^4
 -1.02324827724e-12 y^6
 +9.22133522654e-15 y^8
 -7.56405993373e-17 y^10+O(y^12)`.

All computed coefficients alternate, with rapidly decreasing magnitude.  The
finite series reproduces the direct source value at `y=1` to the displayed
precision.  This initially motivates a stronger compact conjecture:

`x |-> S'(sqrt(x))/x^(5/2)`

is completely monotone, or at least remains positive, on the modular chart.
Complete monotonicity would turn the Taylor certificate into a positive
measure problem and would be structurally stronger than the rank-three sign
alone.

## Retraction: the jet is not Stieltjes; complete monotonicity survives

Put

`m_j=(-1)^j [x^j] S'(sqrt(x))/x^(5/2)`.

Although all computed `m_j` remain positive through the extended jet, already

`m_0 m_2-m_1^2=-2.14783108222... 10^-17<0`.

The magnitude is about 58 percent of `m_0 m_2`, so this is not a
rounding-level sign.  It falsifies a Stieltjes-resolvent representation, for
which the coefficients themselves would be moments.

It does **not** falsify complete monotonicity.  A Laplace representation uses
the derivative moments `M_j=j! m_j`.  Their first Hankel determinant is

`M_0 M_2-M_1^2=1.55551287398... 10^-17>0`,

and the factorial-weighted Hankel tests remain positive through the computed
`4 by 4` jets.  Thus the Stieltjes strengthening is retracted, while the
broader complete-monotonicity conjecture survives its first correct hostile
tests.  The distinction is essential: coefficient moments and derivative
moments differ by factorial weights.

The modular computation has now been extended through cumulant order 32,
giving 14 alternating coefficients of `S'/y^5`.  Both ordinary and shifted
factorial-weighted Hankel determinants are positive through size `4 by 4`.
This remains diagnostic because the high cumulants were obtained in double
precision, but their values are stable under truncation of the computation.

More importantly for the scalar theorem, the order-32 alternating polynomial
remains positive through `y=7.5`.  At `y=7.2` it gives

`1.47507284e-7`,

while direct theta integration gives approximately `1.47508830e-7`.  Their
difference is about `1.6e-12`, five orders of magnitude below the positivity
margin.  At `y=7.5` the polynomial value is `1.37655e-7`, and its final terms
still decrease geometrically in magnitude.

Thus one modular chart may cover the entire remaining compact interval.  A
rigorous Cauchy or source-moment bound on the Taylor tail after order 32 would
prove `S'>0` on `(0,7.5)` without a second interval-integration chart.

The numerically stable formulation expands the positive function itself,

`B(y)/B(0)=sum_(n>=0) E_0[U^(2n)] y^(2n)/(2n)!`,

then obtains `a=B'/B` by formal series division.  This avoids subtracting
large raw moments to form high cumulants.  Carrying the positive `B` series to
order `y^80` gives at the hostile endpoint

`S'(7.5)/7.5^5=1.37659638783... 10^-7`.

The final retained term has magnitude `6.50e-24`, and its ratio to the
preceding term is `0.3041`.  At `y=7.2` the corresponding values are
`1.47508829622e-7`, `2.92e-25`, and ratio `0.2802`.

Thus the positive-series route supplies about sixteen orders of numerical
separation between the desired sign and the observed truncation scale.  The
remaining rigor task is to enclose the positive source moments and propagate
their tail through reciprocal-series division; high-order cumulants are no
longer needed.

Composite-Simpson refinements with 3,000, 6,000, and 12,000 panels were run
through the *entire* order-80 computation.  At `y=7.5`, the resulting values
of `S'/y^5` agree within approximately `1.3e-20`; at `y=7.2` the spread is of
the same order.  This includes the effect of quadrature errors in every source
moment and their nonlinear propagation through `B'/B`.

The observed quadrature scale is therefore thirteen orders below the
`1.38e-7` endpoint margin, while the observed Taylor tail is another three
orders smaller.  A rigorous certificate need not reproduce this precision:
even a deliberately coarse total enclosure error below `10^-8` closes the
compact sign.  The next implementation target is consequently a bounded
fourth-derivative Simpson remainder for the normalized positive moment
integrands, followed by interval power-series division.

The order-80 polynomial is also strictly decreasing in `x=y^2` on
`0<=x<=56.25`.  Across 10,001 points its derivative lies between

`-7.65e-9` and `-2.14e-9`,

and these bounds are stable under all three Simpson refinements.  Therefore
the hostile polynomial value is the single endpoint `y=7.5`; no sampled
interior dip is hidden by the endpoint comparison.  In the final interval
certificate it is enough to preserve the negative derivative enclosure and
the positive endpoint enclosure, then add the analytic Taylor-tail allowance.

An all-moment fourth-derivative audit now covers every normalized integrand

`Phi(u)u^(2n)/(2n)!`, `0<=n<=40`.

The worst sampled derivative is the zeroth-moment value `812.163...` at
`u=0`, giving the 12,000-panel Simpson allowance

`1.6921e-12`.

The allowances then collapse rapidly: below `7.4e-22` by moment order 10,
below `3.7e-65` by order 40, and below `5.6e-134` by order 80.  The omitted
source tail beyond `u=6` is super-exponentially smaller because its first
theta factor contains `exp[-pi exp(12)]`.

These maxima are still grid diagnostics rather than directed enclosures.
However, the proof budget permits a fourth-derivative majorant almost four
orders larger than the observed worst value.  A coarse analytic/interval
majorant is therefore sufficient; sharp optimization of each moment is
unnecessary.

The coarse directed certificate is now complete.  Using 1,024 interval cells,
70-decimal outward rounding, the first ten theta summands, and an explicit
Gaussian allowance for `n>=11`, it proves uniformly for every normalized
moment through order 80 that

`|d^4/du^4 [Phi(u)u^(2n)/(2n)!]| <952.009`

on `0<=u<=6`.  Consequently the 12,000-panel composite-Simpson remainder is

`<1.984e-12`.

This closes the quadrature-remainder component of the compact certificate.
The remaining step is interval propagation of the resulting moment
enclosures through the positive `B` series, reciprocal-series division, and
the endpoint/derivative tests above.

## Naive reciprocal-series intervals fail by dependency blow-up

The first propagation attempt assigned the certified order-specific moment
intervals coefficientwise and performed ordinary interval division of the
formal series `B_x/B`.  It does not certify the sign: at `y=7.5` the enclosure
inflates to approximately `[-227.7,227.7]` around a true value of order
`10^-7`.

This is not a mathematical near-failure.  Recursive interval division treats
every occurrence of the same source moments as independent and repeatedly
loses their correlations.  Refining scalar quadrature errors cannot repair
that structural dependency problem.

The certificate must instead preserve the common source jet.  Two viable
routes remain:

1. directly enclose `B,B',B'',B''',B''''` on height cells and evaluate `S'`
   as one rational expression; or
2. use affine/Taylor-model arithmetic for the moment series so each moment
   error symbol remains correlated through the reciprocal.

The direct `B`-jet route is smaller and is now preferred.  The failed naive
checker is retained as a falsifier of coefficientwise interval propagation,
not as evidence against rank-three positivity.

Direct `B`-jet evaluation at a fixed height does preserve enough structure.
At the hostile endpoint, including all certified moment errors, it gives

`0.00326598833430 < S'(7.5) <0.00326746717836`.

Thus moment uncertainty is harmless.  However, ordinary interval evaluation
on a height cell of width about `0.0127` expands to roughly `[-0.097,0.106]`:
the remaining dependency is the repeated occurrence of the height variable,
not the source moments.

Uniform subdivision would eventually work but is wasteful.  The appropriate
final representation is a first-order Taylor model in height on each cell:
evaluate the correlated `B` jet at the midpoint, retain the linear height
term, and bound only the quadratic remainder.  The successful fixed-height
enclosure shows that such a Taylor model has ample margin; plain interval
height powers do not.

The first implementation of that idea used a certified midpoint value and a
plain-interval bound on `S''` over each cell.  It was stopped after sustained
deep subdivision: the `S''` interval itself repeats the height and source jet
often enough to recreate the dependency problem.  The exact derivative
identity is correct, but first-order midpoint arithmetic with an ordinary
interval remainder is computationally ineffective.

The next representation must carry the height symbol affinely through the
`B` jet, or retain a second-order Taylor polynomial before intervalizing the
remainder.  This is now the only unresolved numerical-analysis issue in the
compact confluent theorem; fixed-height signs and quadrature errors are both
certified.

## Genuine Taylor cells certify the compact interval away from zero

Retaining the midpoint slope fixes the preceding failure.  Use

`S'(y_0+h)=S'(y_0)+h S''(y_0)+(h^2/2)S'''(xi)`.

The exact `S'''` expression requires tilted cumulants only through order six,
all evaluated from the same certified positive `B` jet.  An adaptive run with
64 initial cells terminates after 144 certified cells and proves

`S'(y)>0` for `0.1<=y<=7.5`.

Its weakest lower endpoint is

`9.1875e-13>0`,

on a cell near `y=0.12`.  Thus the correlation-preserving first-order Taylor
model is sufficient; the earlier stopped calculation had in fact retained no
midpoint slope and was effectively zeroth order.

On the remaining modular interval, interval evaluation of the normalized
order-80 polynomial gives

`3.74194751040e-7
 <=S'(y)/y^5
 <=3.74273607467e-7`, `0<=y<=0.1`.

The finite compact calculation is therefore certified everywhere.  Only the
omitted analytic Taylor tail on `|y|<=0.1` remains to be written as an explicit
Cauchy bound.  Taking the comparison circle `|y|=1`, positivity of the `B`
coefficients gives `|B(y)-B(0)|<=B(1)-B(0)` and hence a zero-free denominator
once `B(1)<2B(0)` is enclosed.  A coarse bound for the normalized rational jet
on that circle, multiplied by `0.01^N/(1-0.01)` at the retained degree, is
already many orders below the `3.74e-7` margin.

## The modular Cauchy tail closes the confluent theorem

The certified positive moment sums give

`B(1)/B(0)<1.024`, `B(2)/B(0)<1.097`.

The omitted positive tails after moment order 80 are below `10^-90` under the
same exponential source majorant.  For complex `|y|<=1`, positivity of the
coefficients gives

`|B(y)|>=B(0)-|B(y)-B(0)|>=2B(0)-B(1)>0.976 B(0)`.

Thus the logarithmic jet is analytic on that disk.  Moreover,

`|B^(j)(y)|<=integral Phi(u)u^j exp(u)du
 <=j! B(2)`.

Dividing by the lower bound for `|B|` gives the raw logarithmic-jet bounds
`|B^(j)/B|<1.13 j!`.  The cumulant recurrence then yields, for orders one
through four, the coarse bounds

`1.13, 3.537, 17.328, 117.501`.

Substitution into

`S'=3q(v+y c_3)+a y^2 c_4`

on `|y|=1` gives `|S'|<425`.  Since `S'/y^5` is even and removable at zero,
the corresponding analytic function of `x=y^2` has modulus below 425 on
`|x|=1`.  The interval polynomial retains degrees `0` through `38`, so on
`|x|<=0.01` its omitted tail is bounded by

`425 (0.01)^39/(1-0.01)<4.3e-76`.

This is negligible against the certified polynomial lower bound
`3.7419475e-7`.  Therefore `S'(y)>0` on `(0,0.1]`; the adaptive Taylor cells
prove it on `[0.1,7.5]`, and the completed-zeta outer theorem proves it on
`[7.5,infinity)`.

Since `S(0)=0`, it follows that `S(y)>0` for every `y>0`.  By the exact
confluent factorization, every three-height Pick determinant has a positive
confluent limit at every positive height.  This is the universal confluent
rank-three positivity theorem.  It does not yet prove positivity for three
separated heights.

## Logarithmic hyperbolic-secant geometry of separated heights

The nonlocal problem has a cleaner exact coordinate system.  Put

`x=log y`, `f(y)=a(y)/y`, `g(x)=-log f(exp x)`,

and `h(x)=x-g(x)=log a(exp x)`.

For `x_i<x_j`, write `Delta x=x_j-x_i` and `Delta h=h_j-h_i`.  Since `f`
decreases and `a` increases, the rank-two theorem is exactly

`0<Delta h<Delta x`.

The normalized Pick entry simplifies without approximation:

`rho_ij
 =[y_i f_i+y_j f_j]/[(y_i+y_j)sqrt(f_i f_j)]
 =cosh(Delta h/2)/cosh(Delta x/2)`.

Thus the separated rank-three problem is positivity of the kernel

`K_h(x,z)=cosh([h(x)-h(z)]/2)/cosh([x-z]/2)`.

Pairwise positivity says only that `h` contracts logarithmic distance.  The
confluent theorem controls its infinitesimal curvature.  Three separated
heights ask whether this nonlinear contraction preserves the hyperbolic-
secant correlation triangle globally.

For a linear contraction `h(x)=c x+d`, `0<=c<=1`, the kernel becomes the
translation-invariant model

`cosh(c(x-z)/2)/cosh((x-z)/2)`.

The Xi problem is a variable-slope deformation of this model.  The next
theorem should control variation of `h'`, rather than manipulate the raw
three-height determinant.  The smallest global falsifier remains one triple
for which

`1+2K_12 K_13 K_23<K_12^2+K_13^2+K_23^2`.

## Separated rank three is exactly an angle triangle inequality

Define the source angle

`theta(x,z)=arccos K_h(x,z)`.

Rank-two positivity ensures `0<=K_h<=1`, so this angle is real.  The standard
three-correlation identity gives

`1+2 cos A cos B cos C-cos^2 A-cos^2 B-cos^2 C
 =4 sin(s)sin(s-A)sin(s-B)sin(s-C)`,

where `s=(A+B+C)/2`.  Therefore the separated `3 by 3` determinant is
nonnegative exactly when its three source angles satisfy the triangle
inequalities.  For ordered `x_1<x_2<x_3`, the decisive inequality is

`theta(x_1,x_3)
 <=theta(x_1,x_2)+theta(x_2,x_3)`.

Universal separated rank-three positivity is thus equivalent to saying that
the Xi source angle is a metric on the logarithmic height line.  The
confluent theorem proves the corresponding infinitesimal triangle condition;
the remaining theorem is global subadditivity.

A logarithmic sweep used 61 heights from `exp(-6)` through `exp(6)` and tested
all 34,695 triples.  No determinant or angle slack was negative beyond
`10^-10`.  Apparent angle violations were at most `8.4e-12`, only where all
correlations equal one to many digits and `arccos` is ill-conditioned.  This
is a hostile diagnostic, not a proof.

The next analytic attack is one-dimensional: prove subadditivity of `theta`
under concatenation of logarithmic intervals, or find one ordered triple
where it fails.  This is sharper and more stable than direct determinant
expansion.

## Increasing angular differences are a sufficient global mechanism

For `x<z`, differentiation gives the exact right-end angular velocity

`partial_z theta(x,z)
 =K_h(x,z)/[2 sin theta(x,z)]
  {tanh([z-x]/2)-h'(z)tanh([h(z)-h(x)]/2)}`.

Suppose this velocity increases when the left endpoint moves right:

`partial_x partial_z theta(x,z)>=0`, `x<z`.

Then for `x<m<z`,

`theta(x,z)-theta(x,m)
 =integral_m^z partial_t theta(x,t)dt
 <=integral_m^z partial_t theta(m,t)dt
 =theta(m,z)`.

This is exactly the required triangle inequality.  Hence increasing angular
differences are a sufficient source theorem for universal separated
rank-three positivity.

The 61-height hostile grid tested this stronger velocity comparison on every
ordered triple.  No failure exceeded `10^-10`; the smallest values were
negative only at the `10^-11` scale in the small-height cancellation regime.
The next task is to reduce `partial_x partial_z theta>=0` to an explicit
inequality in the endpoint data `h,h'`, then compare it with the proved
contraction and confluent-curvature laws.

That endpoint reduction is exact.  Put

`X=z-x`, `H=h(z)-h(x)`, `p=h'(x)`, `q=h'(z)`,

`T_X=tanh(X/2)`, `T_H=tanh(H/2)`,

and `K=cosh(H/2)/cosh(X/2)`.  Direct differentiation and cancellation give

`partial_x partial_z theta>=0`

if and only if

`(T_X-p T_H)(T_X-q T_H)
 >=(1-K^2){sech^2(X/2)-p q sech^2(H/2)}`.

No second derivatives occur; all curvature information is compressed into
the two endpoint slopes and the secant slope `H/X`.  This inequality survived
all 1,830 pairs on the 61-height grid.  The smallest apparent negatives were
only `5.1e-23`, again in the modular cancellation regime.

## Concave contraction alone is insufficient

The Xi data suggest `0<q<=H/X<=p<1`, i.e. `h` is increasing, concave, and
contractive.  That qualitative package does **not** imply the endpoint
inequality.  A random admissible package

`X=0.3234312`, `H=0.0796768`,

`p=0.621579`, `q=0.114301`,

has endpoint margin approximately `-7.03e-4`.

Thus a general hyperbolic-contraction theorem at this level is false.  The Xi
proof must use a quantitative restriction on the drop `p-q` relative to the
interval length and secant slope.  The universal confluent rank-three theorem
is exactly the available local curvature control from which such a distortion
bound might be integrated.

## The confluent theorem supplies a hyperbolic slope-distortion bound

Let `w=h'`.  The normalized reserve from the confluent proof is `1-w`.  Its
logistic inequality becomes

`w'>=w^2-1`.

Therefore

`d/dx artanh(w)>=-1`,

and for an interval of length `X`, with endpoint slopes `p=w(x)` and
`q=w(z)`,

`artanh(q)>=artanh(p)-X`.

This endpoint bound alone is still insufficient: a random package satisfying
it but choosing an arbitrary secant slope gives a negative endpoint margin
about `-3.73e-4`.

If `w` is also nonincreasing, however, the differential bound constrains the
secant slope `r=H/X` much more sharply.  Put

`tau=artanh(p)-artanh(q)`,

`I=log[cosh(artanh p)/cosh(artanh q)]`.

The fastest admissible descent follows `w'=w^2-1`.  Moving this descent segment
to the beginning or end of the interval gives the necessary bounds

`[I+q(X-tau)]/X <=r<=[p(X-tau)+I]/X`.

Two million random packages satisfying

`0<=q<=r<=p<=1`, `tau<=X`,

and these sharp secant bounds produced no endpoint-inequality failure beyond
`3.1e-16`.  The earlier concavity counterexamples all violate this feasible
secant interval.

This suggests an abstract distortion theorem:

> If `0<=w<=1`, `w` is nonincreasing, and `w'>=w^2-1`, then the source angle
> has increasing differences and is a metric.

The differential lower bound is already the confluent rank-three theorem.
The new source obligation is monotonicity `h''=w'<=0`; after that, the
remaining work is a finite hyperbolic inequality over the explicit endpoint
region above.

## Concavity of the logarithmic response is one scalar cumulant inequality

Since

`w=h'=y a'/a`,

direct differentiation shows `h''<=0` exactly when

`r>=w q`,

where, as before,

`q=a-y a'`, `r=-y^2 a''`.

In tilted-theta statistics this is

`-y^2 kappa_3
 >=[y Var(U)/E(U)] [E(U)-y Var(U)]`.

The confluent theorem supplies the complementary upper bound

`r<=q(1+2w)`.

Thus logarithmic concavity would trap the curvature defect in the interval

`wq<=r<=q(1+2w)`.

A 181-point logarithmic sweep from `y=10^-3` to `10^3` found no failure.  At
the modular point,

`r-wq=[-2 kappa_4/3]y^3+O(y^5)
 =2.9738079... 10^-4 y^3+O(y^5)`.

The raw margin grows from `2.97e-13` at `y=10^-3` to order `10^-1` at large
height.  This source lemma is numerically much less delicate than the
confluent propagation inequality and is now the preferred next certificate.

The denominator can be removed completely.  Because `a>0`, put

`D=a(r-wq)=y^2[(a')^2-aa'']-yaa'`.

Then `D>=0` is equivalent to `h''<=0`.  This polynomial form admits the same
directed positive-`B` machinery as the confluent certificate, without an
interval division by `a`.  The modular series certificate gives

`1.37398272675e-5
 < D(y)/y^4
 <1.37419656173e-5`

for `0<=y<=0.1`.  On `0.1<=y<=7.5`, second-order Taylor propagation from
directed `B`-jet enclosures closes in 53 adaptive cells; its weakest certified
lower bound is

`D>9.43071783506e-10`.

Consequently `h''(log y)<0` is now rigorous for `0<y<=7.5`.  The remaining
source lemma is solely the completed-zeta tail `y>=7.5`.  In that chart the
exact target is

`y^2[(K'')^2-K'K''']-yK'K''>0`,

where `K(y)=log Xi(1/2+y)`.  The earlier outer signs `K''''>0` and
`(yK'')'>0` do not by themselves imply this inequality, so the tail requires
its own enclosure rather than a formal reuse of the confluent argument.

That outer bridge is now certified through `s=100`.  Use the completed-zeta
decomposition for `K'`, `K''`, and `K'''`; enclose the digamma and polygamma
terms by their convergent reciprocal sums plus integral tails, and retain all
prime powers through 100.  The omitted von Mangoldt tails are dominated by
the corresponding all-integer log-power integrals.  Directed adaptive
subdivision then gives

`D>1.24923918614e-3`

throughout `8<=s<=100`, equivalently `7.5<=y<=99.5`.  Combined with the
theta-source certificate, logarithmic concavity is therefore rigorous on
`0<y<=99.5`.  The only remaining portion is the coarse asymptotic half-line
`s>=100`; there `D` is numerically already greater than `0.208` and tends to
`1/4`, so a rational Stirling/Dirichlet majorant should close it without a
further compact bridge.

## The asymptotic half-line closes by three coarse bounds

For `s>=100`, put `y=s-1/2`, `a=K'`, `v=K''`, and `E=(yv)'=v+yc_3`.
The completed-zeta terms satisfy

`v>=2/(5s),       a<=log s,       E<=3/s^2`.

Here is a termwise derivation.  For the variance, discard the positive prime
series and use the first two integral terms of the trigamma sum:

`v >=1/(2s)+1/(2s^2)-1/s^2-1/(s-1)^2 >=2/(5s)`.

For `a`, the prime contribution is negative and the standard digamma bound
`psi(x)<log x-1/(2x)` makes `a<log s`.  Finally, in `E` every prime-power term
has factor `1-y log n`, hence is nonpositive because `y log 2>1`.  Apply the
enveloping Euler--Maclaurin bounds to the remaining trigamma/tetragamma
combination.  After cancellation of its `n=0` term against the `s`-pole and
expansion of the `(s-1)` pole, the upper remainder is geometric and gives

`E <=2/s^2+8/s^3 <3/s^2`.

Since

`D=y^2v^2-ayE`,

these estimates imply

`D >=(4/25)(1-1/(2s))^2-3 log(s)/s`.

At `s=100` the right side is

`0.0202488944203...>0`.

Its first term increases, while `log(s)/s` decreases for `s>e`; hence it stays
positive for every `s>=100`.  Together with the directed modular, compact,
and completed-zeta bridge certificates, this proves

> `h(x)=log a(e^x)` is strictly concave on the whole real line.

Equivalently, the Xi source satisfies `w'=h''<0` at every positive height.
The separated rank-three problem is therefore reduced completely to the
abstract hyperbolic endpoint inequality under

`0<=w<=1`, `w'<=0`, and `w'>=w^2-1`.

## Half-angle coordinates expose the remaining abstract obstruction

For an interval put

`alpha=(X+H)/2`, `beta=(X-H)/2`.

The source angle has the exact form

`tan^2(theta/2)=tanh(alpha/2)tanh(beta/2)`.

Both `alpha` and `beta` add under concatenation.  It is tempting to conclude
that the two-variable angle function is subadditive, but this is false.  A
hostile search finds margins below `-1.56`; even imposing nonnegative,
decreasing average slopes leaves margins below `-0.42`.  Those examples make
an abrupt slope transition and violate the differential constraint.

Writing `u=artanh w` turns the two source inequalities into the especially
simple control condition

`-1<=u'<=0`.

Under this condition a 200,000-path hostile test supports the sharp chord--
length comparison

`theta(x,z) <= (1/2) integral_x^z sech(u(t)) dt`.

The extremal flow `u'=-1` saturates its endpoint derivative.  This comparison
does not alone prove the triangle inequality—the corresponding upper bounds
on the two subinterval angles point in the wrong direction—but it identifies
the correct extremal control.  The remaining proof must compare the endpoint
angle derivatives for a whole interval and its terminal subinterval while
using `-1<=u'<=0`; equivalently, it must prove increasing differences inside
the sharp reachable set, rather than unrestricted subadditivity.

The first bang--bang reduction is not quite sufficient: a hostile scan shows
that the margin can attain its minimum at an interior secant.  It remains
positive, but checking only the two reachable boundary controls would miss
the actual minimizer.

There is nevertheless a decisive algebraic collapse.  Put

`T=tanh(X/2)`, `R=tanh(H/2)`.

If `M` denotes the increasing-differences margin, then direct expansion gives

`(1-R^2)M = N(R)`,

where

`N(R)=T^2(T^2+pq)-T(p+q)R
      +(1-2T^2-T^2pq)R^2+T(p+q)R^3`.

The transcendental dependence on the secant is therefore only the monotone
change of coordinate `H ->R`.  For fixed `X,p,q`, the minimum over the sharp
reachable interval occurs at its two endpoints or at a root of the quadratic

`N'(R)=-T(p+q)+2(1-2T^2-T^2pq)R+3T(p+q)R^2`.

The abstract theorem has consequently become a finite algebraic problem:
prove `N>=0` at two bang--bang endpoints and at any stationary root lying
between them.  No functional optimization remains.

Two further eliminations isolate the only difficult case.  At the full
endpoint `R=T`, the cubic factors exactly as

`N(T)=T^2(1-T^2)(1-p)(1-q)>=0`.

At an interior stationary point set

`B=1-2T^2-T^2pq`, `C=T^2(T^2+pq)`.

Using `N'(R)=0` to eliminate `T(p+q)` gives

`N(R)=C-B R^2(1+R^2)/(1-3R^2)`.

Thus the stationary inequality is linear in the remaining symmetric slope
parameter `pq`.  The apparent singularity at `R=1/sqrt(3)` is removable in
the original equations: the stationary equation there forces `B=0` in the
corresponding limit.  A million-package classification found 453,361
reachable stationary roots below `1/sqrt(3)` and only 562 above it, with no
negative value beyond floating cancellation.  The next algebraic step is to
insert the sharp reachable lower bound for `R` in the first regime and the
upper bound in the second; no cubic analysis remains.

A larger hostile classification reveals that this split is more complicated
than necessary.  Among three million admissible endpoint packages, every
stationary root with genuinely negative cubic value lay *above* the sharp
reachable interval; none lay below it.  Thus only the upper bang--bang bound
is active.  In rapidity variables it is

`H_max=p(X-tau)+log(cosh(u_p)/cosh(u_q))`,

where `p=tanh(u_p)`, `q=tanh(u_q)`, and `tau=u_p-u_q`.  It is attained by
holding `u=u_p` and placing the maximal descent `u'=-1` at the end of the
interval.  The proposed final algebraic lemma is therefore

> If the positive stationary root of `N` has `N<0`, then
> `R>tanh(H_max/2)`.

This is the exact contrapositive needed: the control-reachable interval never
enters the cubic's negative basin.  The lower bang--bang bound drops out.

The upper control itself has a useful exact degeneration.  Put

`L=X-tau>=0`, `I=log(cosh(u_p)/cosh(u_q))`.

Then its boundary variables are

`T=tanh((tau+L)/2)`, `R_max=tanh((I+pL)/2)`.

At `L=0` the control is pure extremal descent `u'=-1`, and direct hyperbolic
substitution gives the identity

`N(T,R_max,p,q)=0`.

Consequently the upper-bound problem is the one-variable deformation

`F_(p,q)(L)=N(tanh((tau+L)/2),tanh((I+pL)/2),p,q)>=0`.

For `L>0` this is exactly a constant-rapidity segment followed by the
extremal descent.  A three-million-package boundary sweep found no negative
value beyond roundoff.  Since `N'` has a unique positive root, the complete
algebraic proof splits cleanly:

1. if `N'(R_max)<=0`, monotonicity on `[0,R_max]` reduces everything to
   `F_(p,q)(L)>=0`;
2. if `N'(R_max)>0`, the stationary point lies inside the boundary and its
   eliminated value
   `C-BR^2(1+R^2)/(1-3R^2)` must be shown nonnegative.

This is now two one-variable extremal-control inequalities with the common
zero case `L=0`, rather than a free endpoint inequality.

The boundary deformation is not monotone, but its observed shape is rigid.
For each of 20,000 hostile endpoint pairs, sampled on 100 logarithmic holding
times, the derivative sign pattern was exactly `(+,-)`: `F` rises from its
exact zero at `L=0`, has one maximum, and falls back to zero as `L` tends to
infinity.  No other sign pattern occurred.  Thus the first one-variable lemma
can be sharpened to unimodality.  An analytic proof should differentiate in
the variables

`T=tanh((tau+L)/2)`, `R=tanh((I+pL)/2)`,

use `T'=(1-T^2)/2`, `R'=p(1-R^2)/2`, and show that the remaining factor of
`F'` has a unique zero.  The endpoint signs are fixed: the first variation at
`L=0` is positive for `q<p<1`, while the large-`L` variation is negative.

The differentiation can be made completely explicit.  With `S=p+q` and
`P=pq`,

`N_T=4T^3+2TP-2T(2+P)R^2-SR(1-R^2)`,

`N_R=-TS+2(1-2T^2-T^2P)R+3TSR^2`,

and therefore

`2F'=(1-T^2)N_T+p(1-R^2)N_R`.

Along the boundary orbit,

`artanh(R)-p artanh(T)=(I-p tau)/2`,

so

`dR/dT=p(1-R^2)/(1-T^2)`.

This turns unimodality into a phase-plane statement: the orbit crosses the
algebraic zero curve of `(1-T^2)N_T+p(1-R^2)N_R` exactly once.

The equality endpoint also rationalizes.  If

`a=tanh(u_p/2)`, `b=tanh(u_q/2)`,

then at `L=0`

`T=(a-b)/(1-ab)`,
`R=(a^2-b^2)/(1-a^2b^2)=T(a+b)/(1+ab)`.

Thus both `F(0)=0` and the positivity of its first variation reduce to
rational polynomial identities on `0<=b<=a<1`; no logarithms remain at the
initial boundary.  The remaining global step is uniqueness of the phase-plane
crossing.

There is a useful critical-point formulation.  Let

`G=(1-T^2)N_T+p(1-R^2)N_R=2F'`

and `D=(1-T^2) partial_T+p(1-R^2) partial_R`.  It is enough to prove, along
the boundary orbit,

`G=0 implies D G<0`.

Then every critical point of `F` is a strict maximum, so its derivative cannot
cross back from negative to positive.  A 100,000-pair hostile root search
found `D G<0` at every critical point.  The largest value was `-7.45e-12`, in
a near-degenerate small-slope package.

The orbit restriction is essential.  Although `G` is linear in `q`, solving
`G=0` for `q` and attempting a box proof fails: the off-orbit package

`(T,R,p,q)=(0.234331,0.233310,0.470264,0.442709)`

has `D G approximately 0.13014>0`.  Therefore the conserved relation

`artanh R-p artanh T=(I-p tau)/2`

must be imposed before the curvature sign can hold.  This falsifies an
attractive but invalid universal polynomial strengthening.

The weaker orbit sign is still insufficient.  Actual boundary orbits have

`J=artanh R-p artanh T<=0`,

because the image of the descent is strictly smaller than `p tau`.  But the
package

`(T,R,p,q)=(0.181265,0.0403624,0.661431,0.454595)`

has `J approximately -0.08085`, satisfies `G=0`, and nevertheless has
`D G approximately 0.22144>0`.  Hence the proof must use the exact
endpoint-dependent constant

`J_0(p,q)=(1/2)[(1/2)log((1-q^2)/(1-p^2))
                -p(artanh p-artanh q)]`,

not merely its sign.  This second falsifier sharply identifies the remaining
transcendental content of the phase-plane lemma.

The exact Hessian contraction also identifies the correct boundary
normalization.  At a critical point,

`D G=-2T(1-T^2)N_T-2p^2R(1-R^2)N_R
     +(1-T^2)^2N_TT
     +2p(1-T^2)(1-R^2)N_TR
     +p^2(1-R^2)^2N_RR`.

The two vanishing corners are different: `D G` is of order `-p^2` as
`p->0`, while it is of order `-(1-p^2)^2` when `p,q->1` together.  The
natural quantity for a compact certificate is therefore

`-D G/[p^2(1-p^2)^2]`.

A 100,000-package hostile critical-point sweep using the exact derivatives
found this normalized margin positive throughout.  A second 100,000-package
search aimed at the boundary corners found minimum approximately `0.60729`.
This removes the apparent small raw margins: after normalization the proposed
curvature theorem has order-one numerical separation from zero.

Targeted boundary charts locate the sharp corner more precisely.  As
`p=q->1`, the critical holding time converges to

`L_* approximately 2.10651`,

and the normalized negative curvature converges to approximately

`0.59120`.

If `(p-q)/(1-p)` stays positive, the limiting margin is larger; for example
the diagonal-scale choice `p-q=1-p` tends to approximately `0.751`.  At the
opposite boundary `p->0` the same normalized curvature grows rather than
shrinks (roughly logarithmically), so that corner is not delicate.  The
global infimum is therefore conjecturally the coalescing unit-slope limit.

This determines the certificate architecture: isolate the `p=q->1` chart and
prove its one-variable limiting margin exceeds, say, `0.59`; use continuity
for a collar of that corner; the remaining normalized parameter region is
compact with a substantially larger margin.  The unbounded holding-time
chart belongs to `p->0`, where the normalized quantity is coercive.

The coalescing chart has an explicit elementary limit.  Put `p=q=1-delta`,
`x=L/2`, `t=tanh x`, and `s=1-t^2`.  Direct second variation of the cubic at
`p=q=1`, where `R=T=t`, gives

`F_(p,p)(L)=delta^2 f(x)+O(delta^3)`,

with

`f(x)=t^2 s-2x t s^2+(1+3t^2)x^2 s^2`.

Since `D G=4F''(L)` and `p^2(1-p^2)^2=4delta^2+O(delta^3)`, the limiting
normalized negative curvature at the critical point is exactly

`-f''(x_*)/4`, where `f'(x_*)=0`.

Direct evaluation gives

`x_* approximately 1.053255...`, `L_*=2x_* approximately 2.10651...`,

and `-f''(x_*)/4 approximately 0.59120`, reproducing the independent boundary
sweeps.  The most delicate chart has therefore become a one-variable
elementary hyperbolic inequality, suitable for a short directed interval
certificate.

That limiting certificate is now complete.  Seventy-decimal directed
arithmetic gives

`f'(1.0532)>1.29600351493e-4`,

`f'(1.0533)<-1.06883834306e-4`.

On 128 directed subcells covering this bracket,

`-2.36539880860 < f'' < -2.36428484690`.

Hence there is a unique critical point in the bracket and its normalized
negative curvature satisfies

`-f''/4 >0.591071211725`.

Thus the sharp `p=q->1` boundary limit is rigorously positive with a margin
above `0.591`.  What remains for the phase-plane theorem is a uniform collar
estimate transferring this limiting certificate to `p,q` near one, followed
by the compact normalized interior.

The full unit-slope corner has a two-scale parameter.  Write

`p=1-epsilon`, `q=1-(1+k)epsilon`, `k>=0`.

The diagonal chart is `k=0`; for fixed positive `k`, the rapidity gap has the
nonzero limit `(1/2)log(1+k)`.  Hostile critical-point sweeps at
`epsilon=10^-3,10^-4,10^-5`, over

`k=0, .001, .003, .01, .03, .1, .3, 1, 3, 10, 30, 100`,

show strict monotonic increase of the normalized curvature in `k` on every
row.  The `k=0` limit is `0.59120...`; `k=1` tends to about `0.751`, and the
large-`k` margin grows rapidly.  This supports the sharper collar lemma:

> In the `p,q->1` limiting family, the normalized critical curvature is
> minimized at `k=0`.

Proving this monotonicity would make the directed diagonal certificate
uniform over all approaches to the unit-slope corner.  It is now the preferred
collar attack; a generic two-dimensional continuity estimate would discard
the substantial margin gained for `k>0`.

The limiting family can be evaluated without any small-`epsilon`
subtraction.  At `epsilon=0`, put

`tau_0=(1/2)log(1+k)`, `t=tanh((tau_0+L)/2)`, `s=1-t^2`.

The first-variation vector of `(p,q,T,R)` is

`v=(-1,-(1+k), sk/8, -s(L/2+k/8))`.

All first derivatives of `N` vanish at `(p,q,T,R)=(1,1,t,t)`.  Hence the
exact limiting margin is the Hessian quadratic

`Phi_k(L)=(1/2) v^T Hess(N) v`.

This cancellation-free model reproduces the finite-scale limits:

`k=0:   L_*=2.1065096, curvature=0.5912047`,

`k=.1:  L_*=2.0640506, curvature=0.6014501`,

`k=1:   L_*=1.7798660, curvature=0.7510726`,

`k=10:  L_*=1.0941321, curvature=3.0787498`,

`k=100: L_*=0.7129853, curvature=22.9262568`.

Thus the observed monotonicity is intrinsic to the exact limiting family,
not a finite-`epsilon` artifact.  The collar lemma is reduced to proving that
`-partial_L^2 Phi_k` at its unique critical point increases with `k>=0`.

A dense sweep of this exact Hessian family over 5,001 logarithmically spaced
values `0<=k<=1000` found no monotonicity reversal.  Its minimum was the
diagonal value

`0.5912047074...` at `k=0`,

while at `k=1000` the curvature had grown to `114.54`.  Thus a prospective
directed proof may split at a moderate finite `k`: certify the compact family
there and use a coarse coercive estimate in the large-`k` tail.

Expanding the Hessian quadratic produces only 28 monomials and factors to a
short closed form.  With

`t=tanh((L+(1/2)log(1+k))/2)`, `s=1-t^2`,

write `Phi_k=Phi_0+k Phi_1+k^2 Phi_2`, where

`Phi_0=t^2s-Lts^2+(1+3t^2)L^2s^2/4`,

`Phi_1=ts(t^2+2t-1)/2
       +Ls^2(1-2t+3t^2)/4`,

`Phi_2=-(1-t)^3(1+t)^2(3t-1)/16`.

At `k=0`, `Phi_0(L)=f(L/2)` as required.  The negative sign of `Phi_2` shows
that monotonicity is not a trivial coefficientwise statement: the increase
comes from the simultaneous `k`-dependence of
`t=tanh((L+(1/2)log(1+k))/2)`.  Nevertheless the full limiting collar is now
an explicit elementary two-variable function, ready for directed
differentiation and subdivision.

A first direct interval implementation of this closed form was deliberately
hostile-tested and rejected.  Even on a moderate mesh, independent interval
evaluation of `Phi_0+k Phi_1+k^2 Phi_2` loses the exact correlation between
`k` and `t(k,L)`; for large `k`, cancellation between the three displayed
terms produces wide false-negative curvature intervals.  Narrowing to
`0<=k<=1` improves but does not remove the dependency blowup.  This is an
enclosure defect, not a counterexample.

The viable certificate must use centered Taylor models in
`u=log(1+k)` and `L`, retaining their common perturbations through `t`, or
factor the differentiated expression before interval evaluation.  The
unbounded `k` tail should be handled separately by coercivity.  The rejected
prototype was removed rather than retained as a misleading checker.

A general second-order interval-automatic-differentiation implementation of
the centered form was then tested on the sharp `0<=k<=1` collar.  It retains
the correct correlations, but its object-heavy Decimal evaluation is too slow
for adaptive two-dimensional subdivision, even after caching powers and
seeding a mesh.  That prototype too was stopped and removed.

The mathematical representation remains the centered `Q,DQ` formulation.
The implementation lesson is specific: generate flat formulas for
`Q,Q_u,Q_L,Q_uu,Q_uL,Q_LL` once from the sparse polynomial and evaluate those
directly.  This avoids rebuilding general Hessian objects for every monomial
in every box and should reduce the certificate to ordinary directed
polynomial arithmetic.

The flat centered implementation now closes the sharp limiting collar
`0<=k<=1`.  It evaluates the sparse polynomial partials directly and applies
the chain rules

`t_u=s/4`, `t_L=s/2`, `k_u=1+k`

through second order.  A 16-by-16 seeded adaptive certificate on

`0<=u=log(1+k)<=log 2`, `1.5<=L<=2.25`

produces 156 certified critical boxes, discards 380 noncritical boxes, and
leaves zero unresolved boxes.  On every box that can meet `Q=0`,

`-partial_L^2 Phi >0.501979070458`.

Directed endpoint enclosures give, uniformly in `0<=k<=1`,

`Q(L=1.5)>0.490762374394`,

`Q(L=2.25)<-0.224074510762`.

Therefore each member of the sharp limiting family has exactly one critical
point in this strip, that point is a strict maximum, and the normalized
critical curvature is uniformly greater than `0.5019`.  This is the first
rigorous two-parameter collar theorem.  It extends the sharper diagonal bound
`0.591071...` without assuming monotonicity in `k`.

The same flat centered method now covers the limiting family through `k=100`
in four aligned strips.  Every strip has zero unresolved critical and endpoint
boxes:

| `k` range | `L` strip | certified `-Phi_LL` lower bound |
|---|---|---:|
| `[0,1]` | `[1.5,2.25]` | `0.502662874872` |
| `[1,3]` | `[1.2,2.05]` | `0.502446512821` |
| `[3,10]` | `[0.8,1.7]` | `0.504110075274` |
| `[10,100]` | `[0.45,1.35]` | `0.501901468435` |

Adaptive centered endpoint bounds prove `Q>0` at every left edge and `Q<0`
at every right edge.  In the widest final strip they give

`Q(0.45)>0.704828868361`, `Q(1.35)<-1.18984945179`.

Therefore the exact two-scale unit-slope limiting family has a unique strict
maximum and normalized curvature greater than `0.5019` for every
`0<=k<=100`.  The only limiting-family remainder is the coercive tail
`k>=100`, whose diagnostic curvature already exceeds `22.9` at the handoff
and grows thereafter.

Attempting to extend the `u=log(1+k)` certificate directly to
`100<=k<=1000` is needlessly expensive: the sparse polynomial still carries
large `k^2` terms.  The correct tail compactification is

`z=(1+k)^(-1/2)`, `E=e^L`, `t=(E-z)/(E+z)`.

Group the critical polynomial as

`Q=C_00+kC_01+k^2C_02+L(C_10+kC_11)+L^2C_20`.

The dangerous coefficient factors as

`C_02=(t-1)^2(t+1)(9t^2-t-2)/16`.

Since

`(1-t)/z=2/(E+z)`,

the scaled equation `Q_bar=z^2Q=0` extends regularly to `z=0`.  Its terms are

`z^2C_00+(1-z^2)C_01
 +(1-z^2)^2 [(1-t)/z]^2 (1+t)(9t^2-t-2)/16
 +z^2LC_10+(1-z^2)LC_11+z^2L^2C_20`.

Thus the infinite tail `k>=100` becomes the compact rectangle

`0<=z<=1/sqrt(101)`, approximately `0.45<=L<=0.85`,

with no singular coefficients.  At a critical point,

`-Phi_LL=-(1-t^2)Q_L
          =-[(1-t^2)/z^2] partial_L Q_bar`.

The prefactor grows like `1/z`, explaining the observed coercive curvature.
The next directed checker should use centered forms for `Q_bar` and its
`L` derivative on this compact tail chart; the aborted direct-`u` tail run is
not part of the certificate.

The compactified tail certificate is now complete on the slightly larger
range `0<=z<=0.1`, equivalently `k>=99`.  A 16-by-16 centered directed
certificate on `0.45<=L<=0.85` produces 49 critical boxes, discards 207
noncritical boxes, and leaves zero unresolved boxes.  At every possible zero
of `Q_bar`,

`-partial_L Q_bar >1.11092893495`.

The endpoint signs are uniform:

`Q_bar(0.45)>0.134317627461`,

`Q_bar(0.85)<-0.118514472704`.

Hence the tail has exactly one critical point and it is a strict maximum.
Because `(1-t^2)/z^2>0`, the original limiting curvature is strictly
negative there and grows coercively as `z->0`.

The overlap of the certificates `[0,100]` and `[99,infinity)` proves the
complete exact two-scale limiting-family theorem:

> For every `k>=0`, `Phi_k` has a unique critical point, that point is a
> strict maximum, and the associated normalized curvature is positive.

The next obligation is no longer a limiting-family problem.  It is a uniform
finite-`epsilon` transfer from this boundary theorem into an actual collar
`p,q<1`, followed by the compact interior of the original boundary-control
family.

The strongest possible transfer principle is now the preferred attack.  In
the exact variables

`p=1-epsilon`, `q=1-(1+k)epsilon`,

let `C(epsilon,k)` be the normalized negative curvature at the unique
critical point.  The proposed inward-monotonicity theorem is

`C(epsilon,k)>=C(0,k)`.

A 3,000-package hostile sweep, with `epsilon` logarithmically distributed
from approximately `10^-5` into the deep interior and `k<=1000`, found no
failure.  Its smallest gap was

`C(epsilon,k)-C(0,k)=1.61971e-5>0`

at `epsilon approximately 1.0347e-5`, `k approximately .2916`, exactly where
convergence to the boundary makes the gap smallest.  If inward monotonicity
holds, the completed limiting-family certificate transfers without loss and
also subsumes the compact interior curvature theorem.  The next algebraic
target is therefore the envelope derivative `partial_epsilon C` along the
critical equation, not a generic continuity collar.

The missing endpoint `q=0`, where `k=epsilon^-1-1` can exceed the earlier
diagnostic cap, is strongly safe.  The inward-minus-limiting curvature gaps
are

`1.79` at `epsilon=.1`, `9.62` at `.01`, `47.14` at `.001`, and `176.22` at
`.0001`.

Along the critical manifold `G(epsilon,k,L_*)=0`, the exact envelope formula
is

`dC_*/d epsilon
 =(C_epsilon G_L-C_L G_epsilon)/G_L`.

A 10,000-package finite-difference sweep away from the cancellation-dominated
boundary found this derivative positive throughout; its smallest sampled
value was approximately `1.74`.  At extremely small `epsilon` and large `k`,
raw double precision becomes unreliable because the normalization divides a
high-order cancellation.  Such apparent derivative noise is not treated as a
counterexample; that region belongs to the exact limiting expansion already
certified.  A proof should expand the numerator

`C_epsilon G_L-C_L G_epsilon`

in the same scaled `(epsilon,k)` charts and establish its sign directly.

At the conjectured worst endpoint `k=0`, the first inward coefficient can be
computed without cancellation.  For `p=q=1-epsilon`, write

`F_epsilon(L)=epsilon^2 phi(L)+epsilon^3 psi(L)+O(epsilon^4)`.

If `L_0` maximizes `phi`, then the critical-point displacement is

`L_1=-psi'(L_0)/phi''(L_0)`.

Using `p^2(1-p^2)^2=4epsilon^2(1-3epsilon+O(epsilon^2))`, the first normalized
inward coefficient is

`A(0)=-psi''+psi'phi'''/phi''-3phi''`,

all derivatives being evaluated at `L_0`.  A cancellation-free third-order
jet gives

`L_0=2.10650960091`, `phi''=-0.591204709614`,

`psi'=0.646425749194`, `psi''=-0.561650083282`,

and therefore

`A(0)=1.67958010993>0`.

This matches the finite-`epsilon` extrapolation.  The putative global minimum
of the boundary curvature is locally repelling in the inward direction with
an order-one margin.  The next extension is the exact two-scale third
variation `A(k)`; diagnostics indicate it increases from this diagonal value.

The exact two-scale third variation is now regular.  The rapidity and image
increments have the opposite expansions

`tau=(1/2)log(1+k)+D(epsilon)`,

`I=(1/2)log(1+k)-D(epsilon)`,

where

`D(epsilon)=sum_(n>=1) [(1+k)^n-1]/[2n 2^n] epsilon^n`.

Substitution through order three gives cancellation-free `phi_k` and `psi_k`
and hence the same envelope coefficient

`A(k)=-psi_k''+psi_k'phi_k'''/phi_k''-3phi_k''`.

Representative values are

`A(0)=1.67958007`, `A(.1)=1.70240792`, `A(1)=2.12984895`,

`A(10)=14.7964347`, `A(100)=657.490859`.

A 501-point logarithmic sweep on `0<=k<=100` found no monotonicity reversal;
its minimum was exactly the diagonal value at `k=0`.  Thus the first inward
variation appears to satisfy the stronger theorem

`A(k)>=A(0)>1.6795`.

This is now the preferred local-collar certificate: prove the two-scale third
variation uniformly positive, then bound the fourth-order remainder for a
nonzero `epsilon` collar.  The large-`k` coefficient is coercive rather than
delicate.

The apparent division by `phi_k''` can be removed.  At a limiting critical
point put

`P=phi_k''<0`, `B=psi_k'`, `C=psi_k''`, `D=phi_k'''`.

Then `A=-C+BD/P-3P`, so, because `P<0`,

`A>0 iff R:=PC-BD+3P^2>0`.

Every entry in `R` is obtained by repeated application of the polynomial
flow derivative `D_L=partial_L+(1-t^2)partial_t/2`; hence `R` is a sparse
polynomial in `t,L,k`.  There is no interval division.  Numerically,

`R(0)=0.99297563`, `R(.1)=1.02391346`, `R(1)=1.59967117`,

and `R(100)=15073.8060`.

This order-one diagonal margin makes `R>0` the correct directed certificate
target.  The already-certified `Q=0` boxes can be reused and subdivided only
where the natural or centered enclosure of `R` meets zero.

The symbolic generator produces `R` with 278 nonzero rational monomials,
degrees `(16,5,5)` in `(t,L,k)`.  Direct natural intervals are too dependent;
a centered mean-value implementation retains the sign but remains too slow
when each box evaluates all monomials and their gradients with Decimal
arithmetic.  Two bounded attempts were stopped, and the slow prototype was
removed rather than labeled a certificate.

The remaining optimization is mechanical rather than mathematical: compile
`R,R_t,R_L,R_k` into grouped Horner form in `t`, with coefficient polynomials
in `(L,k)`, and evaluate midpoint values and gradients together.  The target
boxes and the reserve margin are already known; the current obstacle is the
cost of the generated evaluator.

There is a lower-cost global route.  Along the already-certified critical
curve `Q(k,L_*(k))=0`, a 1,001-point logarithmic sweep through `k=1000` found
the reserve strictly increasing, from

`R(0)=0.9929756494`

to approximately `3.4028748e6`.  Differentiating the critical equation gives

`dR_*/dk=(R_k Q_L-R_L Q_k)/Q_L`.

The limiting-family theorem already certifies `Q_L<0`, so reserve
monotonicity is equivalent to the denominator-free polynomial inequality

`M:=R_k Q_L-R_L Q_k<=0`

on `Q=0`.  Proving this would reduce the whole first-inward certificate to
the single diagonal bound `R(0)>0.9929`; no direct 278-term positivity
certificate would be needed outside the sharp endpoint.  The new preferred
target is therefore the sign of `M` on the certified critical boxes.

The first directed diagnostic of this target is unusually favorable.  Using
`M=Q_L dR_*/dk` along the numerically solved critical curve gives

`M(0)=-0.40708`, `M(.1)=-0.54709`, `M(1)=-1.77964`,

`M(10)=-95.90`, `M(100)=-4.90e4`, `M(1000)=-1.28e7`.

No near-zero interior regime appears: the least negative value is the sharp
endpoint `k=0`, already separated from zero by about `0.407`.  Thus the
certificate should be organized around `-M`, not around direct positivity of
the 278-term reserve.  A finite compact zone only needs to preserve an
order-one endpoint margin, while the large-`k` tail is coercive.  These values
remain discovery-level finite-difference diagnostics; the theorem still
requires a directed interval evaluation of the exact polynomial `M` on the
certified `Q=0` boxes.

An exact symbolic reconstruction now sharpens that task.  Before restriction,
`M` has 589 terms and degrees `(22,6,6)` in `(t,L,k)`.  Polynomial division
in the holding variable, using the quadratic critical equation `Q=0`, gives

`M=-(1-t^2)^2 [A(t,k)L+B(t,k)]/[8192 t^5(3t-1)^5(3t+1)^5]`.

Here `A` and `B` are exact rational polynomials; the numerator is affine in
`L`.  The certified critical charts lie in `t>1/3`, so every displayed
denominator factor is positive.  The monotonicity theorem has consequently
been reduced to the single polynomial inequality

`A(t,k)L+B(t,k)>0`

on the certified critical boxes.  This is materially smaller than enclosing
the original 589-term `M`: interval dependence in six powers of `L` has been
eliminated exactly before evaluation.

A direct Decimal centered-interval prototype for this reduced numerator was
still too slow: even after caching its 348 rational coefficient intervals, a
compact-zone run did not finish its first report in one minute.  It was
stopped and removed rather than retained as a purported certificate.  The
remaining bottleneck is now sharply identified as evaluation architecture,
not interval dependence in `L`.  The next implementation should compile the
two coefficient polynomials `A(t,k)` and `B(t,k)` and their first derivatives
into grouped Horner form, then reuse their shared powers and midpoint values
across every critical box.

Grouped Horner evaluation was implemented and tested, but it revealed a
deeper dependency problem.  At the diagonal critical point the reduced
numerator is approximately `4.8510964e7`; nevertheless a centered box only
`0.01` wide in both chart variables encloses approximately
`[-5.41e7,1.52e8]`.  Thus evaluation speed is not sufficient: an independent
box in `(u,L)` destroys the correlation imposed by `Q=0`.  The Horner
prototype was stopped and removed.

The correct next chart must use the critical equation before interval
evaluation.  Since `Q` is quadratic in `L`, there are two viable exact routes:

1. isolate the certified critical root `L_*(t,k)` by the quadratic formula
   with a directed square-root interval, then evaluate `A L_*+B`; or
2. use an interval implicit-function enclosure
   `L-L_0=-(Q_t/Q_L)(t-t_0)-(Q_k/Q_L)(k-k_0)+remainder`.

The first route is preferred because the existing endpoint signs already
select the unique critical root and it removes the transverse `L` width
entirely.

The quadratic coefficients factor explicitly:

`q2=t(t-1)(t+1)(3t-1)(3t+1)/4`,

`q1=(t-1)(t+1)[9kt^3-5kt^2-kt+k-16t^2]/4`.

On the certified domain `1/3<t<1`, `q2<0`.  The maximum branch is therefore

`L_*=(-q1-sqrt(Delta))/(2q2)`,

because its derivative is exactly `Q_L=-sqrt(Delta)<0`.  Put

`C=-Aq1+2q2B`.  Then

`A L_*+B>0 iff C-A sqrt(Delta)<0`.

Diagnostics through `k=100` show the stronger pair `A>0`, `C<0`, which makes
the desired inequality immediate without enclosing the square root.  At the
critical points these signs range from `(A,C)=(3.38e7,-1.66e7)` at `k=0` to
approximately `(2.35e12,-1.75e13)` at `k=100`.  A first directed Decimal
checker for these two polynomial signs was nevertheless too slow to report a
zone within ninety seconds and was removed.  This suggests static generated
tables and a lower-level interval evaluator are required for the rigorous
compact certificate.  The sign reduction itself is exact; its uniform sign
claim remains discovery-level.

The tail is genuinely different: by `k=1000`, `A` is negative while `C`
remains negative.  Hence the compact sign shortcut cannot simply be extended
to infinity; the tail must compare `C^2` with `A^2 Delta` with the correct
sign bookkeeping, preferably after the existing `z=(1+k)^(-1/2)`
compactification.

The compactified tail boundary now has an exact sign.  Factoring

`H=C^2-A^2 Delta=(t^2-1)t^6(3t-1)^6(3t+1)^6 P(t,k)`

and assigning the tail weights `1-t~2z/E`, `k~z^(-2)` gives weighted
valuation `-13` for `P`.  Its leading coefficient is

`-79164837199872 (E^6+9E^4-15E^2+9)/E^9`.

For `E>1`, put `x=E^2>1`.  The shape polynomial

`x^3+9x^2-15x+9`

equals `4` at `x=1` and has derivative `3(x^2+6x-5)>0` thereon.  Hence the
leading coefficient of `P` is strictly negative.  Since `t^2-1<0`, this
proves `H>0` at the compactified boundary `z=0`.  The tail is therefore
asymptotically safe rather than marginal.  A finite directed enclosure is
still required to extend the sign across `0<z<=0.1`.

The full denominator clearing can be performed without a global rational
expansion.  For each monomial `c t^a k^b` of `P`, expand

`c(E-z)^a(E+z)^(48-a)(1-z^2)^b z^(22-2b-9)`

coefficient by coefficient.  All negative powers cancel.  The result is a
509-term polynomial `W(z,E)` of degrees `(56,48)`, with

`sign W = sign P`

for `z>0`, and boundary

`W(0,E)=-79164837199872 E^39(E^6+9E^4-15E^2+9)<0`.

Thus the remaining tail proof is a conventional compact polynomial sign
certificate on `0<=z<=0.1`, `0.45<=L<=0.85`, restricted to the already
certified critical boxes.  No singular arithmetic remains.

High-precision evaluation reveals the correct overlap for a two-regime
certificate.  The raw uncompactified polynomial is numerically unstable and
gave spurious alternating signs; evaluating `W/E^39` at 80 digits gives

| `z` | `k=z^-2-1` | `A` | `C` | `W/E^39` |
|---:|---:|---:|---:|---:|
| .100 | 99.0 | `+2.33e12` | `-1.62e13` | `+4.28e13` |
| .095 | 109.80 | `+2.34e12` | `-3.44e13` | `-1.12e13` |
| .090 | 122.46 | `+1.62e12` | `-7.37e13` | `-7.35e13` |
| .085 | 137.41 | `-8.74e11` | `-1.60e14` | `-1.45e14` |

Thus `H` becomes positive before `A` changes sign.  There is a genuine proof
overlap at `z=0.09`: the unsquared argument still works because `A>0,C<0`,
and the squared tail argument already works because `W<0`.  The directed
certificate should therefore split at `z=0.09`:

- extend the compact `A>0,C<0` chart only through `k=0.09^-2-1<123`;
- certify `W<0` on the tail chart `0<=z<=0.09`.

No delicate certification of either sign-change location is required.

There is a still cheaper tail certificate.  Normalize `U=W/E^39` and let
`Qbar=z^2 Q`, the regular critical equation used by the existing tail chart.
Along `Qbar=0`,

`dU_*/dz=(U_z Qbar_L-U_L Qbar_z)/Qbar_L`.

An 80-digit profile finds this derivative strictly positive with a large
margin:

| `z` | `U` | `dU_*/dz` |
|---:|---:|---:|
| .090 | `-7.35e13` | `+1.34e16` |
| .070 | `-4.33e14` | `+2.36e16` |
| .050 | `-1.07e15` | `+4.17e16` |
| .020 | `-3.05e15` | `+9.83e16` |
| .002 | `-5.36e15` | `+1.64e17` |

Thus `U` appears increasing throughout the tail.  A directed proof of the
denominator-free numerator

`J=U_z Qbar_L-U_L Qbar_z`

with the already-certified sign of `Qbar_L` would reduce the entire tail to
the single endpoint inequality `U(0.09)<0`.  This is now preferred over a
direct 509-term sign enclosure because the derivative margin grows toward
the compactified boundary.

The compactified endpoint is exactly solvable.  The regular critical equation
has expansion

`Qbar=-(E^2-3)/E^2 - 2(2E^2L-8E^2+13)z/E^3+O(z^2)`.

Hence `E_0=sqrt(3)`, `L_0=(1/2)log 3`, and implicit differentiation gives

`L_*'(0)=sqrt(3)(11-log 27)/9`.

The coefficient-wise construction of `W` also gives

`[z^1]W=13194139533312 E^38`

`*(19E^8+568E^6+2880E^4-6288E^2+4941)`.

Combining it with the derivative of `W(0,E)/E^39` yields the exact boundary
margin

`U_*'(0)=316659348799488 sqrt(3)(33 log 3+280)>0`.

Numerically this is `1.7345596966212889e17`, agreeing with the high-precision
interior profile.  Thus the proposed monotonicity certificate is not
degenerate at either end of the tail interval.

Clearing the derivative denominators is also exact.  Write

`Qbar=N/(E+z)^5` and `U=W/E^39`.  Then

`J=K/[E^39(E+z)^6]`,

where

`K=W_z[(E N_E+N_L)(E+z)-5EN]`

` -(E W_E-39W)[N_z(E+z)-5N]`.

The denominator is positive.  The resulting integer polynomial `K` has
1,781 terms and degrees `(62,53,2)` in `(z,E,L)`.  At the exact endpoint,

`K(0,sqrt(3),(1/2)log 3)`

`=-59622635402543133100081152(33 log 3+280)<0`.

Thus the final tail certificate is the ordinary polynomial sign `K<0` on
the already-certified critical boxes.  Both its boundary and its numerical
interior have large negative margins.

Division by the quadratic critical numerator `N` reduces `K` from degree two
to degree one in `L`.  The exact representative is

`K == R(z,E,L)/[z(-2E+z)(-E+z)(-E+2z)] mod N`,

where `R` has 1,350 terms and degrees `(66,57,1)`.  On the tail chart all
three linear factors after `z` are negative, so the displayed denominator is
negative.  Consequently `K<0` is equivalent to `R>0` on `N=0`.

The apparent `z=0` pole is removable on the critical surface.  Its numerator
boundary factors as

`R(0,E,L)=-2849934139195392 E^48`

`*(E^2-3)(E^4+6E^2-5)`.

Meanwhile `N(0,E,L)=-E^3(E^2-3)`.  Therefore subtracting

`2849934139195392 E^45(E^4+6E^2-5) N`

from `R` cancels the entire `z^0` coefficient without changing its value on
`N=0`.  The difference is exactly divisible by `z`.  If

`G=[R-2849934139195392 E^45(E^4+6E^2-5)N]/z`,

then the tail derivative theorem reduces to the regular polynomial inequality

`G(z,E,L)>0`

on the critical boxes.  This removes the compactified endpoint singularity
before interval evaluation.

Exact generation corrects one clause in the preceding expectation: the
multiple of `N` used to cancel the endpoint necessarily reintroduces its
quadratic `L` coefficient.  Thus `G` is regular but quadratic, not affine.
It has 1,358 terms and degrees `(65,57,2)`.  Its boundary factors as

`G(0,E,L)=52776558133248 E^45`

`*(209E^10+72E^8L+3974E^8+432E^6L+2076E^6`

`-360E^4L-49512E^4+15903E^2+29646)`.

At the exact critical endpoint this becomes

`357735812415258798600486912 sqrt(3)(33 log 3+280)>0`.

So desingularization trades the affine representation for a regular endpoint;
it does not achieve both simultaneously.  The useful outcome is still a
smaller, nonsingular polynomial with a large positive boundary margin.

The tempting stronger claim that `G>0` on the entire tail rectangle is false.
A `51 x 51` profile after the exact substitution `E=e^L` found

`G(0.09,0.674) approximately -1.26e31`,

and negative corner values at `L=0.45`.  These points are off the critical
surface.  Thus the positivity is genuinely conditional on `N=0`; discarding
the critical equation would prove a false statement.  The final directed
checker must use the already-certified narrow `N=0` boxes or an interval
implicit-function enclosure.  This falsifier rules out a whole-rectangle
Bernstein or coefficient-sign proof.

Because `Qbar_L` is already certified away from zero, the preferred
implementation is an implicit graph enclosure inside each accepted tail box:

`L-L0=-(Qbar_z/Qbar_L)(z-z0)+O((z-z0)^2)`.

Substituting this correlated displacement into the centered form for `G`
removes the transverse direction responsible for the negative off-surface
values.  A plain rectangular interval for `G` is not an admissible proof
strategy.

The existing certified tail cover consists of only 49 accepted boxes, with
maximum widths `Delta z=0.00625` and `Delta L=0.025`, while
`-Qbar_L>1.11092893495`.  A directed point profile of the implicit graph gives

`1.48266 <= L_*'(z) <= 1.76122`,

`2.36979 <= L_*''(z) <= 3.62655`.

Thus a half-box in `z` has a predicted second-order graph remainder below
`0.5*3.627*(0.003125)^2 < 1.78e-5`, tiny compared with the original `L`
width.  This confirms that the graph formulation is numerically well
conditioned.

A first attempt to certify curvature using raw natural intervals on the 49
boxes failed ergonomically: the coarse enclosures widened to roughly
`L' in [-0.13,3.88]`, `L'' in [-147,202]`, and derivative-only subdivision
did not finish within ninety seconds.  It was stopped and removed from the
theorem checker.  The original tail theorem still reruns in seconds.  The
next graph implementation must center `Q_z,Q_zz,Q_zL,Q_LL` themselves (or use
third-order automatic differentiation for their remainders); raw natural
second-derivative intervals are too dependent.

Third-order automatic differentiation repairs this defect.  Centered
mean-value forms for `Q_z,Q_L,Q_zz,Q_zL,Q_LL`, followed by a shallow
geometry-only subdivision, certify the implicit graph with

`1.35494302677 < L_*'(z) < 1.91445302474`,

`0.09017204662 < L_*''(z) < 5.99872718372`.

The directed run used 92 accepted geometry boxes, discarded 134 boxes that
miss `Qbar=0`, and left zero unresolved boxes.  Thus the critical branch is
rigorously increasing and convex.  Even using the original maximum half-width
`0.003125`, its second-order graph remainder is bounded by

`0.5*5.999*(0.003125)^2 < 2.93e-5`.

This supplies the missing rigorous correlation mechanism for evaluating `G`:
each critical subbox can be replaced by a thin parabolic graph enclosure
rather than its full `L` rectangle.

An 80-digit evaluation of `G` on the critical graph shows a large increasing
reserve:

| `z` | `L_*(z)` | `G(z,e^L,L)` |
|---:|---:|---:|
| 0 | .54930614 | `1.96e29` |
| .01 | .56431297 | `2.92e29` |
| .03 | .59538212 | `6.81e29` |
| .05 | .62778691 | `1.70e30` |
| .07 | .66141777 | `4.51e30` |

The smallest observed value is the exact compactified endpoint already
proved positive.  Evaluation of the unreduced rational critical equation
became numerically unstable in the same profiling script beyond `z=.07`, so
no later floating values are retained as evidence.  This does not affect the
directed implicit-graph certificate, which covers the full interval.  The
profile indicates that a centered graph evaluation of `G` has an enormous
sign margin and should not require deep subdivision once the correlation is
preserved.

The first directed graph-correlated `G` prototype preserved the implicit
geometry but evaluated `G_z` and `G_L` by natural sparse-polynomial intervals.
At 32 equal `z` cells it certified only 7 cells and left 25 unresolved.  The
worst cell, adjacent to `z=.09`, enclosed `G` by approximately
`[-9.38e32,9.62e32]`, overwhelming the true order-`1e30` reserve.  Scalarizing
the root bisection made the run practical, so this is not a root-solving or
runtime artifact; it is dependency inside the 1,358-term derivatives of `G`.
The unsuccessful checker was removed.

The next required representation is a centered jet for `G` itself: evaluate
`G,G_z,G_L` at the cell midpoint and enclose their variation using grouped
Horner forms for the Hessian (and, if needed, the third derivative along the
implicit tangent).  Simply combining a rigorous graph enclosure with natural
interval derivatives is insufficient.

The true one-dimensional jet confirms that coarse subdivision is sufficient
once derivatives are centered.  For

`g(z)=G(z,e^(L_*(z)),L_*(z))`, an 80-digit profile gives

| `z` | `g` | `g'` | `g''` |
|---:|---:|---:|---:|
| 0 | `1.96e29` | `7.66e30` | `3.31e32` |
| .03 | `6.81e29` | `3.00e31` | `1.43e33` |
| .05 | `1.70e30` | `8.03e31` | `4.07e33` |
| .07 | `4.51e30` | `2.28e32` | `1.21e34` |
| .09 | `1.27e31` | `6.77e32` | `3.77e34` |

At the worst endpoint and 32-cell half-width `r=.00140625`, the actual
linear variation is about `9.52e29` and the quadratic variation about
`3.73e28`, versus reserve `1.27e31`.  Hence a second-order Taylor certificate
has more than an order of magnitude of slack.  The failed natural enclosure
of order `1e33` was roughly a thousand times wider than the true variation.
The next checker should evaluate `g,g',g''` at directed midpoint intervals and
bound only the cubic remainder, rather than interval-enclosing `G_z,G_L`
across the whole cell.

The desingularized polynomial is unexpectedly sparse in the holding degree:
its `(L^0,L^1,L^2)` blocks contain `(698,648,12)` terms.  Moreover the entire
quadratic coefficient factors as

`[L^2]G=-11399736556781568 E^46 z^2`

`*(-2E+z)(-E+z)(-E+2z)(E^4+6E^2-5)`.

On `0<=z<=.09`, `E>=sqrt(3)`, the three linear factors are negative and the
last factor is positive.  Hence `[L^2]G>=0`, with equality only at `z=0`.
The quadratic holding block may therefore be discarded entirely in a lower
bound.  The proof target reduces to the affine minorant

`G_aff(z,E,L)=[L^0]G+L[L^1]G`.

This is not a numerically dominant sacrifice: the dropped positive term is
about `0.12%`, `0.78%`, `3.58%`, and `13.77%` of `G` at
`z=.03,.05,.07,.09`, respectively.  Even at the handoff endpoint the affine
minorant retains more than `86%` of the positive reserve.

The affine blocks do not have independent positive signs on the whole tail.
Along the critical graph,

| `z` | `G0` | `L G1` | `G_aff` |
|---:|---:|---:|---:|
| 0 | `1.73e29` | `2.25e28` | `1.96e29` |
| .03 | `1.04e29` | `5.76e29` | `6.80e29` |
| .05 | `-1.90e30` | `3.59e30` | `1.68e30` |
| .07 | `-1.75e31` | `2.19e31` | `4.35e30` |
| .09 | `-1.25e32` | `1.36e32` | `1.10e31` |

Thus `G1>0` in the profile, while `G0` crosses sign between `.03` and `.05`.
For the upper tail the stable formulation is

`G_aff>0 iff L>-G0/G1`.

The threshold margin `L+G0/G1=G_aff/G1` remains sizable: approximately
`.70` at `z=.03`, `.23` at `.05`, `.13` at `.07`, and `.056` at `.09`.
This ratio separates the two large affine blocks before subtraction and is a
better directed target than their cancellation-prone sum.  A natural split is
to certify `G0>0,G1>0` on the small-`z` collar, then certify `G1>0` and the
threshold inequality on the remaining tail.

A `21 x 21` whole-rectangle profile strengthens the `G1` part of this plan.
On `0<=z<=.09`, `.45<=L<=.85`, its smallest sampled value was

`G1=2.2637249185e26` at `(z,L)=(0,.45)`.

Thus `G1` may admit a proof on the entire rectangle, independent of `N=0`.
By contrast, `G0` reached approximately `-3.02e32` near `(.09,.73)`, so its
sign genuinely cannot be globalized.  The grid is discovery evidence only;
the directed target is now a whole-rectangle certificate `G1>0`, followed by
the graph-dependent threshold inequality.

A generic centered Decimal implementation of this whole-rectangle target was
also rejected: after exact symbolic generation it did not finish the
subdivision within two minutes.  A table-size defect found on its first run
(the full `E` degree is 56, not the residual factor's degree 55) was repaired,
but the corrected evaluator remained impractical.  It was removed from the
symbolic theorem checker.  The next implementation must statically compile
the 648-term block and its two derivatives into shared grouped Horner
recurrences; repeated sparse interval products are the bottleneck.

The natural scale variables expose a much smaller analytic route.  Write

`G1=-2^43 E P1(z,E)`, `x=z/E`, `y=E^2`, and

`R(x,y)=P1(xE,E)/E^46`.

Only 13 `y`-degrees occur.  The coefficient signs are mixed `(327 positive,
321 negative)`, so coefficient negativity is false.  However

`R(0,y)=-432 y(y^2+6y-5)<0`.

On the bounding rectangle `0<=x<=.09/exp(.45)<.058`,
`exp(.9)<=y<=exp(1.7)`, a `21 x 21` profile found

`max R=-16795.99`,

and, crucially,

`min R_xx=3.807050e6>0`.

The first derivative changes sign, so monotonicity in `x` is false; the
residual decreases and then rises.  Convexity is the correct structure.  A
rigorous `G1>0` proof now reduces to

1. certify `R_xx>0` on the bounding rectangle;
2. use the exact negative endpoint `R(0,y)`;
3. certify the other endpoint `R(.058,y)<0`.

A convex function lies below the maximum of its endpoint values, so these
three statements imply `R<0`, hence `G1>0`, everywhere.  This avoids the slow
648-term centered subdivision entirely.

The far endpoint is now directedly certified on a slightly enlarged rational
domain:

`R(.058,y)<-1573.20634303`

for every `2.459<=y<=5.474`.  The endpoint subdivision has zero unresolved
intervals.  Together with the exact formula at `x=0`, both boundary signs in
the convexity argument are closed.

The convexity inequality is now exactly certified.  After the affine rational
change of variables from

`0<=x<=29/500`, `2459/1000<=y<=2737/500`

to the unit square, `R_xx` has tensor Bernstein bidegree `(63,12)`.  Every one
of its `64*13=832` Bernstein coefficients is strictly positive.  The smallest
occurs at index `(63,0)` and is itself a positive rational number.  Since the
Bernstein basis is nonnegative and partitions unity, this proves

`R_xx>0`

on the whole enlarged rational rectangle.  The exact left boundary is

`R(0,y)=-432y(y^2+6y-5)<0`,

because `y>=2459/1000`, while the directed interval certificate gives

`R(29/500,y)<-1573.20634303`.

For each fixed `y`, convexity places `R(x,y)` below the chord joining these
two negative endpoints.  Therefore `R<0` everywhere on the rectangle and

`G1=-2^43 E R>0`

throughout the original tail rectangle.  This closes the whole-rectangle
`G1` lemma.  It does not yet prove `G_aff>0`: the remaining upper-tail target
is the graph-dependent threshold inequality `L>-G0/G1`, together with the
small-`z` collar where `G0>0`.

There is now a sharper candidate that may remove the collar split entirely.
Let

`F(z)=G_aff(z,exp(L_*(z)),L_*(z))`.

On a 101-point implicit-branch profile, `F` has its smallest sampled value at
the compactified endpoint,

`F(0)=1.95956356446e29`,

and its implicit derivative is positive at every sampled point.  The smallest
sampled derivative is again at the endpoint, approximately `7.656e30`; the
largest is approximately `4.711e32` at `z=.09`.  Meanwhile `G0` crosses zero
between `.0333` and `.0342`, confirming that monotonicity of `F`, rather than
separate positivity of `G0`, is the more economical target.

This derivative has an exact algebraic reduction.  If `N(z,E,L)=0` is the
critical equation, then

`L_*'=-N_z/(E N_E+N_L)`

and the derivative numerator is

`T=F_z(E N_E+N_L)-(E F_E+F_L)N_z`.

Reducing `T` modulo the quadratic `N` leaves an affine polynomial in `L` with
1,861 terms and degrees `(79,68,1)`, divided by

`z^3(-2E+z)^2(-E+z)^2(-E+2z)^2`.

The denominator is positive for `z>0` on the tail rectangle.  At `z=0` the
remainder numerator equals

`15199648742375424 E^58(E^2-3)(53E^4+306E^2-245)`,

which vanishes at the critical endpoint `E=sqrt(3)`.  Thus the apparent
`z^-3` behavior is a graph-correlated removable singularity.  The next exact
target is to subtract suitable multiples of `N` through third order in `z`,
producing a regular affine representative whose negativity would prove
`F'>0`.  Until that desingularization and sign certificate are complete, the
monotonicity remains discovery evidence rather than a theorem.

The endpoint singularity has now been removed exactly.  Writing the affine
remainder numerator as `A`, there are polynomial coefficients `h0,h1,h2`
such that

`A-(h0+z h1+z^2 h2)N`

is divisible by `z^3`; all three exact division remainders vanish.  Dividing
by `z^3` produces a regular branch-equivalent polynomial `S` with 1,880 terms
and degrees `(76,68,3)`.  Its critical endpoint is

`115906403222543850746557759488 sqrt(3)`

`*(-209996+10350(log 3)^2+62895 log 3)<0`,

using the same elementary logarithm bracket already certified for the endpoint
Taylor jet.  On the 101-point critical profile `S` stays negative, from about
`-2.58e34` to `-4.76e36`.

Negativity is not a whole-rectangle fact: an off-critical `21 x 21` profile
reaches approximately `+4.58e45`.  This is a useful hostile test, because it
rules out a direct rectangular Bernstein certificate and confirms that the
critical relation cannot be discarded.  The next directed reduction is to
divide the regular cubic `S` by the quadratic `N`, obtain its affine remainder
on the critical branch, and certify that remainder's sign by root orientation
and a discriminant inequality.  The negative off-critical values are not used
as theorem evidence.

That second reduction is now explicit.  Modulo `N`, the regular cubic becomes

`(a(z,E)L+b(z,E))/z^3`.

On the directed critical profile for `z>0`, the orientations are

`a>0`, `b<0`, `q2<0`.

For the selected quadratic root, put

`C=2 q2 b-a q1`, `H=C^2-a^2 Delta`.

The same profile gives `C>0` and `H>0`.  These are the correctly oriented
unsquared and squared inequalities: because `a>0` and `q2<0`, they imply that
the affine remainder is negative at the selected root.  Merely proving `H>0`
without `C>0` would not select the correct sign.

The raw squared obstruction has 3,909 terms and degrees `(170,144)`, but its
scaling is highly constrained.  It has factors `z^6 E^126`, and after

`x=z/E`, `y=E^2`

the residual is a polynomial of bidegree `(164,30)`.  This residual is not
positive on the whole enlarged rectangle: the hostile profile found a
negative value near `(x,y)=(0,5.474)`.  Hence a global Bernstein proof is
again false, not merely inefficient.  The next certificate must retain the
implicit critical graph, using its already certified slope and curvature to
bound the compact residual only in a thin tube around `y=E_*(z)^2`.

A first rigorous thin-tube prototype used directed endpoint root brackets,
monotonicity of `L_*(z)`, and natural interval Horner evaluation of the full
`(164,30)` compact polynomial.  The bounded-depth run did not finish in a
practical interval and was stopped; the slow path was removed from the exact
checker.  This does not indicate a sign failure—the bottleneck was repeatedly
traversing roughly five thousand coefficient slots per adaptive cell.  The
next implementation should precompute local tensor Bernstein coefficients or
use a centered Taylor form along the graph, with the certified slope and
curvature supplying the transverse remainder.

A subsequent generic exact factorization attempt on the compact `(164,30)`
polynomial also failed to finish in a practical bounded run and was stopped;
the call was removed.  This is not an irreducibility result.  It only shows
that black-box multivariate factorization is not a useful proof dependency for
this carrier.  The graph-centered Taylor/Bernstein route remains preferred.

A fixed 32-cell first-order centered interval pass was also attempted and
stopped after exceeding a practical bounded runtime.  Removing adaptivity did
not cure the cost: evaluating the value and two derivative tables over roughly
five thousand large rational slots per cell is itself unsuitable in the
generic Decimal interval class.  That implementation was removed.  A viable
certificate now needs either a generated straight-line kernel with outward
rounded machine intervals, or exact local Bernstein tables computed once and
reused; another interpreted sparse-interval evaluator would repeat the same
bottleneck.

The exact implicit third-derivative formula is

`L'''=-[Q_zzz+3Q_zzL L'+3Q_zLL(L')^2+Q_LLL(L')^3`

`+3(Q_zL+Q_LL L')L'']/Q_L`,

with the identical Faà-di-Bruno pattern for `g'''`.  At the directed-bracketed
critical ordinates, an 80-digit profile gives

| `z` | `g'''` | `|g'''|r^3/6` for `r=.00140625` |
|---:|---:|---:|
| 0 | `1.55e34` | `7.17e24` |
| .03 | `7.30e34` | `3.38e25` |
| .05 | `2.18e35` | `1.01e26` |
| .07 | `6.76e35` | `3.13e26` |
| .09 | `2.16e36` | `1.00e27` |

The cubic remainder is four orders of magnitude below the positive reserve
even at the hard endpoint.  Consequently the directed third-derivative bound
does not need to be sharp: an enclosure of order `1e40` would still be useful.
This changes the implementation priority.  Center `g,g',g''` tightly at each
midpoint, but allow a coarse natural interval for `g'''`; dependency in the
cubic term is tolerable because it is multiplied by `r^3/6`.

At the compactified endpoint the first four Taylor coefficients are exact:

`g(0)=357735812415258798600486912 sqrt(3)(33 log 3+280)`,

`g'(0)=-59622635402543133100081152`

`*(-209996+10350(log 3)^2+62895 log 3)`,

`g''(0)=13249474533898474022240256 sqrt(3)`

`*(-27543774 log 3+811269(log 3)^3+3069306(log 3)^2+39882098)`,

and `g'''(0)` is `-39748423601695422066720768` times

`-1703144338-589615995(log 3)^2+14121972(log 3)^4`

`+22723668(log 3)^3+1797386012 log 3`.

A directed Decimal evaluation on `1.0986<log 3<1.0987` proves all four
coefficients strictly positive.  Thus the first Taylor cell is anchored by an
elementary exact certificate and does not require evaluation of the 1,358-term
polynomial at `z=0`.

Differentiation before enclosure gives the exact factor

`partial_L Phi=(1-t^2)Q(t,L,k)`,

where `Q` is quadratic in both `L` and `k`.  At a critical point `Q=0`,

`partial_L^2 Phi=(1-t^2)D Q`,

with `D=partial_L+(1-t^2)partial_t/2`.  This eliminates the large cancellation
between `Phi_0`, `k Phi_1`, and `k^2 Phi_2`.

A second natural-interval prototype was also rejected: monomial intervals for
`Q` still lose the cancellation defining the surface `Q=0`, so every coarse
box falsely appears critical.  The appropriate rigorous representation is a
centered mean-value form

`Q(z) in Q(z_0)+gradient Q(B).(z-z_0)`,

and likewise for `-(1-t^2)D Q`.  This evaluates the cancellation exactly at
the box center and intervals only the derivative remainder.  The next checker
therefore needs second-order bivariate automatic differentiation in
`(u,L)`, not finer natural-interval subdivision.  The slow rejected prototype
was removed.

## Scope

The universal rank-two theorem and universal confluent rank-three theorem are
proved.  Positivity for three separated heights remains open.  Neither result
constructs the full self-adjoint boundary operator.
