# Operational whole-return assembly

## Current disposition: positive closure at explicitly accepted mixed level

The operator answered **yes** to the additional mixed-level acceptance question. Recorded in `contracts/whole-return-mixed-level-acceptance.v1.json`; live validated resolution: `results/whole-return-mixed-level-accepted.json`. The net target is now **++**, and the net/planner are positive terminal with no remaining action. This combines a freshly safe-Agda-checked operational record with the written all-time classical correspondence; it does **not** assert kernel semantic interpretation or differentiability at the seam.

The entries below preserve the original progression and open gates at each checkpoint. Their historical unaccepted receipts are not rewritten as accepted successes. The final admission checks both the scoped acceptance and the pinned original evidence, rejects stale/cached proof and semantic/seam overclaims, and preserves both earlier half-turn +- attempts.

## Iteration 1: native complex operators

Target remains **open**. This is component progress, not a whole-return certificate or a new positive target outcome.

Freshly inspected the net, `spectral-whole-return-proof.md`, `TickWholeReturnRealization.agda`, `TickCompletionRealization.agda`, and `TickGluedSchedules.agda`. The older realization uses real polynomial interpolation; its domain is a pushout of unrestricted completion charts, explicitly not the metric interval [0,2]. It is historical context and must not be used to claim spectral metric gluing.

New module: `agda/TickComplexNativeOperators.agda`.

- Four-state vectors have actual `ComplexCompletion` amplitudes.
- Native coordinate flips are commuting involutions.
- Both preserve pointwise addition and scalar multiplication.
- On pure tensors, each acts on exactly its own factor.
- Factor exchange is involutive and intertwines the two native flips.

These are exact function equalities, with no scalar ring axioms assumed. The generic definitions are instantiated at the implemented complex completion operations. They do **not** yet prove all complex ring laws, norm preservation, spectral interpolation, or correspondence to the exported source witness.

Verification: cached pass (4.43 seconds), then fresh safe `--ignore-interfaces` closure (67.744 seconds). Receipt: `results/complex-native-operators-fresh.json`. The receipt explicitly sets `whole_return_proved` to false and records no target outcome.

## Iteration 2: operational complex commutative ring

New module: `agda/TickComplexCompletionRing.agda`.

Proved addition associativity, zero, inverse and commutativity; multiplication associativity, unit, distributivity and commutativity for complex pairs over a commutative ring. Instantiated this at the existing `CompletionCommRing` to construct `ComplexCompletionCommRing`. Public correspondence paths show that its carrier, addition, multiplication, negation, zero and one are definitionally the existing `ConstructiveComplexCompletion` implementation—not replacement operations or an assumed scalar field.

Symbolic component proofs use the checked ring solver before instantiation, avoiding normalization of operational Cauchy schedules. This discharges the foundational complex ring algebra, not the spectral projectors, their norm laws, or their metric behavior.

Verification: cached pass (5.522 seconds), then fresh safe `--ignore-interfaces` closure (78.481 seconds). Receipt: `results/complex-completion-ring-fresh.json`. The target remains open; the receipt records no target outcome. The native-operator receipt from iteration 1 is unchanged.

## Iteration 3: spectral formula and exact native endpoints

New module: `agda/TickSpectralLocalOperators.agda`.

Defined the two spectral components `E+ = (I+P)/2`, `E- = (I-P)/2`, and `local P t = E+ + phase machinPi t * E-`, using the actual complex ring and native flips. Constructed the half scalar from the rational embedding and proved its double equals one. Generic symbolic ring identities then prove `local P 0 v = v` and `local P 1 v = P v` for every vector (and every operator P), specializing to both native flips. These are all-vector exact endpoint laws, not sample calculations or real polynomial interpolation.

The finish proof uses the existing operational Machin endpoint. It does not itself assert standard-real identification. Although the definitions are named positive/negative projectors, their idempotence, orthogonality and sum-to-identity laws still require proofs; endpoint laws alone do not establish those properties.

Verification: cached pass (7.409 seconds), then fresh safe `--ignore-interfaces` closure including Machin endpoint dependencies (943.248 seconds). Receipt: `results/spectral-local-operators-fresh.json`. Whole-return remains open, with no target outcome recorded.

