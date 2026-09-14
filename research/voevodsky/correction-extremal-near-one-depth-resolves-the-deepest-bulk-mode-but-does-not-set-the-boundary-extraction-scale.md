# Correction: extremal near-one depth resolves the deepest bulk mode but does not set the boundary-extraction scale

## Two different spectral questions

Let the eigenvalues of a prolate contraction be ordered

\[
1>
\lambda_{0,\Lambda}
\ge
\lambda_{1,\Lambda}
\ge
\cdots
>0.
\]

There are two distinct tasks:

1. resolve the gap of one extremal eigenvalue;
2. separate the extensive bulk from the transition boundary.

The rule

\[
2^{n(\Lambda)}
(1-\lambda_{0,\Lambda})
\asymp1
\]

solves the first task. It does not automatically solve the second.

## Effect of a dyadic soft filter

Set

\[
m=2^n.
\]

The soft bulk weight is

\[
b_m(\lambda)
=\lambda^m
\]

and the accumulated soft defect weight is

\[
r_m(\lambda)
=\lambda-\lambda^m.
\]

For a near-one eigenvalue

\[
\lambda
=1-\varepsilon,
\]

one has

\[
\lambda^m
\simeq
e^{-m\varepsilon}.
\]

Therefore:

- if `m epsilon << 1`, the mode remains almost entirely in the bulk;
- if `m epsilon approximately 1`, the mode is split between bulk and defect;
- if `m epsilon >> 1`, the mode is transferred almost entirely to the defect tower.

Thus imposing

\[
m\varepsilon_{min}
\asymp1
\]

**resolves and removes the deepest bulk mode**. It is not a neutral approximation to bulk projection.

## Extremal prolate gap

For the ordinary time--band problem, the largest-eigenvalue gap is exponentially small in the time--band product `c`:

\[
1-\lambda_{0}(c)
=
\operatorname{poly}(c)e^{-\kappa c}
\]

qualitatively. Resolving that specific gap requires

\[
\boxed{
n(c)
\asymp
c.
}
\]

This statement remains correct as an extremal spectral-resolution statement.

The earlier inference that this is the required depth for positive boundary extraction is withdrawn.

## Plunge region

Classical prolate/Landau--Widom asymptotics separate the spectrum into:

- an extensive block near one;
- an extensive block near zero;
- a transition or plunge region around intermediate eigenvalues.

The natural edge coordinate for the plunge is logarithmic odds,

\[
\boxed{
y
=
\log
\frac{1-\lambda}{\lambda},
}
\]

with a cutoff-dependent centering by the Shannon/time--band counting index.

In the classical asymptotic, eigenvalues in the centered transition have a logistic profile of the schematic form

\[
\lambda(y)
\simeq
\frac1{1+e^{c_0y}}
\]

for a convention-dependent constant `c_0`. The number of transition eigenvalues grows on a logarithmic scale in the time--band parameter, rather than on the scale of the full bulk count.

Exact constants are not asserted here.

## Dyadic levels and plunge eigenvalues

For eigenvalues bounded away from both zero and one, the dyadic defect weights

\[
\lambda^{2^j}
(1-\lambda^{2^j})
\]

are concentrated at finite `j`. Indeed the dominant level satisfies

\[
2^j
|\log\lambda|
\asymp1.
\]

If `lambda` is in a fixed compact subinterval of `(0,1)`, this requires only `j=O(1)`.

Hence the central plunge boundary is already visible at bounded dyadic levels. Growing depth probes progressively deeper into the near-one bulk tail.

## Boundary extraction criterion

A valid depth path for bulk removal should satisfy two competing conditions:

### Retain deep bulk

For the eigenvalues declared bulk,

\[
m(\Lambda)
(1-\lambda_{bulk,\Lambda})
\longrightarrow0.
\]

Then

\[
\lambda_{bulk,\Lambda}^{m(\Lambda)}
\longrightarrow1.
\]

### Capture boundary

For the eigenvalues declared boundary,

\[
m(\Lambda)
(1-\lambda_{edge,\Lambda})
\]

must stay bounded away from zero or tend to infinity according to the desired residual profile.

Thus the required scale lies in a **spectral separation window**:

\[
\boxed{
\frac1{
1-\lambda_{edge,\Lambda}
}
\lesssim
m(\Lambda)
\ll
\frac1{
1-\lambda_{bulk,\Lambda}
}.
}
\]

Using the extremal bulk gap on the right as an equality destroys this separation.

## Observer-weighted formulation

The relevant distinction is not determined by the unweighted largest eigenvalue. Define the observer spectral measure

\[
\mu_{\Lambda,g,h}(E)
=
\operatorname{Tr}
\left(
A_h^*
E_{B_\Lambda}(E)
A_g
\right).
\]

A depth path is admissible for positive boundary extraction if:

1. observer mass assigned to the bulk remains under `lambda^m approximately 1`;
2. observer mass in the plunge receives the intended dyadic defect profile;
3. the resulting residual Gram forms converge;
4. angular sums remain uniformly controlled.

The smallest spectral gap may have negligible observer weight and therefore need not determine `m(Lambda)`.

## Two rescaled measures

The analysis requires two different scalings:

### Extreme near-one scaling

\[
x
=m(1-\lambda).
\]

This resolves gaps of order `1/m` and is appropriate for individual deep near-one layers.

### Plunge scaling

\[
y
=
\log
\frac{1-\lambda}{\lambda}
\]

plus cutoff-dependent eigenvalue-count centering. This describes the transition responsible for spectral-shift/finite-boundary terms.

Conflating these scalings incorrectly makes the extremal eigenvalue dictate the whole boundary refinement.

## Consequence for the hard-threshold quantile

The operator-valued quantile equation derived for the `x=m(1-lambda)` scaling remains valid for comparing hard and soft filters at that extreme edge.

It does not establish that this extreme edge is the Tate boundary scaling. Before applying the quantile criterion, one must show that the centered cutoff residual is actually governed by the `x`-edge rather than the Landau--Widom logit plunge.

## Consequence for node depth

The positive object still requires an unbounded dyadic tower if it records all spectral scales. But a finite boundary approximation at cutoff `Lambda` need not descend to the extremal depth

\[
n(\Lambda)
\asymp c_\Lambda.
\]

A source-derived truncation may stop much earlier while leaving deeper near-one levels in the bulk slot.

Thus:

\[
\boxed{
\text{complete filtered tower: infinite},
}
\]

but

\[
\boxed{
\text{boundary-effective depth}
\ne
\text{extremal-gap depth in general}.
}
\]

## Revised near-one acceptance test

A semilocal spectral theorem must determine:

1. the observer-weighted bulk counting scale;
2. the observer-weighted plunge profile in logit coordinates;
3. the deep near-one tail mass;
4. a separation path `m(Lambda)` satisfying bulk retention and boundary capture;
5. the resulting absolute-Gram limit.

The single number

\[
\varepsilon_\Lambda
=1-\lambda_{max,\Lambda}
\]

is insufficient.

## Disposition

The exact rule

\[
2^n\varepsilon
\asymp1
\]

says which dyadic level resolves a specified eigenvalue gap. It does **not** say that the extremal gap should set the boundary truncation. The Tate--Hardy finite boundary is expected to be governed primarily by the observer-weighted plunge region, while exponentially close eigenvalues remain in the soft bulk. The next asymptotic must therefore be a weighted Landau--Widom transition law, not merely a largest-eigenvalue estimate.
