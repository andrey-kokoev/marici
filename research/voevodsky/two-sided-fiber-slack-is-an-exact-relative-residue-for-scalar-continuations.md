# Two-sided fiber slack is an exact relative residue for scalar continuations

## A smaller structural package

The previous coherence control retained the complete fine archive. In the bounded scalar-fiber class, the semantic information needed for arbitrary threshold continuations has a cleaner description.

Fix the source chart and a public point y. Let the original fine fiber be the nonempty interval [l(y),u(y)]. Relative to a reference function s(y), define

    J_s(E)(y)=(alpha,beta)=(s(y)-l(y), u(y)-s(y)).

Then

    [l,u]=[s-alpha,s+beta].

This pair is an EXACT relative fiber residue: it records the extent of the fine possibilities that selecting s alone discards. This terminology describes slack relative to a selected presentation, not a differential jet or an established analytic residue map.

The pointwise representation is injective once the reference s, public support and source chart are fixed. For the owning fixed-t1 m=4 family it reconstructs the fine source relation because h determines the actual source vector. In a higher-dimensional source with unrecorded hidden directions, scalar slack would not suffice.

## Minimality relative to a declared continuation language

Permit arbitrary rational upper and lower threshold refinements and exact pointwise admission queries. For a nonempty interval:

- appending h<=q leaves a witness iff l<=q;
- appending h>=q leaves a witness iff u>=q.

Two distinct intervals have distinct lower or upper endpoints. A rational threshold strictly between unequal endpoints distinguishes their future admission answers. Thus an exact interface for this language must distinguish every distinct interval. Conversely, the endpoints decide every finite conjunction of such thresholds.

So the interval—or equivalently its two relative slacks—is a complete minimal SEMANTIC descriptor, up to injective re-encoding, for this continuation contract. This does not prove that two particular machine registers or a given number of bits is minimal; nor does it make a parameterized envelope cheap to encode. Public support and the empty-fiber flag must also be retained.

## Refinement transport

Append L(y)<=h<=U(y). At the SAME reference s,

    alpha' = min(alpha, s-L),
    beta'  = min(beta, U-s).

The new fiber is nonempty iff alpha'+beta'>=0. The old reference remains an admitted section iff BOTH alpha'>=0 and beta'>=0.

These are different tests. Starting from [0,1] with selected h=1 and appending h<=1/2 produces slacks (1,-1/2). The selector fails, but the fiber is [0,1/2], not empty.

An empty fiber is represented explicitly and remains empty under further intersections. An update is never allowed to resurrect it by forgetting the earlier contradictory row.

## Recentring is a change of presentation

For another reference t=s+d, the same interval has residue

    (alpha_t,beta_t)=(alpha+d,beta-d).

This change of base is invertible and preserves the decoded fiber. For a nonempty refined fiber its midpoint gives the canonical centered presentation

    t=s+(beta-alpha)/2,
    alpha_t=beta_t=(alpha+beta)/2.

A reference need not itself lie in the fiber; signed slack remains a valid encoding. Therefore an algebraic change of reference is NOT automatically an admitted homotopy of witnesses. Straight-line witness homotopy is justified only when both endpoints lie in the same admitted convex fiber.

## The checked comparison cell

The basic square is

    fine interval E_y  -- intersect [L,U] -->  refined interval
          | J_s                                  | J_s
          v                                      v
       (alpha,beta) -- min-slack update --> (alpha',beta').

It commutes exactly by decoding the endpoint formulas. Changing reference before or after refinement gives the same fiber, with the correspondingly shifted coordinates.

For two refinements F,G, direct intersection, staged updates with recentering after each step, and reversed updates all give the same canonical centered interval or the same empty result. This is more than sorting archived rows: it checks that transport survives a change of selected representative between steps.

The proof is pointwise max/min algebra. It therefore applies over an entire public domain, not only sampled y. For finite affine lower/upper bounds, the envelopes remain piecewise affine; on the surviving domain their midpoint is a continuous section. Empty and lower-dimensional surviving domains must still be treated explicitly.

## Why projecting each refinement separately is insufficient

For [0,1], both h<=1/4 and h>=3/4 separately admit witnesses, but their conjunction does not. Adding their two inequalities gives 0<=-1/2.

Thus the two separately projected admission bits do not determine the admission of the combined fine refinement. The missing datum is COMMON-WITNESS compatibility, precisely what the interval residue retains. This is the elementary obstruction to treating existential projection as preserving arbitrary intersections.

Public refinements are different: they are saturated conditions P^-1(F), for which

    P(E intersect P^-1(F)) = P(E) intersect F.

That identity explains why the earlier public-restriction checkpoint transports are safe without recovering extra hidden-fiber information.

## Authority remains separate

The residue of an ACTUAL interval contains the history distinction insofar as that distinction affects the permitted continuations. If retirement merged histories with different intervals, producing their actual residue again requires retained information or authorized provenance. A common section cannot infer it.

An archive of both candidate residues still gives alternatives, not the actual branch. This geometric minimality result does not replace the authority boundary established by the archive restoration work.

## Checks and scope

The exact finite control checks 16,875 two-refinement comparisons, 375 changes of base, 210 distinguishing threshold queries and the A/B envelopes at all eighteen owning public vertices. It includes selector failure without emptiness and separate-feasibility without joint feasibility. The general claims follow from the displayed identities, not finite extrapolation.

    python research/voevodsky/checkers/check_relative_fiber_residue.py

Artifact: `results/relative-fiber-residue.json`.

This identifies an injective relative residue in the scalar continuation class. It does not yet identify the earlier analytic residue jet or furnish a literal 4-simplex/5-cone. The important new bridge is explicit: selected presentation, retained relative defect, invertible change of base and coherent refinement transport now have exact formulas in one admitted source class.
