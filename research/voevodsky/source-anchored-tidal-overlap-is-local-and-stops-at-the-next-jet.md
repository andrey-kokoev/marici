# A source-anchored tidal overlap is local and stops at the next jet

## Result and fresh leaf

Fresh resume selected `source-anchored-tidal-jet-overlap:v1`.
There is a nonempty, explicitly sourced overlap over an observer-local electric
tidal jet. It is NOT an equivalence of Newtonian and relativistic source spaces.

The owner's original fixed Newtonian fixture does not match the Rosen wave:
a rank invariant forbids it. A newly declared pair of positive Newtonian point
sources does match, with explicit calibration and a freely falling local frame.
The agreement controls leading relative acceleration. A spatial derivative of
the tidal field already separates the two sources.

The appropriate structure is therefore a witnessed pair over a common reading
(a fiber product over the tidal jet), not identification of the source fibers.

## 1. Do not silently reuse the old fixture

Freshly read `research/nima/agda/NewtonianTidalFixture.agda`. It declares masses
2 and 1 at radii 3 and 4 along x and y, with denominator 1728. Its tidal tensor is

    E_old=diag(-229,74,155)/1728.

Its determinant is -1313315/2579890176, which is nonzero. The previously studied
Rosen wave p=cosh(u/4), q=cos(u/4) has

    E_wave=diag(-1/32,+1/32,0)

in the retained parallel observer frame. It has rank two. No orthogonal frame
change, nonzero scalar unit change or invertible congruence makes a full-rank
form equal to a rank-two form. Adding an affine Newtonian potential does not
change its Hessian. Thus the old fixed fixture cannot be declared the common
source witness by relabelling components.

## 2. New source data, not new field equations

Keep the supplied Newtonian law with G=1. Declare NEW point sources

    m_x=36 at b_x=(12,0,0),
    m_z=18 at b_z=(0,0,12).

Their potential, with the usual zero-at-infinity convention, is

    Phi(X)=-36/|X-b_x|-18/|X-b_z|.

On the ball |X|<=1 it is smooth and harmonic: both sources are at distance 12.
The source-to-reading formula is the same previously supplied Newtonian Hessian,
not a matrix chosen without a potential:

    Hess Phi(0)=sum_s m_s/r_s^3 [I-3 n_s n_s^T].

Here the weights are 1/48 and 1/96, so

    Hess Phi(0)=diag(-1/32,+1/32,0)=E_wave.

These are new selected source data, not the owner's old a,b literals or an
inferred modification of their admission policy. The operator-authorized own
experiment uses the existing source/kernel/native arithmetic interfaces; no
owner artifact is changed.

## 3. Frame, units and the common local datum

The Newtonian lower jet is also calculated from this actual potential:

    Phi(0)=-9/2,
    grad Phi(0)=(-1/4,0,-1/8).

Choose the instantaneous freely falling, nonrotating observer frame and remove
only the corresponding affine potential:

    Phi_ff(X)=Phi(X)+9/2+x/4+z/8.

It has zero value and gradient at the origin, with unchanged Hessian. Its
quadratic jet is

    Q(X)=(-x^2+y^2)/64.

On the Rosen side retain the central unit observer tau=sqrt(2)u and initial
orthonormal axes: transverse x,y and longitudinal z. The exact vacuum equations
p''/p+q''/q=0 give E_wave above. The factor 1/2 in E comes from the proper-clock
normalization; it is not discarded to force a match.

The shared physical statement is leading relative acceleration:

    Newtonian: delta acceleration = -Hess Phi(0) xi + O(|xi|^2),
    Rosen: Jacobi relative acceleration = -E_wave xi.

Newtonian absolute time is calibrated to the observer's proper time at this
local comparison; no global time identification is asserted. Q represents the
same electric tidal operator with zero lower scalar jet. It is NOT the full
second jet of the relativistic metric, the full Riemann tensor, or a complete
Newtonian replacement for the relativistic field. Other curvature channels
are not identified by this comparison.

No light-propagation law for Newtonian gravity is invented here. The radar
measurements remain on the relativistic side.

## 4. Weak-field qualification and its price

The integer prototype above has |Phi(0)|=9/2, so it must not be advertised as
a global weak-field approximation to a relativistic two-body solution.
There is, however, an explicit family of new Newtonian sources preserving the
same local Hessian:

    b_s -> s b_s, m_s -> s^3 m_s, 0<s<=1.

Then

    Hess Phi_s(0)=E_wave,
    Phi_s(0)=-(9/2)s^2,
    grad Phi_s(0)=(-s/4,0,-s/8).

For example s=1/16 gives |Phi_s(0)|=9/512. This is a physical change of selected
masses and positions in the same units, not an undocumented unit conversion.
The rational family is checked with exact Fraction arithmetic; the Agda source
fixture below certifies the integer prototype and its common numerator.

The controlled source-free ball now has radius s, not a fixed radius. Higher
spatial derivatives grow as s decreases. Thus the weak-potential family does
not license a uniform comparison on one fixed neighborhood or a global
Newtonian/Einstein equivalence. Field equations, boundary/source choices and
dynamical assumptions remain separately supplied.

## 5. Quantitative local approximation and a separating next observation

For the unscaled prototype, |X|<=1 implies each source distance is at least 11.
The third directional derivative of a Coulomb term along a unit vector has
magnitude at most 24m/r^4. Taylor's one-dimensional integral remainder along
s -> sX therefore yields

    |Phi_ff(X)-Q(X)| <= (216/14641)|X|^3.

