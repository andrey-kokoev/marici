# Three-record triangle through the native compiler

## Supplied triangle

`agda/ThreeRecordTriangleRegression.agda` instantiates the existing native
normalization route compiler with three distinct record presentation types A, B,
and C. Each carries one Boolean payload. The input includes these link laws:

- A -> B flips the payload.
- B -> C flips the payload.
- A -> C preserves the payload.

The direct link is written separately. Its agreement with the composition is
proved by Boolean case analysis before it receives a coherent-map certificate.
The compiler checks this supplied triangle; it does not discover its link laws.

| Starting payload | Via B | Direct | Terminal payloads agree |
|---|---|---|---|
| 0 | A(0) -> B(1) -> C(0) | A(0) -> C(0) | yes |
| 1 | A(1) -> B(0) -> C(1) | A(1) -> C(1) | yes |

These are two test inputs for the same three-presentation triangle. Three
primitive record presentations is not a claim that the total payload-state
space has cardinality three.

## Native compilation and retention

The via route contains two native comparison steps; the direct route contains
one. Both are compiled by `NativeNormalizationRouteCompiler.compile` and
certified by its `compile-leaves` theorem. Their outcomes agree both by explicit
Boolean calculation and by the existing `effects-agree` theorem.

The route syntax remains distinct: applying a step-count discriminator to an
alleged equality yields true=false. `compare-compilations` keeps both histories
in one joint comparison package, together with the effect witness. Its
`next-comparison-Q` result supplies the next cycle's actual input.

A second native compiler instance at the next universe level runs normalization
and reconstruction on that complete comparison package. The regression checks
that the previous comparison is literally its input and that the two original
routes remain distinct inside it.

| Stage | Package per starting payload | Retained content |
|---|---|---|
| Input | Three linked record presentations | The AB, BC, AC laws and one chosen payload |
| First compilation | One joint comparison package | Direct history (1 step), via history (2 steps), outcome equality |
| Promotion | One next-level Complete input | The whole comparison package |
| Second compilation | One retained compilation package | Two normalization/reconstruction steps and the previous complete comparison as input |

The second route is supplied explicitly. It checks persistence across promotion;
it adds no new link interaction or record-pair generation.

## Conflicting-link test

Change only AC to flip its payload. Then:

- input0 has direct result1 and via result0;
- input1 has direct result0 and via result1.

`bad-direct-disagrees` proves the mismatch at input0, which already refutes
universal agreement. `bad-link-cannot-be-admitted` proves that the bad link
cannot carry a coherent-map certificate for the same fixed A and C coordinates.
Consequently this compiler cannot silently admit the conflicting edge into the
same comparison class. It does not implement a dynamics that repairs the edge.

## What the example establishes

Three linked presentations support comparison of a direct route with a route
through a distinct third record. The resulting relation between routes is
retained as next-level input. Agreement of outcomes preserves the distinction
between their one-step and two-step histories.

This is the first explicit multi-link comparison in this small experiment,
in contrast with the previous four independent Boolean row trajectories. It
is not a proof that three records are minimal for every kind of coherence:
parallel arrows and loops can also carry path comparisons.

The common-coordinate framework already requires admitted maps to be coherent.
The Boolean calculation checks that requirement, and the hostile theorem
exhibits what fails it. Boundary seed availability is inherited from the
existing compiler. No particle, mass or spin identification follows from this
test.

## Verification

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ThreeRecordTriangleRegression -Fresh
```

Fresh verification passed with `--safe --cubical --guardedness` and
`--ignore-interfaces`.

- Source: `agda/ThreeRecordTriangleRegression.agda`
- Receipt: `results/agda-ThreeRecordTriangleRegression.json`
- Log: `results/agda-ThreeRecordTriangleRegression.log`
