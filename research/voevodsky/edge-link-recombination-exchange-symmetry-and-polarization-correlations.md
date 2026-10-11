# Research Note: Edge-Link Recombination, Exchange Symmetry, and Polarization Correlations

**Date:** 2026-10-09  
**Status:** Constructive investigation; universal composition law unresolved  
**Continuation of:** Simplicial Recombination and Particle Interaction Structures; Dimensional Resolution in Simplex Interaction

## 1. Research objective

Determine whether the proposed two-triangle output of an edge-sharing tetrahedral interaction follows from intrinsic simplicial composition.

Candidate transformation:

2Δ³ → 2Δ²

Experimental reference:

electron + positron → 2 photons

The broader objective remains a universal composition law that generates admissible output structures, their correlations, and their relative probabilities.

The investigation uses established experimental observations as constraints without adopting conventional subatomic interpretations as structural premises.

## 2. Edge-sharing input complex

Take two tetrahedra sharing edge AB:

K = ABCD ∪ ABEF

Their link at AB consists of two disconnected edges:

Lk(AB) = CD ⊔ EF

The link has two connected components. Its zeroth homology over the real numbers is therefore two-dimensional:

V = H₀(Lk(AB); ℝ)

Choose basis elements:

x = [CD], y = [EF]

This provides an intrinsic two-dimensional vector space associated with the edge-sharing configuration.

It does not by itself provide a Euclidean metric, physical polarization directions, or a nontrivial continuous rotation action.

## 3. Symmetry analysis of the 2→2 construction

We previously proposed the output:

ACE ∪ BDF

The input has symmetries exchanging A with B, C with D, E with F, and the two tetrahedra.

The 20 possible triangles form symmetry orbits of sizes 4, 4, 4, and 8.

An initial conclusion was that these symmetries prohibited selecting exactly two output triangles.

That conclusion was incorrect.

A deterministic output invariant under every input automorphism is different from a symmetry-equivariant family of possible outputs.

Four complementary two-triangle configurations are available:

| Configuration | Output |
|---|---|
| L₁ | ACE ∪ BDF |
| L₂ | ACF ∪ BDE |
| L₃ | ADE ∪ BCF |
| L₄ | ADF ∪ BCE |

Every output partitions the six vertices into two disjoint triples.

Each triple contains one vertex from each of the pairs AB, CD, and EF.

All four configurations have the same abstract incidence type.

An orientation-dependent convention can distinguish them. Whether that convention follows intrinsically from oriented simplicial composition remains unresolved.

## 4. Reversibility and retained correspondence

The proposed output L₁ loses the original shared edge AB and the link edges CD and EF.

Consequently, its incidence structure alone does not uniquely reconstruct the input.

Introduce the retained vertex correspondence:

τ = (AB)(CD)(EF)

This exchanges the output triangles:

τ(ACE) = BDF

With τ and the distinguished original edge AB retained, the original two tetrahedra can be reconstructed.

The reversible state therefore contains more than the output complex.

Candidate state representation:

X = (K, τ, distinguished edge, orientation data)

The additional correspondence must be transported through recombination.

This identifies a possible role for structured morphisms between simplicial complexes: preserving information required for inverse construction.

## 5. Topology of the two proposed output channels

The face-sharing construction produces:

ADE ∪ BDE ∪ CDE

The edge-sharing construction produces:

ACE ∪ BDF

| Property | 2→2 | 2→3 |
|---|---|---|
| Output triangles | 2 | 3 |
| Connected components | 2 | 1 |
| Shared output edge | None | DE |
| Euler characteristic | 2 | 1 |

These are distinct abstract topological structures.

Experimentally, the two photons produced by annihilation exhibit correlations despite their spatial separation.

Therefore, connectedness of the output simplicial complex cannot alone determine whether its associated observable outputs are correlated.

The retained correspondence τ was investigated as a possible source of joint structure.

## 6. Candidate geometric polarization rule

Embed the two tetrahedra in three-dimensional space.

Let P project vectors onto the plane perpendicular to their shared edge AB.

Define:

u = P(D − C)

