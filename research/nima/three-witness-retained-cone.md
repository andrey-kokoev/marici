# Three retained witnesses lift to a 1–4–6–4–1 presentation cone

## Question

Operator stimulus: compare the three charge–mass–recoil witnesses pairwise and test whether retaining their whole comparison produces the 1,4,6,4,1 backbone. This is a non-evidential construction proposal, not an asserted physical result. The applicable SCC obligations are attachment transport and route/coherencer compatibility.

Conjecture: three lossless witness-focused presentations, together with their common retained packet, admit a filled tetrahedral comparison structure. Rival: equal readouts, invertible pairwise maps and the correct cell counts alone suffice, without packet-preserving attachments.

## Claim boundary and construction

Let P be the complete input packet. It retains the original three witnesses, their context and a supplied original triangle face. Choose three focus maps selecting the respective witnesses; their types may differ.

For a focus f:P->A define

    View_f = Sigma(p:P) Sigma(a:A) (a=f(p)).

The map p -> (p,f(p),refl) and projection back to p are inverse up to specified paths. A focused view therefore retains the entire packet, not only the selected witness or its scalar readout. All three views are equivalent to P.

Use four pointed types as vertices:

    0: (P,p)
    1: (View_first, decorate_first(p))
    2: (View_second, decorate_second(p))
    3: (View_third, decorate_third(p)).

The common packet is the apex. Univalence supplies paths from it to the three lossless views. Pairwise comparisons are transported through this common reference, resolving the otherwise heterogeneous witness types.

The safe Cubical construction chooses a chain of pointed paths a:0->1, b:1->2, c:2->3. Its six edges are a, b, a.b, c, b.c and (a.b).c. Two faces are reflexivity witnesses and a third is path associativity. The existing `RetainedTetrahedralPackage` WG horn constructor supplies the remaining face and the tetrahedral interior, retaining all supplied edges and faces.

This is the path-coherence specialization of WG, not a claim about arbitrary noninvertible witness relations. Nor does it fill an arbitrary independently specified four-face boundary: one face is generated together with its filler.

The combinatorial carrier consists of the subsets of four labelled vertices. Its augmented counts are:

| Size | Meaning | Count |
|---|---|---:|
| 0 | empty face | 1 |
| 1 | pointed presentations | 4 |
| 2 | comparison edges | 6 |
| 3 | comparison faces | 4 |
| 4 | tetrahedral cell | 1 |

The first 1 is not a fifth physical object. These are labelled simplex counts, not independent observables, degrees of freedom, or a measured spatial dimension. The simplex is a cone; this does not produce nontrivial topology by itself.

### Two coherence levels must not be conflated

The input triangle relates the three momentum descriptions A, B and C. Its witnesses are part of P. The NEW triangle on vertices 1,2,3 compares presentations focused on those witnesses, each still carrying P. Its face is not the old face relabelled. The old face is retained inside the packet and recovered exactly from any view.

`PathWitnessTriangle` in the formal module specializes P to actual paths ab, bc, ac and a proof ab.bc=ac. The construction requires that old proof as input; it does not conjure one from the presence of three fields.

## Tests and disposition

`agda/ThreeWitnessRetainedCone.agda` freshly checks under safe Cubical Agda. It proves the view equivalences, six typed paths, completed surface/interior, recovery of the input horn and recovery of the supplied original face. Its pointed-type construction raises the universe level, not a physical dimension. The existing unrelated import warning in `TypedGeneratorLayers` remains.

The exact Python fixture uses the previous charge–mass–recoil preparation. It retains three executable comparison records for A=m1*delta_v1, B=-m2*delta_v2 and C=q1*q2*G, including both route descriptions and the original face routes. It checks six inverse transports, four commuting faces, 24 full vertex-order routes and the augmented boundary-of-boundary identity. This is a concrete data-level fixture, not an end-to-end Agda formalization of physical charge and inertia.

Two hostiles prevent overclaiming:

1. Change only the comparison history by adding an identity operation. All numerical momenta agree and one selected witness is unchanged, but the whole packets differ. Every full focused view distinguishes them; a selected witness alone cannot recover the missing history.
2. Twist one apex adapter by swapping those two packets. All edge maps remain invertible and numerical readouts stay fixed; the base triangle 123 still commutes. Faces 012 and 013 fail. Thus counts and scalar agreement do not certify a retained cone. The failure is already in packet-preserving transport, not an unexplained numerical error.

A further invalid-input control shows that lossless views of a false original comparison can still commute as data transports. The original comparison validator rejects it. Structural packaging therefore cannot certify the claims being packaged; the formal path-triangle specialization enforces the missing input proof by its type.

**Disposition:** the proposed backbone is constructible, with genuine higher-coherence witnesses, after adjoining the retained whole and specifying the lossless view adapters. It is not forced by pairwise comparison alone. The apex policy and original triangle validity remain explicit premises. No new excitation, physical clock, charge normalization, mass or particle dynamics is derived.

Verification:

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ThreeWitnessRetainedCone -Fresh`
- `python research/nima/checkers/check_three_witness_retained_cone.py`
- Formal receipt: `results/agda-ThreeWitnessRetainedCone.json`.
- Exact controls: `results/three-witness-retained-cone.json`.
- Owner-local SCC model: `scc-models/three-witness-retained-cone.json`.

The new model is downstream of the conditional impulse triangle. It does not change the previously recorded obstruction to producing a numerical contrast from the unperturbed WG baseline. No existing source law was modified. Operator stimulus and a bounded report to marici.Voevodsky were graph-admitted under proposal `ep_54810d04-efb3-4d51-bb55-48e5124532ed`; that policy admission is not scientific certification. The work remains uncommitted.
