# Actual proton/electron seed paths: retained rung bridge and predictive readout

## Question and scope

Does a rung-4 packet retain enough labelled information to determine its next
reading under a specified source extension?

This construction uses the actual collection's proton/electron affine sources,
the existing six-arrow proton manifest, the existing endpoint-composition
function, and both existing retained rung-transport policies. The successor is
explicitly **independent endpoint-compatible word extension**. It is not claimed
to be the assembly's physically selected cycle, a pair interaction, or a new
clock. Word depth is not elapsed time. No Hamiltonian or SI conversion is added.

## Actual seed input

The supplied affine maps generate moving correspondences:

- proton: AB, BC, CA, AD, DB, BA (6);
- electron: AB, BC, CD, DE, EA (5).

The checker derives these from the source maps, verifies collection source
hashes, and matches the proton manifest. Affine labels use A as the origin and
subsequent labels as coordinate axes. The declared current pair vertex is
(A,E), not an identification of both attachment seeds with that vertex.

Primitive IDs include owner, correspondence index and directed endpoints.
Opposite arrows remain distinct. The joint context graph has 20 vertices and
50 addressed edges: 6 proton arrows times 5 held electron contexts, plus 5
electron arrows times 4 held proton contexts. These are references to **11
primitives**, not 50 new primitives.

Paths retain every contextual step and original primitive reference. They are
possible continuation words, not newly issued physical execution receipts.
Each extension appends every compatible local step using the existing compose
operation; parent prefixes are recoverable.

## Reuse the retained rung transport

Every word is a leaf row with its full path in the label, joint source/target,
unit member weight and the existing identity-matrix response. Both incoming
promotion policies and both routes through the clarified rung diagram are
reused. The reference stays at d4=2I.

Both routes retain the exact original words, registry and current depth. The
ordinary fixed-reference aggregate is -I at every tested stage: it does not see
the changing endpoint distribution. Row member weights are path-context counts,
not particle masses. This input is not the old 137-row shared-leg fixture.

Write R for this retained adapter and define the induced full-packet successor
by recovering, extending and re-encoding the words. The checked square is

    R F = F_retained R.

That identity alone is expected from exact recovery. The substantive predictive
check below independently operates on the much coarser endpoint profile.

## A closed endpoint profile

Let rho(i,j) count words ending at joint vertex (i,j). Define A_p and A_e with
entry (b,a) counting supplied moving arrows a->b. Then

    rho_next = T rho,
    T = A_p tensor I_5 + I_4 tensor A_e.

The checker applies this rule without decoding the ordered paths, and compares
it with actual word extension before and after both rung transports:

    P_next F = T P.

This profile closes under the declared successor. T is an integer
path-multiplicity transfer, **not a Hermitian Hamiltonian or unitary evolution**.
A 20-component pair profile at rung 4 is not four-dimensional spacetime.

All full frontiers through word depths 1..4 pass. Starting from (A,E), their
path counts are 3, 8, 21, 55; one-step continuation counts are 8, 21, 55, 144.

## Where counts fail, and where they suffice

Allow an explicitly prepared nonempty subfamily of valid length-two words.
This preparation interface is an additional declared input, not a selection
law derived from the seed assembler.

Family X:

- proton AB then proton BA;
- proton AD then proton DB.

Family Y:

- proton AB then proton BC;
- proton AD then electron EA;
- electron EA then proton AD.

Both have (primitive count, word depth, one-step continuation count)=(11,2,6).
After extension their one-step continuation counts are respectively **16 and
15**. Thus that coarse triple does not determine its own next reading on this
prepared domain.

However, adding the current number w of path contexts closes these aggregate
counts in this particular graph:

    w_next = q1,
    q1_next = 3 q1 - w.

This is checked on all 255 nonempty unit-coefficient subfamilies of the eight
length-two words. The labelled endpoint profile also closes throughout this
finite domain. It is sufficient, not claimed minimal for aggregate prediction.
These aggregate counts still do not reconstruct labelled configuration.

## History is retained even when this successor ignores it

The words proton AD / electron EA and electron EA / proton AD reach the same
joint endpoint. Their profiles and next profiles agree under independent
extension, while their ordered records remain distinct through both transports.
A future history-sensitive interaction might require more than rho; this
construction establishes no closure for such a different law.

A changed retained target label is rejected. Source hashes are checked again
at the end of the run.

## Result

A positive retained source/transport square and a closed labelled endpoint
readout are constructed for actual seed correspondences under a declared
endpoint successor. Equal scalar counts can fail to predict the next count;
a small count enrichment closes only aggregate evolution, while endpoint
labels supply configuration-sensitive prediction and full words preserve
provenance.

Still unestablished: the actual source-selected proton/electron interaction,
whole-configuration coherence admission, canonical momentum, physical cycle
clock, transport of our proposed Hamiltonian, and Planck-to-observed units.

## Verification

    python research/nima/checkers/check_actual_pair_endpoint_rung_bridge.py

Fresh run: **965 exact checks pass**, including the reused endpoint-composition
and original rung-fixture assertions, both policies/routes, full-path recovery,
independent endpoint prediction, all 255 prepared subfamilies, count collisions,
order retention, altered-endpoint rejection and stable source hashes.

Receipt: `results/actual-pair-endpoint-rung-bridge.json`.
This is standard-library Python verification, not a new Agda proof.
