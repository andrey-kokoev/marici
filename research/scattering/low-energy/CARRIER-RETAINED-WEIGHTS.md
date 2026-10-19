# Full-tail carrier retained weights: a small named error despite projector gap one

[Contract](contracts/carrier-retained-weights.v1.json) · [exact interval checker](check_carrier_retained_weights.py) · [receipt](results/carrier-retained-weights.v1.json)

## Result and preparation boundary

For the fixed native eleven-state and enriched nine-state **conditional three-chain models**, prepare the unit-normalized carrier-difference character centrally, with all leads initially zero. Its total point-sector weight is certified in these rational intervals:

| Model | Carrier-difference retained point weight |
|---|---|
| Native | [0.120818958780, 0.120818958781] |
| Nine-state enrichment | [0.114712845124, 0.114712845125] |

The native-minus-enriched difference lies in

```
[0.006106113655, 0.006106113657].
```

For **either normalized initially central single carrier**, the exact symmetric contribution is shared, so its retained-weight difference is half of this:

```
[0.0030530568275, 0.0030530568285].
```

Thus the ambient point-projector gap of one from the [point-sector audit](ENRICHED-BOUND-SECTOR.md) is not a unit weight error for these named visible preparations. Nor do the five-versus-three mode counts determine their weights. This is not a bound for every initial state.

These are point-projection weights for central release, not incoming scattering-profile probabilities, physical capture, photon branching fractions or complete escape probabilities. The complement is not identified here with an outgoing asymptote. Absolute single-carrier weights still require the common symmetric contribution; only their difference is determined here.

## 1. Scalar port resolvent and its full-tail residue

Use the normalized antisymmetric compliance from the preceding exact enrichment:

```
m(E)=n(E)/q(E),    q(E)=det(EI-A),
m(E)=<u,(A-E)^(-1)u>/<u,u>.
```

The port projection has rank one and the seed is cyclic. Its core matrix element of the full coupled resolvent `(EI-H)^(-1)` above the band is

```
g(E)=-n(E)/[q(E)+(1+s(E))n(E)],
E(s)=2+s+1/s,     0<s<1.
```

This includes both the +P core contact shift and the decaying lead self-energy. There is no square-summable threshold state to add.

For d=deg(q), define polynomials

```
N(s)=s^(d-1)n((1+s)^2/s),
F(s)=s^d[q(E(s))+(1+s)n(E(s))].
```

The native and enriched secular degrees are eleven and seven. The point-sector audit proves exactly three and one antisymmetric roots respectively in (0,1). Coprimality of n,q excludes a bound root at a bare compliance pole. Single-port cyclicity makes the bound kernels one-dimensional, and the strict monotone Schur derivative makes each secular root simple.

At a root s_*, the positive residue in **energy**, not in decay parameter, is the point weight for the normalized central port preparation:

```
w(s_*) = (1-s_*^2) N(s_*) / [s_* F'(s_*)].
```

Indeed the energy Jacobian is `dE/ds=1-1/s^2`; differentiating the denominator at the root gives the displayed formula. This is a spectral-resolvent residue, not a fitted overlap.

It includes the complete tails. Equivalently choose core vector `x=(A-E)^(-1)u`. Then, with `t=s^2/(1-s^2)`,

```
w=m(E)^2/[m'(E)+t m(E)^2]
 =1/[(1+s)^2 m'(E)+t],
```

using the bound equation `m(E)=-1/(1+s)`. The term t is precisely the geometric lead-tail norm contribution. Omitting it would overstate the enriched mode's weight by **more than 1/2500**; that failure is separately checked. A one-core/one-lead scalar test with A=5 has root s=1/4 and exact full-tail weight 15/16, testing the normalization and Jacobian together.

## 2. Exact root and interval certificates

The starting decay brackets are:

| Model | Disjoint coarse brackets |
|---|---|
| Native | [43/1024,11/256], [67/512,135/1024], [51/256,205/1024] |
| Enriched | [191/1024,3/16] |

Each has a strict exact sign change of F. Their numbers equal the independently proved point-mode counts. Thus each contains exactly one root and no antisymmetric point mode is missing. Numerical exploration located these brackets but supplies no proof evidence.

Fifty exact bisections refine each bracket to width 2^-60. Horner interval arithmetic over Q(sqrt(151)) encloses N, F' and the residue throughout each refined interval. The interval denominator must exclude zero; every mode enclosure is positive. The checker sums all full-tail mode weights, then rounds **outward** to the 10^-12 rational grid by exact field comparisons. No floating-point value is used in the certificate.

For orientation only, the native modes have energies approximately 25.69167, 9.72445 and 7.21592, with weights approximately 0.00000002674, 0.00816645 and 0.11265248. The enriched mode has energy approximately 7.52690 and weight approximately 0.11471285. The weak high-energy mode is included, not silently rounded away. All energies are in stored K units; no dimensional calibration is inferred.

The enlarged model changes its surviving mode as well as removing point dimensions. Consequently the retained-weight difference is not obtained by simply summing the two smallest native weights.

## 3. Single-carrier consequence and remaining task

The preceding point audit establishes that the normalized single-carrier character has equal orthogonal symmetric and antisymmetric weights. Both coupled operators reduce this decomposition, and their symmetric point projections intertwine exactly. Hence

```
w_native(carrier_j)-w_9(carrier_j)
    =[w_native(carrier_difference)-w_9(carrier_difference)]/2,
    j=1,2.
```

This gives the small named-preparation error above without transferring native bound counts or inferring a universal state error. The remaining concrete weight task is to compute the **common symmetric retained contribution**, giving absolute belt, carrier-sum and single-carrier retained weights rather than only equality/difference statements.

## Verification boundary

The checker freshly replays the coupled point audit, binds the exact scalar compliance polynomials, verifies normalized leading coefficients, strict disjoint brackets, exhaustive root counts, derivative-denominator separation, interval positivity and outward rational rounding. Tests cover negative interval division, exact scalar residues, root/scope guards and the actual certificate. Residue spectral interpretation and the previously established functional-calculus/decomposition argument are documented mathematics, not machine-formalized proofs.

No physical law, detector or branching ratio is admitted. C1–C12 and budgets remain unchanged, no high-energy protocol cycle is used, and historical source-owner receipts and ancestor drift remain preserved. The new above-band calculation is part of this fixed low-energy conditional comparison, not execution of the paused high-energy workbench protocol.

```sh
python -S research/scattering/low-energy/check_carrier_retained_weights.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_carrier_retained_weights.py
```
