# EF1-B: a relative quantum coordinate unitary, not yet an emission operator

[Contract](contracts/relative-photon-measure.v1.json) · [checker](check_relative_photon_measure.py) · [receipt](results/relative-photon-measure.v1.json)

## Result and assumptions

The [classical CM completion](CM-SEPARATION-MAP.md) now has an explicit quantum **coordinate** continuation on its three-output, symmetric-reference-geometry branch. A positive Jacobian supplies a linear unitary between declared relative-coordinate Hilbert spaces. There are explicit normalizable Bose-symmetric conditional profiles, and coherent phases have an observable effect that an incoherent mixture would miss.

This imports standard massless Lorentz-invariant phase space, photon symmetrization and a measurable polarization frame. It does **not** derive these from native geometry, select an incoming native amplitude, supply a physical interaction, or construct a wavepacket in the total four-momentum. All examples are conditional relative states at fixed future-timelike total momentum, not normalizable full Fock-space states.

## 1. Weight ratios and the exact measure

Keep the preceding three 120-degree seed directions. Use positive projective weights

```
(w1,w2,w3) proportional to (1,u,v),  u,v>0,
D=u+v+uv.
```

For final energy fractions e_i=E_i/M, define y_i=1-2*e_i. The CM formula gives

```
y1=uv/D,  y2=v/D,  y3=u/D,
y_i>0,  y1+y2+y3=1,
u=y1/y2,  v=y1/y3.
```

Thus the open positive weight-ratio quadrant is in bijection with the interior energy simplex. Its absolute chart Jacobian is

```
|d(y1,y2)/d(u,v)| = uv/D^3.
```

For example, the numerator matrix of the derivatives, with common denominator D^2, is

```
[ v^2       u^2 ]
[-v(1+v)     u  ].
```

Its determinant is uvD. This cleared polynomial identity is checked exactly, not inferred from numerical differentiation.

At fixed M, labelled massless three-body Lorentz-invariant phase space is flat in two independent invariant masses. With normalized orientation Haar measure dR,

```
dPhi3 = M^2/(128*pi^3) dy1 dy2 dR,
Phi3_total = M^2/(256*pi^3),
dnu3 = dPhi3/Phi3_total = 2 dy1 dy2 dR.
```

Here R rotates the ordered completed reference configuration. The shape-dependent choice of reference body frame does not change normalized Haar measure. The normalization assumes the standard convention `(2*pi)^4 delta^4(P-sum p) product[d^3p/((2*pi)^3 2E)]`. The conventional identical-particle factor 1/3! cancels when conditioning and normalizing within this sector; it must not be discarded in a later calculation of unnormalized interaction rates.

The pullback density is therefore

```
rho(u,v)=2uv/(u+v+uv)^3,
dnu3=rho(u,v) du dv dR.
```

The standard phase-space formula and general change-of-variables argument are documented analytic inputs; they are not machine-formalized or source-native theorems.

## 2. A coherent coordinate unitary, with the half-density included

Declare the labelled relative spaces

```
Hseed=L2(du dv dR),
H3=L2(2 dy1 dy2 dR).
```

The flat seed reference measure is a declared coordinate convention, **not a native preparation law**. Define

```
(Uf)(y,R)=f(u(y),v(y),R)/sqrt(rho(u(y),v(y))),
(U^-1 psi)(u,v,R)=sqrt(rho(u,v))*psi(y(u,v),R).
```

Both maps are linear; the positive half-density preserves phases and inner products. Since the chart is a bijection of open domains and the Jacobian is strictly positive, they are inverse unitaries. Omitting the half-density is not unitary for these measures. Alternatively one may equip the seed space directly with rho du dv dR, but that is a different explicitly stated convention.

This acts only on the specified weight-ratio/orientation coordinates. Any common seed scale, additional phase, parent geometry or residual record is an external retained tensor factor on which the map acts as the identity. This is not a quantization of the entire general EF1-B map with its records removed.

## 3. Bose symmetry and helicities

First construct U on labelled spaces, then restrict to the Bose subspace. Permuting the three reference rays is represented by a proper rotation of their plane in three-dimensional space; its accompanying right action on R preserves Haar measure. Weight permutation also changes the projective chart. In particular

```
(12): (u,v) -> (1/u,v/u),  |det DT|=1/u^3,
(23): (u,v) -> (v,u),      |det DT|=1.
```

The checker verifies rho(T(u,v))*|det DT|=rho(u,v). In flat seed coordinates the transported permutation representation includes its square-root Jacobian. Merely declaring f(u,v) symmetric while omitting that factor would not be the correct Bose condition.

The profiles below are invariant under every y permutation and independent of R. Choose all photon helicities equal in a fixed measurable, momentum-local polarization frame, so permutations also preserve the helicity labels. They define symmetric scalar coefficients in that assumed photon sector. This does not identify their total angular momentum, prove physical Lorentz/helicity intertwining, or bind any native spinor preparation. In particular no map from a lone spin-half input into an integer-spin photon sector is being asserted.

