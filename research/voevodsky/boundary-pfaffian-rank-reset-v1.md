# Boundary Pfaffian rank-reset skeleton

## Scope

`agda/BoundaryPfaffianRankReset.agda` formalizes the abstract finite turn

```text
primitive -> defect -> reconciliation -> typed residual
```

without asserting an analytic realization or an unrestricted iteration theorem.

## Formal objects

`Bicharged` records a state with incoming and outgoing boundary maps.

`RankResetSystem` records:

- primitive, defect, certificate, residual, and next-primitive types;
- defect exposure;
- reconciliation into certificate and residual;
- residual retyping;
- direct minimalization;
- a path equating direct minimalization with reconciliation followed by retyping;
- common incoming and outgoing port types;
- preservation of both ports under retyping.

`ContextualValidity` records admitted contexts and requires behavior preservation between a primitive presentation and its direct minimal form.

## Derived statements

`reconciledBehavior` proves that every admitted context gives the same observation after taking the longer route through defect exposure, reconciliation, and retyping.

`boundaryRetyping` combines incoming and outgoing preservation into one path of paired boundary values.

These are the formal counterparts of

```text
Min ~= Retype o Reconcile o Boundary
```

and

```text
behavior before compression = behavior after typed rank reset.
```

## Deliberate omissions

The module does not postulate:

- a specific Pfaffian implementation;
- finite Hankel rank;
- stabilization under an unbounded constructor alphabet;
- equality of distinct port types without a transport;
- a physical interpretation;
- automatic iteration of `NextPrimitive` as `Primitive`.

The last omission is important: self-recursion requires a separately supplied equivalence or indexed family connecting successive systems.

## Verification

Checked successfully with Agda 2.8.0.1 and Cubical 0.9:

```text
agda --transliterate \
  -i research/voevodsky/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/voevodsky/agda/BoundaryPfaffianRankReset.agda
```

The generated `.agdai` file is excluded by `research/voevodsky/agda/.gitignore`.