## Iteration 4: complementary projector and composition laws

New module: `agda/TickSpectralProjectorLaws.agda`.

For an arbitrary involutive index permutation over a commutative ring with a normalized half scalar, proved both projector idempotence laws, both mixed compositions equal to zero, sum-to-identity, and spectral composition `U(z) U(w) = U(z*w)`. Instantiated these theorems at the actual complex completion and both native flips. Four public correspondence paths identify the projectors with iteration 3's exact definitions.

Using the already proved operational phase addition law, proved `leftLocal s (leftLocal t v) = leftLocal (s+t) v` and the corresponding right law for all completion-valued times and all vectors. No rational-time restriction or sampled check is involved.

The zero-composition laws are algebraic orthogonality, **not yet Hermitian orthogonality or self-adjointness**. No unitarity or metric regularity of vector-valued local operators is claimed by this component.

Verification: cached pass (9.452 seconds), then fresh safe `--ignore-interfaces` closure (922.656 seconds). Receipt: `results/spectral-projector-laws-fresh.json`. Whole-return remains open and no target outcome is recorded.

## Iteration 5: conjugation, scalar norms and local inverses

New modules: `agda/TickComplexConjugation.agda` and `agda/TickSpectralLocalInverse.agda`.

Proved conjugation involution, additivity and multiplicativity, the conjugate-product identity, conjugation invariance of squared norm and multiplicativity of squared norm. Exact correspondence paths identify conjugation with `conjugateComplex` and squared norm with the existing `TickPhaseNormTransfer.normSquared`.

The freshly checked scalar unit-norm theorem supplies both conjugate inverses of the operational phase, for every completion-valued scale and time. Spectral composition then constructs and verifies two-sided inverses for each native local operator at every completion-valued time and every vector. These inverses use the conjugated phase; they are not substituted for the positive-phase reversed schedule required for whole-return.

**Invertibility is not unitarity.** No vector norm preservation or identification of these inverses as adjoints is claimed. Both the receipt and the target boundary keep this obligation open.

Verification: cached pass (9.91 seconds), then fresh safe `--ignore-interfaces` closure, including operational scalar norm and Machin endpoint dependencies (1886.214 seconds). Receipt: `results/spectral-local-inverse-fresh.json`. Whole-return remains open and no target outcome is recorded.

## Iteration 6: all-vector local norm preservation

New module: `agda/TickSpectralLocalNorm.agda`.

Defined `vectorNormSquared` as the sum of the four operational scalar squared moduli. A symbolic two-coordinate energy identity separates the input energy from a correction proportional to `normSquared(z)-1`. The constructed half scalar and the all-time phase norm theorem eliminate the correction and normalize the energy coefficient. Applying this identity to each native flip pair proves `left-local-norm` and `right-local-norm` at every completion-valued time and for every completion-valued complex vector.

The module also publicly exposes the four previously checked inverse equations for these same operators. Thus local norm preservation and two-sided invertibility are now both kernel-checked. An explicit complex-linearity theorem and a packaged unitary-operator record remain to be supplied; no adjoint characterization is claimed. In particular, this component does not establish metric regularity, piecewise generator laws, or gluing.

Verification: cached pass (14.605 seconds), then fresh safe `--ignore-interfaces` closure including the inverse, projector and scalar norm dependencies (1856.915 seconds). Receipt: `results/spectral-local-norm-fresh.json`. Whole-return remains open and no target outcome is recorded.

## Iteration 7: packaged local linear norm equivalences

New module: `agda/TickSpectralLocalUnitary.agda`.

Proved additivity and homogeneity over every operational complex scalar for both local operators. Constructed `left-local-unitary` and `right-local-unitary`, inhabiting `LinearNormEquivalence` for the same `leftLocal t` and `rightLocal t`. Each record carries the inverse map, complex linearity, all-vector squared-norm preservation, and both inverse equations, for every completion-valued time. The generic certificate syntax avoids expanding operational Cauchy schedules during record checking.

