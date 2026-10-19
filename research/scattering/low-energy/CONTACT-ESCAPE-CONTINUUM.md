# Contact escape continuum: complete local release and a retained bound cloud

[Contract](contracts/contact-escape-continuum.v1.json) · [checker](check_contact_escape_continuum.py) · [receipt](results/contact-escape-continuum.v1.json)

## Result and changed model

The finite [graded contact code](GRADED-CONTACT-VERTEX.md) now has an explicit self-adjoint **infinite escape completion**. In a declared weak-coupling regime an initially occupied encoded contact pair leaves every finite contact neighborhood and has a complete free outgoing asymptote. A second positive-energy example instead retains an exactly calculable bound cloud. Neither conclusion deletes a record or replaces unitary evolution by a decay channel.

This is a **new Jacobi escape model**, not a derivation of physical photon dispersion or native encounter dynamics. The lattice coordinate, band, boundary form factor and coupling strengths are explicit added inputs. The finite-band trapped state must not be identified with physical capture or binding merely because its weight is nonzero.

## 1. Operator and preparation

For each active singlet/triplet component replace the selected finite output mode by a half-line. Use source site 0 and output sites n>=1:

```
(H psi)_0=epsilon*psi_0-g*psi_1,
(H psi)_1=2*psi_1-g*psi_0-psi_2,
(H psi)_n=2*psi_n-psi_(n-1)-psi_(n+1), n>=2,
epsilon=3.
```

The minus sign of g is a lead phase convention. The active total operator is one singlet copy with g_s and three identical triplet copies with g_t. The inherited photon-profile/helicity labels are internal channel data; charge, C, fermion parity and native rotations are preserved. The twelve typed fermion spectators and the sixty-dimensional raw-pair complement from the prior construction remain separate, unchanged sectors. Complete release below is **not** asserted for arbitrary states in these spectators.

H is a bounded self-adjoint Jacobi operator on the full half-line; no finite truncation or absorbing boundary is used. The output lead has absolutely continuous band [0,4] and dispersion E(k)=2-2*cos(k). This is not physical photon dispersion E=|p|. Its spectral representation can be paired with the preceding relative-photon profiles at energy E, but their physical energy measure and source coupling envelope have not thereby been selected. A lattice site is not yet an independently calibrated photon separation coordinate.

The initial state in each active block is the localized bare source e0. It has

```
<H>=epsilon=3,
Var_H(e0)=g^2.
```

It is **not a sharp total-energy eigenstate**. This is a model of contact release, not silently the same preparation as a physical energy-sharp incident electron/positron beam. A time-independent self-adjoint H conserves its full spectral energy distribution; it need not conserve the uncoupled bare energy label at each instant. Physical incoming wavepackets, source occupation and total-momentum normalization are still unbound.

## 2. Positivity and exact spectral measure

On finite-support vectors (a,b1,b2,...),

```
<psi,H psi>
=|b1-g*a|^2+(epsilon-g^2)*|a|^2
 +sum_(n>=1)|b_(n+1)-b_n|^2.
```

Thus the tested g^2<3 examples are nonnegative Hamiltonians. The stronger g^2=4 diagnostic has a negative-energy bound state and is not admitted as a positive-energy model.

For the free Dirichlet output lead let m(z)=<1,(L-z)^-1 1>. It solves

```
m^2-(2-z)*m+1=0,
m(z) ~ -1/z at infinity.
```

For E in (0,4), its upper boundary value is

```
m(E+i0)=[2-E+i*sqrt(E*(4-E))]/2.
```

The source resolvent and its continuous spectral density are

```
G00(z)=1/[epsilon-z-g^2*m(z)],
rho_g(E)=(g^2/2)*sqrt(E*(4-E))
         / {pi*[(epsilon-E-(g^2/2)*(2-E))^2
                 +(g^4/4)*E*(4-E)]}.
```

For g!=0 this density is positive throughout the open band. The algebraic resolvent has no embedded poles or singular-continuous part; possible discrete masses are outside the band. At epsilon=3:

- a below-band eigenvalue exists exactly when g^2>3;
- an above-band eigenvalue exists exactly when g^2>1;
- equality gives a nonnormalizable threshold resonance, not a bound state.

These statements follow from strict monotonicity of epsilon-z-g^2*m(z) on each exterior interval and its endpoint signs. A g=0 source is instead a decoupled embedded eigenstate at 3; it cannot be grouped with weak nonzero couplings.

The source is cyclic for every g!=0: the Jacobi recurrence generates each site from e0. Consequently its spectral measure describes the whole active block. The normalization comes from G00(z)~-1/z and its pole residues via Stieltjes inversion, not from a finite-time numerical plot.

## 3. Weak channels really escape locally

Choose the **declared test values**

```
g_s=1/2, g_t=1/3.
```

Both are strictly inside 0<g^2<1. There is no point spectrum and no singular-continuous spectrum on any active block, so every initial encoded-pair component is ac. The spectral densities are integrable with nonsingular endpoint denominators. Riemann–Lebesgue gives source amplitude tending to zero. Each fixed lead-site amplitude is another Fourier integral of a bounded polynomial times this density, so every finite contact neighborhood empties as t -> +infinity.

