# Discrete control execution audit

## Formal theorem boundary

`MariciFormal/DiscreteControlExecution.lean` defines the minimal deterministic
discrete-time data:

- state type `State`;
- control type `Control`;
- transition `step : State → Control → State`;
- execution of finite words `List Control`.

Lean proves identity execution for the empty word and temporal composition:
executing `first ++ second` equals executing `first`, then `second`.

The positive executable example is the rational integrator
`step x u = x + u`. Its exact coefficient type is `ℚ`; execution adds the
finite control sum, and every rational target is reachable in one step.

## Hostile distinctions

- A frozen Boolean system satisfies execution composition but cannot reach
  `true` from `false`.
- An autonomous integer drift satisfies composition but does not preserve zero
  as an equilibrium.
- The frozen system cannot satisfy the explicit one-step state-feedback
  objective of sending every state to `true`.
- Rational reachability does not produce authorization: under the predicate
  withholding every word, no `AuthorizedPlan` exists.

These results distinguish temporal execution from controllability, a stated
equilibrium property, feedback achievement, and synthesis authority.

## Missing interfaces and scope

This increment does not define continuous time, topology, norms, stability in
the Lyapunov sense, admissible control constraints, disturbances, outputs,
series interconnection, feedback composition, costs, robustness, or a
controller compiler. Each requires separately fixed source conventions.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/DiscreteControlExecution.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

Both commands were executed successfully. The final targeted run exited zero
without output or warnings, and the project build completed with 8798 jobs.
The first targeted run exposed proof-shape defects in the rational-step
unfolding and frozen-run induction; both were repaired without weakening any
statement. No placeholder or assumed active-conjecture conclusion remains.
