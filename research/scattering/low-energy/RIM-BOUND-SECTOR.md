# Full rim point sector: accessible bound modes are not the whole core

[Exact checker](check_rim_bound_sector.py) · [receipt](results/rim-bound-sector.v1.json)

## Audit verdict

The [autonomous source](../../strominger/neutron-autonomous-rim-scattering.md) already retained the nineteen-dimensional dark complement and explicitly reported its six zero-energy source-bank directions. It did **not** assert that the two computed accessible levels exhaust the full point spectrum. This audit is not a correction to that source and does not rewrite its numerical receipts.

For the same supplied principal fixture, the exact source matrices and the argument below give:

| Point sector | Dimension, counting multiplicity | Location |
|---|---:|---|
| Pure-core dark bank modes | 6 | E=0, below the supplied threshold 1/2 |
| Other pure-core dark modes | 13 | E>1/2, embedded in the continuum |
| Accessible exponentially decaying modes | 2, distinct and simple | 0<E<1/2 |
| **Full point subspace** | **21** | 8 below threshold; 13 embedded; none at threshold |

These are not twenty-one distinct energies, particles, or physical binding products. In particular, an embedded pure-core mode is not an incoming capture product. C1/C4 concern incoming threshold scattering, not release of every core preparation.

No new numbered conjecture is needed to record this source/model coverage audit. C1–C12 and their edges remain unchanged, C12's exhausted protocol is not renewed, and no high-energy protocol is executed.

## Fixed operator and exact split

Use exactly the principal two-channel point contact, not the unequal-threshold control:

```
Hilbert space: [L2(R) tensor C2] direct-sum C24,
theta=1/2, kappa=1, eta=2, ell=1, hbar=1.
```

In the original rational core chart, its physical norm is `x* M x / 3`. Write B for the two contact columns and `S=B^T M/3` for their adjoint; `SB=I2`. Thus `P=BS` is the positive metric-orthogonal contact projection. The boundary equations are

```
psi'(0+)-psi'(0-)=2(psi(0)-Sx),
E x=(K+2P)x-2B psi(0).
```

The checker freshly verifies C1's source hashes and positive metric, then independently generates `V=span{K^m B}` over Q. Its dimension is five. It constructs the M-orthogonal complement D by exact nullspace elimination, with dimension nineteen, and verifies

```
K V=V K_b,       K D=D K_d,       S D=0,
P_D=D(D^T M D)^(-1)D^T M,
P_D^2=P_D,       P_D K=K P_D,     P_D B=0,
P_D+P_V=I24.
```

The inherited metrics are positive because their basis columns are independent and M is positive. Exact symmetric congruence checks show K is nonnegative. On D they give

```
inertia(H_d K_d)                 = (13 positive,0 negative,6 zero),
inertia(H_d (K_d-theta I))        = (13 positive,6 negative,0 zero).
```

The six standard zero-mode core coordinates are precisely 18 through 23 (zero-based). Every eigenvector in D extends to a full eigenstate with identically zero lead field. The finite-dimensional metric spectral theorem supplies nineteen eigenvectors counting multiplicity; a general superposition in D need not be stationary but never emits into the leads.

## Exact count and isolation of the two accessible levels

For E<theta put `q=sqrt(theta-E)>0`. Every square-integrable lead solution, by continuity at the origin, has the form

```
psi(x)=exp(-q |x|) u,
u=Sx/(q+1).
```

Substitution into the core equation gives, on the five-dimensional accessible sector,

```
F(q)=K_b+(q^2-theta)I+[2q/(q+1)]P_b.
```

In its positive inherited metric, `P_b` is a positive orthogonal projector of rank two, freshly checked. For q>0,

```
F'(q)=2q I+2/(q+1)^2 P_b > 0.
```

Thus all five weighted secular eigenvalues increase strictly. Exact congruence gives inertia (3,2,0) at q=0 and (5,0,0) at q=1; positivity persists for q>1 by monotonicity. There are exactly two roots on q>0, counted with multiplicity, and no unseen far-decaying root.

