# Pi critical-path branch: convergent Machin construction

Active action: `prove/completion-pi-half-turn`. The regularity attempt is paused at its proved-continuity checkpoint; its derivative obligation is preserved. Neither pause nor this construction checkpoint is a terminal proof-attempt outcome.

## What is constructed

`agda/TickSmallArctangent.agda` defines the alternating odd-power recurrence

```
a(q,0) = q
a(q,n+1) = -a(q,n) q^2 (2n+1)/(2n+3)
A(q,N) = sum[n=0..N] a(q,n)
```

For every rational q with |q| <= 1/2 it proves, in safe Agda:

- `|a(q,n)| <= 2^-n`;
- `|A(q,m+k)-A(q,m)| <= 2^-m`, for every m and k;
- the partial sums form a `RegularCauchy` object;
- the error bound holds at **every later cutoff**, not merely at sampled indices.

`agda/TickMachinInputs.agda` supplies the bounds for q=1/5 and q=1/239 and exposes their exact sample equations.

`agda/TickMachinPiCandidate.agda` constructs the actual completion element

`machinPi = 16*A(1/5) - 4*A(1/239)`.

Integer scaling uses repeated addition, so no expensive rational-radius search is needed. The quotient formula is proved in `machin-pi-formula`. No arctangent or pi constant is assumed as an input.

## Exact rotation certificate and its verification level

The generic commutative-ring theorem `Certificate.sibling-rotation` in `agda/TickMachinRotationIdentity.agda` proves the polynomial identity underlying the Machin rotation. For s=4 and a=119, the relevant fourth power is

`(5+i)^4 = 476+480i = 4*(119+120i)`,

and `119+120=239`. Thus, over the rationals with nonzero denominators,

`((5+i)/(5-i))^4 * ((239-i)/(239+i)) = i`.

`checkers/check_machin_pi_candidate.py` verifies the concrete substitution with **exact Fraction arithmetic**, and verifies that squaring the resulting rotation gives -1. The generic polynomial identity is kernel-checked; the concrete rational specialization is an exact Python audit. These evidence levels are deliberately distinguished.

The same audit checks the recurrence against the alternating odd-power sum through cutoff 40. Combining the individual all-later-cutoff estimates gives a candidate enclosure with radius `20/2^40`, lying strictly between 3 and 4. This is an enclosure derived from the series estimates, **not** an operational sine/cosine endpoint proof or a separately kernel-checked decimal pi theorem.

## Identification with the reference pi: classical argument

The exported standard witness in `uniform-local-core-proof.md` and `spectral-whole-return-proof.md` uses the usual standard-real pi. Under the ordinary interpretation of rational Cauchy classes into the reals, the constructed series is classical arctangent on |q| <= 1/2: integrate the uniformly convergent geometric series for `1/(1+x^2)`, obtaining the alternating odd-power expansion. Its recurrence is exactly the one above.

Put A=atan(1/5), B=atan(1/239), and theta=4A-B. Alternating-series bounds give

`4*(1/5 - (1/5)^3/3) - 1/239 < theta < 4/5`,

so theta is positive and less than 1. Also pi/2>1, since `atan(1)=integral[0,1] 1/(1+x^2) dx > 1/2`. Hence theta lies in (0,pi/2).

The classical Cayley formula and the exact rotation identity give `exp(2*i*theta)=i`. The stated range fixes the branch: theta=pi/4, not an arbitrary angle modulo pi. Therefore `16*A-4*B=pi`, the same standard constant used in the exported witness.

This is an explicit **classical identification argument**, not a new Agda theorem equating operational trigonometric values with classical ones. It does not close the operational endpoint node.

## Addition-law foundations: earlier component checkpoint

Three new safe Agda modules prepare the composition proof:

- `agda/TickTrigAdditionCoefficients.agda` proves the cosine and sine Cauchy-product coefficient identities for **distinct rational inputs**, in every degree. It factors the derivative weights using their rotation recurrence and reuses the factorial-normalized exponential convolution theorem. This is not the earlier same-input norm cancellation.
- `agda/TickTrigAdditionResidual.agda` identifies the two addition defects of the actual `cosinePartialSum` / `sinePartialSum` functions with rectangular-minus-triangular residuals. For every nonnegative radius r, a constructed offset E(r) works for every |x|, |y| <= r, every precision k and **every cutoff n >= E(r)+k**: both defects have magnitude at most `2^-k`. Neither the coefficient nor the offset depends on x or y within the radius.
- `agda/TickTrigPartialSumTransfer.agda` proves that, for any rational q, every sufficiently late cosine/sine partial sum is within the requested completion metric precision of the **implemented** `completionCosine (embedMetricℚ q)` / `completionSine (embedMetricℚ q)`. It compares a later cutoff with a native canonical sample, then uses regular-Cauchy density. No alternative trigonometric backend is introduced.

