# Context saturation has three frontier verdicts

## Question

What are the decisive outcomes when a recovery domain is saturated under all
source-authorized contexts required for later composition?

## Claim boundary

Represent the admitted total contexts by a directed graph on the state carrier:
an edge (x\to y) exists when an admitted context sends (x) to (y). The
context saturation of a seed domain is its directed reachable set.

For total finite contexts, three structural cases matter:

1. the seed closes inside a proper invariant subcarrier;
2. the seed reaches the complete connected carrier;
3. finite cutoffs close, but their saturation sizes diverge in a directed
   colimit, forcing an infinite recovery domain.

For typed partial contexts there is an earlier possible rejection: proposed
equivalent representatives may disagree on whether a composite is defined, on
its typed fiber, or on its resulting equivalence class. That is not a large
saturation. It means the quotient is not defined.

## Finite proper closure

If the context graph has several forward-invariant components, a seed may remain
inside one component. Provenance need only separate process action on that
component, subject to the partial-congruence and fault gates.

The exact fixture has three disjoint two-state cycles. A seed in the first cycle
saturates to exactly two states.

## Full connected closure

If the context graph is strongly connected, every nonempty seed reaches the
complete carrier. Any provenance quotient intended to survive arbitrary
admitted contexts must then be faithful on the full state action.

The exact fixture is a directed six-cycle. Every singleton seed saturates to all
six states.

## Forced infinite closure

Consider the directed chains

\[
0\to1\to\cdots\to N-1.
\]

At every finite cutoff the seed zero has a finite saturation, but its size is
(N). The colimit saturation is therefore infinite. Cutoffwise finite closure
does not supply a finite completion-stable provenance interface.

## Partial-congruence rejection

Suppose two histories are identified at the endpoint, but an admitted downstream
context is defined for one representative and not the other. The quotient's
constructor domain depends on representative choice and is invalid.

Even equal defined outputs are insufficient when attached support, residual
capability, authority kind, or other typed fibers differ. Identification then
requires an independently source-authorized coherence cell transporting those
fibers.

## Frontier compiler

For each sector, compute:

1. the seed recovery domain;
2. the admitted context graph or partial action;
3. the reachable saturation at every finite cutoff;
4. strongly connected or invariant components;
5. representative-independent definedness;
6. equality or authorized transport of typed fibers;
7. completion behavior of saturation size and observability gain.

Return exactly one of these verdicts:

- finite proper context closure;
- full or forced-infinite context closure;
- invalid provenance quotient from partial or fibred incongruence.

## Sector readings

- In control, feedback may enlarge an open-loop observable component to the
  entire reachable carrier.
- In optics, cavity recirculation may saturate field modes that a one-pass probe
  never visits.
- In topological measurement, braid and fusion contexts may connect logical
  sectors or expose a forbidden partial domain.
- In flavor, additional preparations may enlarge the calibrated coupling
  domain, while thresholds create genuine partiality boundaries.
- In authority compilation, downstream constructors test both history
  congruence and equality of attached authority fibers.

## Disposition

The finite trichotomy is closed, including an exact family whose cutoff
saturation grows without bound. Physical sector classification still requires
source-derived context graphs, partial domains, and completion topologies.

Verification is provided by
`research/nima/checkers/check_context_saturation_trichotomy.py` and
`research/nima/results/context-saturation-trichotomy.json`.