The checker bisects rational decay intervals using the **full five-dimensional** inertias, not numerical seed energies. It isolates a unit inertia change in each of two disjoint energy intervals of width at most 10^-12. All retained endpoints are nonsingular and both intervals lie strictly between zero and theta. This also proves that the two modes are distinct and simple. Their approximate energies agree with the source table:

```
E1 ≈ 0.239564867092
E2 ≈ 0.406258480176
```

The rational intervals in the receipt, not these displayed decimals, are the certificates. For a mode with core x and lead boundary u, the full norm includes both infinite tails:

```
||x||_(M/3)^2 + ||u||^2/q.
```

Central normalization alone would give wrong spectral weights. This audit does not compute those weights or claim a retained percentage for the accessible preparations.

## Why this exhausts the point spectrum

The reducing dark and accessible spaces split the full operator as `K_d direct-sum H_accessible`, leaving all continuous lead coordinates in the latter.

For E>theta an L2 solution of the free lead equation must vanish on each half-line. At E=theta the affine solutions also vanish if L2. Continuity and the jump condition then imply `psi=0` and `Sx=0`, while `Kx=Ex`. An invisible K eigenvector is orthogonal to every K^m B and hence belongs to D; there is no such nonzero vector in the accessible space. The dark inertia excludes E=theta as well. These statements concern square-integrable eigenstates, not an assignment of flux at zero velocity.

For E<theta, all L2 lead solutions were included in the exponential elimination. Exact monotone counting exhausts its accessible roots. Combining these two simple modes with the nineteen dark modes therefore exhausts the **point** subspace. The essential spectrum starts at theta. Relative to free leads plus K, at any negative resolvent energy the difference solves the homogeneous lead ODE away from the contact. Its continuous lead field is in the span of two decaying Green functions, and its core component is finite-dimensional. The resolvent difference consequently has finite rank (the loose bound 26 suffices); the compact-resolvent-difference form of Weyl's theorem preserves the essential spectrum. The thirteen pure-core modes above theta are accordingly embedded, not states above the top of a finite lead band. Here the continuum is unbounded above, unlike the three-chain model.

## Preparation consequence: an exact retention lower bound

For any normalized initially central preparation x0, set `d0=P_D x0`. The dark component evolves as `exp(-it K)d0` in the original core chart (equivalently under K_d in D-basis coordinates), remains core-supported and preserves its norm. Its core vector stays metric-orthogonal to the accessible component. Consequently, at every time,

```
P_core(t) >= ||P_D x0||_(M/3)^2.
```

For x0 in D this is identically one. For x0 in the contact span B it gives zero, not a claim of complete escape: the two accessible bound modes can still contribute. Incoming asymptotic scattering states have no dark component and do not autonomously capture into an orthogonal point subspace under this stationary Hamiltonian. Capture would require a different admitted preparation or energy-exchange operation.

## Remaining gate and verification boundary

This establishes the full point-sector count and the dark retention bound for the fixed supplied contact. It does **not** establish absence of singular-continuous spectrum, wave-operator completeness or the outgoing asymptote of every non-point component. Those are a nonredundant next analytic audit; C2's discrete three-chain theorem cannot simply be transplanted here. In particular, the point interaction is not a bounded finite-rank perturbation of the continuum Hamiltonian: a completeness argument must handle its finite-rank **resolvent** difference instead.

The checker replays finite rational identities, inertias and root brackets. The self-adjoint contact setup, elementary L2 lead classification and finite-dimensional spectral/monotonicity argument are documented mathematics, not machine-formalized analysis. It never imports NumPy/SciPy, reruns a source-owner stationary solver, changes a historical receipt, assigns a neutron mass or selects a physical continuum law.

```sh
python research/scattering/low-energy/check_rim_bound_sector.py --check
python -m unittest discover -s research/scattering/low-energy -p test_rim_bound_sector.py
```
