# Wilson parity: equal effects, inequivalent instruments

Status: exact finite instrument theorem for string lengths `2 <= L <= 6`.

## Question

Do two source protocols implement the same Wilson-loop port merely because
they return the same parity probabilities?

## Two protocols

Let `W=prod_e Z_e` on a marked noncontractible string.

The coherent global protocol couples one retained ancilla to the complete
string and measures only `W`.  Its outcome instrument is the Lüders map

\[
\mathcal I_b^{global}(\rho)=\Pi_b\rho\Pi_b,
\qquad \Pi_b=(I+(-1)^bW)/2.
\]

The refined protocol measures every `Z_e`, retains the fine bit string `z`,
and only afterward reports its parity.  If that fine record is discarded, its
coarse instrument is

\[
\mathcal I_b^{fine}(\rho)
=\sum_{z:\,|z|=b}\Pi_z\rho\Pi_z.
\]

Both have the same effect `Pi_b` and therefore the same outcome probability
for every state.  Their state updates differ.

## Exact witness

For `a=00...0`, `b=110...0`, the state

\[
|\psi\rangle=(|a\rangle+|b\rangle)/\sqrt2
\]

has even parity.  The global instrument preserves its off-diagonal
coherence.  Fine measurement followed by classical parity coarsening deletes
that coherence.  The normalized outputs have exact trace distance `1/2`.

A symmetric reported-bit flip with probability `1/10` gives identical noisy
effects for both protocols, yet their subnormalized even-output maps remain
at trace distance `9/20`.  Classical output noise therefore does not erase
the physical-instrument distinction.

## Toric typing and resource tradeoff

On each checked torus, the closed length-`L` Wilson support has zero star
syndrome, while each individually resolved `Z_e` has two star endpoints.
The refined protocol consequently interrogates nonconserved microscopic
operators and can disturb star-sector coherence even though its reported
parity agrees with the Wilson port.

The coherent mobile-ancilla constructor retains one record bit and has
sequential depth `L`.  The parallel refined constructor has data-coupling
depth one but creates `L` record bits/environmental distinctions.  Deleting
those bits from the displayed record does not unmeasure them.  Depth, record
extent, and back-action are independent resource coordinates.

## Carrier and coefficient boundary

Carrier geometry identifies the common closed support and parity functional.
The quantum coefficient lens supplies completely positive instruments,
coherence, environmental records, and trace distance.  Equality of Carrier
readout functions proves equality of effects, not equality of instruments.

## Assumptions, falsifiers, and limits

The theorem assumes ideal projective `Z` measurements followed by an optional
classical bit flip.  It is falsified if the two effects differ, if the refined
coarse map preserves the witness coherence, or if the exact trace distance is
not `1/2` (`9/20` after the subnormalized noisy outcome).

This does not compare fault-tolerant cat-state circuits, correlated hardware
noise, feedback using the retained fine record, or generic dressed Wilson
operators.  The trace-distance witness is an ambient string-state witness,
not a ground-code-state witness; it proves inequivalence on the declared
ambient instrument domain.  A protected-subspace distance calculation is a
successor falsifier.  These are successor protocols, not consequences of
effect equality.
