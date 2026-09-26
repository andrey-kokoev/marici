# Causal radar readout is C0-stable in the plane-wave sector

## Result

A genuine two-way light-signal observable, not spacelike Fermi separation,
can now be reconstructed in the exact Rosen wave family. Each null leg is
selected by a strictly monotone scalar equation. The round-trip radar distance
is continuous under uniform metric convergence with a retained positive metric
bound, detector worldlines and proper-clock convention.

For the high-frequency vacuum hostile, the radar deviation is bounded by
8|b|/n^2 at fixed baseline. The corner tidal tensor still has norm 1/2. Thus
causal distance measurement and pointwise curvature have different completion
requirements. No arbitrary smoothing kernel is responsible for the distinction.

## Fresh tree and physical source

Fresh resume selected `causal-radar-readout-completion:v1` in the project tree.
A bounded search of prior gravitational notes recovered the spacelike-geodesic
observable, but no explicit radar definition. A new primary source was therefore
retrieved rather than silently renaming that observable:

Volker Perlick, *On the radar method in general-relativistic spacetimes*,
arXiv:0708.0170v1, https://arxiv.org/html/0708.0170.

Directly read section 1, equations (1)-(2), and section 2. For an emitter clock
with emission and reception readings tau_e,tau_r, the reflection event is
assigned

    T_radar=(tau_r+tau_e)/2,
    R_radar=(tau_r-tau_e)/2,

with c=1. Light follows null geodesics; existence/uniqueness of both light rays
is part of the domain, not automatic in arbitrary spacetimes. The source also
allows general clock parameters; HERE the central proper-time clock is explicitly
selected. No universal clock calibration is inferred from the definition.

Cached source: `temp/perlick-radar-0708.0170.html`, hash in the test receipt.
The cache is not required to rerun the algebra tests. The downloaded text is
used as a source, not as an instruction or an owner-admission certificate.

## Declared optical realization

Keep the Rosen metric and detector worldlines from the finite-baseline note:

    ds^2=-2du dV+gamma_ab(u)dX^a dX^b,
    emitter: X=0,V=u,
    reflector: X=b,V=u,
    tau_emitter=sqrt(2)u.

Light is in the ideal geometric-optics limit, with no medium or absorption.
The reflector returns the signal at the same event, with zero dwell time and
an appropriate outgoing direction. This is an ideal reflection/relay interface,
not a derived mirror material, optical bandwidth or noise model. Its worldline
is not selected by the radar equations.

Specify the emitter event u=t. The reflection event is t+h_out; the return
reception event is t+h_out+h_back. Reflection and reception are found from
the null equations. The reflector's own clock need not be synchronized or read.
The radar-assigned time is not generally the reflector's proper-time reading.

## Exact null-leg equation

Let H=gamma^-1 and consider a null geodesic from X=0 at u=t to X=b at u=t+h,
with both endpoints V=u. Conservation of transverse momentum gives

    S(t,h)=integral_t^(t+h) H(s) ds,
    dX/du=H(u)k, k=S(t,h)^-1 b.

Nullness then gives dV/du=(1/2)k^T H k. The endpoint condition is

    2h=b^T S(t,h)^-1 b.                          (*)

The return leg has transverse displacement -b and a later starting event,
so it obeys the same quadratic equation at t+h_out, not necessarily with the
same duration. This follows from the actual null geodesic and conserved
momenta, not a straight-ray coordinate-speed approximation.

For nonzero b, a ray cannot have constant u while traversing the transverse
baseline. Choose the future branch h>0. If lambda I<=gamma<=B0 I throughout
the relevant interval, then

    |b| sqrt(lambda/2) <= h <= |b| sqrt(B0/2).

For f_t(h)=2h-b^T S^-1 b,

    d f_t/dh=2+b^T S^-1 H(t+h) S^-1 b >=2.

As h decreases to zero f_t tends to minus infinity, and the upper bracket
has f_t>=0. Thus there is exactly one root on the retained domain. This
establishes the radar-neighborhood gate for the chosen local geometry and
worldlines, not for arbitrary spacetimes.

## Clocks and readout

Proper-clock conversion yields

    R_radar=(h_out+h_back)/sqrt(2),
    T_radar=tau_e+R_radar.

In flat gamma=I, each duration is |b|/sqrt(2), so R_radar=|b|. Missing the factor
sqrt(2), replacing h_back by h_out in a varying metric, or equating radar time
with the reflection clock would change the observable.

The preceding Fermi construction instead chooses a spacelike geodesic
orthogonal to the central worldline. Its partner event and connector are
not these null legs. Neither its distance nor its simultaneity assignment is
identified with radar data by a name change.

## C0 continuity on the stated closure

