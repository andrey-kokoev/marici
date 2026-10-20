# Anchored boundary presentations: coherence without collapse of the represented structure

## Question and operator direction

The operator's dot/interface intuition treats domain and codomain as relative
roles in a witnessed return, then treats the whole gate and its certificate as
a possible object of another configuration. The requested continuation is to
make that account structural without importing physical time or an unexplained
ambient lattice.

The key distinction is between a space of PRESENTATIONS and the structure
PRESENTED. A contractible space of anchored presentations need not make its
represented content contractible. This packet states that distinction precisely,
recovers existing implementations, and supplies a finite groupoid/lattice test.

## Recovered constructions, not newly invented universal mechanisms

`research/voevodsky/a-common-graph-presentation-generates-all-opposite-edges-at-fixed-realization-dimension.md`
already constructs a retained common graph M and complete chart maps

    e_i:M -> V_i,     e_i(x)=(x,q_i(x)).

The full source anchor is retained. Therefore E_ij=e_j e_i^-1 supplies actual
reverse chart maps and coherent triangles by cancellation. Unanchored shadows
q_i can remain noninjective. The analytic note separately retains topology,
closability and missing source-edge qualifications; its graph trick does not
supply those premises or physical inversion of a lossy observation.

`research/voevodsky/observer-relative-computation/anchored-dependent-records.md`
already gives a dependent-record equivalence with the underlying Boolean content.
Changing a comparison while holding its endpoint Boolean fixed can change the
anchored value. Forgetting comparison data is not generally harmless.

`research/voevodsky/closure-four-presentations-hott-proof.md` already treats both
input and output presentations of an independently constructed, possibly
noninvertible operation. Its compatible map-and-square fiber is contractible,
including a higher comparison of the square witnesses themselves. It does not
infer invertibility of the operation from equivalence of its presentations.

These are better starting points than an additional unsupported generic
certificate tower. Their formal checks were read through the reports, not rerun.

## Two spaces, with a precise general statement

In an adopted univalent universe containing a fixed P, define

    Pres(P) = Sigma(X:U) Equiv(P,X),
    Content(P) = Sigma((X,e):Pres(P)) X.

Univalence identifies Pres(P) with the total based path space
Sigma(X:U)(P=X), which is contractible. This is a standard conditional theorem,
not a new assertion of literal equality between serialized type descriptions.

However,

    Content(P) ~= P,
    normalize(X,e,x)=e^-1(x).

The inverse embeds p as (P,id,p). Their homotopy inverse laws follow from the
based path/transport construction. Thus the represented content retains exactly
P's homotopy type even though the anchored presentation space is contractible.
This generalizes the previously checked anchored Boolean record example; the
finite checker below is not a proof of univalence.

For fixed anchors e:P~=X and f:P~=Y, the compatible comparison type is

    Sigma(h:X~=Y) (h composed with e = f).

It is the fiber of an equivalence (precomposition by e), hence contractible.
The complete pair includes its anchor-compatibility witness. Omitting that
witness, or fixing incompatible higher boundaries independently, changes the
problem and does not inherit this contractibility statement.

The canonical comparison is f e^-1. Compatible composites have canonical
comparison witnesses through the same anchor. Existing all-finite-dimensional
relative coherence results apply to these contractible fibers. They do not
contract P, an unanchored automorphism space, or arbitrary filling problems.

## Where a boundary lattice belongs

Supply source fields q_i:P->Y_i and a selected collection of field subsets A.
For each A retain the complete graph presentation

    Graph_A(P) = {(p,(q_i(p))_(i in A)) : p in P}.

Each graph is equivalent to P. If the permitted subsets are closed under union
and intersection, they form a lattice of boundary selections. This lattice is
derived from that supplied field family, not from the WG type alone.

The shadow p -> (q_i(p))_(i in A) can have noncontractible fibers. Retention of p
is what makes complete graph changes reversible. The complete graph and its
shadow are not interchangeable representations with the same recovery rights.

No physical time is assigned to subset inclusion, map composition, recursion
depth, or a selected orientation. A domain/codomain distinction can index which
complete presentation is an input and which an output; both coexist in the same
configuration diagram.

## Noninvertible operations retain independent meaning

Given an actual operation F:P->Q and anchors e:P~=X, f:Q~=Y, its presentation is

    F_(e,f)=f composed with F composed with e^-1.

Changing input or output charts is reversible, but F need not be. Therefore the
common-anchor mechanism supports coherent descriptions of irreversible-looking
shadows without claiming that every source operation itself has an inverse.
Making F reversible by retaining its entire input changes the output package;
that record must remain explicit.

This is essential to the domain/codomain intuition: a witnessed chart return
cannot silently serve as a recovery witness for an independently lossy process.

## Exact finite test

`checkers/check_anchored_boundary_presentation_synthesis.py` uses the declared
source P={0,1}^2. Three labelled copies, each with all 24 bijective anchors, give
72 anchored presentations. Its groupoid arrows are anchor-preserving bijections.

Fresh exact checks establish:

- all 5184 ordered presentation pairs have exactly one anchor-preserving arrow;
- all 373248 triangles compose coherently;
- the presentation groupoid is connected with trivial automorphism groups;
- the total presented-content groupoid has FOUR components, each with 72
  presentations, preserving the four source values;
- forgetting anchors permits 24 automorphisms per copy, not one;
- the same displayed value 0 under identity versus swapped anchor normalizes
  to different source values, explicitly blocking anchor-free decoding.

The two coordinate fields give the Boolean four-cut lattice. Every complete
graph contains four retained source records. Its shadow fibers have respectively
sizes 4, 2, 2 and 1. The full graph diamonds commute, but an incomplete shadow
alone cannot recover its source.

Finally, all 576 input/output anchor pairs present a fixed rank-two noninjective
process on the four-state source. Every presentation remains rank two. Retaining
(input,output) instead gives four distinguishable records and explicit recovery.
A full interface record can be placed as the payload of another record and
recovered exactly; this last control is retention, not discovery of new proofs.

Groupoid contractibility here is not literal equality of its 72 objects. The
checker establishes the finite categorical facts; the general homotopy claims
use the stated mathematical framework. No arbitrary higher filling is inferred
from finite triangle enumeration.

## Structural synthesis and remaining boundary

A precise candidate for the operator's meta-coherence picture is a system of
complete anchored boundary presentations, with source-indexed content, canonical
compatible comparisons, and explicitly supplied recursive reification. Its
presentation fibers can be coherently trivial while its content and unanchored
symmetry structure remain nontrivial.

This improves the earlier proposed ambient diagram lattice: the lattice is now
specified by actual source fields and selections, while coherence is supplied
by retained anchors and compatibility fibers. It does not produce the source P,
choose the fields, or construct genuinely new non-equivalent structure from
nothing. Such a change remains an additional operation with its own boundary.

Recursively naming the presentation of a presentation therefore does not by
itself imply increasing geometric dimension. Complete package reification is a
distinct constructor, with universe levels retained as in the existing
whole-package WG implementation.

## Verification

    python research/strominger/checkers/check_anchored_boundary_presentation_synthesis.py

Fresh execution exits 0. Receipt:
`results/anchored-boundary-presentation-synthesis.json`, with the lattice, fiber
counts, hostiles and source-note/checker hashes. Source-owner files were read only.
No Agda rerun, universal WG synthesis theorem, physical claim, graph publication,
commit or push.
