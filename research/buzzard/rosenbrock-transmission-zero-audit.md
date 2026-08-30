# Rosenbrock transmission-zero audit

Sources:

- `research/nima/theta-scalar-zero-is-a-transmission-zero-not-an-observability-defect.md`
- `research/sontag/transmission-zero-factorization.md`

## Formal compiler

`MariciFormal/RosenbrockTransmissionZero.lean` defines a typed linear
discrete-time realization over an arbitrary field and modules:

```text
x⁺ = A x + B u
y  = C x + D u.
```

At parameter `λ`, its Rosenbrock operator maps `(x,u)` to
`(λx-Ax-Bu, Cx+Du)`. An invariant transmission zero is defined by a nonzero
kernel witness. Lean proves the expanded state/output equation compiler.
Selected output ports are explicit linear postcompositions; they are not
identified with the complete output family.

## Exact passive hostile

The rational one-state, one-input, two-output fixture uses

```text
A=3/5, B=-12/25, C=(4/5,0), D=(9/25,4/5).
```

Lean proves the exact storage identity, nonzero input and complete-output
state couplings, and the selected-first-port transmission-zero witness
`λ=5/3`, `x=-9/20`, `u=1`. At that witness the first output is zero while the
second output equals `4/5`.

Thus losslessness, elementary reachability/visibility witnesses, and a bright
complementary port do not imply selected-port zero-freeness or minimum phase.

## Missing RH interfaces

This is an exact finite control compiler and hostile countermodel. It does not
construct a theta state space, reachable/observable quotient, source-authorized
selected port, analytic continuation, stability domain adapter, or theorem
identifying a transfer determinant with completed zeta or xi. No RH conclusion
is assumed or proved.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/RosenbrockTransmissionZero.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

Both commands were executed successfully. The final targeted run exited zero
without output or warnings, and the project build completed with 8799 jobs.
Early elaboration exposed only proof-construction defects in product-valued
linearity and kernel-equation projection; those were repaired without changing
or weakening any theorem statement. No placeholder or active-conjecture
conclusion remains.