v = P(F − E)

Rotating the second tetrahedron about AB changes the direction of v continuously while preserving abstract incidence.

This produces a relative angle θ between u and v.

A candidate rule identifies these transverse geometric directions with polarization axes of the two output objects.

The rule encountered two problems.

First, recombination removes the original edges defining u and v. The directions cannot be reconstructed from the output triangles alone.

Second, the continuous SO(2) action belongs to the geometric embedding or an additional representation. It does not follow from the two-dimensional zeroth homology space merely because that space has dimension two.

A viable geometric construction must therefore transport the required directional information through recombination.

## 7. Exterior algebra and the alternating amplitude

Represent the two output triangles as oriented vertex products:

T₁ = A ∧ C ∧ E

T₂ = B ∧ D ∧ F

Exchanging the two degree-three products changes the sign:

T₁ ∧ T₂ = −T₂ ∧ T₁

This is an intrinsic exterior-algebra identity.

Now consider two vectors u and v in an oriented Euclidean plane.

Every rotationally invariant real bilinear scalar has the form:

A(u,v) = a(u · v) + b det(u,v)

If the amplitude must be antisymmetric under exchanging u and v, the symmetric term disappears:

A(u,v) = b det(u,v)

For unit vectors:

A(u,v) = b sin θ

Its squared magnitude is proportional to:

sin² θ

This establishes a mathematical implication:

**Alternating bilinear composition in an oriented two-dimensional Euclidean space produces the sine-squared angular dependence.**

It does not establish that the physical interaction selects this composition.

The requirement that the measured amplitude inherit simplicial-join antisymmetry remains a hypothesis.

## 8. Joint-state construction

The link space provides two basis states, x and y.

The tensor product V ⊗ V permits an antisymmetric joint state:

Ψ₋ = (x ⊗ y − y ⊗ x) / √2

For orthonormal basis vectors, this state is normalized.

It produces the ideal joint probabilities:

| Outcomes | Probability |
|---|---|
| ++ | sin² θ / 2 |
| +− | cos² θ / 2 |
| −+ | cos² θ / 2 |
| −− | sin² θ / 2 |

The resulting correlation is:

E(θ) = −cos(2θ)

This angular form is compatible with polarization correlations reported for annihilation photons.

For ideal polarization measurements, the corresponding CHSH expression can reach 2√2.

Actual annihilation-photon measurements often use Compton scattering to infer polarization correlations. Detector analyzing powers and experimental conditions affect the observed contrast.

The angular agreement therefore does not uniquely identify the underlying simplicial construction.

## 9. Attempt to construct the joint state from link topology

Define:

w = x + y

d = x − y

Exchanging the two link components preserves w and reverses d.

Their alternating tensor composition gives:

Q₋ = (d ⊗ w − w ⊗ d) / (2√2)

Expanding:

Q₋ = (x ⊗ y − y ⊗ x) / √2

This constructs the desired antisymmetric state from the two link components.

But the same link also supports symmetric states, including:

Q₊ = (x ⊗ y + y ⊗ x) / √2

and:

Ψ₊ = (x ⊗ x + y ⊗ y) / √2

Both Ψ₋ and Ψ₊ are invariant as state vectors under simultaneous SO(2) rotations in a chosen Euclidean representation.

Thus the link structure permits the desired antisymmetric state but does not uniquely select it.

## 10. Exchange symmetry and orientation

Two exchanges must be distinguished.

**Tetrahedron exchange:** Interchanges the two components CD and EF of the link.

**Output exchange:** Interchanges the two triangles, implemented in the candidate construction by τ = (AB)(CD)(EF).

These are different transformations.

The alternating state changes sign under exchange of its tensor factors:

PΨ₋ = −Ψ₋

A symmetric state satisfies:

PΨ₊ = +Ψ₊

We investigated whether reversing the orientation of the original encounter could compensate for the alternating sign.

A candidate complete amplitude is:

Q = sQ₋

where s is an orientation sign that reverses under the relevant exchange.

Two sign reversals then produce an exchange-invariant complete expression.

