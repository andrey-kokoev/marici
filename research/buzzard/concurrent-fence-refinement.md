# Concurrent fenced-history refinement

`ConcurrentFenceRefinement` connects a two-operation concurrent observation to
the existing sequential fenced-effect specification. A witness supplies one of
the two sequential orders, proves that the observed site outcomes agree with
that order, and respects completed-before-invoked precedence in both directions.

Positive fixture: overlapping attempts presenting token `4` refine to left then
right, producing `(true,false)`. The corresponding finite trace has one success
and one protected effect.

Hostile fixtures:

- `(true,true)` for two copies of token `4` cannot refine either sequential
  order;
- if the right operation completes before the left is invoked, an observation
  claiming the left won violates real-time precedence and has no refinement.

This is intentionally a two-operation bridge. Arbitrary finite concurrent
histories still need operation identity, a permutation witness, and a general
real-time partial-order preservation interface.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/ConcurrentRefinement.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8720 jobs).` The site build was not run.
