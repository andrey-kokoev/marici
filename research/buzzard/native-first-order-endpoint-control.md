# Native first-order endpoint control

Owner: `marici.Buzzard`

Source locator: `Correction: the native first-order channel controls the
endpoint` in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

`FirstOrderEnergyCertificate` records real scalars `a`, derivative square,
bulk square, endpoint square, and total energy. It requires `a > 0`,
nonnegativity of all square terms, and the exact identity

`energy = derivativeSq + a^2 * bulkSq + a * endpointSq`.

Lean proves:

- `a * endpointSq ≤ energy`;
- `endpointSq ≤ energy / a` at each fixed positive `a`;
- uniformly on any region `a ≥ delta > 0`,
  `endpointSq ≤ energy / delta`.

This is the exact algebraic consequence of Strominger's native first-order
identity. The identity is certificate data rather than an assumed conclusion:
the formalization does not derive integration by parts or the gauge removal.

## Boundary hostile family

`boundaryCertificate a` sets both interior terms to zero, endpoint square to
one, and energy to `a`. For every proposed finite nonnegative constant `K`,
Lean chooses `a = 1/(K+1)` and proves

`K * energy < endpointSq`.

Thus pointwise control for every `a > 0` does not imply a uniform endpoint
constant as `a` approaches zero. A positive regional lower bound is an
independent premise.

## Relation to the previous countermodel

The generic nonclosability witness remains valid against claims that target
transport repairs an arbitrary source graph defect. This native certificate
supplies the missing source control for the actual theta endpoint at fixed
strip parameter. The two theorems are complementary rather than conflicting.

## Missing analytic interfaces

A faithful sector theorem still needs:

- the function space and boundary trace type;
- the oriented operator `A_s` and its dense domain;
- the gauge transformation removing the imaginary part;
- integration by parts with boundary behavior;
- identification of all scalar fields with squared norms;
- the relation `a = 1 - Re(s)` and the admitted strip;
- completion/extension from the estimate to the endpoint operator.

The abstraction generalized the nonnegative energy consequence while keeping
the source analytic identity outside the shared ontology.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/NativeEndpointControl.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/NativeEndpointControl.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/native-first-order-endpoint-control.md`