Fresh safe `--ignore-interfaces` dependency closure **passed in 690.964 seconds**, with stable source/compiler/library hashes. Receipt: `results/trig-addition-foundations-fresh.json`. A separate exact Fraction regression checks 325 coefficient cases and 125 finite residual cases; those samples are not the proof of the all-degree or all-later bounds.

**Boundary of that receipt:** scalar partial-sum transfer alone did not transfer composite products and sums. That remaining transfer is now discharged by the newer component below; the earlier receipt is retained unchanged.

## Operational completion addition: fresh component checkpoint

The following unconditional laws now have fresh safe Agda closure, for **all completion inputs**, not merely rational angles or sampled schedules:

```text
cos(x+y) = cos(x)*cos(y) - sin(x)*sin(y)
sin(x+y) = sin(x)*cos(y) + cos(x)*sin(y)
phase p (s+t) = phase p s *complex phase p t
```

Every function and product here is the existing operational completion implementation. No trigonometric addition law, arctangent relation or endpoint is supplied as a premise.

- `agda/TickCompletionRingContinuity.agda`: joint metric continuity of completion multiplication with a local modulus depending only on the centers, plus sum/negation continuity. The nearby canonical-radius bound controls both varying factors; there is no claim of global uniform continuity of multiplication.
- `agda/TickCompletionLimits.agda`: a truncated all-later-index notion of convergence, preservation by continuous operations, uniqueness for asymptotically close sequences, and extension from rational density.
- `agda/TickRationalTrigAddition.agda`: scalar native-schedule transfer is combined with completion products/sums and the uniform finite defects to prove both rational-input addition equalities.
- `agda/TickCompletionTrigAddition.agda`: continuity and density extend each input in turn, giving `completion-cosine-addition` and `completion-sine-addition` for arbitrary completion inputs.
- `agda/TickPhaseComposition.agda`: `operational-phase-addition` transports these laws to the **same** `TickCompletionPhase.phase`, for every completion scale and both completion times.

Fresh safe `--ignore-interfaces` dependency closure **passed in 703.843 seconds**, with stable source/compiler/library hashes. Receipt: `results/completion-trig-addition-fresh.json`. Cached checks have a separate receipt and cannot admit this component.

The net records this as a supporting component of the active pi attempt and removes angle composition from its remaining obligations. It does **not** record a new whole-goal outcome, resume the derivative attempt, or close pi endpoints.

## What remains open

`agda/TickMachinPiEndpointContract.agda` fixes the exact obligation:

```agda
MachinEndpoints =
  (completionCosine (-completion machinPi) ≡ (-completion oneCompletion)) ×
  (completionSine (-completion machinPi) ≡ zeroCompletion)
```

It proves only the conditional transport from those equalities to the existing `phase machinPi oneCompletion` endpoint.

The next analytic work is the arctangent/Cayley relation for the **implemented** cosine and sine. For the constructed small-input series A(q), the required bridge is that the operational rotation at 2*A(q) equals the rational Cayley rotation `((1-q^2)/(1+q^2), 2*q/(1+q^2))`. The new addition laws then support composition of the Machin factors; the concrete rational specialization and exact endpoints must still be kernel-certified. The classical identification must also be connected at the accepted formal level. No inhabitant of `MachinEndpoints` is currently claimed.

This is the distinction between a convergent construction of the correct standard numerical constant and a proof that this particular operational implementation takes its required exact endpoint values there.

## Arctangent first-order and geometric-series support

`agda/TickAtanDerivativeAlgebra.agda` proves reciprocal cancellation, the odd-power term factorization, the geometric denominator identity, and an exact first-order remainder recurrence. `agda/TickAtanFirstOrderBounds.agda` bounds that remainder quadratically, uniformly over all later cutoffs, without assuming a differentiation theorem.

`agda/TickAtanGeometricCompletion.agda` constructs the geometric regular sequence and proves convergence of both unshifted arctangent and geometric partial sums to their completion classes. It also proves that the embedded denominator-cleared rational approximants converge to one, and now proves `geometric-completion-inverse`: the actual completion product of the embedded denominator `1+q²` and `geometricValue q h` equals embedded one.

`agda/TickRationalProductLimits.agda` supplies the generic rational-product limit transfer and uniqueness-of-limit lemmas. The earlier specialization timeouts were resolved by keeping `geometricValue` opaque outside its abstract construction/convergence block and checking the inverse outside abstract scope. A public class path retains access to the actual representative; no multiplication backend is replaced.

