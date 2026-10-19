# Multi-object orbital continuation — iteration 3 of 5

## Combined-scattering follow-up

`combined-orbital-scattering.md` now includes this scalar orbital-record channel
alongside the vector triple channel, checking full bright-matrix unitarity,
normalized flux bounds and nonmonotone coupling sensitivity with 43 checks.

## Result

Constructed a **scalar three-object channel that retains distinct orbital
records**, with its genuine independent-motion Hamiltonian and infinite-volume
self-energy. All **25 checks pass**. This supplies the missing alternative to the
previous vector three-output endpoint vertex, without erasing orbital mismatch.

The orbital/internal representation choices and attachment sites remain declared
model inputs. No physical photon identification or native coupling is derived.

## 1. Fresh state and why a new vertex is needed

Freshly read the on-band continuation and the checked orbital and typed-spin
receipts. The preceding product endpoint vertex b_3=|0>^tensor3 reaches symmetric
internal vector outputs. A scalar epsilon_ijk is antisymmetric and vanishes under
Bose projection if every object has the same orbital record.

The earlier typed audit retained a symmetric scalar witness by pairing internal
antisymmetry with three distinct antisymmetric orbital records. Here those records
become actual lattice positions, acted on by the already declared one-body
operator h=2I-shift-shift^dagger, not static labels.

## 2. Exchange-symmetric vertex with independent motion

Use the normalized orbital Slater state

    b_A=|0 wedge 1 wedge 2>
       =(1/sqrt(6)) sum_(a,b,c permutations of 0,1,2)
                           epsilon_abc |a,b,c>.

The normalized internal state is epsilon_ijk/sqrt(6) in W^tensor3. Their product
has amplitudes epsilon_ijk epsilon_abc/6 and is invariant under whole-object
exchange: each factor changes sign. The checker reuses the retained witness and
verifies its norm, exchange symmetry and all three rotation generators.

The output space contains

    wedge^3 ell^2(N_0) tensor wedge^3 W
        embedded in Sym^3(ell^2(N_0) tensor W).

The orbital operator is H_A=sum_a h_a restricted to the exterior orbital space,
with identity on the internal scalar. It has band [0,12]. Independent positions
are retained, subject to orbital antisymmetry; positions are not constrained to
move together. Antisymmetry of one factor is **not** a declaration of fermion
statistics for the whole object.

For the core scalar projector P_s, attach

    B_A x=lambda_A b_A tensor (epsilon/sqrt(6))
                            <vec(I),x>/sqrt(2).

Its Gram is lambda_A^2 P_s. The vertex is finite rank and bounded. Collapsing the
three orbital records to one annihilates it, an exact loss-control check. Internal
contraction with the old vector three-output map is zero, also checked exactly.

## 3. Finite Hamiltonian check with retained positions

For six sites, the orthonormal orbital basis is all increasing triples a<b<c.
There are binomial(6,3)=20 states. The Hamiltonian has diagonal 6 and off-diagonal
-1 for allowed single-site nearest-neighbor hops into an unoccupied site. A hop
cannot cross an occupied position, so no additional reordering sign is hidden.

The checker retains all twenty records, verifies positive definiteness of H_A
and 12I-H_A, and checks eight endpoint moments against the independent
infinite-volume determinant calculation. The finite operator is a validation
control, not the continuum used for the self-energy.

## 4. Infinite spectral measure: the orbital records change the answer

The half-line sine transform satisfies

    phi_1(theta)/phi_0(theta)=2-E,
    phi_2(theta)/phi_0(theta)=(2-E)^2-1,
    E=2-2cos(theta).

The Slater transform is a determinant divided by sqrt(6). Factoring phi_0 from
its columns gives the Vandermonde determinant. Thus the joint energy measure is

    dmu_A=(1/6) product_a rho_1(E_a)
                 product_(a<b)(E_a-E_b)^2 dE_1 dE_2 dE_3,

where rho_1(E)=sqrt(E(4-E))/(2pi) on [0,4]. It has mass one: the determinant of the
one-body orbital Gram is one. Its energy-sum density rho_A is the pushforward
under E=E_1+E_2+E_3, not the simple triple convolution rho_3 of identical endpoint
preparations.

