# Calibrated radar determines the metric, but raw radar completion does not preserve curvature

## Result

Within the declared Rosen plane-wave source, complete labelled radar records
at arbitrarily small baselines determine the transverse metric. The metric
and the retained observer frame determine the tidal tensor. This establishes
an exact inverse in this scope, not a failure of identifiability.

The inverse is nevertheless discontinuous from the uniform norm on raw
normalized radar records to pointwise tidal curvature. The exact vacuum hostile
already proves this even when ALL baseline lengths and emission times are
available. More measurements of the same weak norm do not repair derivative
loss. A conditional finite-resolution error budget is possible only with an
explicit regularity prior and calibration/noise bounds.

## Fresh leaf and retained source

Fresh resume selected `radar-resolution-curvature-inverse:v1`.
The forward map and source definition are those in
`causal-radar-readout-is-c0-stable-in-the-plane-wave-sector.md`, grounded in
Perlick arXiv:0708.0170v1. No new ideal detector or arbitrary filter replaces
that map here.

Retain: a Rosen chart and reflector congruence, labelled initial transverse
baseline vectors b, central proper clock tau=sqrt(2)u, zero reflection delay,
positive metric bounds, and the initial observer frame. Initial baseline
calibration and directional labels are inputs; they are not inferred from
unlabelled distance values. Claims concern this fixed source class, not
reconstruction of arbitrary spacetime outside the probe family.

## Small-baseline reconstruction

Let R(t,b) denote the two-way radar distance with emission u=t. For a fixed
vector v and epsilon>0, write b=epsilon v. The exact leg equation implies

    limit_(epsilon->0) R(t,epsilon v)/epsilon
        =sqrt(v^T gamma(t) v).

Indeed the leg lengths are O(epsilon), so their averaged inverse metrics tend
to gamma(t)^-1. The return leg starts O(epsilon) later and has the same limit.
This argument requires continuity and the retained positive metric bound,
not a geometrical-optics expansion in curvature amplitude.

Define q_t(v) as the square of this limit. Three calibrated directions suffice:

    gamma_11=q_t(e1), gamma_22=q_t(e2),
    gamma_12=[q_t(e1+e2)-q_t(e1)-q_t(e2)]/2.

The baseline epsilon(e1+e2) is labelled as such; treating it as an unlabelled
unit-length probe would change the normalization. Losing labels also permits
axis swaps and loses the intended tensor components.

Knowing gamma as a smooth function then gives

    Gamma=(1/2)gamma^-1 gamma', F'=-Gamma F,
    E=(1/2) F^T[-gamma''/2+gamma' gamma^-1 gamma'/4]F.

F is determined by its separately retained initial frame. At a calibrated
corner with gamma=I,F=I this reduces to

    E=-gamma''/4+gamma'^2/8

in the transverse block, with zero longitudinal block. Derivatives here are
in u, and the factor 1/2 converting to the unit observer has already been
included. Proper-time differentiation must respect tau=sqrt(2)u.

Thus the full record identifies gamma and its tidal readout within the source
class. It does not identify a unique global matter state, a coordinate-free
frame without calibration, or an unrestricted spacetime.

## Exact identifiability does not give a continuous inverse

Use the previous smooth vacuum family

    beta_n=(1-cos(nu))/n^2,
    r_n''=-beta_n'^2 r_n, r_n(0)=1,r_n'(0)=0.

Let D_n(t,b)=R_n(t,b)/|b| for nonzero b, and D_flat=1. The proven envelope gives

    sup_(t in [0,1],0<|b|<=1/4) |D_n(t,b)-1| <= 8/n^2,

uniformly over baseline directions as well. Yet

    ||E_n(0)-E_flat(0)||=1/2.

Therefore no continuous inverse from the raw normalized-data uniform topology
to this pointwise tidal readout can exist on the admitted smooth source class
or its corresponding completion. A putative uniform Lipschitz constant would
have to grow at least as n^2/16.

The data are not exactly equal at finite n. No finite-n nonidentifiability or
failure of the exact small-baseline inverse is claimed. The obstruction is
stability/completion: arbitrarily close records can encode a fixed tidal gap.
The structural fibration equivalence may still retain all those exact records.
Its existence does not supply the missing inverse continuity estimate.

## A finite-baseline bias bound

Assume lambda I<=gamma<=B0 I and ||gamma'||<=B1 on the relevant compact interval.
For the exact radar response one obtains

    |R(t,epsilon v)/epsilon - sqrt(v^T gamma(t)v)|
        <= C_R epsilon |v|^2,

    C_R = sqrt(B0/2)/(4 sqrt(lambda))
          * [B0^2 B1/lambda^2+B1].