For the homothetic family on |X|<=s, the corresponding bound is

    |Phi_ff,s(X)-Q(X)| <= [216/(14641 s)]|X|^3.

These are conservative source-derived bounds, not fitted errors.

There is already an exact separation at the next tidal jet:

    partial_x E_Newtonian,xx(0)=partial_x^3 Phi(0)=-1/96,

or -1/(96s) in the scaled family. The z-source contributes zero to this odd
x derivative. Affine frame subtraction leaves it unchanged.

For the wave, the Brinkmann transformation gives

    ds^2=-2du dv+dx^2+dy^2+a^2(x^2-y^2)du^2, a=1/4.

Its curvature components are constant and the connection vanishes on the
central line x=y=0. Thus the covariant curvature gradient, and hence the tidal
gradient with parallel-extended observer/frame at that corner, is zero.
A nonzero tensor cannot be made zero by an invertible frame change.

Consequently, refining the common reading from E to (E,spatial tidal gradient)
separates this matched pair. This is an explicit physical obstruction to
promoting the local tidal match to equality of source germs.

## 6. Relation to radar: a controlled limit, not the frozen finite reading

The earlier frozen nine-clock protocol does NOT already equal E_wave. For the
local comparison, explicitly change to a protocol family centered at proper
time zero, with emission times -h,0,h and baselines epsilon*(3,0),(0,4),(3,4).
The exact geodesic worldlines and analytic metric extend across zero; the
initially-resting preparation is retained at that corner.

Let G_epsilon(tau) be the finite quadratic shape fit from the exact radar rays.
The prior small-baseline theorem yields

    ||G_epsilon(tau)-gamma(tau/sqrt(2))||_max <= C epsilon.

On the fixed wave domain -1<=u<=2, one may use lambda=1/2, B0=2, B1=1.
The earlier radius-response constant is at most 17*sqrt(2)/4<7. With maximum
probe length 5, squaring gives a bound 2625*epsilon on the quadratic probe
values; the design inverse norm 1/8 gives C=2625/8.

For |tau|<=1, the fourth proper-time metric derivative has bound M4=1/64.
At the corner gamma'=0, F=I, so E=-gamma_ddot/2. Hence

    ||Y_epsilon,h(0)-E_wave||_max
      <= 2C epsilon/h^2 + M4 h^2/24.

Choosing epsilon=h^4 and h->0 gives O(h^2) convergence. This is a declared
resolution limit for this fixed analytic source, not uniform recovery on the
high-frequency hostile class.

If calibrated distance errors obey sigma<=epsilon, the previous exact finite
readout bound adds at most

    (17/4) sigma/(epsilon*h^2).

The schedule sigma=h^8 is consequently sufficient for O(h^2) total error.
These are consistency schedules, not claims about achievable hardware precision.
The earliest/latest rays stay in the controlled domain for the small baselines
used here. Time jitter and source uncertainty would need their own bounds.

Thus the common local tidal datum can be approached from this causal readout
under explicit stronger controls. It cannot be recovered continuously from
unrestricted raw radar completion merely because the carrier is reversible.

## 7. Formal and exact verification

`agda/SourceAnchoredTidalOverlap.agda` uses the owner's actual source/kernel
and independently computed native jet operations. It verifies:

- both new direction norms and reciprocal-cube certificates;
- all nine point-source tensor components over denominator 1728;
- all nine independent native components over denominator 8*1728;
- the +/-1/32 normalization identities;
- affine removal of the correctly calibrated lower physical jet.

The lower entries of NT's per-source u-coordinate polynomial jet are NOT simply
called physical potential and gradient. For these equal-radius sources, scalar
entries require a radius-squared factor and first entries a radius factor;
Hessian entries already have the desired normalization. Exact checks verify
this calibration explicitly. The formal physical-jet lower entries are supplied
by the displayed analytic potential calculation, not derived from a false
identity of those normalized rows.

Run:

    python research/voevodsky/check_native_radar_formal.py --overlap --fresh
    python research/voevodsky/check_source_anchored_tidal_overlap.py

The final fresh safe/cubical closure passes, together with the retained-evidence
rejection control. The exact audit passes 48 checks. The vacuum, Taylor,
homothety, covariant-gradient and radar-limit arguments are written mathematics;
no formalization of the whole continuum field theory is claimed.

Two earlier compilations passed but the old overbroad freshness guard detected
concurrent edits to an UNIMPORTED owner file, `RationalComponentArithmetic.agda`.
The checker now audits the actual transitive static imports, compiler-reported
checked sources and library configuration, and reports unrelated copied-source
drift separately. The final required dependency hashes are current. This is a
scope correction, not ignoring a changed proof dependency. No owner file was
modified by this work.

Receipts: `source-anchored-overlap-formal.json` and
`source-anchored-tidal-overlap.json`.

## Disposition and successor

The selected overlap leaf is resolved: the original fixture has an invariant
obstruction; newly declared source data give a controlled common electric tidal
jet; a next-jet observation separates the pair; and the appropriate radar limit
is explicit.

Next, encode this as a retained, typed comparison OVER the common tidal reading,
with distinct Newtonian and Rosen source evidence on its two sides. The common
boundary witness must not imply equality of source packages, and refining the
reading by the tidal gradient must refuse the same identification. This tests
the intended structural synthesis more sharply than another unmarked matrix
comparison or an assertion of a universal foundation.
