# Prior research clues for the operational Cayley bridge

This is a read-only research search and a proposed proof route, not a new Agda receipt. The operational Cayley identity and Machin endpoints remain unproved.

## Strongest prior results

1. `rational-rotor-source-audit.md`, `agda/RationalRotorNumerators.agda`, and `checkers/check_rational_rotor_source_audit.py` supply the exact rational rotor law

   `V(t) = ((1-t²), 2t)/(1+t²)`,
   `V(t)V(u) = V((t+u)/(1-tu))`.

   The Agda module proves homogeneous numerator norm and composition identities in a generic commutative ring and instantiates the older constructed rational ring. Its statements can be instantiated in the preferred rational ring; denominator cancellation, positive inverse bounds, and operational completion transport still need checking. The Python checker also verifies `V'(t)=2J V(t)/(1+t²)` and invariance of the rational differential, but those derivative assertions are not Agda theorems.

2. `retained-rational-flow-jets.md` and `checkers/check_retained_rational_flow_jets.py` contain the exact intended formal identity `E(ell(t))=V(t)`, where `ell(t)=2 atan(t)`. The all-order coefficient recurrence and uniqueness are formalized in `agda/FormalRotorCoefficients.agda`; the full formal-series composition identity is not. Formal substitution cannot be treated as an evaluation theorem for the operational completion functions.

3. `retained-rotor-norm-completion.md` gives an earlier analytic route to precisely this bridge: convergence of selected rotor polynomials, compact-uniform derivative tails, and equal ODE plus initial value. Its checker tests rational finite certificates and records a boundary negative control: differentiated clock partial sums at `t=1` alternate between zero and two. The note explicitly says this is not an Agda formalization of real analysis. It therefore provides a mathematical blueprint, not a missing kernel proof ready to import.

4. `unit-circle-understanding-review.md` recommends separating finite algebra, fixed-input convergence, and completion transport, and reusing the existing generic residual/product machinery. It explicitly found no ready operational ODE uniqueness theorem. Much of its older trigonometric coefficient gap has since been addressed by our addition/norm work; its warning against duplicating infrastructure remains applicable.

## More direct finite-increment route suggested by the search

Write `A(x)` for the constructed small arctangent, and `R(a)` for the actual operational rotation `(cos(a), sin(a))`. For adjacent partition points `x,y`, set

- `delta = y-x`;
- `t = delta/(1+xy)`;
- `dA = A(y)-A(x)`.

The rational composition law gives **exactly** `V(y)=V(x)V(t)`. Moreover,

`t - delta/(1+x²) = -x*delta² / ((1+xy)(1+x²))`.

This identity is a finite rational numerator cancellation, not a derivative-limit theorem. On a same-sign partition of the small interval, both denominators are at least one. Combined with the already proved arctangent slope remainder, it should give a uniform quadratic bound on `dA-t`.

Define the comparison invariant

`H(x) = R(2A(x)) V(-x)`.

Using actual operational addition and rational rotor composition,

`H(y)-H(x) = R(2A(x)) [R(2dA)-V(t)] V(-y)`.

Now the first-order terms of `R(2dA)` and `V(t)` cancel up to `2(dA-t)`. The completion-valued operational estimates for `cos(a)-1` and `sin(a)-a`, together with exact rational formulas for `V(t)-(1,2t)`, should make the bracket uniformly quadratic in `delta`. Importantly, one must also bound `dA` so that the operational small-angle estimate's radius hypothesis is satisfied; choosing a sufficiently fine partition is not itself that proof.

The outer rational rotor is bounded. The outer operational rotation needs a uniform bound over the arctangent range; a fixed-radius Taylor majorant would suffice, so extraction of sharp component bounds from unit norm is optional. A uniform completion-product magnitude lemma must be supplied rather than treating metric continuity as a numerical product bound.

After those bounds are actually checked, apply `TickCompletionTelescoping.quadratic-dyadic-partition-constant` componentwise. `H(0)=(1,0)` follows from the checked zero laws. Constancy gives `R(2A(q))=V(q)` by the rational inverse law. This route avoids constructing a general differentiation or ODE uniqueness framework.

## Reusable library interfaces, inspected rather than reimplemented

- `research/voevodsky/agda/CauchyProductCongruence.agda`: `pointwise-product-difference-bound` uses the exact decomposition of a product difference and two magnitude estimates. The same module supplies bounded rational-density and eventual-comparison transport for products and sums of products.
- `research/voevodsky/agda/CauchyProductErrorBounds.agda`: first/second product errors, their decomposition, and refined scale absorption.
- `research/voevodsky/agda/CauchyProductBounds.agda`: `arbitrary-multiplier-bound`, `nonnegative-multiplier-bound`, and `add-magnitude-bounds` are the rational scalar estimates behind these product proofs.
- `research/voevodsky/agda/AbsoluteTaylorSeriesMultiplication.agda`: generic finite rectangular/triangular residual estimates and global majorants. These are relevant to a formal-series alternative or fixed-radius operational bounds, not evidence that the Cayley comparison itself has been proved.

## Findings that do not close the bridge

`research/kitaev/checkers/check_theta_rational_enclosures.py` uses the classical Machin identity to construct rational pi enclosures. It does not derive that identity for the implemented completion functions. Other Cayley hits concern Cayley--Menger determinants, scattering/impedance transforms, or finite group tables and do not address this rotation bridge.

## Recommended next proof, not another general abstraction

Instantiate the existing rotor numerator identities for the relative parameter `t`, prove the displayed rational quadratic increment identity with explicit denominator bounds, and combine it with the checked arctangent remainder. Then prove the actual bracket estimate `R(2dA)-V(t)=O(delta²)` and its bounded-product transport. Those are the missing local hypotheses of the already checked telescoping criterion. No additional generic telescoping theorem is needed.
