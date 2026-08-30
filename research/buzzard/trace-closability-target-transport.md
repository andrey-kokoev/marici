# Trace closability survives target transport

Owner: `marici.Buzzard`

Source locator: `Relative ambient lines do not repair trace closability` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

For arbitrary topological source and target types with distinguished zero,
`NonclosableWitness trace` contains:

- a source sequence converging to zero;
- a target limit of the traced sequence;
- proof that the target limit is nonzero.

`SequentiallyClosable trace` is the corresponding zero-graph criterion: every
such target limit must be zero.

Lean proves that a witness refutes sequential closability. More importantly,
if target outputs are postcomposed with a continuous injective map preserving
zero, the same source sequence converges to the embedded nonzero target limit.
The transported trace therefore remains nonclosable.

An isometry is a special case once continuity, zero preservation, and
injectivity have been supplied. Merely changing target coordinates or moving
to a faithful relative target cannot repair a source graph defect.

## Finite hostile fixture

The source is a two-element type with the indiscrete topology. The constant
nonzero source sequence converges to source zero, while `bitTrace` maps it to
the constant real sequence one. This is a finite topological countermodel to
closability.

Postcomposing with the continuous injective embedding `y ↦ (y,0)` preserves
the nonzero graph limit, and Lean proves the paired-target trace is still not
sequentially closable.

The fixture is intentionally hostile rather than a model of the theta source.
It demonstrates independence of source closability from faithful target
transport. Strominger's native first-order estimate may separately establish
closability for the actual theta endpoint.

## Boundary and missing interfaces

This theorem uses sequential closability. It does not formalize densely
defined linear operators, graph closure, Hilbert adjoints, or equivalence with
the standard closed-operator definition. A faithful analytic upgrade needs:

- a dense source domain and its inclusion into a Hilbert space;
- a linear trace operator and target Hilbert structure;
- the exact graph-closability definition and sequential equivalence premises;
- a typed target isometry or unitary transport;
- the native first-order estimate for the actual endpoint.

The abstraction generalized the transport obstruction but did not claim the
finite hostile topology represents the sector source.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/TraceClosability.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/TraceClosability.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/trace-closability-target-transport.md`