## 4. Explicit normalized profiles and a phase-sensitive test

Let S2=y1^2+y2^2+y3^2, and use dnu3. The exact simplex identity

```
integral 2*y1^a*y2^b*y3^c dy1 dy2
=2*a!*b!*c!/(a+b+c+2)!
```

gives

```
<S2>=1/2,  <S2^2>=4/15,
psi0=1,
psi1=sqrt(60)*(S2-1/2),
<psi_a,psi_b>=delta_ab.
```

Both functions are Bose-symmetric and square integrable. Their pullbacks sqrt(rho)*psi_a are orthonormal seed-coordinate wavefunctions. This is an explicit two-dimensional coherent code in an assumed continuous relative-output Hilbert space, **not an identification with the native spinor code**.

For psi_plus/minus=(psi0 +/- psi1)/sqrt(2), the expectation of the bounded symmetric observable S2 differs by

```
<psi_plus,S2 psi_plus>-<psi_minus,S2 psi_minus>=1/sqrt(15).
```

The incoherent equal mixture of psi0 and psi1 lacks this interference term. The checker also normalizes (psi0+i*psi1)/sqrt(2) and evaluates the actual half-density map at exact field-valued anchors. It does not replace a coherent state by its probability distribution.

For two outputs, use normalized solid angle dnu2=dOmega/(4*pi). The even functions

```
chi0=1,
chi1=sqrt(5)*(3*cos(theta)^2-1)/2
```

are orthonormal and invariant under the photon exchange n -> -n. These are conditional two-ray angular profiles with equal helicities, not a selected angular distribution or a relative two-versus-three amplitude.

## 5. Normalization does not select a spectrum

For additional explicit positive symmetric examples, set

```
|psi_alpha|^2 = C_alpha^2 * product_i y_i^(alpha-1),
C_alpha^2 = Gamma(3*alpha)/(2*Gamma(alpha)^3),  alpha>0.
```

For alpha=1 this is constant density; for alpha=3 it is 2520*y1^2*y2^2*y3^2. Both integrate to one. They have

```
<E_i/M>=1/3,
Var(E_i/M)=1/[18*(3*alpha+1)].
```

Thus the variances are respectively 1/72 and 1/180 under the same conservation, symmetry and phase-space assumptions. These are example states, not two derived physical predictions. As an explicit negative control, take the correctly normalized alpha=3 state's seed pullback and omit the half-density when mapping it back. The resulting target squared norm is 8/55, not one; the checker evaluates this simplex integral exactly. An independently specified preparation/interaction must choose the amplitude, including its phase. Fitting alpha or a general profile to observations is not a source derivation.

The exact equal-area EF1-B configuration is a single energy shape. A delta at that point is not an L2 relative state: its support has zero measure, whereas a nonzero L2 equivalence class cannot be supported on a null set. Promoting it to a finite-width normalized profile requires an additional input; the measure alone supplies no width.

## 6. Remaining executable gates

The coordinate/normalization gap is narrowed, not the physical encounter solved. The [native-pair audit](NATIVE-PAIR-INTERTWINER.md) now constructs isometric diagonal-native-group maps into both two- and three-output Bose **scalar coefficient** spaces. Shape-only scalar profiles cannot retain the pair triplet, and the finite symmetry does not select multiplicity. The [three-photon](THREE-PHOTON-HELICITY.md) and [two-photon](TWO-PHOTON-HELICITY.md) helicity continuations now construct conditional relative rotation maps, carefully distinguishing finite native symmetry from continuous physical total spin. The [native charge/preparation audit](NATIVE-CHARGE-PREPARATION.md) now leaves pair C sign and preparation correlations unselected by the inspected sources. The [graded contact extension](GRADED-CONTACT-VERTEX.md) now constructs that finite Hermitian vertex under explicit statistics/charge postulates, but exhibits recurrence and leaves independent coefficients. The [Jacobi completion](CONTACT-ESCAPE-CONTINUUM.md) now supplies conditional local escape and bound-cloud retention, but its band/envelope and energy-uncertain preparation still need physical/source binding before claiming an emission law. A full outgoing Fock wavepacket additionally requires an independently supplied square-integrable distribution over total four-momentum and consistent helicity transformations. No such distribution is silently supplied by fixing M. The [total-momentum successor](TOTAL-MOMENTUM-PACKET.md) now explicitly supplies a normalizable imported Fock packet and coarea isometry, not a source-selected envelope or physical incident state.

Conditional sector normalization does not determine relative sector probabilities. Phi2=1/(8*pi) and Phi3=M^2/(256*pi^3) are dimensionful phase-space factors with different dimensions, not a branching ratio. Contact amplitudes, their dimensions, spin selection, incoming flux and detector binding are still missing.

C1–C12 and the exhausted C12 protocol remain unchanged; high-energy execution remains paused. Owner receipts and historical source warnings are untouched. EF1-N remains rejected under its original literal-normal readout.

```sh
python -S research/scattering/low-energy/check_relative_photon_measure.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_relative_photon_measure.py
```
