# Testing the proposed 5346/3 + 54 route

## Verdict

The belt has a genuine threefold symmetry, and 54-transfer interface maps arise naturally. However, **combining them into 1836 mixes two different arrow-counting conventions**. The tested route does not produce a 1836-coefficient network under the original counting rule.

## The actual symmetry

The 120-degree spatial rotation acts on both triangle placements and the three Cartesian coordinate labels. Its action is free on the 54 coefficient ports at each stage. All three compiled matrices are exactly equivariant, and their selected collective vector is invariant.

This rotation preserves each of the three seed families. It does not identify those families with one another. A separate naive cycle of the three small triangles within each face fails matrix equivariance and is not an alternative justification for division by three.

## Arrow histories versus coefficient entries

The spatial symmetry acts freely on the 5346 original arrows, giving 1782 arrow-history orbits:

| Stage | Original arrows | Arrow-history orbits | Unique quotient coefficient pairs |
|---|---:|---:|---:|
| L | 162 | 54 | 54 |
| G | 2268 | 756 | 252 |
| N | 2916 | 972 | 324 |
| Total | 5346 | 1782 | **630** |

In G and N, three different arrow-history orbits acquire the same source and target quotient ports. Their weights add into a single matrix coefficient. There is no cancellation to zero.

The history-orbit records are retained in the artifact; they are not silently discarded. But they are not three distinct nonzero entries of the quotient coefficient matrix. Counting them as three transfers would adopt a history-labelled multigraph cost instead of the original unique typed coefficient-pair cost.

The quotient itself satisfies GL=LG=N and NGL=N, with a rank-one collective return. Its 630 arrows have the positive closed-cycle deletion certificate. It already closes; no 54-arrow closure defect appears.

## Where 54 genuinely arises

There are 18 quotient ports per stage and 54 original ports. Define

```text
E: copy each quotient coordinate to its three original representatives,
Q: average the three original representatives into their quotient coordinate.
```

Each map has exactly 54 nonzero coefficients. QE=I, and for every original stage A and its quotient Abar,

```text
A E = E Abar,
Q A = Abar Q.
```

The original complete return is recovered on every input:

```text
N_original = E N_quotient Q.
```

Thus the counts using the original coefficient convention are:

- quotient core: **630**;
- quotient with one interface adapter: **684**;
- quotient with both original input and original output interfaces: **738**.

The last is a different, five-step factored implementation, not deletion of arrows inside the old fixed three-stage graph. It therefore does not contradict that graph's 5346-arrow deletion certificate.

The expression 1782+54=1836 instead adds a history-orbit count to a coefficient-adapter count. It is arithmetic, but not the requested same-measure derivation.

## Verification

```text
python research/voevodsky/checkers/check_coupled_six_piece_belt.py
python research/voevodsky/checkers/check_belt_threefold_quotient.py
```

The coupled source was freshly regenerated and its proton regression and deletion certificate passed. The quotient checker passes fifteen exact checks, including equivariance, parallel-history multiplicities, quotient return, stagewise intertwiners and reconstruction of the original full return.

Artifacts:

- `results/belt_threefold_quotient.json`
- `results/belt_threefold_quotient_store.json`

During replay checking, the coupled-source serializer was corrected to canonicalize adjacency keys as strings before hashing; serialized root replay is now explicitly asserted. This changes its packet root, not its geometry, coefficients or 5346 count. The original proton and geometric input artifacts remain unchanged.

This rejects the tested natural C3 quotient-plus-adapter route under the existing counting convention. It is not a proof excluding every conceivable new completion rule.
