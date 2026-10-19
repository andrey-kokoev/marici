# Multi-object orbital continuation — iteration 2 of 5

## Orbital-record follow-up

`orbital-record-selfenergy.md` adds a distinct-orbital scalar triple channel,
with its exterior-power free Hamiltonian, Vandermonde-weighted spectral measure
and certified self-energy. It is not the vector triple channel computed below.

## Result

The genuine two-/three-object channels now have **certified infinite-volume
on-band self-energies at the common energy E=6**. A declared typed encounter
fixture gives normalized bright-channel scattering probabilities. All **24
checks pass**; source hashes are current.

These remain conditional free half-line object channels, not photon channels
or a derived native interaction law.

## 1. Fresh inputs and the propagating bands

Freshly read `multiobject-orbital-selfenergy.md` and its checked receipt. Retain
independent orbital Hamiltonians H_k=sum_a h_a, with two-object band [0,8] and
three-object band [0,12], and the product-endpoint vertices.

The endpoint spectral measures have densities rho_k=rho_1 convolved k times,
where rho_1(x)=sqrt(x(4-x))/(2pi) on [0,4]. E=6 is strictly inside both bands.
No finite-volume poles or artificial imaginary broadening are used here.

## 2. Real and imaginary parts at a common energy

Write

    g_2(6+i0)=a_2-i b_2,  b_2=pi rho_2(6),
    g_3(6+i0)=    -i b_3,  b_3=pi rho_3(6).

The three-object real part vanishes exactly by reflection symmetry of the
spectral density about its band center 6. This is a property of this endpoint
measure, not an assumption about all channel real parts.

For the pair real part, integrate the exact one-body retarded response first:

    g_1(z)=[z-2-sqrt((z-2)^2-4)]/2,

with the branch satisfying g_1(z)~1/z at infinity. At z=6-x+i0 the real part is
(4-x)/2, minus sqrt((4-x)^2-4)/2 for x<2. Since the endpoint mean x is 2,

    a_2=1-(1/2) integral_0^2 rho_1(x) sqrt((4-x)^2-4) dx.

This has no remaining principal-value singularity. The density calculations use

    rho_2(6)=integral_0^4 rho_1(x)rho_1(6-x) dx,
    rho_3(6)=integral_[0,4]^2 rho_1(x)rho_1(y)rho_1(6-x-y) dx dy.

Both are strictly positive. The convolution and one-body spectral representation
justify these boundary values; they are not obtained by taking a finite-box
resolvent to a real pole.

## 3. Certified integration, not a quadrature-difference estimate

Use equal energy cells with n=128,256,512 per coordinate. On every cell, enclose
the radicand x(4-x), including its interior maximum at x=2 and the zero extension
outside [0,4]. Enclose each nonnegative square-root product by integer square
roots at fixed scale 10^12. Multiply the resulting ranges by exact cell volumes.

Pi is enclosed by Machin's identity

    pi=16 arctan(1/5)-4 arctan(1/239),

using rational alternating-series bounds. All integrations and endpoint bounds
are rational. The lower/upper integral sums contain the continuum value even at
support boundaries. Successive mesh widths decrease, but that observed convergence
is not the source of the error certificate.

An independent exact control is

    rho_2(4)=8/(3pi^2), Re g_2(4+i0)=0.

Its density lies inside every corresponding box enclosure. Pair-density reflection
rho_2(2)=rho_2(6) is also checked.

Readable outward-rounded n=512 enclosures are

| Quantity | Certified containing range |
|---|---|
| rho_2(6) | [0.1169074, 0.1184042] |
| rho_3(6) | [0.2183979, 0.2215448] |
| Re g_2(6+i0) | [0.5126259, 0.5199241] |

The receipt retains tighter exact rational endpoints. These error bars are
intentionally visible; no extra precision is inferred from a decimal midpoint.

For arbitrary real declared couplings, the self-energies are

    Sigma_in=lambda_in^2 (a_2-i b_2) I_4,
    Sigma_2 =lambda_2^2  (a_2-i b_2) P_s,
    Sigma_3 =lambda_3^2  (-i b_3) P_v.

Their widths are Gamma=-2 Im Sigma, positive on the appropriate typed sectors.

## 4. A declared common-energy scattering fixture

For a constructive normalization test, choose

    H_core=6 I_4,
    lambda_in=lambda_2=lambda_3=1.

These choices are explicit fixture parameters, not energies or couplings derived
from the native annulus/pentachoron records. H_in=V tensor conjugate(V) has scalar
projector P_s of rank one and vector projector P_v of rank three.

Use normalized bright channel fibers, with

    S=I-i Gamma^(1/2) G_core Gamma^(1/2).

The scalar sector couples the incoming pair to the two-output channel. Its
reflection and transmission probabilities at E=6 are

    R_s=a_2^2/(a_2^2+b_2^2),
    T_s=b_2^2/(a_2^2+b_2^2).

The vector sector couples the incoming pair to the three-output channel:

    D_v=a_2^2+(b_2+b_3)^2,
    R_v=[a_2^2+(b_2-b_3)^2]/D_v,
    T_v=4 b_2 b_3/D_v.

Both identities R_s+T_s=1 and R_v+T_v=1 hold exactly. They follow by expansion of
the displayed expressions, equivalently from the core optical identity
G-G^dagger=-i G Gamma G^dagger. Rational controls independently test the latter
probability identity. Certified interval propagation contains the exact sums.

For unpolarized incoming rho=I_4/4, scalar weight is 1/4 and vector weight 3/4:

    P_2=T_s/4,
    P_3=3T_v/4,
    P_survival=R_s/4+3R_v/4.

Outward-rounded containing ranges are

| Outcome in this fixture | Probability range |
|---|---|
| Two output objects | [0.08251, 0.08699] |
| Three output objects | [0.53581, 0.56594] |
| Incoming pair survives | [0.35289, 0.37672] |

Their exact correlated values sum to one. Independently propagated interval
endpoints need not sum to one; this is not a probability deficit or excess.
The ratio lies in [0.14580,0.16235], not near the supplied working ratio 372.
No empirical comparison is warranted without physical channel identification,
input preparation and a derived vertex/coupling law.

## 5. What is and is not normalized

These are energy-fiber incoming-flux probabilities. They are not the retained
bound-subspace weights of a central-only preparation. Independent multi-object
coordinates enter through their convolution density and hence their widths.

Only bright combinations coupled to the finite endpoint vertex participate in
the core scattering. Orthogonal dark orbital fibers remain free channels. The
four central coordinates do not claim to span the full multi-object continuum.

The product endpoint attachment still reaches only separately symmetric orbital
and internal states. A scalar three-object channel with antisymmetric internal
and orbital records needs the distinct vertex described in the preceding typed
audit; the present vector three-output channel is not that vertex.

## 6. Next nonredundant continuation

Extend controlled self-energy evaluation away from the band center and test
energy-dependent flux, channel thresholds and core/coupling sensitivity. Then
construct an orbital-record-retaining alternative vertex, rather than collapsing
all output objects into one endpoint mode. A source-bound native full-spinor
attachment remains a separate obligation.

## Reproduction

```sh
python research/voevodsky/checkers/check_multiobject_onband.py
```

Receipt: `results/multiobject_onband.json`, with exact pi and continuum integration
enclosures, mesh refinement controls, typed self-energies and normalized flux
fixture probability bounds.
