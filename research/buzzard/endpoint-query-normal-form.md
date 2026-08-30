# Endpoint-query normal form and commutation gate

Owner: `marici.Buzzard`

Source locator: `Normal form for endpoint queries` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

`EndpointQueryNormalForm` contains a finite set of valuation constraints and a
rational Mellin parameter. Composition unions the constraint sets and adds the
parameters. Lean proves associativity, left and right identity, and
commutativity.

For an action of query normal forms on an arbitrary state type,
`RespectsEndpointQueryComposition` requires the action of a composite query to
equal functional composition of the two actions. Lean proves every such action
has commuting images.

This makes the hidden premise explicit: the union/addition normal form is valid
for sector constructors only after proving their represented actions commute.

## Hostile countermodel

On Boolean states, let `toggle` negate the state and let `erase` send every
state to false. Their two composition orders differ. Lean proves there is no
composition-preserving representation of the commutative endpoint-query normal
form that maps one declared query to `toggle` and another to `erase`.

Pairwise availability of two constructors therefore does not authorize a
commutative normal form. The commutation or simultaneous-diagonalization cell
is an independent premise.

## Boundary and missing interfaces

The constraint language here is `Finset Nat`, composition uses idempotent
union, and the Mellin parameter is rational. Strominger's sector statement
uses valuation predicates and a real Mellin parameter. A faithful upgrade
needs:

- the typed valuation-constraint language and its consistency rules;
- real parameter addition and character action;
- projector idempotence and intersection/union convention;
- simultaneous diagonalization or explicit pairwise commutation;
- proof that every source constructor word reduces to the normal form;
- uniqueness or a quotient relation for equivalent normal forms;
- execution-cost semantics, which do not follow from normalization.

The abstraction generalized the algebra of an admitted commutative normal form
and supplied a hostile rejection for noncommuting sectors. It does not force
all constructor algebras into this representation.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/EndpointQueryNormalForm.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/EndpointQueryNormalForm.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/endpoint-query-normal-form.md`