This is the linear norm-preserving equivalence presentation of local unitarity, not an adjoint presentation. It does not claim interval continuity, derivative/generator compatibility, closed-piece gluing, or whole-return correspondence.

Verification: cached pass (8.323 seconds), then fresh safe `--ignore-interfaces` closure (1897.792 seconds). Receipt: `results/spectral-local-unitary-fresh.json`. The whole-return target remains open and no target outcome is recorded.

## Iteration 8: exact Hamiltonian algebra

New module: `agda/TickSpectralHamiltonian.agda`.

Defined the actual Hamiltonian `H = piComplex * negativeProjector`, hence `pi(I-P)/2`, with the same Machin candidate and native flips as the local operators. Proved the negative-projector spectral eigenvalue identity `E- U(z) = z E-`, and identified multiplication by `-i*pi` with the existing scalar phase generator convention. For each native operator, the scalar-derived candidate `phaseGenerator machinPi t * E- v` now equals `-i * H (U(t)v)` at all completion-valued times and vectors.

Fresh inspection of `TickCompletionDerivative.agda` confirms that `HasMetricDerivative` is an all-increment metric remainder bound. The algebraic candidate identity is **not** that bound. This component deliberately records `vector_metric_derivative_proved: false`; affine complex multiplication of the scalar remainder still needs quantitative metric control.

Verification: cached pass (9.744 seconds), then fresh safe `--ignore-interfaces` closure (861.006 seconds). Receipt: `results/spectral-hamiltonian-fresh.json`. Whole-return remains open and no target outcome is recorded.

## Iteration 9: genuine vector metric continuity

New module: `agda/TickSpectralLocalContinuity.agda`.

Fresh inspection found the existing joint metric continuity theorems for real completion addition and multiplication in `TickCompletionRingContinuity.agda`. Lifted these to complex addition and multiplication, then established continuity of `a + f(t)*b` for arbitrary fixed complex completion coefficients. Applied this to the exact spectral formula and the checked operational phase continuity.

Defined `VectorWithin` using all four complex coordinates and `VectorMetricContinuous` with **one local modulus controlling all four coordinates simultaneously**. A finite maximum construction combines the coordinate moduli under propositional truncation. Both native local paths now satisfy this metric continuity notion, for every fixed completion-valued vector and every completion-valued time. This is not continuity in the topology of Agda path equality, and does not require changing the implemented scalar backend.

Verification: cached pass (6.695 seconds), then fresh safe `--ignore-interfaces` closure (766.879 seconds). Receipt: `results/spectral-local-continuity-fresh.json`. No metric derivative, interval gluing, or target outcome is claimed.

## Iteration 10: exact affine remainder and restricted derivative transport

New module: `agda/TickComplexAffineRemainder.agda`.

Proved for arbitrary fixed complex coefficients and every completion-valued increment that the actual `firstOrderRemainder` of `a + f(t)*b`, at candidate derivative `v*b`, equals the remainder of `f` multiplied by `b`. Its squared norm is consequently exactly the original squared norm multiplied by `normSquared b`.

Also proved `affine-unit-derivative`: when `normSquared b = 1`, an actual `HasMetricDerivative f t v` certificate transports to the affine curve, with the same modulus and all-increment bound. This is a genuine derivative rule, but its explicit unit-norm premise is **not** available for arbitrary coordinates of `E- v`. It does not close the vector derivative obligation.

Fresh inspection of `TickCompletionOrderLimits.agda` found rational-limit order transfer, not an already packaged general multiplication-monotonicity/Archimedean absorption rule for this completion cone. The unrestricted coefficient case remains quantitative work, now isolated by the exact remainder identity.

Verification: initial elaboration exposed ambiguous inferred arguments; supplying explicit curve values and the exact right-hand remainder budget resolved them. Cached pass (6.101 seconds), then fresh safe `--ignore-interfaces` closure (1078.334 seconds). Receipt: `results/complex-affine-remainder-fresh.json`. No arbitrary-coefficient derivative, vector derivative or target outcome is recorded.

## Iteration 11: arithmetic of the actual closed order

New module: `agda/TickCompletionOrderArithmetic.agda`.