Fresh safe `--ignore-interfaces` closure passed again via `checkers/check_atan_geometric_completion.py --timeout 900`; receipt: `results/atan-geometric-completion-fresh.json`, with `completion_inverse_proved: true`. The operational Cayley bridge, standard-π identification, and `MachinEndpoints` remain open. No net outcome is promoted by this supporting checkpoint.

### Completion-valued first-order estimate

`agda/TickCompletionMagnitudeBounds.agda` defines a closed magnitude bound on the quotient using existential representatives and arbitrarily small rational slack, and proves that eventual rational bounds transfer through completion convergence. It does not descend a fixed-precision boundary predicate.

`agda/TickAtanCompletionFirstOrder.agda` proves convergence of the denominator-cleared arctangent remainder under the **actual** completion addition, negation, and independently scheduled multiplication. `cleared-atan-completion-bound` bounds this completion-valued remainder by `quadraticBudget e` for small rational inputs whose difference has magnitude at most nonnegative `e`. Its opaque arctangent presentation has an explicit class path to `smallAtanValue`.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickAtanCompletionFirstOrder --timeout 900`; receipt: `results/atan-completion-first-order-fresh.json`. This proves a completion-level first-order estimate on rational inputs, not a derivative for all completion-valued increments and not the operational trigonometric Cayley law. Those gates and the exact endpoints remain open; the paused derivative attempt and net outcome are unchanged.

### Denominator-free slope estimate and initial value

`agda/TickAtanCompletionSlope.agda` now proves the direct completion remainder bound for `atan(y) - atan(x) - (y-x)*atanSlope(x)`, with bound `scale e + scale e` (i.e. `16*e²`) on small rational inputs. `atanSlope` is the existing geometric completion value, with a checked inverse identity against embedded `1+x²`. The module also proves the exact initial value `atanCompletion 0 h = embedMetricℚ 0`.

Fresh safe `--ignore-interfaces` closure passed via `check_atan_geometric_completion.py --module TickAtanCompletionSlope --timeout 900`; receipt: `results/atan-completion-slope-fresh.json`. This supplies the rational-input first-order slope estimate and initial value for a future uniqueness argument. It does not prove that the implemented sine/cosine satisfy the requisite uniqueness hypothesis, nor that the operational Cayley bridge holds. No endpoint or whole-goal outcome is promoted.

### Operational trigonometric side of the Cayley attempt

`agda/TickOperationalTrigFirstOrder.agda` proves uniform rational Taylor remainder bounds and transfers them to completion-valued presentations of the **implemented** sine and cosine. On small rational inputs bounded by nonnegative `e`, both `cos(q)-1` and `sin(q)-q` have closed magnitude bound `e²`. Explicit class paths identify the opaque presentations with `completionCosine (embedMetricℚ q)` and `completionSine (embedMetricℚ q)`; no alternate trigonometric backend is introduced. Directly expanded transport statements caused elaboration timeouts and were not retained.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickOperationalTrigFirstOrder --timeout 900`; receipt: `results/operational-trig-first-order-fresh.json`. `CompletionMagnitudeBound` is now opaque with a public definition path to the same existential-representative predicate, avoiding premature operational schedule evaluation.

**The requested operational Cayley bridge is still not proved.** These bounds are on embedded rational angles, whereas the arctangent increments needed by the bridge are completion-valued. The remaining proof must extend the quantitative estimates to those increments and establish a vanishing Cayley defect (for example by a verified finite-partition/telescoping uniqueness argument). Small-angle estimates, addition laws, and arctangent slope estimates alone are not evidence for the exact identity. π endpoints remain unclaimed.

### Completion-valued operational small-angle estimates

`agda/TickCompletionMagnitudeBounds.agda` now proves bounds for any chosen representative and preservation of closed bounds under arbitrary completion convergence (not just rational sequences). `agda/TickSmallAngleDensity.agda` provides a quantitative density extension with squared slack absorption and a working radius `e <= 1/4`.

`agda/TickCompletionTrigSmallAngle.agda` instantiates this extension for the implemented trigonometric residuals: on **arbitrary completion inputs** bounded by nonnegative `e <= 1/4`, `cos(a)-1` and `sin(a)-a` each have closed magnitude bound `e²`. Public definition paths identify the opaque residual functions with the actual operational sine/cosine expressions. Generic remainder-agreement lemmas in `agda/TickCompletionSumPaths.agda` avoid evaluating canonical schedules while elaborating the rational-to-completion paths.

