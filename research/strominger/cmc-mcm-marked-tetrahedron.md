# CMC/MCM marked tetrahedron and identity-preserving handoff

## Construction already grounded in the existing prototype

Freshly read `demos/particle-overlap-tetrahedron/model.mjs` already supplies
C0,M0,C1,M1 and the exact proposed P/N directed windows. This experiment imports
the actual module via Node rather than inventing a new coincident-looking source.
It formalizes the missing opposite-vertex, type, duality and handoff conditions.

    C0=(1,1,1), M0=(1,-1,-1), C1=(-1,1,-1), M1=(-1,-1,1).

All six squared edges are8; volume8/3. Proton is the MARKED ordered face
(C0,M0,C1), neutron(M0,C1,M1). Both belong to the same geometric prototype;
this is not an assertion that two physical particles are one occurrence.
The complementary vertices are respectively M1 and C0. The shared directed edge
is M0->C1. Each triangular window is codimension1 in the tetrahedron, and the
shared edge is codimension1 in each triangle. This does not give C and M
vertices different geometric dimensions: physical C/M grading is still proposed.

## Two explicit C/M point lattices and a regular chain

Let

    Lambda=Z(-2,0,-2)+Z(-2,0,2)+Z(0,4,0),
    L_C=(1,1,1)+Lambda, L_M=(1,-1,-1)+Lambda.

These disjoint affine lattices together equal the OLD B FCC vertex family,
not the original diamond A/B families. Its old A barycentric centers have not
been reclassified as C/M by this constructor. Thus no earlier diamond coloring
or mixed-core obstruction is silently repaired. This is a new selected marking
on an existing geometric source, not a derivation of physical C/M identities.

An exact edge-sharing chain is

    C_i=(1-2i,1,(-1)^i),
    M_i=(1-2i,-1,-(-1)^i),
    T_i=(C_i,M_i,C_(i+1),M_(i+1)).

A common glide g(x,y,z)=(x-2,y,-z) advances the chain and preserves each point
lattice. Its square translates by(-4,0,0). Every T_i is regular; consecutive
cells share exactly the C_(i+1),M_(i+1) edge and nonconsecutive cells have no
identified vertices. They occupy consecutive x slabs, so this chain is not
silently a tetrahedral space-filling tiling or a full3D interaction law.

Inside T_i, P_i/N_i share M_i->C_(i+1). Across cells, N_i/P_(i+1) share
C_(i+1)->M_(i+1). The next M vertex is therefore present in the P context and
the previous C vertex in the N context. No vertex needs an ambiguous double type.

## Two precise kinds of contravariance

1. Taking the complement of a face reverses inclusion and is involutive on all
   face subsets. It pairs the CMC face with opposite M1 and MCM with opposite C0.
2. R(x,y,z)=(-x,-y,z), a proper180degree rotation, sends local index k to3-k
   and exchanges the proposed C/M point lattices. Applying R AND reversing a
   path sends the P window to the N window. For every composable path pair,

       A(p then q)=A(q) then A(p).

   The shared directed edge maps to itself. R g R=g^-1 provides the matching
   reversal of chain handoff.

These are explicit source maps, not assertions that different identities are
equal or that the transformation is a native physical P-to-N conversion. The
labels/readers must be transported. Opposite-vertex complement alone forgets
face direction: C0->M0->C1 and its reverse have the SAME opposite vertex.
The full marked occurrence order is indispensable.

## Exact information audit

* P face alone loses M1: a source perturbation at M1 is invisible there but
  visible at the next N window. N alone similarly omits C0.
* Keeping only C/M type sums loses the difference between C0 and C1, even
  though both are C. A carrier type is not an occurrence identity.
* Both compatible marked faces recover all four source values, with their
  shared M0/C1 values required to agree. Conflicts are REJECTED, not averaged.
* In an eight-cell chain there are32 local vertex occurrences and18 globally
  distinct vertices. Every occurrence-to-global-identity map is retained.
  The32 local scalar values have14 gluing constraints, giving18 independent
  values. All18 original global basis states reconstruct, and every available
  zero/one/two-window reader square agrees.
* Proposed gluings must match BOTH type and global identity. Cross-type maps,
  same-type wrong-node maps, incomplete packets and inconsistent values fail.

Critically, a rolling four-vertex window by itself is NOT a lossless history.
Advancing discards C_i,M_i. The test supplies an explicit old-state witness
invisible in the next window. A persistent global ledger, or archived outgoing
identities/values, makes the handoff reversible. Two handoffs are tested on all
eight input basis states including the newly supplied future values. The fourth
vertex supplies complementary CONTEXT; it does not replace accumulated history.

## Scope, DPC and next test

Problem: make the required CMC/MCM windows compatible with four vertices and
identity retention. Candidate: ordered marked faces plus opposite context and
explicit edge handoff. Risks: full source module/metric agreement, all inclusion
and path anti-functor squares, actual C/M lattice placement, full-state readers,
wrong-identity gluings and discarded-history witnesses. Disposition: this
geometric/typed constructor exists, including exact positive and negative tests.

It does not independently select physical C/M grading, native event origin,
spin, charge, mass or particle behavior. Earlier source-origin nonselection and
native protocol obstructions are not erased by proposing a coordinate marking.
Next source-enabled test: compare the explicit glide/rotation and marked face
maps with actual retained native P/N preparation/readout/action data; require
full commuting squares and compatible phase/history attachment, not just matching
words or active ranks. A failed lift must be retained as a scope obstruction.

    python research/aspect/scc/scc.py check cmc-mcm-marked-tetrahedron-v1 --verbose

Source specification: `inputs/cmc-mcm-marked-tetrahedron-v1.json`.
Receipt: `results/cmc-mcm-marked-tetrahedron/verification.json`.
No forces or fitted physical coefficients are introduced; unrelated conjecture
net current pointers and prior scientific receipts are not changed.
