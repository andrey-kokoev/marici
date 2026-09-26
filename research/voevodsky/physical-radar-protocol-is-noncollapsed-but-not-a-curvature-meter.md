# Physical finite radar is noncollapsed, but its shape reading is not curvature alone

## Result

Fresh resume selected `physical-radar-protocol-noncollapse:v1`.
The previously frozen nine-record protocol now has a certified nonzero reading
from an exact vacuum wave with the same initially-resting preparation as the
flat static reference. This establishes noncollapse on the physical source
image, not merely on arbitrary numerical packets.

A separate moving-detector control in exactly flat spacetime also has nonzero
reading. Therefore nonzero finite radar-shape acceleration is not equivalent
to nonzero curvature. The distinction survives exact null propagation and
correct proper-clock factors.

## Unchanged protocol and physical source class

Keep epsilon=1/32, the labelled vectors (3,0),(0,4),(3,4), proper emission times
3/4,1,5/4, and the instantaneous null-return convention. No coefficients or
probe schedule were fitted after inspecting results.

Freshly read the general vacuum and observer formulas in
`two-polarization-shear-selects-area-and-parallel-frame.md`. For

    ds^2=-2du dV+p(u)^2 dX^2+q(u)^2 dY^2,

vacuum is p''/p+q''/q=0. With initial frame I, parallel transverse frame
F=diag(1/p,1/q), and central proper clock tau=sqrt(2)u,

    E=diag(-p''/(2p),-q''/(2q),0).

Einstein dynamics, wave shape, corner data and observer preparation remain
supplied. These are explicit members of the prior general Rosen source class,
not claims that the fibration selects a metric. The new wave is not a member
of the particular beta_n high-frequency sequence; its own domain bounds are
proved below.

### A nonflat initially-resting wave

Choose a=1/4 and

    p(u)=cosh(a u), q(u)=cos(a u).

Then p''/p=a^2, q''/q=-a^2, hence Ric=0 exactly, and

    E_wave=diag(-1/32,+1/32,0).

At u=0, gamma=I and gamma'=0. The constant-transverse-coordinate worldlines
(u,V,X)=(u,u,b) and central worldline b=0 are exact timelike geodesics, initially
at rest relative to the initial orthogonal connector, as in the prior source.
They have proper time sqrt(2)u. This wave and the static flat reference thus
share initial baseline and velocity preparation.

### A curvature-free moving control

Choose p=q=1+a u. Then p''=q''=0 and E=0. This is explicitly Minkowski space under

    x=(1+a u)X, y=(1+a u)Y,
    v=V+(a/2)(1+a u)(X^2+Y^2).

Constant Rosen transverse labels still describe inertial worldlines, but their
relative velocities are now nonzero: gamma'(0)=2a I. This change in preparation
is declared, not conflated with the initially-resting comparison. Initial
baseline lengths still agree because gamma(0)=I.

## Exact null response and certified clock records

For the wave, each leg with transverse displacement (b_x,b_y) and starting u=t
has duration h satisfying the prior strictly monotone equation

    2h=b_x^2/S_x(t,h)+b_y^2/S_y(t,h),
    S_x=[tanh(a(t+h))-tanh(at)]/a,
    S_y=[tan(a(t+h))-tan(at)]/a.

Its residual derivative is at least 2. On 0<=u<=2,

    (1/2)I < gamma < 2I,

because cos(1/2)^2>1/2 and cosh(1/2)^2<2. Thus every leg has
|b|/2<h<|b|. The last emission u is 5/(4 sqrt(2)); adding twice the largest
baseline 5/32 still leaves u<2. No caustic or unproved extrapolation is crossed.
All 18 wave legs are bracketed and enclosed.

For the moving flat control, let d=|b| and

    alpha=[a d^2+sqrt(a^2 d^4+8d^2)]/4.

Direct integration gives

    h_out=(1+a t)alpha,
    h_back=(1+a t)(1+a alpha)alpha,
    R=(1+a t)alpha(2+a alpha)/sqrt(2).

