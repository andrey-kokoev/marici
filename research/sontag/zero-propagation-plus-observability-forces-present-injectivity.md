# Zero Propagation Plus Observability Forces Present Injectivity

## General no-go

Let \(X\) be a state space, \(r:X\to Y\) a pointed readout with distinguished
zero, and \(F_w\) every admitted future constructor word.

Assume zero propagation:

\[
r(x)=0
\Longrightarrow
r(F_wx)=0
\]

for every state \(x\) and word \(w\).

Assume joint faithfulness of the future probes:

\[
r(F_wx)=0,\quad w\in T^*
\Longrightarrow x=0.
\]

Then \(r(x)=0\) implies that every future probe vanishes by propagation, and
joint faithfulness implies \(x=0\). Hence

\[
\ker r=\{0\}.
\]

The two gates force the present readout itself to be pointed-monic. Future
iteration contributes no additional separation inside its zero fiber because
zero propagation has required that entire fiber to remain behaviorally zero.

For a linear scalar readout on a Carrier of dimension greater than one, this is
impossible. The native RH pure-flux line is the exact first-jet realization of
the general kernel obstruction.

## Minimal process criterion

At instrument level, replace scalar probes by joint record words. Let
\(Z\subseteq X\) be the states producing the distinguished present record.

The process form of zero propagation is **zero-class safety**: every admitted
conditioned update from a state in \(Z\) produces only future record histories
belonging to the declared zero language.

The process form of joint faithfulness is **zero-class separation**: no
nonzero admitted state has the same complete distribution of sequential record
words as the zero state.

Together these again imply that the present zero class contains no nonzero
admitted state. Therefore the minimum criterion is not ordinary observability
alone. It is:

1. a source domain \(A\);
2. a present instrument whose zero-record fiber intersects \(A\) only in the
   zero state;
3. conditioned update closure for every admitted continuation;
4. lineage-correct joint record evaluation.

If the present scalar zero fiber is nontrivial on the ambient Carrier, a source
or boundary relation must first restrict the admitted domain so that

\[
A\cap\ker r=\{0\}.
\]

This is exactly a source-transversal theorem. Adding future scalar probes cannot
repair a zero fiber that zero propagation has made invariant.

## Three admissible repairs

### Joint present record

Replace the scalar readout by a jointly injective record packet, such as value
and flux together. Its simultaneous zero fiber may be trivial. A second readout
helps only if the joint present kernel is zero on the admitted source domain.

### Source-derived boundary relation

Retain the scalar value readout but prove that admissible pointed states satisfy
a relation excluding nonzero pure flux at the relevant boundary. This changes
the source domain; it does not make value probes observable on the full jet
Carrier.

### Relation-valued propagation

Allow a present value zero to generate additional typed obligations or records
rather than insisting that every later scalar value remain zero. This abandons
the scalar zero sieve and replaces it with a richer invariant relation.

Flux-to-value mixing alone takes this third route: it exposes the hidden line
but necessarily violates scalar zero propagation.

## Bisimulation boundary

For a deterministic or stochastic process on a fixed closed interface,
sequential record bisimulation is the correct equivalence when it matches:

- current record labels or distributions;
- every admitted conditioned transition;
- and the bisimulation relation after each matching branch.

This is sufficient only for that interface. If compatible environments,
ancillas, reference systems, or hidden ports may later be supplied, the
relation must also be a congruence under every such extension and plugging.
Call this **environment-complete sequential equivalence**.

In quantum language the stronger criterion is equality under every compatible
ancilla-assisted causal tester, equivalently equality of the process/comb at
the declared open slots under a tomographically complete convention. Ordinary
reduced-system bisimulation can identify processes that a retained environment
later separates.

Thus sequential bisimulation is exact only after the boundary is frozen and
declared complete. Environment-complete equivalence is required for claims
stable under arbitrary admitted boundary extensions.

## RH consequence

For the native value--flux jet, value-zero propagation preserves the pure-flux
line. No amount of future value probing can be jointly faithful there. A valid
RH route must derive at least one of:

- a second present record making the joint kernel trivial;
- a reciprocal or endpoint boundary law excluding nonzero pure flux from the
  distinguished source domain;
- a richer relation-valued propagation theorem with instrument-level updates.

None may assume scalar nonvanishing. The boundary law must be constructed
without dividing by the completed scalar or selecting the desired state after
inspection.

## Verification boundary

The dependency-free checker realizes the general no-go over the two-dimensional
binary linear Carrier. It verifies the invariant hidden line, an observable
mixing repair that breaks zero propagation, a joint present record satisfying
both gates, and a source restriction on which the scalar readout becomes
injective. This is a finite exact analogue, not an RH theorem or quantum comb
reconstruction theorem.
