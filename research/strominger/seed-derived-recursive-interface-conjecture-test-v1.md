# Testing source-derived recursive witnessing on the actual six-arrow seed

## Conjecture under test

The operator requested testing the conjecture that native source structure
supplies a nontrivial witnessed interface whose complete retained package supports
recursive WG construction naturally under source-preserving relabelling, without
arbitrary symmetry choices.

This test separates three claims: existence of a source-natural comparison,
coherent lifting to retained records, and determination of a genuinely
structure-generating constructor. A graph-level comparison is not automatically
an admitted native WG operation.

## Source signature and recovered prior work

The checker imports PACKETS directly from
`research/nima/checkers/check_natural_tower_return.py`:

    AB, BC, CA, BA, AD, DB.

The declared signature is the directed incidence graph, with movable vertex and
edge names. The registry's serialization order and an ordered pair of triangle
roles are NOT treated as fixed intrinsic colours. This is exactly the symmetry
signature of the existing seed comparison work, not a completion to all twelve
possible directed arrows.

Prior results already establish the nonidentity graph automorphism, its action
on the two cyclic full-support tours, and its transport of spectral records:

- `research/nima/seed-typed-execution-and-spectral-windows.md`
- `research/nima/seed-spectral-port-symmetry-comparison.md`
- `research/nima/seed-section-comparison-boundary-audit.md`

The new work recovers this fact rather than claiming a new seed symmetry, and
connects it to recursive retention and constructor underdetermination. No native
formal closure was rerun or modified.

## First gate: a source-derived nonidentity comparison EXISTS

Exhausting all 24 vertex permutations gives

    Aut(G)={id,sigma},    sigma=(A B)(C D),    sigma^2=id.

For any relabelling h:G~=G', the unique nonidentity automorphism of G' is
h sigma h^-1. Uniqueness therefore proves naturality over the entire isomorphism
class of this source, not only commutation with its own two automorphisms. The
checker verifies all 24 relabellings and all 576 two-relabel composition pairs.

Unlike the unstructured four-point model, this source DOES distinguish a
nonidentity symmetry without a chosen preferred vertex. Selecting a symmetry
uses conjugation naturality; selecting a vertex or a tour is a different problem.

The induced edge comparison is

    AB <-> BA,    BC <-> AD,    CA <-> DB.

It transports entire valid words, their endpoints, order and incidence seams,
commutes with every cut/concatenation, and squares to identity. The checker
exhausts all valid structural words of lengths one through six: 6,10,16,26,42,68.
These are descriptions, not newly issued execution occurrences.

## Second gate: whole-record lifting works, but admits different policies

Let H=Aut(G). Consider two completely source-natural retention policies:

    Forced_n = P x {sigma}^n,
    All_n    = P x H^n.

At each level transport the source point by h and each retained automorphism by
conjugation. This lifts to a coherent action on the WHOLE record; the last-field
projection commutes with transport. Since H=C2, conjugation is trivial on this
fixed source, though transport between differently labelled copies remains
explicit.

Both policies retain a nonidentity sigma witness and allow its reversible action
on the complete package. Neither chooses a preferred source vertex. Nevertheless
their forget-last-field fibers are inequivalent:

| Policy | Projection fiber | States at depth n | Source-relabelling orbits |
| --- | --- | --- | --- |
| Require sigma in each new field | singleton | 4 | 2 |
| Retain every admitted symmetry as a possible new field | H, size 2 | 4*2^n | 2*2^n |

Depths zero through three are exhausted. The formulas and coherence laws follow
uniformly from the displayed products and group action.

Thus coherent recursive retention of the unique nonidentity interface need NOT
increase the represented type: Forced_n is equivalent to P. All_n has genuinely
additional record distinctions, but it uses the explicit policy 'retain all
symmetry choices as possible fields'. Merely requiring source naturality and
recovery does not select that policy over Forced_n.