Proved that the existing `CompletionNonnegative` cone is closed under addition, that nonnegative rationals embed into it, and that zero belongs to it. From these and checked ring identities, proved reflexivity and transitivity of the existing `CompletionLE`. Proved nonnegativity of every completion square by rational approximation and closed-limit transfer, then nonnegativity of every complex squared norm by cone addition.

The cone-addition proof respects existential representatives and spends one precision bit before adding their eventual lower bounds. No replacement order, assumed ordered-field structure, or choice of representatives is introduced. These laws support derivative coefficient absorption but do not supply multiplication monotonicity or an upper bound by themselves.

Verification: cached pass (5.047 seconds), then fresh safe `--ignore-interfaces` closure (82.698 seconds). Receipt: `results/completion-order-arithmetic-fresh.json`. Nonnegative multiplication, arbitrary-coefficient derivative transport and whole-return remain explicitly unproved.

## Iteration 12: nonnegative multiplication and order transport

New module: `agda/TickCompletionPositiveProduct.agda`.

Recovered eventual lower bounds on any fixed representative of a nonnegative completion value. Defined positive rational approximants by replacing negative approximants with zero, and proved they still converge to that value in the existing completion metric. Rational product positivity and the existing moving-product/closed-cone limit theorems then prove `completion-nonnegative-product`.

Derived `completion-multiply-monotone`: `a <= b` and nonnegative `c` imply `a*c <= b*c`, for the actual `CompletionLE` and operational multiplication. The proof uses checked ring distributivity on `(b-a)*c`; it introduces neither a new order nor a choice principle.

Verification: cached pass (5.038 seconds), then fresh safe `--ignore-interfaces` closure (81.807 seconds). Receipt: `results/completion-positive-product-fresh.json`. This completes the previously missing nonnegative multiplication/order transport, but does not yet establish coefficient absorption or arbitrary-coefficient derivatives. Whole-return remains open.

## Iteration 13: unrestricted affine metric derivatives

New modules: `agda/TickCompletionCoefficientBound.agda` and `agda/TickComplexAffineDerivative.agda`.

Constructed a propositionally truncated dyadic upper bound for every completion value, using its canonical bounded rational representative and closed-order transfer. Proved `precision(d+k)^2 * dyadicRadius(d) <= precision(k)^2`, then lifted this bound through embedded order and nonnegative multiplication, retaining the increment's exact squared factor even at zero.

`affine-metric-derivative` now transports the actual all-increment `HasMetricDerivative f t v` to `a + f(t)*b` with derivative `v*b`, for **arbitrary** complex completion coefficients `a,b`. The dyadic bound on `normSquared b` chooses finer precision `d+k`; the scalar modulus at that precision controls all subsequently quantified completion-valued increments. No unit-norm premise, division by the increment, rational-time restriction or representative choice axiom is used.

Verification: cached pass (6.295 seconds), then fresh safe `--ignore-interfaces` closure (1122.764 seconds). Receipt: `results/complex-affine-derivative-fresh.json`. This closes the unrestricted affine lifting component, not the whole-return target.

## Iteration 14: genuine vector Hamiltonian dynamics

New module: `agda/TickSpectralLocalDynamics.agda`.

Applied unrestricted affine derivative transport to the four coordinates of each native spectral path. Defined `HasVectorMetricDerivative` in the finite-product metric with **one modulus** controlling all coordinate remainder bounds and all completion-valued increments, including zero. Combined the finite coordinate moduli under propositional truncation and transported the resulting derivative through the already checked `-i H U` identities.

`left-hamiltonian-derivative` and `right-hamiltonian-derivative` now prove actual metric derivatives, not merely equality of formal candidates. Constructed `left-local-dynamics` and `right-local-dynamics` records packaging linear norm equivalence, vector metric continuity, and these derivatives for the same operational flows at every completion-valued time and vector. The native endpoint and composition laws remain available in their checked prerequisite modules.

Verification: explicit function/point/vector arguments resolved non-injective inference during elaboration. Cached pass (11.292 seconds), then fresh safe `--ignore-interfaces` closure of all assembled local analytic dependencies (1798.421 seconds). Receipt: `results/spectral-local-dynamics-fresh.json`. The local dynamics component is now complete in this metric presentation. External interval gluing and whole-return obligations remain open.