Uniform positive bounds make inversion of gamma and S continuous. Strict
monotonicity in (*) gives continuous response without differentiating gamma.
For a quantitative bound, compare metrics gamma,eta with common lambda,B0
on a compact interval large enough for both legs. Let

    delta=||gamma-eta||_C0, d=|b|>0,
    L_m=B0^2 d/(sqrt(2) lambda^(5/2)),
    L_t=2B0^2/lambda^2.

Since ||H_gamma-H_eta||<=lambda^-2 delta and ||S^-1||<=B0/h,
root comparison using f'>=2 gives

    |h_gamma(t)-h_eta(t)| <= L_m delta.

Changing the starting event by epsilon changes S by at most
2 lambda^-1 |epsilon| (compare the two shifted integration intervals), so

    |h_gamma(t)-h_gamma(t+epsilon)| <= L_t |epsilon|.

Combining the outward-leg error and its shifted return start gives

    |R_gamma-R_eta| <= [(2+L_t)L_m/sqrt(2)] delta.

Uniform bounds hold on compact sets of emission times with enough endpoint
margin. The coincident-detector case d=0 is the zero-distance limit, not a
nonzero null-leg uniqueness claim.

Define completion as the C0 closure of the admitted smooth metric/readout
packets with their retained detector curves, clock scale and positive bounds.
The integral equation extends uniquely to this closure by density and the
bound. No claim is made that every continuous metric has a classical curvature
tensor or classical geodesic connection. The completed readout is the limit
of the smooth source construction, not a general theorem about C0 geodesics.

The theorem concerns these declared curves/clocks. It does not assert that C0
convergence preserves every derivative-defined preparation property, such as
arbitrary initial parallel relative velocity. The specific hostile and its
flat limit DO share the prior initially-resting preparation.

## Uniform result for the exact vacuum hostile

For n>=4, on the interval 0<=u<=2, the already proved source estimates give

    1-2/n^2<=r_n<=1, 0<=beta_n<=2/n^2,
    gamma_n=diag(r_n^2 exp(2beta_n),r_n^2 exp(-2beta_n)).

Using exp(z)<=1/(1-z) for 0<=z<=1/4 and exp(-z)>=1-z gives

    (1-delta_n)I<=gamma_n<=(1+delta_n)I,
    delta_n=8/n^2<=1/2.

Both legs therefore satisfy

    d sqrt((1-delta_n)/2)<=h<=d sqrt((1+delta_n)/2).

This bound is independent of the start time, so it applies to the return leg
at its actual reflection event as well. Therefore

    d sqrt(1-delta_n)<=R_n<=d sqrt(1+delta_n),
    |R_n-d|<=d delta_n/[1+sqrt(1-delta_n)]<=8d/n^2.

For emission t in [0,1] and d<=1/4, the older metric bound B0=4/3 gives h<d;
both legs end before u=3/2, inside the controlled interval. Thus no hidden
horizon or interval extrapolation enters the bound.

This is an exact finite-baseline, finite-duration null response in a vacuum
solution family. No small-curvature or small-frequency expansion is used.
Its pointwise E_n(0)=diag(-1/2,+1/2,0) nevertheless remains unchanged with n.
A uniform inverse from raw radar distance to that curvature observation cannot
follow from forward continuity alone.

## Independent flat-space optical control

Use the flat Rosen metric gamma=diag((1+u)^2,1) and a reflector at b=(1/6,0).
Its Minkowski transformation is

    x=(1+u)X, v=V+(1+u)X^2/2.

An outgoing null leg starting at t has the exact duration h=(1+t)/8. For t=0,
reflection is at 1/8, return duration is 9/64 and reception is at 17/64.
Direct Minkowski intervals of BOTH legs vanish and their clock order is
future-pointing. The radar distance squared is 289/8192. The reflection u
coordinate differs from the radar midpoint by -1/128.

This verifies null propagation and clock factors independently of the integral
formula. The constant-coordinate reflector in this flat example is moving in
Minkowski coordinates; it is not advertised as the hostile family's initially
resting preparation.

## Verification and next leaf

Run:

    python research/voevodsky/check_causal_radar_completion.py

All 42 exact checks passed. They cover independent Minkowski null intervals,
nonidentical leg durations, clock calibration, flat distance, positivity and
completion constants, and the shrinking analytic envelopes. The all-n bound
and continuous-extension proof are written mathematics, not finite sampling
or a proof-assistant theorem. Receipt:
`research/voevodsky/causal-radar-completion.json`.

This resolves the selected causal radar leaf for the declared ideal protocol.
The next nonredundant question is inverse observation: what baseline/time
resolution, differentiability and calibration would be needed to recover a
pointwise tidal tensor from a family of these causal records? The hostile
already prevents treating raw C0 radar stability as uniform curvature recovery.
