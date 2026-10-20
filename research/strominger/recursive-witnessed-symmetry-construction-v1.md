# Witnessed symmetries construct new configuration types and operations on retained packages

## Question and source discipline

The operator asked whether the common-anchor account can explain genuinely new
structure rather than only equivalent presentations, and requested a construction.
This packet supplies one explicit finite constructor and tests its naturality,
retention, recursive symmetry action, and selection boundary.

The source is the same supplied four-element set P used in the preceding
anchored-presentation model. Its automorphisms are computed as all 24 bijections,
including their exact inverses and composition. No physical identity, energy,
time, spatial dimension, or preferred nonidentity symmetry is inferred.

## A constructor that is not a re-presentation

Define

    C_0=P,
    C_n=P x Aut(P)^n.

A complete state is (p,a_1,...,a_n), retaining the source value and every symmetry
record. Each symmetry is a witnessed reversible map, not an uninterpreted label.
The projection C_(n+1)->C_n forgets only the last symmetry coordinate. Its fibers
have 24 elements; they are not contractible in this discrete model. Therefore
C_(n+1) is not just an equivalent presentation of C_n.

The identity section appends the identity symmetry and recovers the old package
under projection. That is a section, not a two-sided equivalence. Constructing
the whole carrier of possibilities is different from selecting a particular
inhabitant: the identity section does not produce every possible symmetry record.

Under source relabelling h, transport the ENTIRE package by

    Phi_n(h)(p,a_1,...,a_n)
      =(h(p), h a_1 h^-1, ..., h a_n h^-1).

Conjugating the symmetry records is essential. Changing p alone would not retain
the meaning of its witnessed gates. Exact group identities imply uniformly in
finite n:

    Phi_n(hk)=Phi_n(h) Phi_n(k),
    Phi_n(h^-1) Phi_n(h)=id,
    projection Phi_(n+1)(h)=Phi_n(h) projection.

The identity sections are equivariant as well. These are algebraic relations,
not trajectories in physical time.

This construction uses the inherited source symmetry group at every depth. It
does NOT silently replace Aut(P) by all permutations of the flattened C_n set.
There may be other admissible structured symmetries, but none is assumed merely
from the larger cardinality.

## New configuration structure survives relabelling

The finite checker exhausts depths 0,1,2:

| Recursion depth | Retained states | Source-relabelling orbits |
| --- | --- | --- |
| 0 | 4 | 1 |
| 1 | 96 | 7 |
| 2 | 2304 | 107 |

These are counts of states and orbits, not spatial dimensions. The increase in
orbit count shows that the additional configurations are not all mere renamings
of the same old package.

At depth one an orbit is classified by the cycle length containing the marked
point p and the partition of the other cycle lengths of a_1. The seven orbit
sizes are 4,8,12,12,12,24,24. Stabilizers are retained in the receipt: an ordinary
orbit set would discard their symmetry information. The corresponding action
groupoid is a richer object than its set of seven components.

Independent Burnside enumeration agrees with direct orbit enumeration. The
uniform finite-depth count for this supplied four-point source is

    |C_n|=4*24^n,
    orbit_count(C_n)=(4*24^n+12*4^n+8*3^n)/24.

The identity permutation fixes four points and centralizes 24 symmetries; the
six transpositions each fix two points and centralize four; the eight 3-cycles
each fix one point and centralize three. Other conjugacy types fix no source
point. These facts prove the formula for all finite n; the three enumerated
levels are independent regression controls, not its sole justification.

## A retained witness supplies a natural nonidentity operation

There is a constructive distinction between selecting a first symmetry and
using an actual retained one. For n>=1, define

    T_n(z)=Phi_n(a_n)(z).

The last stored symmetry a_n is unchanged by conjugating it by itself. Therefore

    T_n^-1(z)=Phi_n(a_n^-1)(z)

is a two-sided inverse. The operation is equivariant under source relabelling,
because the selected symmetry is itself transported by conjugation.

The checker verifies both inverse laws and equivariance on every retained state
at depths one and two. T_1 changes 72 of 96 literal states; T_2 changes 2136 of
2304. These are nonidentity operations on complete packages, not merely wrappers
around an unchanged endpoint.

They remain within each source-relabelling orbit: they do not by themselves
construct a new orbit or supply a previously absent symmetry record. The new
configuration types come from the explicit C_(n+1) constructor; T_n demonstrates
how an existing witness can serve as executable structure at another level.

## Selection and flattening hostiles

### No source-free nonidentity selection in this model

An equivariant choice s:P->Aut(P) must satisfy

    s(hp)=h s(p) h^-1.

At p=0, s(0) must centralize every source permutation fixing 0. Exhaustive checks
show that this centralizer is the identity alone. Hence the only such choice on
the unstructured four-point source is the identity section.

A chosen transposition is a valid nonidentity symmetry, but relabellings fixing
p can change it. Selecting it requires additional marking or a supplied witness;
it is not forced by the bare source. Once it is retained in C_1, the natural
T_1 operation above can use it. This localizes the first selection obligation
rather than laundering it through recursive certification.

### Flattening loses the structured symmetry contract

A permutation swapping only (0,id) with (1,id) in the 96-state flattened set is
a bijection, but it does not preserve the source projection: another state over
0 stays over 0. No single base map makes that permutation commute with projection.
It is therefore not an inherited source-structured symmetry.

Treating all 96! flattened permutations as legitimate next-level source
symmetries would change the constructor's contract. Conversely, merely counting
24 inherited lifts is not a classification of every possible structured
automorphism; only this declared family is used.

## Relation to WG and the common-anchor result

The preceding presentation construction had contractible anchor-compatible
comparison fibers while preserving the represented content. This constructor
has noncontractible projection fibers and new source-relabelling classes. The
two mechanisms are explicitly different and can coexist.

A finite family constructor can enumerate the admissible symmetry packages from
this source; it need not choose one nonidentity symmetry to construct the family.
A state-level WG must separately specify its selected successor. For n>=1, T_n
is a concrete nonidentity candidate using the supplied retained witness, with
inverse and equivariance evidence. None of this proves arbitrary proof search,
source creation from an empty type, or a unique physical assembly rule.

The implementation is a finite executable model, not a new generic Agda WG term.
The existing whole-package and indexed-refinement machinery are the integration
points; their formal closures were not rerun here.

## Verification

    python research/strominger/checkers/check_recursive_witnessed_symmetry_packages.py

Fresh execution exits 0. It exhausts the stated finite carriers, inverse and
naturality laws, the first-level group action law, independent orbit counts,
selection obstruction and flattened-permutation hostile. Receipt:
`results/recursive-witnessed-symmetry-packages.json`.

No cross-owner mutation, physical claim, formal-kernel verification, graph
publication, commit or push.