## Iteration 15: actual external interval and continuous charts

New module: `agda/TickCompletionMetricInterval.agda`.

Constructed `UnitInterval` and `ReturnInterval` as the existing completion-order subtypes `[0,1]` and `[0,2]`, with inherited `CompletionWithin` metric balls. Proved interval extensionality and metric separation using propositional order bounds. Constructed start, seam and finish; the left chart is the inclusion and the right chart translates by one. Both charts are metrically continuous, with exact endpoint and shared-seam paths. Defined the left and right restricted-piece subtypes on the actual return interval.

This is **not** a global gluing theorem. The charts alone do not supply an eliminator for the whole interval, and no decidability/totality of completion order is assumed. The older unrestricted pushout remains unsuitable. A constructive global construction (for example using continuous clipped time coordinates), together with its agreement on both pieces, still needs to be supplied.

Verification: explicit interval endpoints resolved inference of the non-injective order predicates. Cached pass (8.289 seconds), then fresh safe `--ignore-interfaces` closure (82.671 seconds). Receipt: `results/completion-metric-interval-fresh.json`. No global path, gluing or target outcome is recorded.

## Iteration 16: continuous completion positive part

New module: `agda/TickCompletionPositivePart.agda`.

Constructed `positiveCompletion`, the quotient-descended operation `max(0,t)`, from the rational positive-part operation. Proved the rational directed nonexpansive inequality, regularity of the transformed Cauchy sequence, preservation of metric equivalence, and actual completion metric continuity. Proved exact laws: it fixes nonnegative completion values and vanishes on nonpositive ones, using the existing cone and representative lower bounds.

Only rational comparisons are decided. There is no decision procedure or total-order split on arbitrary completion values. This supplies the missing constructive building block for clipped time coordinates and hence a possible global gluing formula, but is not itself a global path or gluing proof.

Verification: cached pass (4.892 seconds), then fresh safe `--ignore-interfaces` closure (77.524 seconds). Receipt: `results/completion-positive-part-fresh.json`. Whole-return remains open.

## Iteration 17: constructive global metric gluing

New modules: `agda/TickCompletionClippedTime.agda` and `agda/TickSpectralGlobalPath.agda`.

Defined continuous `secondTime(t)=max(0,t-1)` and `firstTime(t)=t-secondTime(t)`, with exact restriction laws on both closed pieces. Constructed the global positive-phase path `U_b(secondTime(t)) (U_a(firstTime(t)) v)` and restricted it to the actual `ReturnInterval`. Its vector metric continuity is proved directly, including varying state input to the outer local operator; no closed-cover case split is assumed.

Proved agreement with `U_a(t)v` whenever `t<=1` and with `U_b(t-1) P_a v` whenever `1<=t`. Thus the two closed-piece formulas genuinely have one continuous global realization. Proved its start is `v`, finish is `P_b P_a v`, and squared norm is preserved for both native orders, at every completion-valued time (hence throughout the interval).

This component is parameterized by traversal order and initial vector. Binding the traversal to reversed native schedule tags and setting the initial vector to the native double-flip target remain explicit next obligations. Piecewise derivatives of the global path also still need transport; no seam differentiability is claimed.

Verification: cached pass (17.771 seconds), then fresh safe `--ignore-interfaces` closure (1667.252 seconds). Receipt: `results/spectral-global-path-fresh.json`. Global metric gluing is now proved; whole-return remains open.

## Iteration 18: native returns and faithful whole-record interpretation

New modules: `agda/TickComplexNativeBasis.agda` and `agda/TickSpectralRetainedReturn.agda`.

Constructed the operational complex delta basis, proved its unit norm and exact action under both native flips. Bound the global spectral path to actual `TickRetainedStructure.G.Schedule` tags in reversed order, with initial state `P_R P_L basis(s)`. Proved explicit correspondence of that state to `basis(G.run leftFirst s)`, return start/finish, metric continuity and unit norm throughout the actual interval.

