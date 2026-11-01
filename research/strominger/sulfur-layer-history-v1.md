# Layer history as a candidate source of the retained b state

## Result

The layers contain the **kind of hidden information** needed: two paths can
occupy the same directed edge with the same present colour while differing in
a previous red/blue choice. The current edge colour cannot distinguish them;
retaining that older choice can.

There is a particularly small, geometry-selected interface: the **first merge
and its following fork**. In every layer it yields two outgoing coloured ports,
with two distinguishable causal history classes on each. One retained older
colour supplies an independent binary state beside the current port colour.

This is a candidate information-bearing interface, **not yet an assignment to
native b or a successful native-route prediction**. The audit imports the layer
builder only; it does not use native routes to choose histories or signs.

## Exact witness

After two branch choices, histories BR and RB reach the same central white edge.
They retain different most-recent branch colours across that white segment.
Following its next fork gives:

| Causal history | Current outgoing port | Retained older colour | Candidate b | Possible remaining completions |
|---|---|---|---|---|
| BRR | red | red | + | 32 |
| RBR | red | blue | - | 32 |
| BRB | blue | red | + | 32 |
| RBB | blue | blue | - | 32 |

Here the declared convention is **older red = +, older blue = −**. The bit is
computed from the path prefix, never from a route ID or an untraversed suffix.
Equivalently, at these outgoing ports it is the penultimate branch colour.
The pair (current port colour, retained bit) distinguishes all four rows.

The same convention works on all eight layers, despite changes in arrow
orientation and geometric left/right. This follows inherited colour/history
labels through the prescribed reflections, not an assumed native correspondence.
Reversing the global sign convention works equally well for this layer-only test.
A sign naming convention by itself is harmless; the missing port and state
correspondence is the substantive issue.

## Why the latest colour alone fails

For example, BRB and RBB occupy the **same blue arrival edge** at the next white
segment. Their present edge and colour agree, but the older colour is red in
BRB and blue in RBB. The current colour therefore provides a port label, not the
extra distinction needed between records on that port.

At later merges, a single older bit does not identify every history: several
prefixes may share both the current colour and the candidate bit. No identities
are collapsed or claimed to be recoverable from this one-bit state alone.

## Counting and causality controls

Each layer has 256 complete routes but only 255 distinct prefixes observed at
its 36 white edges, summed over stages. Future suffix choices are not counted as
additional present identities. A depth-n prefix has 2^(8−n) possible completions.
At the selected interface the four prefix classes each have 32 completions.

These are **possible path histories**, not four demonstrated conserved physical
strands. No claim is made that a fork creates new identities, or that a prefix
class is already one native wire. Paths outside this local interface remain in
the unchanged layer construction.

Truncating every route immediately after this fork yields the same candidate
bit assignments, with no future edges available. A streaming two-colour memory
(previous/current branch) reproduces the prefix calculation. White traversal
preserves that memory. Neither the layer gap nor route IDs determine the bit.

## Which local boundary fits—and which does not

The useful two-port/two-history interface is the **outgoing boundary after the
first merge and fork**, not the complete incoming star of a single white edge.
Across all 168 complete white-edge neighbourhoods, none has exactly two distinct
causal prefixes on each incoming port. We do not select four convenient paths
from a larger incoming set to force that match.

The outgoing layer fork has a different directed incidence pattern from the
native incoming join. Its abstract information capacity therefore does not
establish a graph, geometric, or arrow-preserving identification. The earlier
native angle obstruction has not been removed by giving histories bit names.

## Remaining correspondence test

A native carrier assignment cannot honestly be scored until we specify, without
consulting desired exits:

1. How this directed layer interface corresponds to native arrival ports and
   their frame, preserving the declared flow.
2. How current port colour and layer context supply native a,p,e labels. Red/blue
   layer edges are not automatically the native compound wire colours.
3. Which prefix populations correspond to conserved native records, rather than
   arbitrarily treating four possible histories as four physical strands.

Only then can the retained older bit be tested as native b. Feeding it to native
positions and identities selected from the desired answer would make the check
circular, so no such comparison or success percentage is reported here.

The target is now concrete: a correspondence for this **merge–white–fork
boundary**, rather than an unrestricted search through layer histories. Its
information content is sufficient for a two-port plus one-memory-bit interface;
its identification with the native boundary remains open.

## Reproduction

- node --test tests/sulfur-layer-history.test.mjs
- node scripts/check-sulfur-layer-history.mjs
- Layer-only audit: research/realization-tower/sulfur-layer-history.mjs
- Receipt: results/sulfur-layer-history-v1/verification.json

No viewer geometry, original route, inter-layer connection or population was
changed.
