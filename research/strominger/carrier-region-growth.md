# Do existing shared-boundary constraints stop assembly growth?

## Question and claim boundary

Operator asks to add attachments and find whether the joint admissible state
vanishes. Test the already implemented boundary-sharing layer before inventing
an occupancy rule or interpreting 12/3/1 as established port dimensions.

Source: the P/N/E route words and H=P+E recipe in the existing circuit fixture;
C entry/exit ports are derived by the unchanged sewing constructor. Boundary
states are Q-valued functions on simultaneous binary port assignments, a declared
representation, not native particle states. There is one variable per ORIGINAL
port, not one per atom. No entry-to-exit equality, interior projector pullback,
energetic condition, spatial packing or one-use-per-port limit is added.

Obligation: forward boundary realization and global static compatibility of
explicit faithful restriction maps. Not a native molecular or physical-coherence
claim. The missing full-state interior/interface map remains deferred rather
than replaced by a speculative hypothetical carrier.

## Frozen experiment

Use 1 through 12 atoms, plus a 64-atom long-chain/ring stress control and a
64-attachment star. Chain seams identify each exit with the next entry; a ring
adds the final exit-to-first-entry seam. A star identifies one hub exit with k
other entries. The existing graph-pushout constructor permits the latter: a
one-use rule would be an additional hypothesis, not a discovered limit.

Each seam equates its two explicitly mapped binary values. Count ALL satisfying
assignments, not merely one witness. The compatible boundary-function dimension
is that count; the mismatch complement has dimension 2^(2n) minus that count.
Retain the original port labels, seam maps, component assignments and template
lineage. A diagonal projector is represented exactly by its predicate on every
binary basis label; a dense exponential matrix need not be allocated.

Predictions before execution:

- Chain of n atoms: n-1 independent seams, dimension 2^(n+1).
- Ring of n atoms: n independent seams, dimension 2^n, not zero. The cycle in
  the ATOM graph is not a cycle of port-equality constraints: entry and exit
  remain distinct variables.
- Hub with k attachments: dimension 2^(k+2), not zero at any k.
- Honest simultaneous per-port relabellings preserve these dimensions.
- Four locally admissible seams in a K2,2 incidence pattern, with one inconsistent
  twist, have zero compatible assignments. This deliberately changed span is a
  global chart/restriction obstruction, not a molecular prediction.

Independently brute-force every assignment for cases with at most five atoms.
Compare with a signed-component solver; retain every constraint and a full
assignment witness for larger cases. Check each seam using the existing admission
function, and use the existing graph pushout to preserve P/E instances.

## Why finite counts suffice for a general negative conclusion

For identity seams, assign zero to EVERY original boundary port. This solves
any finite set of seams, regardless of degree, shape or number of atoms.
More precisely the solution count is 2^c, where c is the number of connected
components in the PORT equality graph, including isolated ports. With globally
coherent bijective relabellings, transport that same assignment by each port's
fixed bijection. Thus identity sharing and its honest relabellings cannot by
themselves enforce a maximum region size or coordination number. The finite
sweep tests the implementation; the all-zero construction proves the unrestricted
finite-family statement. This is not an extrapolation from testing 64 atoms.

## Issue-boundary DPC and disposition criterion

1. Problem: could the currently implemented crossing/sewing constraints already
   explain a finite assembly limit without inserting a capacity by hand?
2. Candidate: increasing attachments or closing a ring eventually annihilates
   the admissible boundary state, under the existing faithful sharing rule alone.
3. Rivals: unrestricted identity-compatible growth; a hidden one-use-port rule;
   accidental entry/exit identification; inconsistent global seam charts;
   restrictions from native internal comparisons that are not yet pulled back.
4. Risk: a claimed limit must produce a genuine empty compatible set with the
   original source spans, not one manufactured by a new occupancy convention.
5. Strongest test: chains/rings/stars through 64, exact dimensions, exhaustive
   small-case agreement, honest chart changes and a deliberately frustrated
   four-seam control that MUST produce the empty set.
6. Disposition: execution receipt governs the observed result. If the predictions
   hold, the claim that sharing ALONE imposes a finite limit is rejected. Native
   interior comparisons are NOT rejected or tested. A boundary-compatible state
   need not extend to an admissible interior state, bind, or be physically stable.

## Reproduction

    python research/aspect/scc/scc.py check carrier-region-growth-v1 --verbose

Fixture: `inputs/carrier-region-growth-v1.json`.
Checker: `checkers/check_carrier_region_growth.py` (standard library only).
Receipt: `results/carrier-region-growth/verification.json`.

The next native test requires source-defined restrictions from complete internal
comparison states to the shared boundary. Then intersect the pulled-back local
admissible spaces. Binary boundary functions are not a substitute for those maps;
no waiting-only successor or invented capacity is created here.
