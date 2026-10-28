# Trial P/E-dependent neutral routing

**Falsification update:** the conjecture that the stated symmetries force 126 open response pairs is false. Equally reversible, C3-symmetric and geometrically P/E-dual companion-strand rules give 198 pairs and 128 or 144 closed loops. The reference result below is conditional on fixing the companion three strands straight. See [conjecture and counterexamples](n-routing-conjecture-falsification.md).

## Explicit rule, before interpreting its counts

The previous opposite-edge N rule did not read P/E occupancy. This trial retains the same native N carrier lattice, but makes its local port matching depend on occupied P/E face neighbours.

1. Embed the object sector in a larger ambient sector. Only the object's P/E tetrahedra are occupied. N carriers exist inside and outside the object.
2. For each N octahedron, compute `drive = adjacent occupied P faces − adjacent occupied E faces`.
3. If drive is zero, retain all six straight opposite-edge strands.
4. If drive is ±1 and exactly one face is occupied, or exactly one face is unoccupied, select that distinguished face. These cases cover the nonzero drives in the tested sectors. Other nonzero-drive configurations are explicitly unsupported, not guessed.
5. Orient its three edge ports cyclically using the outward geometric face normal. Match them to the three opposite-face edge ports with a one-place cyclic shift for positive drive, the inverse shift for negative drive. The remaining three strands stay straight.
6. Trace all strands, retaining every local pass. Ports are paired reversibly; crossings do not merge.

This is a local, reversible, threefold-symmetric **trial scattering rule**, not a derived neutron field equation. Choosing cyclic matching is an assumption; the identity matching remains a different possible model. Edge ports are still zero-area fibre contacts, not finite-width void passages. P/E strands themselves have not been constructed.

## Results

| Object edge | P/E-rerouted open channels | Geometric dual response pairs | Closed loops |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 3 | 36 | 18 | 0 |
| 5 | 120 | 60 | 0 |
| 7 | **252** | **126** | **0** |

At edge 7, 248 N cells switch: 124 with positive and 124 with negative drive. This includes 80 carriers inside the object and 168 immediately outside it; external carriers are not omitted merely to change the count.

With two ambient shells there are 726 open channels: 474 unchanged, 252 rerouted. All 252 changed channels have changed boundary-port partners. Three ambient shells increase the background channel count to 1,014 but leave **252 rerouted channels and 126 dual pairs** unchanged. Removing P/E occupancy entirely yields no switches, no response and no loops.

Every local routing matching commutes with the native geometric P/E duality. The 126 pairs are checked on the **full response trajectories**, up to reversal, not inferred by dividing 252 by two: there are no self-dual response routes and none lack a dual.

The tested pair counts follow `3 n (n−1)` for n=1,3,5,7. This is a combinatorial pattern in this rule/sector family, not evidence by itself for nuclear content.

## Meaning and limits

The number 126 is noteworthy, but **126 geometric route pairs are not established as 126 neutrons**. No pair has been shown to be a single independent physical mode, have neutron quantum numbers, carry a particular energy, or form a bound state. All response channels remain open; no closed loops occur. Geometric pairing does not remove half the underlying strand records.

The cell inventory remains 224 P, 231 N, 224 E; the void and exposed-face inventories also remain unchanged. `localizedNeutronCount` is deliberately null. This is an occupancy-dependent scattering response after ambient comparison, not a Pb-208 identification or a complete signed-state construction.

## Viewer

In **Single octahedron — edge 7, no belt**, open **N tube routing trial** and select **P/E-coupled response (trial)**. White dashed polylines show each path from its first modified local pass to its last modified pass. Unchanged ambient tails are omitted, and the viewport expands to include the near-object response region. Curved routes are drawn through their actual edge ports, not replaced by endpoint chords.

The panel reports rerouted channels, geometric dual pairs and closed loops with the interpretation warning. The table adds P/E-rerouted channels separately from cells, voids and the uncoupled reference. **Uncoupled response (reference)** still yields zero changed paths, as it should.

## Verification

- `tests/pe-coupled-n-routing.test.mjs`: all four sizes; involutive 12-port matchings; no strand merging/loss; exact dual trajectory pairing; opposite-drive balance; no closed loops; zero-occupancy control; ambient shell stability; unchanged viewer cell/void counts.
- `scripts/probe-pe-coupled-n-routing.mjs`: audit output, including the two controls.
- Browser checks exercise the 252-polyline overlay, the explicit unresolved neutron count and unchanged previous processes.
