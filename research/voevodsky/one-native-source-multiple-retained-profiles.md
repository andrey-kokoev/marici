# One native source, multiple retained observation profiles

Fresh resume selected `native-retained-fiber-family:v1`. The operator refined
its objective to the diagram connecting one full source, separate observations,
joint refinement, coarsening and recovery—not an isolated encoding exercise.

## Native representation without selecting every fiber

`agda/NativeRetainedProfiles.agda` uses the actual owner's `Core.Node`,
`E-node`, `paths-node`, `maps-node`, and `retain-node` constructors.
For a supplied source node with carrier A and reader r:A->V it constructs

    fiber(v) = sum(a:A) [r(a)=v],
    total = sum(v:V) fiber(v).

The family consists of UNPOINTED graphs. Paths are represented by actual path
nodes and the dependent sums by actual E nodes. The reader and source node are
retained as typed graph data. No state is chosen in each fiber.

This works even if the entire source A is empty. A checked empty-source example
has a graph but no possible marked value. When a source point a0 IS supplied,
only the total is marked, at (r(a0),a0,refl); its original source node and point
are explicitly retained too.

## The two-profile diagram

For the SAME source A and independently supplied r:A->V and s:A->W, the module
constructs native packages for r, s and the paired reader (r,s). It provides:

- source/representation equivalences and both recovery laws;
- native comparison packages between separate profiles and from joint to each;
- preservation of the recovered complete source value;
- recovery of the original joint reading coordinates via their path witnesses;
- a checked triangle: joint->first->second equals joint->second on total values.

These are equivalences of full retained SOURCE REPRESENTATIONS. They do not
assert V is equivalent to W, that r and s are the same physical reading, or that
arbitrarily selected fibers of different profiles are equivalent.

The profile-to-profile comparison package retains both profile nodes. Discarding
that certificate and retaining only its target is NOT a theorem of preservation
of the old policy history.

## Coarsening really retains the old profile

The separate native coarsening construction takes the ENTIRE old indexed total
as its new source, with reader q composed with the old index projection. Thus
its payload still includes the old index, source value and witness; its source
node retains the old reader and graph. Both total-data recovery laws hold.

A constant-coarsening control keeps the original `true` index available even
though the new observation is always `false`. This is regrouping, not a quotient
or replacement by a representative.

## Joint observations require a shared source witness

The joint fiber at (v,w) is proved isomorphic to

    sum(a:A) [r(a)=v] x [s(a)=w].

The SAME a must support both observations. It is not the unconstrained Cartesian
product of two independently inhabited marginal fibers.

The checked counterexample uses A=Bool and both readers equal to identity.
The first fiber over false and second fiber over true are individually inhabited,
but the joint fiber at (false,true) is empty. Thus the implementation rejects
manufacturing joint evidence by combining separately valid readings from
incompatible source states.

## Complete native histories, not scalar replacements

`NativeHistories` instantiates the same diagram on the owner's actual native
resolution closure for any supplied admission policy and chosen admitted
history. The universe is raised because the carrier includes complete native
packages and derivations. Recovery preserves the declaration and every premise
port, not merely a scalar output or an endpoint hash.

The history is carried as typed data, not serialized or truncated. This does
not yet give an operational rule that computes arbitrary physical readers, or
invent continuum evidence absent from the supplied source.

## Admission boundary

Building an unpointed family graph and a retained comparison certificate does
NOT produce a `Resolve` derivation under an unchanged source policy. In
particular, we do not use a family of complete marked packages when some fibers
are empty, and do not invent admission witnesses for them. Representation and
constructor-rule admission remain distinct obligations. No owner file changed.

## Verification and next structural question

    python research/voevodsky/check_native_radar_formal.py --native-profiles --fresh

Fresh safe/cubical closure passes. The upstream potential-only and false-sixth
negative controls reject as intended. New positive proofs cover the recovery
and triangle laws, shared-source joint witnesses, incompatible marginal readings,
empty fibers, empty sources, and impossibility of marking every fiber.
Receipt: `native-retained-profiles-formal.json`.

The next useful synthesis step is the universal shared-source gluing rule:
identify the joint retained profile with the homotopy pullback of the separate
representations along their source-recovery maps. Keep source-equality witnesses
and both profile graphs. This should distinguish coherent gluing from independent
product formation without deleting any admitted source or observation fiber.
