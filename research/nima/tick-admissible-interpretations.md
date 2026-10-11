# Admissible Tick interpretations and non-uniqueness beyond speed

## 1. Declared interpretation class

Fix the existing Bool/notEquiv Tick at source `s`. Use the four basis
vectors `e_q` of the real probability simplex, indexed by `q ∈ Bool²`.
Let `L` and `R` be its two bit-flip permutation matrices.

An admissible **retained stochastic schedule realization** supplies:

1. The original full Tick as a recoverable structural component. Its actual
   two ordered schedule tags are used, not replaced by fixed tags.
2. Continuous matrix-valued axis legs `A_L(t), A_R(t)`, `0≤t≤1`, with
   nonnegative entries and column sums one.
3. Exact operator endpoints `A_L(0)=A_R(0)=I`, `A_L(1)=L`, `A_R(1)=R`.
4. For each retained schedule, the corresponding two-leg path on `[0,2]`,
   joined at its actual intermediate state, starting at `e_s` and ending
   at the encoded Tick target.
5. A chosen reverse path returning from the target to the source.

This is a declared class of external annotations, not a source-derived
law of motion. Retaining the full Tick proves source recoverability; it
is NOT proof that the continuous path itself faithfully encodes the Tick.
No requirement of unitarity, invertibility between corners, an autonomous
flow/semigroup law, or a physical interpretation of cubical interval
coordinates is included.

The full Bool Tick classification justifies that source record equality
has no additional independent return-section or proof-term distinctions
beyond the ordered tags at this fixed source. It does not turn the chosen
reverse real-time path into the dependent Agda return section. A functorial
interpretation of that section as analytic geometry would need a separately
specified target category and preservation laws.

## 2. Equivalence under time reparameterization

For a fixed Tick, consider one retained schedule at a time. Two forward
paths are equivalent if an increasing endpoint-preserving homeomorphism
`ρ : [0,2] → [0,2]` makes `γ₁(ρ(t)) = γ₂(t)` for every `t`. Requiring
preservation of the intermediate time would only strengthen this condition.
An equivalence of interpretations must respect each ordered schedule.

The counterexample below rules out even an arbitrary parameter function
with that pointwise equality. Thus it is stronger than a rate distinction.

## 3. Two admissible families

Straight:

    A_L(t) = (1-t) I + t L
    A_R(t) = (1-t) I + t R

Bowed:

    B_L(t) = (1-t)² I + t L + t(1-t) R
    B_R(t) = (1-t)² I + t R + t(1-t) L

All coefficients are nonnegative on `[0,1]`, sum to one, and give the
required operator endpoints. These are continuous polynomial matrices.
They are generally NOT unitary or invertible; stochasticity is the declared
condition for this counterexample.

For leftFirst, define the global path for either family `C` by

    γ_C(t) = C_L(t) e_s                 for 0≤t≤1
    γ_C(t) = C_R(t-1) e_(Ls)            for 1≤t≤2.

The formulas agree at `t=1`, so ordinary finite closed-interval pasting
proves continuity. RightFirst exchanges `L` and `R`. At `t=2` the target
is `e_(LRs)` for both. Reverse each global path to obtain the chosen return.
Both families handle every source and all four possible ordered pairs of
retained tags, including repeated tags allowed by the existing record.

They can also instantiate the earlier endpoint algebraic contract via
`U_C(a,b)=C_R(b) C_L(a)`: all four operator corners have the same values.
For these particular families the operators are polynomials in commuting
`L,R`, although commutation is not needed for the individual endpoint checks.

## 4. A state-image obstruction—not a speed rescaling

Take leftFirst. The whole straight path lies in the face spanned by

    e_s, e_(Ls), e_(LRs).

Consequently its coordinate at `Rs` is identically zero on BOTH legs.
At the midpoint of the bowed first leg,

    γ_B(1/2) = (1/4)e_s + (1/2)e_(Ls) + (1/4)e_(Rs).

Its `Rs` coordinate is `1/4`, so it is not in the image of the straight
path at ANY time. No parameter substitution can identify these paths.
For rightFirst, exchange `L` and `R` and use the missing `Ls` coordinate.
This works for all four sources. The reverse paths do not change this
image obstruction.

**Conclusion:** the full Bool Tick does not select a unique realization,
even modulo time reparameterization, WITHIN THIS DECLARED CLASS.
This is not a no-go theorem for uniqueness under stronger, additional
physical axioms or for faithful geometric interpretations not defined here.

## 5. Verification boundary

- `agda/TickRetainedStructure.agda`: machine-checked full source
  classification and readout injectivity.
- `agda/TickInterpretationBoundary.agda`: machine-checked source-retaining
  interpretation wrapper and a general image-invariant obstruction to ANY
  parameter substitution. The wrapper assumes `EndpointModel`; it does
  not assert continuity or stochasticity by itself.
- `checkers/check_tick_interpretation_nonuniqueness.py`: exact rational
  polynomial certificates for both concrete families, endpoints, joins,
  normalization, nonnegativity via degree-two Bernstein coefficients,
  reverse paths, and the zero-versus-1/4 obstruction. 208/208 checks pass,
  covering eight source/schedule image obstructions.
- `agda/TickCompletionSeparation.agda` now proves the embedded rational
  `1/4` differs from completion zero. Quotient effectiveness would otherwise
  force the false exact rational inequality `1/4 ≤ 1/8`.
- `agda/TickConcreteImageObstruction.agda` now constructs both concrete
  completion-valued endpoint models, puts them through the same
  source-retaining contract, and defines the complete bowed leftFirst path
  on the existing glued-chart domain. `no-global-substitution` proves that
  NO parameter function can turn the straight path into that bowed path.
  This concrete Agda theorem is for source `(false,false)` and leftFirst;
  the exact checker covers the eight source/schedule cases.
- The checker still does not consume Agda Tick terms. The real unit-interval
  stochasticity and closed-interval pasting argument above have NOT been
  instantiated as one complete analytic Agda theorem. The new obstruction
  uses the existing pushout of entire completion charts, not a proved real
  interval. The bowed model's endpoint laws and image obstruction are now
  formal; a formal proof of its membership in the full continuous stochastic
  interval class remains a separate obligation.

Fresh headless Agda closure verification of the interpretation-boundary
module exits 0; only the existing dependency export warning remains.