For each leg, averaging H=gamma^-1 changes H(t) by at most ||H'||h/2;
inverse and square-root differences then give the first term in C_R. The
return's shifted start contributes the second term. The two leg durations
are averaged after conversion to radar distance. This is a conservative
bound, not an optimized short-arm asymptotic coefficient.

After squaring and the fixed three-direction polarization formula, the metric
bias is O(epsilon), with constants fixed by the stated source/probe bounds.
If additive distance errors obey |delta R|<=sigma, normalization introduces
sigma/epsilon. For sigma/epsilon bounded and small,

    ||gamma_est-gamma|| <= C_0 [epsilon+sigma/epsilon].

The omitted quadratic noise term is absorbed in C_0 on that bounded regime.
No noise law or laboratory value of sigma is derived. Accurate emission-time
labels, direction and baseline calibration are additional hypotheses.

## Temporal resolution and a conditional curvature budget

Consider an interior event and a central second difference with step h in u:

    D_h^2 gamma(t)=[gamma(t+h)-2gamma(t)+gamma(t-h)]/h^2.

If ||gamma^(4)||<=M4 on the stencil interval, Taylor's integral remainder gives

    ||D_h^2 gamma-gamma''|| <= M4 h^2/12.

A uniform metric reconstruction error eta contributes at most 4 eta/h^2.
First derivatives can be treated by centered differences with the corresponding
third-derivative bound; inverse metrics and frame transport also require their
retained positivity and corner data. At the calibrated corner no transport
reconstruction is necessary because F is already I. On a compact interval,
controlled C1 estimates can instead be propagated through the prior frame ODE.

For bounded lower derivatives and a declared common M4, the resulting leading
curvature error has the form

    error_E <= C [ (epsilon+sigma/epsilon)/h^2 + M4 h^2 ],

with lower-order first-derivative/value terms absorbed for h<=1 and a sufficiently
small metric error preserving positivity. It is a conditional stability budget,
not an error theorem for an unspecified physical detector.

For example, in normalized units with those constants fixed, choose

    epsilon ~ sigma^(1/2), h ~ sigma^(1/8).

The leading error is then O(sigma^(1/4)). With exact distance data, taking
epsilon=o(h^2) and h->0 yields convergence for a fixed sufficiently regular
source. These schedules are mathematical consistency examples, not a proposed
instrument design or a claim of optimality.

Clock jitter would add a term controlled by the metric time-variation bound
before division by h^2. It is not included by silently treating all errors as
distance noise. The displayed budget assumes the stated time calibration.

## The hostile shows why the prior is substantive

For beta_n at the corner, the central second-difference response is

    D_h^2 beta_n(0)
       =2[1-cos(nh)]/(n^2 h^2)
       =[sin(nh/2)/(nh/2)]^2,

while beta_n''(0)=1. At nh=2*pi*m (nonzero integer m), this shape channel aliases
to zero. Recovering this derivative uniformly requires nh->0, not merely
shrinking h without regard to the source frequencies. This formula concerns
the beta shape channel; it is not a claim that every exact nonlinear metric
or radar component vanishes at those samples.

The fourth derivatives of this family are not uniformly bounded: already
beta_n^(4)(0)=-n^2. Hence it lies outside any fixed-M4 inverse theorem. Inserting
such a bound only to exclude this example would be fitting an assumption to
the desired conclusion. A physical bandwidth/regularity prior must have its
own source justification, or the intended readout should remain the finite-
resolution radar quantity rather than pointwise curvature.

## Verification and disposition

Run:

    python research/voevodsky/check_radar_curvature_inverse.py

All 28 exact Fraction controls passed: metric polarization from labelled
probes, label-loss hostiles, temporal-stencil reproduction/bias, adversarial
noise amplification, transfer-series coefficients and the conditional resolution
schedule. Receipt: `research/voevodsky/radar-curvature-inverse.json`.

The continuum small-baseline theorem, discontinuity proof and error budget are
written mathematics. The checker does not derive an instrument's noise floor,
validate a physical bandwidth prior, or prove a general inverse-spacetime theorem.

The selected inverse leaf is resolved in scope: exact recovery is possible,
but raw-data completion does not preserve pointwise curvature. A nonredundant
successor is a finite-resolution observation contract: fix the actual causal
record and declared processing, retain its explicit error amplification, and
ask which observational distinctions that protocol preserves without claiming
it is an exact instantaneous curvature measurement.
