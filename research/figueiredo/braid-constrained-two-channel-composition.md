# Research Note: Braid-Constrained Two-Channel Composition

Date: 2026-10-09
Status: Constructive algebraic model; amplitude parameters unresolved
Research sequence: Shape interaction → permutation gluing → braid histories → unitary composition

## 1. Research objective

Construct a reversible composition law for two interacting shapes that:

1. Permits exactly two or three closed output components.
2. Preserves a distinguished attachment.
3. Retains information about distinct interaction histories.
4. Allows coherent interference between histories.
5. Determines observable output probabilities.

Experimental constraint adopted for subsequent investigation:

P(2 outputs) / P(3 outputs) = 372

The ratio is treated as an input constraint, not as a result of the construction.

## 2. Starting geometry

Consider two oriented shapes, each containing three attachment sites.

A gluing operation joins corresponding attachments.

The resulting number of closed components is determined by the cycle decomposition of the endpoint permutation.

For three strands:

| Permutation | Cycles | Closed components |
|---|---|---:|
| Identity | (1)(2)(3) | 3 |
| Transposition | (12)(3), etc. | 2 |
| Three-cycle | (123) or (132) | 1 |

This follows from the topology of closing the strands.

## 3. Preserved-attachment constraint

Require attachment 1 to return to its original position.

Let B₃ be the three-strand braid group, and let

π: B₃ → S₃

map each braid to its endpoint permutation.

Define:

G = {b ∈ B₃ : π(b)(1) = 1}

G is a subgroup because the condition is preserved under composition and inversion.

Only two endpoint permutations remain:

- Identity: three closed components.
- (23): two closed components.

Thus the admissible output count is restricted to:

N ∈ {2,3}

The one-component channel is excluded by the preserved-attachment condition.

## 4. Distinct histories with identical outputs

The braid group B₃ has generators σ₁ and σ₂ satisfying:

σ₁σ₂σ₁ = σ₂σ₁σ₂

Within G, consider:

a = σ₂

b = σ₁²

Their endpoint permutations are:

π(a) = (23)

π(b) = identity

Both preserve attachment 1.

They do not commute:

ab ≠ ba

Consequently, two interaction histories can have the same endpoint permutation and output multiplicity while retaining distinct braiding information.

Endpoint permutations determine the number of components.

Braid histories contain additional topological information.

## 5. Minimal two-channel state space

Introduce two output states:

|2⟩ = two closed components

|3⟩ = three closed components

The channel state space is:

Hc = span{|2⟩, |3⟩}

Introduce an auxiliary two-state space:

Hi = span{|0⟩, |1⟩}

The complete model space is:

H = Hc ⊗ Hi

It has dimension four.

The auxiliary states provide degrees of freedom for distinguishing interaction dynamics beyond output multiplicity.

Their physical or topological interpretation remains unspecified.

## 6. Candidate composition generator

Let X and Z be Pauli matrices:

X = [[0,1],[1,0]]

Z = [[1,0],[0,-1]]

Define the Hermitian operator:

H = g X⊗X + δ I⊗Z

The two terms do not commute:

[X⊗X, I⊗Z] ≠ 0

Here:

g = channel-coupling strength

δ = internal-state splitting

Both are real parameters.

The corresponding unitary evolution is:

U(t) = exp(−itH)

Since H is Hermitian:

U(t)†U(t) = I

and:

U(−t) = U(t)⁻¹

Thus the dynamics is reversible.

This operator is a candidate two-channel dynamics. A representation mapping the braid subgroup G into this dynamics has not been constructed.

## 7. Evolution from three components

Take the initial state:

|ψ₀⟩ = |3⟩⊗|0⟩

The operator H couples this state to:

|2⟩⊗|1⟩

Within that invariant two-dimensional subspace, H has matrix:

H₂ = [[δ,g],[g,−δ]]

Define:

ω = √(g²+δ²)

Then:

U(t) = cos(ωt)I − i sin(ωt)H₂/ω

The probability of the two-component outcome is:

P(2) = [g²/(g²+δ²)] sin²(ωt)

The probability of the three-component outcome is:

P(3) = 1 − P(2)

Therefore:

P(2)+P(3)=1

No one-component outcome exists in the chosen state space.

## 8. Applying the observed ratio

Adopt:

P(2)/P(3) = 372

Normalization gives:

P(2) = 372/373

P(3) = 1/373

The model must therefore satisfy:

[g²/(g²+δ²)] sin²(t√(g²+δ²)) = 372/373

Because sin² cannot exceed 1, a necessary condition is:

g² ≥ 372δ²

Equivalently:

|δ/g| ≤ 1/√372

Thus, within this model, the assumed ratio constrains the internal splitting relative to the channel coupling.

It also constrains the accumulated evolution angle.

These conditions follow algebraically from the chosen Hamiltonian and the assumed probability ratio.

## 9. Special case: no internal splitting

Set:

δ = 0

Then:

P(2) = sin²(gt)

P(3) = cos²(gt)

and:

P(2)/P(3) = tan²(gt)

The target ratio requires:

tan²(gt) = 372

Hence:

gt = arctan(√372) modulo the corresponding periodic solutions.

The interaction angle remains a free parameter.

The construction accommodates the observed ratio but does not determine it.

## 10. Mathematical results

The following properties follow from the definitions.

A. Closure

The subgroup G is closed under braid composition and inversion.

B. Output restriction

The preserved-attachment condition allows exactly two endpoint-permutation types, producing two or three closed components.

C. History distinction

Noncommuting braid histories can preserve the same attachment and produce identical component counts.

D. Reversibility

The proposed Hermitian generator produces unitary, reversible evolution.

E. Normalization

The two output probabilities sum to one.

F. Nontrivial interference

The exponential evolution operator coherently sums powers of the interaction generator.

G. Numerical constraint

The assumed 372:1 ratio restricts g, δ, and t but does not uniquely determine them.

## 11. Unresolved structural connections

The braid subgroup and the unitary dynamics have been constructed separately.

A complete composition theory must establish their relationship.

Specifically, it must determine:

1. A representation of G on a suitable state space.
2. An amplitude assignment consistent with braid relations.
3. An invariant inner product supporting probability interpretation.
4. A rule mapping braid histories to two- and three-component channels.
5. A composition law for combining alternative histories.
6. A geometric determination of the interaction parameters.

Without these connections, the Hamiltonian is an admissible model rather than a consequence of braid topology.

## 12. Relation to previous simplex research

The earlier investigation used:

- Two tetrahedra sharing a face → three triangles.
- Two tetrahedra sharing an edge → two triangles.
- Simplicial incidence, orientation, and Pachner recombination.
- Link topology and exterior algebra.
- Polarization correlations and alternating joint states.

Those constructions identified possible output structures but did not determine their relative amplitudes.

The present construction shifts the mathematical object of interest.

Instead of treating an interaction only as a transformation between geometric configurations, it treats the interaction as a composition of histories.

The retained topological information is now:

- Attachment correspondence.
- Endpoint permutation.
- Braid history.
- Output component count.
- Internal state.
- Composition amplitude.

Simplicial structures can still represent the participating shapes, but the proposed interaction law operates on their compositional histories.

## 13. Main finding

The preserved-attachment braid subgroup supplies a natural two-channel output classification.

A reversible unitary model can assign amplitudes to those channels while preserving normalization and allowing noncommuting internal dynamics.

The resulting probabilities are:

P(2) = [g²/(g²+δ²)] sin²(t√(g²+δ²))

P(3) = 1 − P(2)

The numerical ratio between the channels depends on the interaction parameters.

Braid topology determines the available endpoint configurations but has not determined their amplitude weights.

## 14. Next research target

Construct a functorial representation of the preserved-attachment braid subgroup into a category of unitary state transformations.

Required structure:

G → U(H)

The mapping must respect composition:

ρ(ab) = ρ(a)ρ(b)

It must also retain enough information to distinguish the two output multiplicities.

The critical acceptance test is whether the representation and its normalization arise from the underlying shape geometry without selecting the measured amplitude ratio in advance.

The central conjecture is that observable multiplicity probabilities are determined by the coherent composition of admissible topological interaction histories.

The present result establishes a candidate algebraic architecture for testing that conjecture.
