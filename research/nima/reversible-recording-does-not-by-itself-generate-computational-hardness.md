# Reversible recording does not by itself generate computational hardness

## Question

Does distributing a record through a long reversible circuit make recovery of
the hidden global relation computationally difficult?

## Claim boundary

Let a source-authorized recording circuit be the ordered word

\[
U=g_L\circ\cdots\circ g_1,
\]

where every gate is invertible and its inverse remains in the admitted gate
set. Then

\[
U^{-1}=g_1^{-1}\circ\cdots\circ g_L^{-1}.
\]

The inverse word has exactly (L) gates. If the original circuit has a layered
parallel schedule, reversing the layer order preserves its depth. Therefore a
known reversible recording circuit does not, by its length alone, create an
asymmetry in circuit complexity between recording and recovery.

This theorem does not say recovery is physically easy. It excludes only one
proposed explanation: complexity cannot be inferred merely from the existence
of a long reversible source history.

## Ordered-history witness

Take two self-inverse but noncommuting gates:

- (X_0), which flips the first bit;
- a controlled-NOT from the first bit to the second.

Their ordered product is reversed by applying the same gates in reverse order.
Replaying them in the original order is not an inverse. Thus a flat multiset of
gate names is insufficient even when every primitive is self-inverse.

The source history must retain:

- gate identity;
- ordered ports;
- causal order or authorized commuting cells;
- parameter values;
- physical support and control authority.

## Where an arrow can enter

Computational or operational difficulty may enter only through additional
structure not supplied by reversible recording itself:

1. The ordered source history is lost, so recovery becomes an identification
   problem.
2. The inverse gate set is unavailable to the controller.
3. Locality forces transport across an expanding support.
4. Noise requires gate precision that tightens with circuit length.
5. Uncontrolled environment carriers make the admitted inverse partial.
6. A logically irreversible controller erases the history needed for replay.

Each is a separate constructor and requires its own source evidence.

## Precision gate

Suppose each implemented inverse gate has certified error at most
(arepsilon) in a subadditive operational norm. The elementary telescoping
bound gives total error at most

\[
L\varepsilon.
\]

To guarantee final error at most (delta), it is sufficient to require

\[
\varepsilon\leq\frac{\delta}{L}.
\]

This is a worst-case sufficient bound, not a universal lower bound. Coherent
error cancellation or fault-tolerant structure can improve it. The relevant
point is that precision scaling is an additional physical gate, unlike exact
inverse circuit length.

## Thermodynamic boundary

No Landauer cost follows merely from applying (U^{-1}), because an exact
unitary inverse is logically reversible. Thermodynamic erasure cost attaches
to resetting or discarding the controller's classical history, fault record,
or syndrome memory. Conflating inverse evolution with erasure would insert an
unsupported thermodynamic arrow.

## Disposition

The finite no-go theorem is closed. Exact reversible recording has an inverse
of equal circuit size and depth. An explanatory arrow of time must therefore
be located in access, history retention, locality, precision, noise, or
logically irreversible controller operations.

Verification is provided by
`research/nima/checkers/check_reversible_recording_inverse_complexity.py` and
`research/nima/results/reversible-recording-inverse-complexity.json`.
