# Good full-band scattering does not preserve the retained point sector

[Contract](contracts/enriched-bound-sector.v1.json) · [exact support checker](check_enriched_bound_sector.py) · [receipt](results/enriched-bound-sector.v1.json)

## Result

The [nine-state enrichment](RESONANT-NATIVE-ENRICHMENT.md) has full-band scattering error <=1/4 under the supplied positive three-chain laws. Its **coupled point spectrum nevertheless has dimension three, not the native five**, counting eigenvalue multiplicity. All these modes lie above E=4 in stored K units.

| Coupled point sector | Native eleven-state | Enriched nine-state |
|---|---:|---:|
| Exact symmetric sector | 2 | 2 |
| Antisymmetric sector | 3 | 1 |
| Total | 5 | 3 |

These are counts for the actual infinite-chain model, not the earlier closed-core pole counts. No finite-chain truncation or numerical root scan is used. The native five-mode result is a comparison replay; the new disposition concerns the enriched model, not a change to C2/C5 or their fixed native operator.

Let J be the nine-state core isometry extended by identity on all lead sites, and let P_b,n and P_b,9 be the respective point-spectrum orthogonal projections. On the native ambient Hilbert space,

```
||P_b,n - J P_b,9 J-sharp|| = 1.
```

This is a maximal **spectral-classification projector gap**, not a claim of unit error for a named preparation, a common outgoing effect, or the same embedded finite-time state. The dimension witness need not lie in Ran(J). Incoming/outgoing scattering profiles and central retained preparations are different comparisons.

The exact symmetric coupled sector remains identically intertwined. Belt and carrier-sum preparations therefore retain their native point weights exactly. For normalized initially central single-carrier characters,

```
w_native(carrier)-w_9(carrier)
    = (w_native(carrier_difference)-w_9(carrier_difference))/2.
```

The antisymmetric weights are **not computed here**. Mode counts do not determine them. Their full-tail normalization is the next executable comparison.

## 1. Decaying-lead Schur reduction, with the contact shift retained

For E>4 write s=exp(-kappa), 0<s<1, so

```
E(s)=2+s+1/s,
psi_(j,n)=(-s)^n x_j,     n>=1.
```

The first lead equation is satisfied because `(E-2)(-s)+s^2+1=0`. Substitution into the core contact equation yields

```
M(s)x=0,
M(s)=E(s)I-K-(1+s)P.
```

The +P core contact and the decaying lead self-energy both matter. At the upper edge the matrix is

```
M(1)=4I-K-2P,
```

not the bare closed-core matrix 4I-K. The checker explicitly verifies the formula and refuses the missing contact term even though a wrong formula could accidentally give the same mode count in a particular fixture.

Every kernel vector at 0<s<1 gives a square-summable tail, and every above-band eigenvector has this unique decaying form. Multiplicities are therefore the kernel dimensions of M(s).

## 2. Exact counts without root isolation

In the inherited positive metric,

```
dM/ds=(1-1/s^2)I-P < 0,    0<s<1.
```

The first scalar coefficient is strictly negative and P is a nonnegative orthogonal projector. As s tends to zero, M(s) tends to positive infinity. Each ordered eigenvalue decreases strictly toward its value at s=1. Every negative edge eigenvalue therefore crosses zero exactly once, counting multiplicity. No zero edge eigenvalues occur in this fixture.

The exact weighted edge inertias are:

| Sector | Native (+,-,0) | Enriched (+,-,0) |
|---|---|---|
| Full core | (6,5,0) | (6,3,0) |
| Symmetric core | (3,2,0) | (3,2,0) |
| Antisymmetric core | (3,3,0) | (3,1,0) |

The negative counts give the displayed coupled above-band mode counts. Sector bases, invariance under K and P, and weighted self-adjointness are freshly checked.

There are no other point modes. The positive edge-difference quadratic form excludes negative eigenvalues. At E=0,4 or inside (0,4), a square-summable solution of the identical free lead recurrence must vanish on each lead. Its port values vanish by the endpoint equations; its core would be an invisible eigenvector. The visible cyclic dimensions are eleven and nine, which excludes such a vector. Thus the above-band count exhausts the point spectrum. This does not assert a new singular-continuous/completeness theorem or complete escape of all central preparations.

## 3. Projector gap and the exactly preserved preparations

J is isometric in the inherited metrics, so `J P_b,9 J-sharp` is an orthogonal projection of rank three on the native space. P_b,n has rank five. The restriction of the former projection to the latter's range has a kernel of dimension at least two. On those native point vectors the projection difference acts as identity; the difference of any two orthogonal projections has norm at most one. This proves the exact gap.

The source and enriched symmetric coupled models are unitarily identified by J. Functional calculus therefore intertwines their point projections on that sector, including complete tails and normalization. The common symmetric point dimension is two; all missing point dimensions occur in the antisymmetric comparison. The projector-gap witness cannot be assumed to be a particular visible port character or a representable reduced initial state.

The normalized single-carrier character is an equal orthogonal sum of carrier-sum and carrier-difference characters. Both point projections reduce this decomposition and agree on the symmetric summand, proving the half-weight difference formula. This does not calculate the remaining antisymmetric weight or imply that a quarter bound on outgoing scattering is a quarter bound on retained probability.

## 4. Full-tail normalization for the next weight audit

For an above-band root s and core vector x, the complete norm is

```
||Psi||^2 = x*H_core x + [s^2/(1-s^2)] x*H_core P x.
```

For a normalized initial central vector v, the mode weight is

```
|x*H_core v|^2 / (x*H_core x + [s^2/(1-s^2)]x*H_core P x).
```

For an unnormalized v divide also by v*H_core v. Sum over a fully normalized orthogonal mode basis, or use spectral projectors for degeneracy. Neither the tail factor nor hidden-coordinate metric may be discarded. This supplies a concrete next task: certify the native/enriched carrier-difference retained weights using isolated decaying roots and these full norms.

## Verification boundary

The checker binds a freshly replayed enrichment certificate, verifies the positive metrics/cores, visible cyclicity, weighted contacts, sector invariance, exact edge inertias and source embedding/adjoint identities. The analytic recurrence, monotone crossing count, projector-rank argument and functional-calculus consequences are documented mathematics, not machine-formalized proofs. No finite-chain spectrum or fitted overlap is used as evidence.

The native owner receipts and historical ancestor warning are preserved. C1–C12 and budgets are unchanged; no high-energy protocol cycle is run. No physical detector/species/capture law is admitted. A change in mathematical bound-sector rank must not be relabeled as a photon multiplicity or physical branching ratio.

```sh
python -S research/scattering/low-energy/check_enriched_bound_sector.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_enriched_bound_sector.py
```
