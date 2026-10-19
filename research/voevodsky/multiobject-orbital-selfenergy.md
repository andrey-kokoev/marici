# Multi-object orbital continuation — iteration 1 of 5

## On-band follow-up

`multiobject-onband.md` now certifies retarded continuum self-energies at the
common propagating energy E=6 and normalized typed-fixture flux probabilities,
with 24 checks. These are infinite-volume boundary values, not finite-box poles.

## Result

Constructed genuine independently moving two-/three-object half-line channels,
with explicit spin-compatible endpoint vertices and their infinite-volume
self-energies. **41 checks pass**, including exact finite Hamiltonians, occupation
metrics, labelled/symmetric operator agreement, spectral moments and certified
below-band resolvent enclosures. Source hashes are current.

This is a declared free-channel model, not a derivation of photon dispersion,
physical positrons, or a coupling to the native eleven-state scalar core.

## 1. Fresh state and channel types

Freshly read `typed-spin-channels.md` and its checked source-bound receipt. Retain
its incoming representation V tensor conjugate(V), scalar/vector projectors
P_s,P_v, and maps M_2,M_3 satisfying

    M_2^dagger M_2=P_s, M_3^dagger M_3=P_v, P_s+P_v=I_4.

The output internal test representation W has dimension three. All three Lie
and both source-cycle covariance controls belong to the preceding receipt.
It remains an SU(2) vector test representation, not a photon polarization space.

## 2. Independently moving orbital Hamiltonians

On ell^2(N_0), with ghost amplitude f(-1)=0, declare

    (h f)(n)=2f(n)-f(n-1)-f(n+1).

This bounded positive Dirichlet half-line operator has spectrum [0,4]. It is the
same simple dispersion convention used for the preceding one-coordinate leads,
not an inferred physical energy or length scale.

For k objects set

    H_k = sum_(a=1..k) h_a.

There are k independent coordinates (n_1,...,n_k), including configurations with
objects at different sites. The energy is the sum of their one-body energies;
the band is [0,4k]. Nothing restricts them to n_1=...=n_k.

The input pair channel is ell^2(N_0)^tensor2 tensor H_in, with distinguishable
objects as a declared convention. Its band is [0,8].

Output channels are the full symmetric spaces

    Sym^k(ell^2(N_0) tensor W), k=2,3,

with H_k acting on positions and identity on internal records. The resulting
bands are [0,8] and [0,12]. H_k commutes with whole-object exchange and rotations.
The vertices below reach the separately orbital-symmetric/internal-symmetric
subspace. This is an invariant subspace of the full object space, not a claim
that other orbital/internal symmetry sectors do not exist.

## 3. Endpoint vertices and a bounded full Hamiltonian

Let b_k=|0>^tensor k, a normalized symmetric orbital state. Attach a four-state
encounter core through

    B_in x = lambda_in b_2 tensor x,
    B_2 x  = lambda_2 b_2 tensor M_2 x,
    B_3 x  = lambda_3 b_3 tensor M_3 x.

These are finite-rank bounded vertices. The lambdas are explicit real coupling
parameters; their magnitudes are not supplied by native geometry or by 372.

With any declared Hermitian H_core on H_in, the full operator on core plus the
three channel spaces is

    H = [ H_core   B_in^dagger  B_2^dagger  B_3^dagger ]
        [ B_in     H_incoming  0           0          ]
        [ B_2      0           H_2         0          ]
        [ B_3      0           0           H_3        ].

It is bounded and self-adjoint. Positivity of the *uncoupled* orbital operators
does not by itself prove positivity of this coupled block operator. Core levels
and couplings must be checked before making a claim about below-band bound modes.

This four-state encounter construction is not an unnoticed identification with
the native eleven-state collective core. A native attachment map and compatible
full-spinor central generator remain required for that identification.

## 4. Infinite-volume spectral measure and self-energies

The one-body sine transform has endpoint weight (2/pi) sin^2(theta) dtheta,
with energy E=2-2cos(theta). Hence the normalized endpoint density is

    rho_1(E)=sqrt(E(4-E))/(2pi), 0<E<4,

and zero otherwise. Independence gives the *energy-sum* measure

    rho_k = rho_1 * ... * rho_1  (k convolutions).

This measure has total mass one. It is not a copy of rho_1 with a channel label.
For z off [0,4k], define

    g_k(z)=integral_0^(4k) rho_k(E)/(z-E) dE.

