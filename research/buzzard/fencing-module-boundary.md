# Fencing module boundary

The fencing and protected-effect theory has been extracted from
`TemporalAuthority.lean` into `MariciFormal/Fencing.lean` without changing its
namespace or theorem names.

The dependency chain is now:

```text
TemporalAuthority
  -> Fencing
  -> RecoveryEvidence
  -> RequestNamespace
  -> ProtocolTrace
  -> ConcurrentRefinement
```

`TemporalAuthority` retains grants, leases, request identity, temporal validity,
and distributed-consumption foundations. `Fencing` owns target-side epoch
validation, ordered resource registers, replica countermodels, atomic protected
effects, and the two crash splits.

This is a structural specialization, not a new abstraction. The extraction
demonstrates that recovery requires fencing, while fencing itself does not
depend on completion witnesses, namespace qualification, or trace semantics.

Verification commands from `research/buzzard/marici_formal`:

```text
lake build MariciFormal.TemporalAuthority
lake env lean MariciFormal/Fencing.lean
lake build MariciFormal.Fencing
lake build MariciFormal.RecoveryEvidence MariciFormal.RequestNamespace MariciFormal.ProtocolTrace
lake env lean MariciFormal/ConcurrentRefinement.lean
lake build
```

All commands passed under Lean `v4.33.1`; the final project result was
`Build completed successfully (8721 jobs).` The site build was not run.