Fresh safe `--ignore-interfaces` closure passed via `check_atan_geometric_completion.py --module TickCompletionTrigSmallAngle --timeout 900`; receipt: `results/completion-trig-small-angle-fresh.json`. This closes the rational-angle restriction in the operational small-angle estimates. The next missing step is the finite-partition/telescoping control of the Cayley defect using these estimates and arctangent slope bounds. **The exact operational Cayley identity and π endpoints are still unproved.**

### Kernel-checked quadratic telescoping criterion

`agda/TickCompletionTelescoping.agda` proves the finite telescoping identity in a generic commutative ring and specializes it to actual completion addition and negation. Closed magnitude bounds are additive, and arbitrarily shrinking bounds force exact equality. The dyadic specialization proves that `2^n` local errors bounded by `L*(2^-n)^2` accumulate to `L*2^-n`; an explicit Archimedean offset absorbs this into any requested precision. `quadratic-dyadic-partition-constant` then yields exact endpoint equality **when its explicit local-bound and grid-endpoint hypotheses are supplied**.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickCompletionTelescoping --timeout 900`; receipt: `results/completion-telescoping-fresh.json`. The receipt explicitly leaves `operational_cayley_local_defect_bound_proved` and `operational_cayley_bridge_proved` false.

**This does not yet prove the requested exact Cayley identity.** No local quadratic estimate for the actual operational Cayley defect has been supplied to the criterion. Establishing it requires the first-order cancellation using the arctangent slope and Cayley rational increment, with bounded completion-product estimates controlling the residual terms. It would be circular to assume that estimate or use the target identity to fill it. Endpoints and net outcome remain unpromoted.

### Constructed grid inverses and rational finite-increment cancellation

Following the prior-research clue, `agda/TickCayleyGridIncrement.agda` constructs the reciprocal of `1+xy` for nonnegative shared-denominator grid values `x=n/D`, `y=m/D`. It proves the reciprocal law and its nonnegative bound by one, rather than assuming a rational field inverse. `grid-increment-cancellation` proves the exact identity between the relative increment `delta/(1+xy)` and the slope increment `delta/(1+x²)`, with correction `-x*delta²/((1+xy)(1+x²))`. `grid-increment-quadratic-bound` bounds the correction by `X*e²` when `|x|<=X` and `|delta|<=e`, for nonnegative `X,e`.

`agda/TickCayleyGridSlope.agda` proves `grid-slope-is-rational`: the existing completion geometric slope at a small grid value equals the embedded constructed rational reciprocal of `1+x²`. It uses independent inverse laws and uniqueness of inverses in the actual completion ring; no operational Cayley identity is assumed.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickCayleyGridSlope --timeout 900`; receipt: `results/cayley-grid-slope-fresh.json`. This supplies the rational finite-increment cancellation and its slope identification, not yet the operational Cayley defect bound. The next step is to combine them with the completion arctangent remainder to control `A(y)-A(x)-delta/(1+xy)`, then obtain the actual rotational bracket estimate and its bounded-product transport. Exact Cayley and π endpoints remain open.

### Completion arctangent versus relative Cayley increment

`agda/TickAtanCayleyIncrement.agda` combines the constructed rational increment cancellation with the actual completion arctangent slope remainder. `relative-atan-grid-bound` proves a closed bound on

`A(y)-A(x)-embed((y-x)/(1+xy))`

for nonnegative shared-denominator small grid inputs, with bound `relativeBudget e = (scale e + scale e) + (1/2)*e² = (33/2)*e²` when the grid difference has magnitude at most nonnegative `e`. The exact remainder decomposition uses the previously checked rational identification of the completion slope and actual completion ring/embedding laws. No operational Cayley equality is assumed.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickAtanCayleyIncrement --timeout 900`; receipt: `results/atan-cayley-increment-fresh.json`. Making the reused slope bounds/class proofs opaque and using matching explicit grid expressions resolved elaboration timeouts; these changes preserve their statements.

The clock-error term in the local rotational bracket is now controlled. Still missing: a bound on the arctangent increment ensuring the completion small-angle radius, the quadratic bracket bound between the actual rotation at twice that increment and the rational Cayley increment, and bounded-product transport into the telescoping defect. The exact bridge and endpoints remain open.

### Actual denominator-cleared rotational bracket

`agda/TickAtanGridSmallAngle.agda` proves `relativeBudget e <= e` for nonnegative `e <= 1/64`, bounds the arctangent grid increment by `2e`, and bounds its double by `4e <= 1/4`. Thus application of the completion operational small-angle estimates is justified, not postulated.

`agda/TickCompletionScalarBounds.agda` proves the closed magnitude bound for multiplication by an embedded rational scalar under actual completion multiplication, using rational approximation and explicit error absorption.

`agda/TickCayleyRotationalBracket.agda` supplies public exact paths identifying its two bracket expressions with

- `(1+t²)*cos(a) - (1-t²)`;
- `(1+t²)*sin(a) - 2t`,

where on the grid `a=2*(A(y)-A(x))` and `t=(y-x)/(1+xy)`. The module proves closed magnitude bounds with explicit budgets

- `(1+e²)*(4e)² + 2e²`;
- `(1+e²)*(4e)² + (1+e²)*(2*relativeBudget e) + 2e³`.

The grid estimates require only the checked small inputs, nonnegative `e <= 1/64`, and the rational step magnitude bound. No unknown operational rotation equality is supplied as a hypothesis. Opaque generic proof wrappers avoid eager normalization of the canonical schedules during specialization.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickCayleyRotationalBracket --timeout 1200`; receipt: `results/cayley-rotational-bracket-fresh.json`. These are **denominator-cleared** local bracket bounds with explicit polynomial budgets. Still required: prove the fixed quadratic budget domination, normalize using a checked bounded inverse for the relative denominator, and transport the bracket through the outer rotation factors to the actual telescoping defect. The exact operational Cayley identity and endpoints remain unproved.