Equivalently it is a k-fold sine-transform integral with denominator
z-sum_a(2-2cos(theta_a)). Exact Schur elimination now gives

    Sigma_in(z)=lambda_in^2 g_2(z) I_4,
    Sigma_2(z) =lambda_2^2  g_2(z) P_s,
    Sigma_3(z) =lambda_3^2  g_3(z) P_v,

    G_core(z)=[zI-H_core-Sigma_in-Sigma_2-Sigma_3]^-1,

where defined. These are matrix-valued self-energies with the required typed
projectors, rather than scalar labels silently attached to the old leads.

For Im z>0, Im g_k(z)<0. The retarded boundary law is

    g_k(E+i0)=PV integral rho_k(x)/(E-x) dx - i pi rho_k(E),
    Gamma_k(E)=-2 Im Sigma_k(E+i0)
              =2pi lambda_k^2 rho_k(E) P_k >= 0.

Thus the spectral law and dissipative sign follow from a positive infinite-volume
measure. No finite-box poles are interpreted as continuum widths.

## 5. Genuine multi-object thresholds

Near the lower edge rho_1(E)~sqrt(E)/pi. Convolution and the beta integral give

    rho_k(E) ~ [Gamma(3/2)^k/(pi^k Gamma(3k/2))] E^(3k/2-1).

In particular

    rho_2(E)~E^2/(8pi),
    rho_3(E)~2 E^(7/2)/(105pi^2).

The densities are symmetric under E->4k-E, so the analogous upper-edge laws
hold. Their different thresholds cannot be recovered by assigning both channels
the old one-body lead self-energy. These are laws of this chosen free half-line
model, not universal physical multi-particle threshold predictions.

## 6. Exact finite checks retain mixed configurations and their metric

Use L=4 sites per object, with Dirichlet upper truncation. The symmetric orbital
basis is indexed by occupations nu with sum nu=k. Its basis vector is the
unnormalized sum of all labelled configurations of that occupation, so

    Gram_nu = k! / product_j nu_j!.

The compressed Hamiltonian is self-adjoint in this Gram, not necessarily in the
unweighted coordinate metric. The checker constructs it from single-object hops
and verifies exact agreement with the labelled tensor-sum operator.

| Objects | Labelled dimension | Symmetric orbital dimension |
|---|---:|---:|
| 2 | 16 | 10 |
| 3 | 64 | 20 |

Both Gram-weighted H_k and 4kI-H_k are positive definite in these finite controls.
Mixed-position occupations are explicitly retained. Finite spectral quadrature
also agrees with the exact rational endpoint inverse.

## 7. Certified infinite-volume resolvent values

The one-body endpoint moments are Catalan numbers C_(n+1): 1,2,5,14,42,... .
The k-body moments are their binomial convolutions:

    m_(k,n)=sum_j binomial(n,j) m_(k-1,j) C_(n-j+1).

Mean energy is 2k and variance k. A rescaled diagonal collective lead would
instead have variance k^2; the checker distinguishes these constructions.

Spectral reflection at the endpoint identifies the moments of 4kI-H_k with
those of H_k. For s>0 this supplies a positive series

    g_k(-s)=-sum_(n>=0) m_(k,n)/(s+4k)^(n+1).

After N+1 terms, the omitted magnitude is at most

    (4k/(s+4k))^(N+1)/s.

The checker uses N=384 and exact rational arithmetic. Finite and infinite
moments agree through degree 2L-1; this is separately checked, not assumed.

Representative certified values are

| Channel orbital count | g_k(-1), approximately |
|---|---:|
| 2 | -0.220594664533506 |
| 3 | -0.1535456819531 |

The three-object enclosure has width below 4.2e-14; all six reported enclosures
at z=-1,-2,-4 have widths below 1e-12. Exact rational endpoints are retained in
the receipt. Decimal views may round distinct bounds to the same floating number.
Multiply these scalar values by lambda_k^2 and the appropriate projector to
obtain the corresponding self-energy matrices.

## 8. Next executable gate

Evaluate the on-band convolution densities and principal-value real parts with
controlled errors; then build a declared typed core scattering fixture and check
its open-channel optical identity and energy-dependent normalized probabilities.
Incoming preparations must specify their scalar/vector weights. Additional
orbital vertices are needed to access the scalar three-object witness from the
previous audit. Native coupling and physical interpretation remain separate gates.

## Reproduction

```sh
python research/voevodsky/checkers/check_multiobject_orbital_selfenergy.py
```

Receipt: `results/multiobject_orbital_selfenergy.json`, including source hashes,
finite occupation Hamiltonians and metrics, endpoint moments, infinite-volume
self-energy formulas and exact below-band enclosures.