The genuine channel response is

    g_A(z)=integral_0^12 rho_A(E)/(z-E) dE,
    Sigma_A(z)=lambda_A^2 g_A(z) P_s.

It is a negative-imaginary retarded response in the upper half-plane. For real
in-band E,

    Gamma_A(E)=2pi lambda_A^2 rho_A(E) P_s >= 0.

The Vandermonde suppresses coincident one-body energies and encodes retained
orbital structure. Replacing it by one would change the vertex, moments and
self-energy; it is not an innocent coarse graining.

## 5. Exact infinite moments and below-band values

For occupied sites a,b=0,1,2, compute the one-body entries

    K_ab(t)=<a|exp(t h)|b>.

The orbital endpoint generating function is det K(t). Exact derivatives, using
binomial convolution of the entry moments, give the infinite moments m_n. This
is an independent exterior-power calculation, not a floating diagonalization.

Controls establish mass one, mean energy 6 and **variance 1**. By contrast the
old triple product endpoint measure has variance 3. The measures are detectably
different even before computing their boundary values.

Staggering each orbital maps H_A to 12I-H_A and multiplies b_A by a phase only.
Therefore its endpoint measure is reflected about 6. With the same positive
series certificate as iteration 1,

    g_A(-s)=-sum_(n>=0) m_n/(s+12)^(n+1), s>0.

After 385 terms the omitted magnitude is at most (12/(s+12))^385/s. Exact rational
arithmetic certifies all three values at z=-1,-2,-4 with width below 1e-12.
In particular

    g_A(-1) is approximately -0.1459724731374.

The prior triple product value was about -0.1535456819531. This is a change in
the channel response caused by the different vertex, not an energy fit.

## 6. Certified on-band width and thresholds

Reflection gives Re g_A(6+i0)=0 exactly. At E=6 the density is the two-dimensional
integral of the joint measure with E_3=6-E_1-E_2. Rational box integration bounds
both the square-root endpoint weights and all three squared energy differences.
Integer square roots and the rational Machin pi enclosure give an actual error
certificate; differences between meshes are not treated as an error estimate.

For meshes 128,256,512, enclosure widths decrease. The final outward-rounded
containing interval is

    rho_A(6) in [0.37202,0.42150].

These deliberately visible error bars are wider than for the product endpoint
because of the extra polynomial factors. The value is strictly positive: the
retained scalar three-object channel is genuinely open at this energy.

Near the lower edge, the Vandermonde contributes degree six beyond the ordinary
triple-convolution exponent 7/2. The Laguerre/Selberg integral gives

    rho_A(E) ~ 32 E^(19/2)/(14549535 pi^2).

The checker verifies the rational gamma-function coefficient. The analogous
upper-edge law follows by reflection. This strong threshold suppression belongs
to the selected Slater vertex, not a universal three-object law.

## 7. A scalar core can now reach both output multiplicities

With input pair and two-output endpoint channels as before, the scalar core
self-energy can be extended to

    Sigma_s=lambda_in^2 g_2 + lambda_2^2 g_2 + lambda_A^2 g_A.

It now has a genuine scalar three-output channel, without the old invalid
common-orbital split. The old vector triple channel is internally orthogonal and
may be retained separately. There is no silently introduced scalar/vector
interference term.

This does not determine lambda_A, identify a physical three-photon state, or
supply a source-bound map from the native full-spinor central generator.

## 8. Next executable continuation

Insert this scalar orbital-record channel alongside the vector channel in a
declared core scattering fixture. Test matrix optical identities, normalized
flux and sensitivity to attachment records/couplings; tighten the on-band bounds
if needed. Extend self-energy evaluation away from band centers. Retain the
native spin/mismatch-to-core attachment as an explicitly open gate.

## Reproduction

```sh
python research/voevodsky/checkers/check_orbital_record_selfenergy.py
```

Receipt: `results/orbital_record_selfenergy.json`, with exact source hashes,
exterior-power Hamiltonian, moments, below-band enclosures and certified
orbital-record on-band density bounds.
