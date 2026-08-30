# Algebraic versus continuous descent

Owner: `marici.Buzzard`

Source locator: the opening theorem before `## Theta consequence` in
`research/strominger/distinction-preserving-completion.md`, specifically the
sequential condition following the algebraic kernel criterion.

Strength: source-typed sequential zero-control theorem and hostile topology.

## Formal interface

`SequentialZeroControl sourceSize repairSize` states that every sequence whose
source size tends to zero also has repair size tending to zero. The size
functions are explicit maps into the real numbers; the formalization does not
silently select norms or completion topologies.

Lean proves that the pointwise uniform domination

`repairSize v ≤ C * sourceSize v`

together with nonnegativity of the repair size is sufficient for sequential
zero-control. The proof is the real squeeze theorem applied to the uniformly
scaled source sequence.

## Hostile separation

On the rational vector space, the identity linear map algebraically factors
through itself. Give the source the zero seminorm and the repair observation
ordinary absolute value. The constant sequence at one has source size zero at
every index, while its repair size remains one. Therefore sequential
zero-control fails despite exact algebraic factorization.

This is the missing completion datum in its weakest explicit form: kernel and
factorization data do not choose compatible topology.

A positive finite fixture proves ordinary absolute value controls itself with
uniform constant one.

## Assumptions and limits

The convergence interface uses real-valued sizes and ordinary sequential
limits. It does not assert that either size is a norm, that the spaces are
complete, or that sequences characterize an arbitrary non-first-countable
topology. Those upgrades require explicit source topology.

The theorem is a sufficient uniform-bound criterion. It does not claim the
uniform bound is necessary in every topological setting. Strominger's
cutoff-family operator inequality still requires separately typed adjoints,
positive forms, cutoff covariance, and a constant uniform across cutoffs.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ContinuousDescent.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25: targeted exit code `0` with no diagnostics; full build
completed successfully with `8737 jobs`. No site build or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ContinuousDescent.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/algebraic-versus-continuous-descent.md`
