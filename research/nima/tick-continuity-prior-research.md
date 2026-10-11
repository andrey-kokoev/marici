# Prior-research clues for the Tick evolution bridge

**Current disposition:** this is a historical search record.
`source-to-generator-audit.md` now contains corrected current claims, not the
withdrawn commutant assertion described below. The existing source-backed
unitary realization is `native-square-controlled-hamiltonian.md`; its distinct
image comparison is closed in `tick-unitary-image-nonuniqueness.md`. A formal
analytic interpretation of the dependent return section remains separate.

## Sources inspected

- `source-to-generator-audit.md`: separates operations, algebra policy, and
  a defining continuous module. This is useful architectural guidance, not
  a theorem that fixes the generator. Its assertion that commutation forces
  `H=a PL+b PR` is too narrow: identity and `PL PR` terms also belong to
  the joint commutant. Its discussion of `H` versus `3H` concerns speed,
  not distinct trajectories modulo reparameterization. Do not restore those
  claims from this older audit.
- `../voevodsky/agda/CauchyProductCongruence.agda`,
  `bounded-product-preserves-eventual`: an existing checked joint product
  estimate, with precision depending on bounds of both factors.
- `../voevodsky/agda/CauchyProductWitnessCoherence.agda`,
  `productClassFromDominance-from-presentations`: identifies products of
  supplied bounded presentations with the completion multiplication class.
- `../voevodsky/agda/CauchyCompletionMultiplication.agda`: defines the
  actual multiplication used in the completion-valued polynomial model.

## Implemented consequence

`agda/TickBoundedProductContinuity.agda` combines the product estimate and
presentation-coherence theorem. `BoundedNear d k u v` has truncated bounded
representatives for both values, each of radius exponent `d`, and eventual
precision `k`. No representative is chosen globally.

For exponent bounds `d,e`, output precision `k` is obtained from input
precision

    suc(d+e) + suc(suc(suc k)).

`product-preserves-bounded-near` proves this for the actual completion
multiplication, producing the existing `CompletionNear` relation on outputs.
This is a joint radius-dependent estimate, not global uniform continuity
of multiplication on an unbounded domain.

Fresh `--safe --cubical --guardedness --ignore-interfaces` Agda verification
exits 0, with the pre-existing `TypedGeneratorLayers` export warning.
Include paths: `research/nima/agda`, `research/voevodsky/agda`, both Nima
adapter directories, and Cubical 0.9.

## Next obligations

1. Completed in `agda/TickPolynomialContinuity.agda` and
   `agda/TickJointEvolutionContinuity.agda`: bounded-nearness certificates
   propagate through addition, negation, and products, retaining output
   radius bounds. A circuit computes input precision demands and proves
   joint continuity of the actual `U(a,b,v)` for both varying parameters
   and all four varying amplitudes on explicit bounded regions. This uses
   the defined `BoundedNear`/`CompletionNear` relations, not an unproved
   identification with an independent metric topology. Fresh headless
   closure verification exits 0 with the existing dependency warning.
2. Implemented an explicit glued-chart parameter domain in
   `agda/TickGluedSchedules.agda`: a pushout of two entire completion
   carriers, with the seam mapped by `legs-join`. Coordinate continuity is
   proved against a declared final-openness criterion. This is not a
   standard interval parameterization: the charts are not restricted to
   `[0,1]`, and the pushout is not claimed equivalent to `[0,2]`.
3. Complex/unitary evolution and the full dependent return-section
   interpretation remain distinct obligations. The polynomial model is not
   a substitute for either.
