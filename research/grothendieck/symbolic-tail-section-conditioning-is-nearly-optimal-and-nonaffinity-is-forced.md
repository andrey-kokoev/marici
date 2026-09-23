# Symbolic tail section conditioning is nearly optimal, and non-affinity is forced

## Frozen norms and owning construction

Use the admitted normalized box

    B_m=product_j [0,b_j], b_j=100+2j,
    L(t)=(U,V)=(sum t_j, sum r_j t_j), r_j=128^-j.

Measure witness differences by sum |delta t_j| and observable differences by
|delta U|+|delta V|. These norms and the owning normalization are fixed before
testing. The conclusions are norm-relative, not coordinate-free claims of
physical ill-conditioning.

The actual symbolic Generator provides the upper greedy profile h(U), lower
profile l(U), and their weighted values H(U),L(U). Its section is

    s(U,V)=l(U)+theta*(h(U)-l(U)),
    theta=(V-L(U))/(H(U)-L(U)).

The global continuity and natural fiber contraction were already established.
This experiment supplies a quantitative law and separates selector overhead
from unavoidable source geometry.

## Matching lower and upper conditioning certificates

For 0<U<T, T=sum b_j=m(m+99), define

    R(U)=||h(U)-l(U)||_1 / (H(U)-L(U)),
    R_m=sup_(0<U<T) R(U).

The distinct slopes make both greedy extremizers UNIQUE among source vectors
with fixed U. Hence every section is forced to take these values at the upper
and lower endpoints of that observable vertical slice. Their distance ratio
is R(U). Every globally Lipschitz section therefore has constant at least R_m.
This lower bound does not assume that the section is the greedy one.

The greedy section is linear in V on each vertical slice. It attains that
slice's optimal Lipschitz constant R(U). On each open greedy U-region,

    partial_V s=(h-l)/(H-L),
    partial_U s=(1-theta)l'+theta h'
                -(h-l)*((1-theta)L'+theta H')/(H-L).

The source profiles are coordinatewise nondecreasing in U, each with total
derivative 1. Thus the first term in partial_U has L1 norm 1. Both weighted
slopes lie in [r_(m-1),1]. Consequently

    ||partial_V s||_1 <= R_m,
    ||partial_U s||_1 <= 1+R_m.

Integrating along observable line segments through the finitely many greedy
regions proves a global bound 1+R_m. Continuity extends it to the polygon
boundary and the two tips. Hence, if L_* is the best achievable global
section Lipschitz constant under these norms,

    R_m <= L_* <= Lip(s) <= 1+R_m.

The selector is optimal for vertical reconstruction and within an additive
one of optimal global conditioning. No assertion that its exact global
constant equals this upper bound is needed.

## Exact calculation of R_m

Let C_k=sum_(j<k)b_j. The two coordinate profiles are clamps with respective
starting points C_j and T-C_(j+1). Therefore the sign of h_j(U)-l_j(U) does
not change with U. If k counts indices with C_j<=T-C_(j+1), then

    ||h-l||_1 = 2[min(U,C_k)-max(0,U-(T-C_k))].

On the partition with breakpoints C_j and T-C_j, both this numerator and
H-L are affine. A ratio of affine functions with positive denominator has
no strict interior extremum. It suffices to check the interior breakpoints
and the common limiting tip ratio

    2/(1-r_(m-1)).

The implementation exports exact rational R_m and a maximizing breakpoint
(or tip), not a numerical grid estimate.

Approximate values:

| m | R_m |
| --- | ---: |
| 2 | 2.015748 |
| 3 | 2.079482 |
| 4 | 4.008296 |
| 8 | 8.174338 |
| 16 | 17.221663 |
| 64 | 103.290296 |
| 256 | 898.621610 |
| 1024 | 11396.256876 |

## All-m growth law

Prefix dominance of the upper greedy allocation gives the summation identity

    H-L = sum_(j<m-1) (r_j-r_(j+1))
                         *sum_(i<=j)(h_i-l_i).

Every prefix difference is nonnegative, so

    H-L >= (127/128) min(U,100,T-U).

Also ||h-l||_1<=2min(U,T-U). Since T>=202,

    R_m <= 128*T/12700.

At U=T/2 the two profiles differ in L1 by at least T-max b_j. Their weighted
gap is bounded above by

    W_infinity = 100/(1-1/128) + 2*(1/128)/(1-1/128)^2.

Thus

    (T-(2m+98))/W_infinity <= R_m <= 128*T/12700.

This proves R_m=Theta(m^2). It is not extrapolated from the finite controls.
A source norm rescaled by total capacity would give a different asymptotic
statement; the metric is part of the observation/accuracy contract.

## Non-affinity is intrinsic for m>=3

Each exposed polygon edge comes from varying exactly one source atom j while
all others are forced to their endpoint values by its exposing normal. Every
point on that edge has a unique source lift.

If a section were affine with linear part A, endpoint differences on these
edges would force

    A(1,r_j)=e_j

for every j. For j=0,1,2 the observable directions satisfy

    (1,r_2)=(129/128)(1,r_1)-(1/128)(1,r_0),

but the corresponding required source identity

    e_2=(129/128)e_1-(1/128)e_0

is false. Therefore no affine section exists on the full polygon for m>=3.
For m=2 the observation is invertible and its inverse is affine.

This strengthens the previous observed disagreement between a direct greedy
lift and interpolation of endpoint lifts. That particular disagreement may
be selector-dependent, but SOME affine-interchange failure is unavoidable
for every section. It does not obstruct continuous sections, natural convex
contractions, or affine sections on suitably restricted visible regions.

## What the conditioning result does and does not authorize

For two admitted observable points, error at most delta in the declared input
norm changes the chosen greedy witness by at most (1+R_m)delta in L1. This
can certify stability of an audit of the SELECTED witness when a corresponding
margin is known. It does not identify the actual source: distinct actual
candidates in one fiber have exactly zero observable difference.

Nor does a Lipschitz section make feasibility classification uniformly stable
at the polygon boundary. Membership and witness reconstruction are different
questions. Exact rational correctness still has arithmetic and output-size
costs; the theorem is not a bit-complexity estimate.

Visible refinement restricts the domain of this same section, so it cannot
increase its true Lipschitz constant. The global bound remains valid on every
retained visible subset. Sharper bounds may be possible when evidence removes
the endpoint pairs forcing the global lower bound.

## Verification

    python research/grothendieck/checkers/check_symbolic_section_conditioning.py
    python research/grothendieck/checkers/verify_symbolic_section_conditioning.py

Contract: `results/symbolic-section-conditioning-contract.json`.
Packet: `results/symbolic-section-conditioning.json`.

The producer freshly replays Nima's independent symbolic-interface verifier
and calls the actual Generator/member implementation. The separate verifier
imports neither the engine nor an optimizer. It independently sums caps and
weighted profiles, reconstructs every breakpoint extremum, checks actual
membership packets and their source lifts, checks the quadratic bounds, and
replays the exact direction-dependence obstruction to affinity.

The analytic derivative proof establishes the continuum Lipschitz bound;
finite implementation checks do not substitute for it. Scope remains the
owning analytical relaxation, not prime-realizability or midpoint separation.
