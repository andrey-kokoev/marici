# Toric reset versus record transfer: frozen conjecture

Owner: `marici.Nima`

## Conjecture

For a nontrivial binary Lüders measurement, conditional pointer reset cannot
close the full source apparatus while retaining the nonselective measurement
channel.  It can only move the outcome record into another degree of freedom.

Equivalently, a reusable constructor for the measurement task requires one
of:

- a retained record/waste port carrying the syndrome;
- reversal of the measurement itself; or
- an imported low-entropy resource that accepts the record.

The expected invariant is the Kraus/Choi rank of the nonselective channel.
The binary dephasing channel has rank two, whereas a dilation whose complete
apparatus returns to one fixed pure state has rank one.

## Falsifiers

The conjecture fails if a source-defined finite unitary circuit simultaneously:

1. implements the nonselective Lüders channel for both syndrome sectors;
2. returns every apparatus, record, and environmental degree of freedom to a
   common input state;
3. uses no imported fresh subsystem; and
4. does not reverse the system measurement.

This is a statement about the complete apparatus.  Resetting one pointer
while leaving a record elsewhere is predicted and does not falsify it.
