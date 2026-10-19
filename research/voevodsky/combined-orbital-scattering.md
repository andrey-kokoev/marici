# Multi-object orbital continuation — iteration 4 of 5

## Off-center response follow-up

`multiobject-energy-response.md` certifies off-center real-axis widths, threshold
closure and complex-energy self-energies with 98 checks. Its finite-eta responses
are explicitly not substituted for real-axis triple principal-value parts; the
on-shell scattering fixture below remains restricted to E=6.

## Result

Combined the two-output, scalar distinct-orbital triple, and vector endpoint
triple channels in a single typed scattering fixture. **43 checks pass**, including
an exact nine-dimensional bright-channel unitarity/covariance control and certified
continuum-derived flux bounds at E=6. All source hashes are current.

The new scalar triple vertex is not merged with the vector triple vertex:
their internal states are orthogonal. Both contribute to the total three-object
probability, without an invented interference term.

## 1. Freshly retained self-energies

Freshly read the orbital-record continuation and load the checked endpoint,
orbital-record and typed-spin receipts. At E=6 write

    g_2=a-i b, g_vector3=-i v, g_A=-i c,

with a,b,v,c strictly positive and enclosed by the preceding infinite-volume
certificates. The scalar-record orbital measure retains its Vandermonde-squared
factor and variance one; it is not replaced by the vector endpoint convolution.

For compact exact arithmetic, response intervals are rounded *outward* to a
rational grid of size 10^-10. The checker verifies enclosure of every original
endpoint; this is not a midpoint approximation or an extra precision claim.

## 2. Declared core and combined self-energies

Retain H_core=6 I_4 and lambda_in=lambda_2=lambda_vector3=1. Vary

    u=lambda_A^2 >= 0.

The scalar and vector core blocks have self-energies

    Sigma_s=[2(a-i b)-i u c] P_s,
    Sigma_v=[a-i(b+v)] P_v.

Their core responses are

    G_s=1/[-2a+i(2b+u c)],
    G_v=1/[-a+i(b+v)].

These are exact Schur responses of the declared infinite channels at E=6,
not an independently assigned transition matrix.

The bright channel multiplicities are three scalar fibers (input pair, two
outputs, scalar three outputs) and two vector fibers of dimension three each
(input pair, vector three outputs). Their total dimension is nine. Dark continuum
fibers remain free and are not discarded from the underlying Hilbert spaces.

## 3. Full optical matrix and covariance

In either sector, for half-widths b_i,

    S_ij=delta_ij-i sqrt(2b_i) G sqrt(2b_j).

For the scalar block b_i=(b,b,u c); for the vector block b_i=(b,v). The full matrix
is S_s direct_sum (S_v tensor I_3).

The identities

    G-G^dagger=-i G Gamma G^dagger,
    S^dagger S=SS^dagger=I

hold algebraically. Independent exact matrix controls use rational detunings and
widths with roots in Q(sqrt(2),sqrt(3),sqrt(5),i). Both multiplication orders,
column probabilities, the core optical identities and full nine-fiber unitarity
are checked without floating tolerances.

Both retained native chiral five-cycle actions commute with the full control
matrix. Scalar/vector mixing is absent. These exact controls certify the optical
construction; the actual E=6 response parameters remain interval-enclosed, not
claimed to equal the rational control values.

## 4. Flux probabilities with the additional orbital-record channel

Set D_s=4a^2+(2b+u c)^2. For scalar input,

    T_s,2=4b^2/D_s,
    T_s,A=4u b c/D_s,
    R_s=(4a^2+u^2 c^2)/D_s.

Their sum is exactly one. For vector input,

    D_v=a^2+(b+v)^2,
    T_v=4b v/D_v,
    R_v=[a^2+(b-v)^2]/D_v,

again summing exactly to one. These formulas include all open bright channels
in each core block; the new triple width also changes the pair and two-output
probabilities through the common denominator.

For unpolarized incoming rho=I_4/4,

    P_2=T_s,2/4,
    P_3,scalar=T_s,A/4,
    P_3,vector=3T_v/4,
    P_3=P_3,scalar+P_3,vector,
    P_survival=R_s/4+3R_v/4.

Certified interval propagation uses the exact normalization identities to
intersect independently obtained ranges. It does not assume independently
extremal endpoint values occur simultaneously.

At unit new coupling u=1, outward-rounded containing ranges are

| Flux outcome | Probability range |
|---|---|
| Two output objects | [0.02517, 0.02961] |
| Scalar orbital-record three outputs | [0.08010, 0.10539] |
| Vector endpoint three outputs | [0.54322, 0.55786] |
| Total three outputs | [0.62333, 0.66325] |
| Incoming pair survives | [0.30715, 0.35150] |

The correlated exact probabilities sum to one. Bounds are visibly finite; the
three-object entries are two orthogonal sectors, not two competing readings of
the same amplitude. Flux probabilities are not retained central-state weights or
incident-wave capture probabilities.

## 5. Coupling sensitivity and a nonmonotone conversion control

The checker sweeps u=0,1/4,1,4,16,64. At zero the scalar triple width vanishes
and the previous fixture is recovered. At u=1 the new channel is certified open
and the two-output probability is smaller than at zero.

Stronger attachment does not indefinitely increase conversion. Differentiate
T_s,A with respect to u to find the unique positive maximum

    u_star=2sqrt(a^2+b^2)/c.

The certified interval is

    u_star in [0.95247,1.09397].

In particular u=64 gives a strictly lower scalar triple probability than u=1,
certified even with the present continuum error bars. As u tends to infinity,
T_s,A tends to zero, T_s,2 tends to zero and R_s tends to one. The orthogonal
vector flux is unchanged throughout the sweep.

This is conditional impedance/resolvent sensitivity, not a fitted physical
coupling law. A topology or channel-count argument alone cannot infer a rate
from the existence of this scalar three-output channel.

## 6. Remaining gates and next continuation

Extend the self-energy evaluation away from E=6, where the triple real parts no
longer vanish. Test threshold opening/closing and energy-dependent optical flux
with the orbital-record measure retained. This is a nonredundant executable
continuation; the current center-energy calculation is not such a test.

Core energy, lattice dispersion, adjacent-site Slater attachment, statistics and
couplings remain explicit choices. A source-bound attachment to the native full
spinor/mismatch generator and physical output-channel identification are still
required before a physical reaction ratio can be claimed.

## Reproduction

```sh
python research/voevodsky/checkers/check_combined_orbital_scattering.py
```

Receipt: `results/combined_orbital_scattering.json`, retaining the exact matrix
control, inherited continuum response enclosures, coupling sweep, probability
bounds and conversion-optimum enclosure.
