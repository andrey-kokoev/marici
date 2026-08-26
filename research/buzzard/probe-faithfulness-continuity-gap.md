# Probe faithfulness versus endpoint control

Owner: `marici.Buzzard`

Source locator: `Pro-Gram faithfulness is weaker than endpoint continuity` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

The coefficient type is rational and the packet type is `Nat →₀ Rat`, the
finitely supported sequences. `coordinateProbe j packet` reads coordinate
`j`; `totalEndpoint packet` sums every supported coordinate.

Lean proves the full countable coordinate family is jointly faithful: if every
coordinate probe vanishes, the finite packet is zero.

For a finite observation set `observed`,
`FiniteProbeFamilyControlsEndpoint observed` means every packet invisible to
those probes has zero total endpoint. Lean proves this property fails for
every finite set.

## Hostile countermodel

Given any finite set of observed coordinates, choose an index `m` outside it
and the singleton packet `e_m`. Every selected coordinate probe is zero, while
the total endpoint is one. This is an executable algebraic witness to the gap
between joint separation by the whole probe family and endpoint determination
by any finite subfamily.

It also refutes every proposed domination inequality using only that finite
family: its right side vanishes on `e_m` while the endpoint magnitude is one.

## Boundary

The theorem formalizes the finite-support algebra behind the coordinate
topology example. It does not construct a locally convex topology or prove a
general continuity characterization. Such an upgrade requires:

- seminorm-valued probes on a topological vector space;
- the chosen finite-max or finite-sum convention for locally convex bounds;
- the endpoint's linearity and scalar norm;
- a theorem equating continuity with domination by a finite probe subfamily;
- completion and density interfaces if the endpoint is to extend.

The result generalized the faithfulness/control distinction without merging
it into the earlier kernel theorem: the whole infinite family has trivial
joint kernel, while every finite subfamily retains a hostile kernel vector.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ProbeContinuityGap.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ProbeContinuityGap.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/probe-faithfulness-continuity-gap.md`