### Normalized rotational bracket with uniform quadratic budgets

`agda/TickCayleyRelativeRotor.agda` constructs the reciprocal of `1+t²` for the actual relative grid parameter `t=(y-x)/(1+xy)`, using the previously constructed grid inverses and the homogeneous denominator identity. It proves this reciprocal nonnegative and at most one. No field inverse or operational Cayley identity is postulated.

`agda/TickCayleyNormalizedBracket.agda` divides the checked denominator-cleared bracket using that constructed inverse and actual completion scalar multiplication. Its grid theorems bound the differences between the implemented cosine/sine at `a=2*(A(y)-A(x))` and the rational relative Cayley components. `agda/TickCayleyQuadraticBudgets.agda` proves fixed budget domination for nonnegative `e<=1/64`; the resulting uniform normalized bounds are **34*e²** for the real component and **99*e²** for the imaginary component.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickCayleyNormalizedBracket --timeout 1200`; receipt: `results/cayley-normalized-bracket-fresh.json`. This completes the normalized local rotational bracket estimate. The remaining step is the exact comparison-invariant difference identity and bounded-product transport through its outer rotation factors, followed by actual grid endpoint identification and application of the telescoping criterion. That invariant's local defect bound, the exact operational Cayley identity, and π endpoints are still not claimed.

### Outer-factor transport infrastructure (iteration 1)

Freshly checked `agda/TickCompletionProductMagnitude.agda`: closed completion bounds multiply under actual completion multiplication. The proof passes scalar approximation bounds through joint continuity and closed-bound limit preservation, explicitly absorbing the approximation error; continuity alone is not used as a magnitude estimate.

`agda/TickRotationDefectTransport.agda` defines completion-valued rotor multiplication and componentwise subtraction, proves the exact factored difference identity, and transports component bounds through two bounded rotor factors. Its `Grid.transported-grid-bracket` uses the actual normalized operational grid bracket (both components weakened to `99*e²`), with resulting budget `((P*(99*e²)+P*(99*e²))*Q)+((P*(99*e²)+P*(99*e²))*Q)` for outer component bounds P,Q. The required outer bounds remain explicit inputs, not claimed theorems about the intended rotations.

Fresh safe dependency closure passed via `check_atan_geometric_completion.py --module TickRotationDefectTransport --timeout 1200`; receipt `results/rotation-defect-transport-fresh.json`.

Next executable steps: construct uniform bounds for the actual outer operational rotor and rational inverse rotor; identify the two products in the factored difference with consecutive values of `H(x)=R(2A(x))*V(-x)` using actual addition and rational composition; establish the grid endpoint paths and then apply telescoping. No invariant-step bound or telescoping application has yet been claimed.

### Concrete outer factors (iteration 2)

Fresh safe closure passed for `agda/TickCayleyConcreteTransport.agda`, receipt `results/cayley-concrete-transport-fresh.json`.

New checked dependencies:
- `TickCayleyOuterRotor.agda`: actual rational grid Cayley and inverse rotors; embedded inverse law; inverse rotor components bounded by 2 on the half-radius input interval.
- `TickOperationalRotorIncrement.agda`: actual operational rotor addition and exact doubled-arctangent grid increment path (including sine summand order).
- `TickAtanOuterAngleBound.agda`: arctangent completion bounded by 2 via finite partial sums and closed-bound limit preservation, hence doubled grid angles bounded by 4.
- `TickOperationalOuterRotorBound.agda`: rotations of inputs bounded by 4 have a uniform component bound `rotorRadius 4`. This deliberately coarse bound comes from scaling by 1/16, applying the checked small-angle estimates, and four applications of operational addition and product magnitude bounds. Each rational doubling is normalized before the next; no large raw denominator normalization is needed.

`TickCayleyConcreteTransport.Grid.concrete-transport-bound` now uses the concrete intended outer factors and their proved bounds. Its first product is identified with `gridInvariant m d hy`. The second is still `(R(gridAngle n)*relativeRotor(n,m))*inverseCayleyRotor(m)`. NEXT: prove rational composition identifies that product with `gridInvariant n d hx` (the constructed relative reciprocal is in `TickCayleyRelativeRotor.agda`). Then construct dyadic grid endpoint paths and step bounds and apply telescoping. The second-product identity and the telescoping application are not yet claimed.

### Actual invariant-step bound (iteration 3)

`TickCayleyRotorComposition.agda` proves the relative rotor equals `inverseCayleyRotor(x)*cayleyRotor(y)` using the constructed reciprocal and exact polynomial cancellation. It also proves completion rotor associativity and cancellation against `inverseCayleyRotor(y)`.

`TickCayleyInvariantStep.agda` identifies the previously open second comparison product with `gridInvariant n d hx`. Its `invariant-step-bound` proves the actual difference `gridInvariant m d hy - gridInvariant n d hx` has both components bounded by `invariantCoefficient*(e*e)` under the existing small-input and step hypotheses. The coefficient is a fixed rational expression independent of the grid and e. The checker now truthfully marks `operational_cayley_local_defect_bound_proved` for this closure.

`TickCompletionTelescoping.agda` now includes `fine-quadratic-dyadic-partition-constant`, allowing local estimates only for meshes n at least a fixed depth. It uses n=errorOffset(L)+(depth+k) and retains the true count 2^n, rather than incorrectly shifting the count. This matches the invariant bound's e<=1/64 hypothesis.

Fresh safe closure passed separately for both modules; receipts `results/cayley-invariant-step-fresh.json` and `results/completion-telescoping-fresh.json`.

NEXT: construct concrete dyadic grids for a target `gridValue N d` within the half-radius interval, prove their shared-denominator adjacent step bounds and endpoint invariant paths (including proof irrelevance for magnitude witnesses and rational inverse uniqueness under re-presentation), and apply the fine-mesh criterion componentwise. The actual local-defect estimate is now complete, but no concrete telescoping application or Cayley endpoint equality is claimed yet.

### Concrete dyadic telescoping applied (iteration 4)

Fresh safe dependency closure passed for `TickCayleyInvariantConstancy.agda`; receipt `results/cayley-invariant-constancy-fresh.json`.

- `TickCayleyDyadicMesh.agda` constructs the shared-denominator mesh `meshPoint N d n j`. It proves its formula `(natℚ j * gridValue N d)*precision n`, exact zero/target endpoints, half-radius bounds for j<=2^n, and actual adjacent-step magnitude <=precision n.
- `TickCayleyInvariantRepresentation.agda` proves the invariant independent of rational grid representation and magnitude witnesses, using rational inverse uniqueness and proof irrelevance of rational inequalities.
- `TickCayleyDyadicTelescoping.agda` constructs total grids by capping j at 2^n and proves the actual invariant endpoint paths and all fine-mesh local bounds.
- `TickRotorTelescoping.agda` packages the checked scalar criterion componentwise, keeping its arguments neutral to avoid eager normalization of concrete operational schedules.
- `TickCayleyInvariantConstancy.invariant-constant` APPLIES this criterion: for any natural N,d with `MagnitudeBound (gridValue N d) one-half`, it proves `gridInvariant 0 0 zero-small = gridInvariant N d h`. This is no longer conditional on unknown local or endpoint paths.

NEXT: evaluate the zero invariant using checked atan and operational sine/cosine zero laws, then cancel the rational inverse rotor to expose `R(2*A(gridValue N d))=cayleyRotor N d`. That explicit rearrangement and the Machin/π endpoint identities are not yet claimed. The outer-factor transport and concrete telescoping application requested in iterations 1–4 have now been kernel-checked.

### Explicit operational Cayley identity (iteration 5)

`agda/TickOperationalCayleyIdentity.agda` evaluates the zero invariant using the checked arctangent, operational cosine, and operational sine zero laws, then cancels the constructed rational inverse rotor. Its public `operational-cayley-grid` proves

`rotation (gridAngle N d h) = cayleyRotor N d`

for natural N,d and `h : MagnitudeBound (gridValue N d) one-half`. The component theorems `operational-cayley-cosine` and `operational-cayley-sine` expose the exact implemented completion cosine/sine identities. This covers nonnegative rational grid presentations N/(d+1) within [0,1/2]. No negative-input extension is claimed.

Fresh safe `--ignore-interfaces` dependency closure passed, with stable sources, via `check_atan_geometric_completion.py --module TickOperationalCayleyIdentity --timeout 1200`; receipt `results/operational-cayley-identity-fresh.json`. The receipt now sets `operational_cayley_bridge_proved=true` and explicitly records the nonnegative half-radius grid domain. `machin_endpoints_proved` and `unitary_half_turn_proved` remain false.

The requested outer-factor transport and concrete telescoping objective is complete, including the resulting explicit operational Cayley identity. Subsequent Machin/π endpoint assembly is a separate remaining objective. Earlier NEXT/open statements above are chronological checkpoints superseded by this section where applicable.

### Machin input instantiation and endpoint reduction

`TickMachinCayleyInputs.agda` proves equality between the generic arctangent completion and the existing opaque fifth/239th values from their actual sample paths. It instantiates the checked operational Cayley theorem at both inputs. `gridCayley` is an opaque alias with a public definition path to the existing rational rotor, not a different backend; this prevents eager normalization of closed scheduled products during specialization.

`TickMachinEndpointReduction.agda` proves rotation inversion, difference cancellation, doubling, the Machin angle rearrangement and negative-half-turn transport. The result `machin-endpoints-from-rational` has just one hypothesis: `RationalMachinGate`, namely `square(square(gridCayley 1 4)) = imaginaryRotor * gridCayley 1 238`. This is the remaining exact rational arithmetic obligation, not an assumed analytic or trigonometric law. No endpoint equality is claimed until that gate is constructed.

Fresh safe closure passed via `check_machin_endpoint_reduction.py --timeout 1200`; receipt `results/machin-endpoint-reduction-fresh.json`. The supporting component is synchronized into the conjecture-net manifest and its admission checker, without closing the pi node or removing MachinEndpoints.

NEXT: prove RationalMachinGate in Agda, preferably by staged symbolic rational normalization rather than expanding large unary denominator products. Then apply the checked reduction; standard-pi identification remains separate.

### Exact Machin endpoints proved

`TickCayleyRationalNormalization.agda` supplies generic fraction cancellation and homogeneous Cayley normalization without expanding large concrete denominator products. `TickMachinRationalGate.agda` uses opaque, definitionally linked fraction rotors and staged arithmetic:

- Cayley(1/5) = (12/13, 5/13);
- its square = (119/169, 120/169);
- its fourth power = (-239/28561, 28560/28561);
- Cayley(1/239) = (28560/28561, 239/28561).

The fourth power is therefore exactly i times Cayley(1/239). This is an Agda proof, not just the earlier external rational audit. `TickRotorQuarterTurn.agda` supplies the neutral completion-level quarter-turn path to avoid eager normalization of scheduled products.

`TickMachinEndpoints.agda` applies the checked endpoint reduction. It proves `machin-endpoints : MachinEndpoints` and `machin-phase-half-turn` for the existing constructed candidate. Fresh safe dependency closure passed via `check_machin_endpoints.py --timeout 1200`; receipt `results/machin-endpoints-fresh.json`.

The net now admits this as a supporting component and removes MachinEndpoints from the remaining obligations. The pi node remains in progress solely for standard-pi identification at the accepted formal level. The separate derivative obligation remains paused; full unitary-half-turn and whole-return outcomes are not promoted. Earlier open endpoint/gate statements in this chronological log are superseded by this section.

### Checked reference-series comparison

`TickMachinReferenceSeries.agda` isolates a single ordinary rational sequence, using the same cutoff n in both arctangent partial sums: `M_n = 16*A_n(1/5)-4*A_n(1/239)` (integer scaling is implemented by repeated addition). It proves the all-later bound `|M_m-M_n| <= 20*precision n` for every m>=n and proves this sequence converges in the actual completion metric to `machinPi`, despite the candidate's independently scheduled addition representatives.

`reference-series-identification` proves `machinPi = referencePi` whenever the same rational sequence is proved to converge to referencePi. The theorem is deliberately conditional: it does not instantiate a standard-pi constant or turn its own conclusion into a definition of standard pi.

Fresh safe closure passed via `check_machin_reference_series.py --timeout 1200`, receipt `results/machin-reference-series-fresh.json`. The net admits this supporting comparison component without removing standard-pi identification.

The local Agda search found no existing standardPi object or canonical classical-real interpretation module. The imported standard witness uses ordinary classical pi in a written proof; the earlier classical Machin identification remains at that evidence level. The remaining work is now a reference interpretation/convergence proof, not another operational endpoint calculation. Do not close the node by relabeling machinPi or by treating this universal comparison theorem's premise as discharged. A nonredundant next route is an independently specified reference-real interpretation carrying rational embeddings and limits, with an actual proof that its standard pi is the limit of this sequence.

### Concrete standard-real semantic identification

`standard-pi-identification.md` constructs `rho([x])=lim_n i_Q(approximation x n)` into the ordinary reals of the imported witness. It proves existence, independence of representative, compatibility with rational embedding and soundness for the actual existential-representative completion balls and convergence interface. It then proves the common-cutoff Machin series converges to ordinary pi using a finite integrated geometric identity with explicit remainder, exact rational rotations, and strict argument bounds. Consequently `rho(machinPi)=pi`, not an unspecified odd half-turn.

This is a complete written classical-real proof, not a new Agda theorem implementing classical R. `check_standard_pi_identification.py --timeout 1200` freshly rechecked both the operational endpoint closure and reference-series closure, audited the exact rational branch and rotation identities, validated the pinned imported standard witness, and bound the written proof and implementation dependencies. Receipt: `results/standard-pi-identification.json`.

The supporting evidence is synchronized into the net at its actual verification level. No parent outcome is promoted: accepting a mixed certificate (kernel operational endpoints plus written standard-real interpretation) or formalizing the interpretation itself remains an explicit acceptance boundary. Further rational fixtures do not discharge that boundary. The derivative remains paused.

### Operator accepts mixed-level closure

The operator explicitly instructed: `accept mixed-level certificate`. Recorded in `contracts/pi-mixed-level-acceptance.v1.json`; live evidence admission passed via `check_pi_mixed_acceptance.py`, producing `results/pi-mixed-level-accepted.json`.

The `completion-pi-half-turn` node is now **++ at the accepted mixed level**: safe Agda construction and exact operational endpoints, with written canonical standard-real interpretation and identification. `standard_pi_identification_kernel_proved` remains false. The prior progress and receipts are retained as historical evidence; they are not rewritten to claim stronger verification.

Only this node closes. The phase derivative is still open, the regularity attempt remains paused without a budget reset, and flow/full-unitary-half-turn/whole-return assembly is not automatically promoted. The net recommends resuming the existing regularity attempt at PhaseDerivativeLaw. Planning is conditioned on accepted pi closure; its retained numerical scenario is not a measured remaining-effort budget.

## Verification and net state

The checker separates cached and fresh receipts:

- `results/machin-pi-candidate-cached.json`;
- `results/machin-pi-candidate-fresh.json`.

Fresh safe `--ignore-interfaces` closure **passed in 251.528 seconds**, with stable source/compiler/library hashes. Only such a fresh pass admits the construction checkpoint. The receipt explicitly leaves `pi_endpoints_proved`, `standard_pi_identification_kernel_proved`, and `full_claim_proved` false.

The pi node remains unresolved and active. Regularity remains unresolved and paused, with continuity already proved. Unit-circle flow, the half-turn and final assembly are not promoted. Original cost/probability estimates remain pre-attempt forecasts; switching branches does not reset the paused attempt or invent an independent retry.

```text
python research/nima/checkers/check_atan_geometric_completion.py --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickAtanCompletionFirstOrder --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickAtanCompletionSlope --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickOperationalTrigFirstOrder --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickCompletionTrigSmallAngle --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickCompletionTelescoping --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickCayleyGridSlope --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickAtanCayleyIncrement --timeout 900
python research/nima/checkers/check_atan_geometric_completion.py --module TickCayleyRotationalBracket --timeout 1200
python research/nima/checkers/check_atan_geometric_completion.py --module TickCayleyNormalizedBracket --timeout 1200
python research/nima/checkers/check_atan_geometric_completion.py --module TickOperationalCayleyIdentity --timeout 1200
python research/nima/checkers/test_machin_pi_candidate.py
python research/nima/checkers/check_machin_pi_candidate.py --timeout 1800
python research/nima/checkers/test_trig_addition_foundations.py
python research/nima/checkers/check_trig_addition_foundations.py --timeout 1800
python research/nima/checkers/test_completion_trig_addition.py
python research/nima/checkers/check_completion_trig_addition.py --timeout 1800
python research/nima/checkers/test_completion_refinement_net.py
python research/nima/checkers/test_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_net.py
```