At the seam, the reversed left-first schedule gives `basis(leftIndex s)` and the reversed right-first schedule gives `basis(rightIndex s)`. Proved these distinct for every source by coordinate evaluation and checked completion zero/one separation. The separation lemma is the only fact reused from the historical polynomial return module; its path construction is not reused.

Applied the existing full retained-record theorem to these exact paths. Proved reconstruction coherence, schedule-swap coherence, schedule injectivity, and **fixed-source faithfulness of whole Ticks**, not just equality of their extracted tags.

Verification: cached pass (23.999 seconds), then fresh safe `--ignore-interfaces` closure (1670.026 seconds). Receipt: `results/spectral-retained-return-fresh.json`. An inherited `TypedGeneratorLayers` non-exported-name warning is retained in the log; the kernel check passes. Global open-piece derivative transport and full exported-witness correspondence remain separate; whole-return is not yet promoted.

## Iteration 19: global-path derivatives on metric-interior regions

New module: `agda/TickSpectralPiecewiseDerivative.agda`.

Proved derivative transport under time translation and local agreement on a metric neighborhood, preserving the actual all-increment vector remainder definition. Applied the global restriction formulas to obtain derivatives on `BeforeSeam` and `AfterSeam`, defined by the corresponding closed-order bound at the center plus a truncated neighborhood of increments staying in that half-line.

For both native schedules and every source, `return-first-hamiltonian` and `return-second-hamiltonian` identify the derivative with `-i H_active returnCurve`. `return-curve-correspondence` ties this full completion-time extension exactly to the source-bound interval return already used for retained-record faithfulness. No derivative at the switching time is claimed.

**Remaining domain obligation:** the metric-interior witnesses are explicit premises. Their identification/inhabitation from the conventional strict order subintervals has not yet been proved. This is recorded separately rather than silently treating a conditional neighborhood theorem as all strict-interval generator compatibility.

Verification: cached pass (74.275 seconds), then fresh safe `--ignore-interfaces` closure (1676.794 seconds). Receipt: `results/spectral-piecewise-derivative-fresh.json`. Whole-return remains open.

## Iteration 20: strict open-piece Hamiltonian laws

New module: `agda/TickSpectralOpenPieces.agda`.

Defined constructive strict completion order by an explicit positive dyadic gap: `a < b` means a truncated witness `k` with `a + precision(k) <= b`. Proved that an increment in the ball of depth `k+2` is bounded above by `precision(k)`, and likewise for its negative. Translation and order transitivity now turn each strict seam margin into the metric neighborhood required by iteration 19.

Constructed the actual interval subtypes `(0,1)` and `(1,2)` with this strict-order definition. `return-first-open-generator` and `return-second-open-generator` prove the global return path's active Hamiltonian derivative at **every point of these open subintervals**, without an extra neighborhood assumption. No seam derivative is asserted. Correspondence of this constructive strict-order presentation with ordinary real strict intervals belongs to the remaining exported-witness interpretation audit.

Verification: the initial cached check timed out at 180 seconds; a 480-second allowance completed in 213.12 seconds. Fresh safe `--ignore-interfaces` closure passed in 1961.941 seconds. Receipt: `results/spectral-open-pieces-fresh.json`. Whole-return remains open; reaching iteration 20 does not promote it.

## Follow-up iteration 1: arbitrary factor-matrix laws

New module: `agda/TickSpectralFactorOperators.agda`.

Defined arbitrary operational complex 2x2 factor matrices, their left/right lifts and composition. Proved lift composition and cross-factor commutation for every matrix and vector. Identified the existing local spectral flows, their checked inverses and Hamiltonians with these matrix lifts. Consequently conjugation by a local flow and its inverse preserves its own factor algebra and fixes every operator in the other factor algebra. Proved the two local legs commute at arbitrary completion times, and each Hamiltonian commutes with all operators on the other factor.

Conjugation is stated with the checked inverse, not a newly established adjoint identity. No sampling, restriction to pure tensors, or replacement scalar backend is used. Separate symbolic scalar expansion lemmas resolved reflection inference in Boolean branches.

