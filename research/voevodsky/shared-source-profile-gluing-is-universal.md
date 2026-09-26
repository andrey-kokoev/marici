# Shared-source profile gluing is universal

Fresh resume selected `native-shared-source-profile-gluing:v1`.

## Binary structural law

Let X and Y be the complete retained representations of one supplied source A
under two observation profiles. Let rho_X:X->A and rho_Y:Y->A be their checked
source-recovery maps. Define

    P = sum(x:X) sum(y:Y) [rho_Y(y)=rho_X(x)].

`agda/NativeProfilePullback.agda` proves that the joint retained profile is
equivalent to P. This is a homotopy pullback: the source-identification witness
is part of the data, not a Boolean test or a truncated existence claim.

The comparison preserves the recovered source. Both joint-profile recovery and
recovery of the entire gluing datum (x,y,p) are proved. Recovery is by typed paths,
not literal serialized-byte equality; no set assumption on A is made.

## Universal property, not just a chosen encoding

For every test type T at the declared universe level, define

    Cone(T) = sum(f:T->X) sum(g:T->Y)
                [(t:T) -> rho_Y(g(t))=rho_X(f(t))].

The module proves isomorphisms

    (T->P)  ~  Cone(T),
    (T->joint-profile)  ~  Cone(T).

Both inverse laws are checked. It additionally proves that the space of
factorizations of each supplied cone is contractible. Thus a compatible pair
of maps, INCLUDING its chosen source-compatibility witness, factors uniquely
in the homotopy-theoretic sense. Matching observed values alone is insufficient.

This is the mapping-space universal property for unpointed retained families.
The concrete native packages also have a checked marked comparison at the
supplied source point. We do not claim a separate fully developed pointed or
higher categorical coherence theory in this turn.

## Why the proof retains information

Each profile's source-recovery map is an equivalence, so its fiber over a
specified source is contractible. This supplies the contraction needed to
recover the other profile and the gluing witness together. It is NOT a proof
that source identity types themselves are propositions, nor permission to
discard a witness from an arbitrary unrelated comparison.

The actual native pullback graph uses E nodes for the two profiles and a path
node for their source equality. It retains both original profile graphs and
both recovery functions. A native comparison package connects it to the joint
profile, preserving the original source and policy data.

No Resolve derivation, new seed admission, or chosen inhabitant in every fiber
is manufactured by constructing this graph.

## Rejection control

A Boolean source is read by two explicitly coarse constant-false observers.
One retained profile value contains source false and the other contains source
true. Their observed values agree, but source-identification glue is impossible.

This is stronger than merely showing unequal readings cannot be combined:
EVEN EQUAL readings do not authorize joining different retained source states.
Both states remain in the source and its fibers; rejecting their identification
does not delete either one.

## Verification and next step

    python research/voevodsky/check_native_radar_formal.py --profile-pullback --fresh

Fresh safe/cubical closure passes, including the new universal mapping-space
isomorphisms, contractible factorization theorem and equal-readings/no-glue
counterexample. The upstream potential-only and false-sixth controls reject
as intended. Receipt: `native-profile-pullback-formal.json`.

No owner files changed. Physical readers, admission and continuum interpretation
remain supplied separately.

The next bounded test is THREE-profile associativity: compare the two binary
gluing orders, explicitly transport their source-path witnesses, and show that
the projections and source recovery agree. Binary universality is now checked;
that next coherence result must not be claimed merely from an informal change
of parentheses.
