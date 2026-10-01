# Reference-context descent and orientation transport

## Readout and return covariance

There are nine outward local-reference contexts once both carrier roots are
fixed. The rooted relabelling group S3 x S3 has36 elements. For context c,
let D_c be its137 selected slots and m_c the arithmetic mean on those slots.
For relabelling g, transport both the context and member data. Then

    m_(g c)(g x) = m_c(x),
    g U_(c,delta)(x) = U_(g c,delta)(g x),

where U adds delta to every slot in D_c and leaves the other ambient slots
unchanged. The edit cost is137*delta^2. All324 context/group combinations pass
these equalities exactly.

## Ambiguity between transport witnesses

Each pair of contexts has four rooted relabellings between them. Their
ambiguity is the local S2 x S2 stabilizer, which permutes the unmarked labels.
It acts nontrivially on generic retained member values.

The137 selected slots have45 stabilizer orbits. Their means provide an
interface independent of the choice of transport witness. Orbit means with
member-count-weighted returns commute with context transport. Averaging member
values within each orbit equals averaging over the four stabilizer actions.

The full member state still contains residuals within those orbits. Preserving
it requires retaining a transport witness or its transformation rule. The
45-dimensional invariant interface is a readout of that state, not a lossless
replacement for it.

## Fixed-state context changes

Changing the selection mask while keeping physical member values fixed can
change the readout. A state supported on one root-outgoing arrow pair gives
mean0 in five contexts and mean1/137 in four contexts.

Indeed the nine context-mean functionals are linearly independent on the160-slot
ambient space. Restrict to the nine pairs of root-outgoing primitive arrows:
the incidence matrix is (J3-I3) tensor (J3-I3), divided by137, which is invertible.

A mean return in one context changes another context's mean by the overlap gain:

| Context relationship | Shared slots | Gain |
|---|---:|---:|
| Same context | 137 | 1 |
| One local mark changed | 126 | 126/137 |
| Both local marks changed | 116 | 116/137 |

Thus covariance under transported data and independence from reference selection
at fixed data are different properties. The latter fails for arbitrary states.

## Sphere classes carry an orientation action

On the FULL retained primitive relation, a permutation of the tetrahedron
vertices acts on H2 by its orientation sign. The checker evaluates this action
on the actual oriented tetrahedron boundary.

At a fixed context, swapping the two unmarked labels reverses the primitive
sphere class. Independent swaps on the two carriers give the four actions

    diag(+1,+1), diag(-1,+1), diag(+1,-1), diag(-1,-1)

on the rank2 degree2 class space of the full product. The common fixed subspace
is zero, while the class space itself still has rank2. A squared coordinate
readout is invariant under these sign actions; choosing its weights requires a
separate metric/readout specification.

This identifies the appropriate context-dependent object: a rank2 orientation
representation with explicit transition actions. Choosing generators globally
requires orientation data. The rank is already reference-invariant. The loops
here are invertible automorphisms in the reference action groupoid, unlike the
noninvertible mean projections studied earlier.

For independently labelled k factors, the same primitive sign rule yields a
rank-k orientation system. This supplies a way to carry the1,2,4 class spaces
without demanding invariant signed generators. The two-factor representation
is computed explicitly in the present checker.

## Structural next step

Construct the context transition action on these orientation systems and their
recursive comparison products. Verify composition, then classify the scalar
readouts and return metrics compatible with that action. The full member records,
45-orbit selected readout, and oriented homology classes are distinct interfaces
that should retain their own transport laws.

## Verification

    python research/nima/checkers/check_reference_context_descent.py

Exact covariance and edit-cost tests, four-witness ambiguity,45 orbit means,
Reynolds averaging, orbit-return covariance, fixed-state counterexample, nine
independent context means, overlap gains, and the full-carrier orientation-sign
representation. The shared sparse rank helper now normalizes zero entries;
the complete biclique-complex regression also passes.
