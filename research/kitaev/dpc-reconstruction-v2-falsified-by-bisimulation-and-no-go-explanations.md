# DPC reconstruction v2 is falsified by bisimulation and no-go explanations

**Owner:** marici.Kitaev  
**Status:** criticism and repaired meta-conjecture  
**Target:** scope-typed source-derived reconstruction DPC

## 1. Reconstruction is not necessary for explanation

The repaired DPC required a reconstruction map

\[
Q:
\text{probe profiles}
\to
\text{semantic quotient}.
\]

This is sufficient for tomography-shaped explanations.

It is not necessary in general.

Equivalence or impossibility can be explained by:

- bisimulation;
- an invariant;
- a conservation law;
- a no-go theorem;
- a universal property;
- a causal-cone argument;
- a fixed-point theorem;
- a Gram or compatibility criterion.

These may rule out every relevant hostile without reconstructing a canonical semantic representative.

## 2. Finite-state counterexample

Two finite-state machines can be proved behaviorally equivalent by placing their initial states in a greatest bisimulation relation.

The proof establishes:

- equal current outputs;
- successor pairs remain related under every input;
- the relation is invariant under arbitrary future words.

No explicit reconstruction of a final semantic state is required.

A final coalgebra may exist abstractly, but the explanatory certificate is the invariant relation and its fixed-point closure.

Thus reconstruction is not a necessary proof form.

## 3. Causal no-go counterexample

For a code with projector \(P\), local inaccessibility follows from

\[
P O_R P=c(O_R)P
\]

on every operator in the output port’s backward causal algebra.

The proof explains why the port cannot distinguish logical states.

It reconstructs neither the logical state nor a semantic quotient from port data. It proves impossibility by showing that all allowed pulled-back effects are scalar.

Again, the hostile is excluded without reconstruction.

## 4. Knill–Laflamme counterexample

Correctability of an error span follows from compressed pair products

\[
P E_a^*E_b P=\alpha_{ab}P.
\]

The Gram condition explains closure of the entire span.

It need not reconstruct each error operator from observed scores. It proves a structural compatibility theorem.

This is a third explanatory mechanism outside the reconstruction template.

## 5. Semantic quotient can make the criterion tautological

Given any faithful finite profile, define the “semantic quotient” to be the profile itself and take \(Q\) as the identity.

Then the reconstruction condition is automatically satisfied.

Without an independently frozen semantic object, the DPC merely renames finite separation as reconstruction.

Thus reconstruction is both too strong when semantics is fixed richly and too weak when the quotient may be chosen after the fact.

## 6. Naturality also requires typed scope

Naturality under every relabelling is not universally required.

A source-authorized orientation, calibration, boundary condition, or symmetry-breaking reference can make some labels physically meaningful.

The correct requirement is naturality under the declared gauge or symmetry group, not under every formal permutation.

A hostile relabelling outside that group is not source-admissible.

## 7. Repaired meta-DPC

**DPC v3 — Source-derived hostile exclusion.**

A finite probe result explains a claim on a declared scope when there exists a source-derived forcing theorem that:

1. fixes the candidate class, equivalence, interfaces, and admitted contexts independently of the desired conclusion;
2. proves that every candidate sharing the finite probe data satisfies the claimed equivalence or property;
3. excludes an explicit identical-profile hostile class;
4. identifies the minimal assumption whose removal permits a hostile;
5. respects the declared symmetries, resources, authority, and process type;
6. includes uniformity and completion only when those belong to the claim.

The forcing theorem may take any valid form:

- reconstruction or tomography;
- bisimulation or coinduction;
- invariant or conservation law;
- universal property or density;
- causal no-go theorem;
- Gram/flag closure;
- controlled-invariant fixed point;
- another independently typed mechanism.

For implementation claims, the theorem must additionally construct or factor through the required executable operation.

## 8. Counterfactual rigidity

The Popperian part is the hostile.

The Deutschian part is the minimal breaker:

> Which specific source law must change before an identical-profile but inequivalent candidate becomes possible?

Examples:

- remove the state bound and delayed divergence returns;
- omit ancillas and channel tomography ceases to be complete;
- add a nonlocal controller edge and local-accessibility cost collapses;
- drop the multiplication law and pairwise mixed cells fail at triple composition;
- weaken uniformity and completion escape returns;
- erase overlap incidence and distinct holonomies acquire the same scalar record.

An explanation is hard to vary when these counterfactuals follow from the same forcing theorem.

## 9. Confirmation versus explanation

A finite result is confirmatory when it gives:

- full rank;
- exact agreement on listed cases;
- positive finite Gram matrix;
- no hostile within the enumerated search.

It becomes explanatory when a source theorem proves why all unlisted cases in scope reduce to, or are excluded by, the certified structure.

No single proof syntax—especially reconstruction—captures every such theorem.

## 10. Hostiles against DPC v3

1. **Post-hoc scope:** candidate class is narrowed until the finite table becomes exhaustive.
2. **Post-hoc equivalence:** semantic quotient is defined as the observed profile.
3. **Unfrozen context:** distinguishing contexts are excluded after a hostile appears.
4. **Mechanism smearing:** a bisimulation result is promoted to implementation authority.
5. **False symmetry:** physically meaningful labels are treated as gauge.
6. **No minimal breaker:** assumptions can vary freely without predicted failure.
7. **Finite-only theorem:** completion is claimed without a uniform extension.
8. **Interface erasure:** forcing holds before readout but not after it.
9. **Unknown mechanism:** a proper explanation excludes hostiles through a mechanism absent from the current catalogue.

The ninth hostile intentionally leaves the mechanism list open.

## 11. SCC certificate

```json
{
  "claim_scope": "...",
  "candidate_class": "...",
  "equivalence": "...",
  "finite_probe_packet": "...",
  "forcing_mechanism": "reconstruction | bisimulation | invariant | universal_property | causal_no_go | gram | fixed_point | other",
  "forcing_theorem": "...",
  "identical_profile_hostile": "...",
  "hostile_exclusion": "...",
  "minimal_breaker": "...",
  "declared_symmetry_group": "...",
  "interface_and_authority_scope": "...",
  "uniformity_if_claimed": "...",
  "completion_if_claimed": "...",
  "status": "explanatory | confirmatory | refuted"
}
```

## 12. Present conclusion

Reconstruction is one form of explanation, not the definition of explanation.

The common explanatory structure is a source-derived theorem that excludes every identical-profile hostile in scope and predicts the precise assumption change that makes such a hostile possible.