However, symmetric composition can also satisfy exchange invariance.

Moreover, the link-component exchange and output exchange must be related by an explicitly defined transport operation before their signs can be combined.

Orientation and exchange symmetry therefore do not yet uniquely select Q₋.

## 11. Statistical test and correlation visibility

The alternating state predicts the ideal angular correlation:

E(θ) = −cos(2θ)

A broader symmetry-compatible family is:

Pλ(a,b | θ) = [1 − λab cos(2θ)] / 4

Here:

- a,b ∈ {−1,+1} are measured outcomes.
- θ is the relative measurement angle.
- λ controls correlation visibility.

Different values of λ preserve the same exchange and rotational symmetries.

Examples:

| λ | Correlation |
|---|---|
| 0 | None |
| 0.5 | Partial |
| 1 | Ideal alternating-state correlation |

Experiments report angular correlation modulation, including changes in contrast between measurement conditions and materials.

A proposed dilution model is:

Vmeasured = f a₁ a₂

where f is the correlated-event fraction and a₁,a₂ are detector analyzing powers.

This model can be tested with independently determined parameters.

It does not distinguish simplicial composition from other models producing the same joint state.

The simplex hypothesis must predict either the state-selection mechanism or an additional observable.

## 12. Current mathematical obstruction

We seek an operator:

Q: K → V ⊗ V

with image restricted to the alternating component:

Im(Q) ⊆ Λ²V

The current structure supplies:

1. The input edge-sharing simplicial complex.
2. Its two-component link.
3. A two-dimensional homology space.
4. An exterior-algebra exchange sign.
5. Four candidate output pairings.
6. A retained reconstruction correspondence.
7. A candidate continuous geometric representation.
8. An alternating joint-state construction.

It does not establish why Q must select Λ²V instead of the symmetric component.

One possible additional law is that composition must be odd under reversal of the oriented encounter.

That rule would select an orientation-odd channel if its action were defined consistently.

Its necessity has not been derived.

Furthermore, reversing the sign of an amplitude leaves its squared magnitude unchanged. A direct test of the proposed sign structure would require relative phase information or another observable sensitive to interference.

## 13. Findings

The investigation has established the following mathematical relationships.

**A. Link structure**

An edge-sharing pair of tetrahedra has a two-component link, yielding a two-dimensional zeroth homology space.

**B. Multiple admissible outputs**

The input admits four symmetry-related complementary two-triangle outputs. A universal operation can return a symmetry-equivariant family.

**C. Retained information**

Reversibility requires transporting correspondence information that the bare output complex does not retain.

**D. Alternating composition**

In a two-dimensional oriented Euclidean representation, antisymmetric bilinearity determines the determinant amplitude up to scale.

**E. Correlations**

A normalized antisymmetric tensor state produces the angular correlation −cos(2θ).

**F. Underdetermination**

The same incidence and exchange structures permit symmetric states and multiple correlation strengths.

No intrinsic selection rule has yet been derived.

## 14. Research position

The candidate universal composition law now has a more precise target.

It must map an enriched input complex into an enriched output complex while preserving the information necessary for inverse construction.

The operation must determine:

1. Which output complexes are admissible.
2. How orientation and incidence correspondences are transported.
3. Which joint-state component is selected.
4. How continuous measurement directions are represented.
5. Which correlation probabilities follow.
6. What measurable result distinguishes the construction from alternative models.

The next critical object is the composition operator itself:

Q: (K, orientation, incidence correspondence) → joint output state

It must determine the output state's exchange structure without imposing antisymmetry as an independent assumption.

Until such an operator is constructed, the sine-squared angular relationship is a successful algebraic reproduction of an observed pattern, rather than an independent prediction.

## 15. Continuation point

Derive an intrinsic composition operation that selects the alternating or symmetric component according to the input simplicial structure.

The immediate mathematical question is:

**Can the boundary, join, link, and orientation operators of a simplicial complex determine a canonical map into the tensor product of its output state spaces?**

The acceptance condition is that the selected joint state follows from the construction, without specifying its exchange parity or observed angular correlation in advance.