This is not a refutation of the existential conjecture. It is a finite
constructive specialization of its comparison and retention parts, and a
counterexample to the stronger inference that those laws uniquely force a
generative constructor.

## Which extra content is actually generated?

For All_n, compose the retained symmetries. At positive depth the observation

    (p,a_1,...,a_n) -> (p, a_n ... a_1)

has eight possible values and fibers of size 2^(n-1). Retained records grow, while
the possible composite source actions remain just identity and sigma. At depth
two, for example, (id,id) and (sigma,sigma) have the same composite but different
complete records.

Consequently this example generates structured witness histories/configurations,
not an ever larger group of endpoint transformations. Whether histories are
retained or identified by their composite is part of the declared boundary
policy. Recursion depth and word position carry no physical-time interpretation.

## Admission and selection hostiles

1. **Comparison is not a primitive transition.** Sigma maps C to D and D to C,
   but CD and DC are not seed arrows. Sigma is an incidence-preserving
   re-description of the whole graph, not a uniformly available primitive edge
   operation at every vertex. A native WG admission rule must say which role is
   intended; the graph calculation cannot silently supply it.

2. **Endpoint return is not erasure of retained structure.** The word AB BA
   returns to A, but is a two-arrow record, not the empty identity word. An
   inverse on vertices is not automatically an inverse on complete histories.

3. **Signature matters.** If the two triangle roles are fixed individually, the
   nonidentity symmetry is excluded and the fixed-source automorphism group is
   trivial. Transport of ordered-role packages to differently labelled targets
   remains possible, but is not a nonidentity automorphism preserving those roles
   at the original fixed source. Which signature the full native WG retains is
   therefore an open admission question.

4. **Unique symmetry does not select a tour.** The two existing directed Euler
   tours are exchanged by sigma. Neither is an invariant unmarked choice. This
   obstructs a deterministic unmarked tour selector but not selection of sigma
   itself: the two outputs obey different transformation laws.

5. **An actual routing is a different constructor.** Exhausting bijective
   endpoint-successor maps gives the existing unique cycle cover
   AD,DB,BC,CA. Its routing r=(A D B C) satisfies r^2=sigma, but r is NOT a graph
   automorphism. Its inverse is not a primitive one-step routing in this source.
   It answers a conditional cycle-cover question, not the comparison question.
   No physical execution or schedule is inferred from either map.

## Sharpened synthesis: the missing object is the admissible-extension family

The common schema is

    next(C) = Sigma(z:C) W(z),
    projection(z,w)=z.

Here W(z) must be the source-admitted family of complete extension witnesses,
with its transport rule and proof obligations. Once that family is supplied,
dependent retention is canonical. Its fibers locate the distinction between
presentation and generation:

- contractible inhabited fibers: equivalent retained re-presentation;
- noncontractible fibers: additional distinctions in the total package;
- empty fibers: a blocked extension at that boundary.

In the two finite policies above W is respectively {sigma} or H. Source
incidence, naturality and round-trip laws alone do not determine which W the
native WG admits or requires. Merely invoking dependent sums does not derive W.

The most productive next structural step is therefore to extract W(z) from the
ACTUAL native constructor/admission signature, including its retained roles,
then prove that its total-package construction respects source transport and
has the claimed fibers. That would connect source derivation, structural
generation and generic WG coherence without replacing the admission policy by
an arbitrary symmetry-family toy.

## Verification and scope

    python research/strominger/checkers/check_seed_derived_recursive_interface.py

Fresh execution exits 0. Receipt:
`results/seed-derived-recursive-interface.json`, including source hashes,
all finite counts, recursive policy comparisons and hostiles.

This is a finite structural test with explicit algebraic uniform laws, not a
formal-kernel WG proof, universal higher-filler theorem, physical process law,
source-free creation theorem, or proof of a uniquely determined constructor.
Only Strominger-owned checker/report/receipt files were written.