The two legs need not have equal duration. Substitution into the null-leg
equation verifies the expressions; the displayed Minkowski transformation
independently identifies the spacetime and inertial preparation.

For both sources the exact reception clock is tau_e+2R. The receipt stores
rational lower/upper enclosures of every reception, a rational rounded clock
record, and its distance and processed-output error bounds. The rounded clocks
are NOT represented as the exact irrational physical clocks.

## Arithmetic certificate

`check_physical_radar_protocol.py` uses rational interval arithmetic with outward
rounding to a 2^-80 grid. All comparisons deciding the signs are rational.
Floating-point conversions are for the displayed summary only.

- exp(x) on [0,1]: degree-24 Taylor polynomial, remainder at most
  3*x^25/25!, using exp(x)<3;
- sin/cos on [0,1/2]: degree-24 Taylor polynomials, absolute remainder at most
  x^25/25!;
- tanh(x)=(exp(2x)-1)/(exp(2x)+1), with denominators bounded away from zero;
- square roots: integer-square-root rational brackets checked by squaring;
- null roots: 48 bisection steps, retaining uncertain starting-event bounds.

If a midpoint residual enclosure straddles zero, the residual derivative lower
bound gives a containing root interval instead of selecting an unsupported sign.
For residual interval [l,r] at m, that interval is

    [m-max(r,0)/2, m+max(-l,0)/2].

The completed outgoing enclosure is retained when solving the return leg.
This is an executable enclosure certificate with a written analytic justification,
not proof-assistant certification or empirical optical validation.

## Physical readouts

The output ordering is (Y_11,Y_12,Y_22), where Y is the frozen proper-time
second-difference radar-shape reading. Rounded displays of the certified ranges:

    initially-resting wave:
      (-0.0339685665925, +0.0001418149424, +0.0284243270562)

    flat moving control:
      (-0.0323053641577, -0.0005156044515, -0.0326659977838)

    flat static reference:
      (0,0,0) exactly.

The wave interval widths are below 6e-13, and the moving-control widths are
smaller; the receipt retains the exact rational endpoints. Zero is excluded
from both wave diagonal readings and both moving-control diagonal readings.
The wave's positive Y_22 also separates it from the moving flat control's
negative Y_22. Noncollapse is therefore established by actual ideal source
solutions, not by assigning arbitrary clock errors.

At the same time, E_wave has zero off-diagonal component and constant diagonal
values +/-1/32, while its finite Y differs from those values. The moving
control has E=0 but nonzero Y. Even its two diagonal Y components differ despite
isotropic gamma, because the frozen probes have different finite lengths and
the light-travel response depends on those lengths. No pointwise-curvature
interpretation follows from the output's three-component matrix representation.

## Direct section comparison and closure scope

For each rounded physical packet, the independent native-section readout agrees
exactly with the source time-first reading. The earlier finite-protocol bound
controls the difference between this rounded reading and the ideal physical
reading. Hence the source/section comparison now has nontrivial physical
instances, not only the zero flat fixture or synthetic perturbations.

The finite-protocol continuity theorem still applies to these records and their
actual source-image completion. This does not restore the discontinuous inverse
to pointwise curvature or prove the owner's entire recursive constructor bridge.
No owner artifact was edited and no owner adoption is inferred.

## Verification and next gate

Run:

    python research/voevodsky/check_physical_radar_protocol.py

All 18 checks passed. Receipt: `research/voevodsky/physical-radar-protocol.json`.
It retains all clock enclosures, rounded packets, output bounds, 18 wave-leg
certificates and source hashes.

This resolves physical noncollapse for the frozen ideal protocol. The next
comparison gate is frame versus apparatus change: determine the transformation
law when the SAME physical probes are relabelled, versus when a new oriented
probe set is used. Finite radar-shape fits must retain actual probe geometry;
a matrix-shaped output is not automatically an apparatus-independent tensor
of spacetime. This is a genuine readout-coherence question for the carrier
comparison, not another request to approximate pointwise curvature.