The coupled operator differs from a decoupled source plus free half-line by finite rank. The trace-class scattering theorem supplies complete ac wave operators. Their adjoints send the initial active state to a free outgoing lead asymptote with the **same norm**, here one. Free half-line propagation carries that asymptote away from finite neighborhoods; no sink has been inserted.

This removes the finite invariant-subspace recurrence of the preceding code without destroying global reversibility. Time-reversing an appropriately coherent incoming radiation state can refocus the source. The theorem is local escape plus a unitary outgoing description, not a globally irreversible quantum channel or a calibrated annihilation rate.

## 4. Positive coupling can still retain a bound cloud

Keep the singlet weak but choose triplet g_t=sqrt(2). Then g_t^2=2<3, so positivity survives. There is exactly one above-band eigenvalue. An unnormalized eigenvector has

```
u0=1,
u_n=g*r^n, n>=1,
(1-g^2)*r^2+(epsilon-2)*r+1=0,
r=(1-sqrt(5))/2,
E_b=2-r-1/r=2+sqrt(5).
```

The other polynomial root has modulus greater than one and is not an admissible tail. Exact normalization, including the infinite tail, gives

```
||u||^2=1+g^2*r^2/(1-r^2)=sqrt(5),
Z=||P_bound e0||^2=1/sqrt(5).
```

The initial source therefore has:

| Quantity | Late-time value |
|---|---|
| Total retained bound norm | Z=1/sqrt(5) |
| Local pair-site probability | Z^2=1/5 |
| Retained lead-cloud norm | Z-Z^2=1/sqrt(5)-1/5 |
| Freely outgoing ac norm | 1-Z=1-1/sqrt(5) |

The source-site amplitude's ac part decays, leaving Z*exp(-i*E_b*t); the bound lead tail remains too. **One minus local pair survival is not the escaped fraction.** In this example it is 4/5, strictly larger than the actual outgoing norm. The difference is a trapped lead cloud, not independent asymptotic radiation.

The checker verifies the exact root, eigenvalue, recurrence, and geometric-tail norm identity at several truncation points **with the remaining tail included**. The spectral argument is analytic; no truncated chain spectrum is mistaken for the infinite operator.

## 5. Preparation and branch accounting remain conditional

For the preceding invariant pair density rho(p)=p*Ps+(1-p)*Pt/3, the all-weak model has outgoing two-/three-sector norms p and 1-p. This reflects complete escape into the one output channel assigned to each irrep by the added CAR/C model. It does not select p, give a coupling-independent law for other theories or determine an experimental branching ratio.

With the positive bound-triplet example the accounting becomes

```
outgoing two norm=p,
outgoing three norm=(1-p)*(1-Z),
retained bound norm=(1-p)*Z,
local pair probability=(1-p)*Z^2.
```

The first three sum to one. Counting everything except the local pair site as escaped would be wrong. Conditional detector counts, time windows, incident flux and physical spin/charge preparation remain separate obligations.

## 6. Verification and next nonredundant gate

Exact checks cover the scalar resolvent boundary identity, spectral endpoint classifications, native irrep boundary covariance, a positive quadratic-form witness, the full bound tail and preparation norm accounting. General self-adjointness, spectral inversion, cyclicity, local decay and wave-operator completeness are documented mathematical arguments using the stated analytic theorems, not machine-formalized claims or finite numerical experiments.

The [unbounded photon-energy tail audit](PHOTON-ENERGY-TAIL.md) now constructs phase-volume-compatible orthogonal output channels: arbitrarily small positive tails remove the cutoff-induced point sector while finite-time operator error stays at most |delta*t|. Its envelope and strength are explicit postulates, not source selections. The [total-momentum successor](TOTAL-MOMENTUM-PACKET.md) now supplies a full imported Fock packet; the [covariant lift](COVARIANT-ESCAPE-LIFT.md) now supplies active lab dynamics under added velocity/mass postulates. Next audit local source support and bind preparation, source envelope and physical propagation. The Jacobi boundary semicircle is a chosen coupling spectral measure, not automatically a physical photon density of states. An energy-dependent form factor can absorb different measure conventions; it still needs an independently specified source amplitude. In particular, test whether the above-band residue survives replacing the hard band with an unbounded photon-energy continuum having nonzero ultraviolet tails. Nor does appending a total-energy envelope by itself identify a physical CM wavepacket. Check normalization/self-adjointness, ultraviolet behavior, thresholds and residual bound modes before calling the completion physical photon propagation. No fitted cutoff, g ratio or 372 target is admitted.

Source licensing, local/cluster support, physical incident preparation and dimensional calibration remain open; full imported photon packets and active lab dynamics now exist conditionally. C1–C12, exhausted C12 effort, paused high-energy execution and historical owner warnings are unchanged. No physical annihilation or capture outcome is admitted.

```sh
python -S research/scattering/low-energy/check_contact_escape_continuum.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_contact_escape_continuum.py
```