Verification: cached pass (8.882 seconds), then fresh safe `--ignore-interfaces` closure (1621.175 seconds). Receipt: `results/spectral-factor-operators-fresh.json`. Covariance, exported-witness correspondence and final whole-return assembly/admission remain open; target outcome is unchanged.

## Follow-up iteration 2: spectral and return covariance

New module: `agda/TickSpectralCovariance.agda`.

Proved general index-intertwining naturality for the exact local spectral flow, Hamiltonian and global clipped-time path. Specialized it to factor exchange: local flows and Hamiltonians exchange L/R; native target and delta basis transform with the exchanged source; the entire source-bound interval return transforms with the exchanged schedule and source. Also proved factorwise identity/flip Boolean relabeling covariance for both local flows, both Hamiltonians, native basis/target and the entire return. The relabelings are proved involutive. No scalar values or times are sampled.

The general naturality theorem accepts any reindexing with the stated intertwining equation. The explicit identity/flip family covers the native Bool relabelings; classification of an arbitrary supplied Bool equivalence into that family is not separately asserted.

Verification: cached pass (39.458 seconds), then fresh safe `--ignore-interfaces` closure (1832.055 seconds). Receipt: `results/spectral-covariance-fresh.json`. Exported-witness interpretation and final whole-return record/admission remain open.

## Follow-up iteration 3: structural exported-witness correspondence and adjoints

New module: `agda/TickSpectralWitnessCorrespondence.agda`.

Proved the local spectral matrix's conjugate transpose equals its already checked inverse matrix and the Hamiltonian matrix is self-adjoint. This resolves the inverse-versus-adjoint matrix presentation gap in the arbitrary factor-conjugation laws. Independently specified the exported 2x2 spectral coefficient matrix and pi-scaled Hamiltonian, proved exact operational agreement, and linked the native free-linearized basis maps. Proved the source-bound actual interval return agrees with the exported positive-phase reversed-order formulas on both closed pieces.

The checker pins the imported export payload/hash, pointer and both written specification documents, in addition to kernel dependencies. Cached pass (15.834 seconds), then fresh safe `--ignore-interfaces` closure (1837.572 seconds). Receipt: `results/spectral-witness-correspondence-fresh.json`.

**Semantic boundary:** these are kernel structural correspondence theorems with the operational phase. They do not prove that the standard-real interpretation sends that phase to `exp(-i*pi*t)` at every time, or identifies the constructed metric/strict intervals with the standard intervals. The earlier explicit mixed-level acceptance covers standard-pi identification; it must not silently be extended into acceptance of additional unverified correspondence obligations. The target remains open pending this interpretation and final record/admission.

## Follow-up iteration 4: one operational kernel bundle

New module: `agda/TickOperationalWholeReturnKernel.agda`.

Constructed `operational-whole-return-kernel : OperationalWholeReturnKernel`, with public explicit types `LocalLaws`, `ReturnLaws`, `GeneratorLaws`, `CoherenceLaws`, `FactorLaws`, `CovarianceLaws` and `StructuralLaws`. One record now carries the same local dynamics, actual interval return endpoints/continuity/unit norm, strict open-piece Hamiltonian derivatives, whole-Tick reconstruction/swap/faithfulness, arbitrary factor conjugation and leg commutation, return covariance, matrix adjoint/inverse and structural exported-rule correspondence. The record is unconditional in the operational backend and introduces no postulates or assumed semantic interpretation.

Verification: cached pass (48.686 seconds), then fresh safe `--ignore-interfaces` closure of the entire assembled dependency graph (2212.784 seconds). Receipt: `results/operational-whole-return-kernel-fresh.json`.

**Full target admission is deliberately withheld.** The all-time standard-real phase/interval interpretation remains absent. The receipt records `operational_kernel_bundle_proved: true`, `standard_real_phase_interpretation_proved: false`, `whole_return_proved: false`, and no target outcome. A new net regression rejects promotion from this partial-semantic receipt. The earlier standard-pi mixed acceptance is not broadened implicitly.

## Follow-up: written all-time semantic correspondence

New proof: `standard-spectral-correspondence.md`. New verifier: `checkers/check_standard_spectral_correspondence.py`.

