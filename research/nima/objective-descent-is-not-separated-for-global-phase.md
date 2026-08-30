# Objective descent is not separated for global phase

## Result

Successful gluing of local objective records does not imply that the local data
determine the global state uniquely. Descent has two independent questions:

1. **Existence:** do compatible local sections glue to any global section?
2. **Separatedness:** can two distinct global sections have the same restriction
   to every admitted local observer?

Loop holonomy obstructs existence. GHZ phase obstructs separatedness.

## Exact three-qubit witness

Consider

\[
\lvert\mathrm{GHZ}_{+}\rangle
=
\frac{\lvert000\rangle+\lvert111\rangle}{\sqrt2},
\qquad
\lvert\mathrm{GHZ}_{-}\rangle
=
\frac{\lvert000\rangle-\lvert111\rangle}{\sqrt2}.
\]

The two global density matrices differ in their off-diagonal phase terms. Yet
their reduced density matrices agree on every nonempty proper subset of the
three qubits. Tracing out even one qubit kills the global cross term.

Therefore a cover by all proper fragments has perfectly consistent local data
but cannot distinguish the two global states.

## Quotient interpretation

The objective pointer record is a quotient of the global state:

```text
global state
    → locally descending pointer record
```

The relative phase lies in the kernel of this readout. It is not a hidden local
value waiting to be recovered from more copies of the same proper-fragment
record. It is stored in the global relationship.

Thus classical objectivity may be fully valid for the pointer quotient while a
full-state reconstruction claim is false.

## Compiler consequence

The target claim must declare which level it needs:

- For an objective pointer value, effective descent of the quotient is enough.
- For reconstruction of the complete global state, the local restriction family
  must additionally be jointly faithful.

A source anchor can choose between multiple visible pointer sections. It cannot
recover a phase direction annihilated by every admitted local restriction.

## Falsifier

The nonzero operator

\[
\Delta
=
\lvert000\rangle\langle111\rvert
+
\lvert111\rangle\langle000\rvert
\]

has zero partial trace on every proper fragment. It is the finite witness for
`nonseparated_global_phase`.