The written proof establishes the canonical interpretation as a real ring/order/metric isomorphism, identifies the dyadic-margin strict intervals with ordinary strict intervals, transfers the actual all-increment derivative bounds to classical derivatives, and uses the initial value/derivative equation to identify the all-time operational phase with the standard exponential. It then identifies the local matrices, factor laws, positive reversed global return and whole-record faithful interpretation with the pinned exported witness.

This is written classical mathematics, not kernel formalization. The verifier validates the current net/import and accepted pi evidence, pins the proof/specification/import/dependency hashes, and reruns fresh safe closure of the assembled operational bundle (2005.471 seconds). Receipt: `results/standard-spectral-correspondence.json`. It explicitly records no additional mixed acceptance and no target outcome.

The semantic proof is now supplied at the export's written mathematical level. The remaining gate is **explicit acceptance of this additional mixed verification level**, or kernel formalization of its interpretation/soundness. The earlier pi acceptance is not broadened by implication. After acceptance, add scoped theorem-specific admission and its freshness/overclaim regression tests before closing the net.

## Fresh correspondence audit and executable continuation

Re-read `uniform-local-core-proof.md`: its factor-algebra obligations are stronger than the currently proved pure-tensor laws for native flips. The remaining work is substantive, not merely attaching existing fields to a record:

1. Arbitrary factor-matrix laws and local matrix adjoint/inverse identification are now proved. Assemble those exact theorem types; avoid introducing a new scalar backend or replacing matrix correspondence with a sampled test.
2. Native factor-exchange and factorwise identity/flip covariance now extend to local spectral operators, Hamiltonians and source-bound global returns. Use these exact theorems in the final correspondence/assembly; do not replace them by sampled covariance checks.
3. Structural exported-witness correspondence (free linearization, spectral coefficient matrix, Hamiltonian, positive reversed closed-piece formulas) is now proved. The written interpretation of completion metric/strict intervals and all-time phase is now supplied in `standard-spectral-correspondence.md`, bound to a fresh operational closure. The existing accepted standard-pi identification is a prerequisite, not automatic acceptance of this new semantic theorem. Obtain explicit additional mixed-level acceptance or pursue kernel formalization.
4. The operational kernel record is now assembled and freshly checked. After the supplied written semantic interpretation is explicitly accepted at its additional mixed verification level (or kernel-formalized), extend the certificate/admission with that exact evidence and freshness pins. A regression already rejects treating the operational-only bundle as full target closure. The target remains unresolved in the net, with component and kernel-bundle progress linked here.

Commands:

```text
python research/nima/checkers/check_complex_native_operators.py --timeout 1200
python research/nima/checkers/check_complex_completion_ring.py --timeout 1200
python research/nima/checkers/check_spectral_local_operators.py --timeout 3000
python research/nima/checkers/check_spectral_projector_laws.py --timeout 3000
python research/nima/checkers/check_spectral_local_inverse.py --timeout 3000
python research/nima/checkers/check_spectral_local_norm.py --timeout 3000
python research/nima/checkers/check_spectral_local_unitary.py --timeout 3000
python research/nima/checkers/check_spectral_hamiltonian.py --timeout 3000
python research/nima/checkers/check_spectral_local_continuity.py --timeout 3000
python research/nima/checkers/check_complex_affine_remainder.py --timeout 1200
python research/nima/checkers/check_completion_order_arithmetic.py --timeout 1800
python research/nima/checkers/check_completion_positive_product.py --timeout 1800
python research/nima/checkers/check_complex_affine_derivative.py --timeout 3000
python research/nima/checkers/check_spectral_local_dynamics.py --timeout 3600
python research/nima/checkers/check_completion_metric_interval.py --timeout 1800
python research/nima/checkers/check_completion_positive_part.py --timeout 1800
python research/nima/checkers/check_spectral_global_path.py --timeout 3600
python research/nima/checkers/check_spectral_retained_return.py --timeout 3600
python research/nima/checkers/check_spectral_piecewise_derivative.py --timeout 3600
python research/nima/checkers/check_spectral_open_pieces.py --timeout 3600
python research/nima/checkers/check_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_net.py
```
