# Replay preservation under composition

## Bounded question

When do two individually replay-preserving generative extensions compose? Is
extra coherence data required?

## Smallest hostile witness

Let a replay predicate `r` classify whether an inherited source obligation is
satisfied. At base packet `0`, extensions `E` and `F` are certified only by

```text
r(E(0)) = r(0),    r(F(0)) = r(0).
```

An exhaustive search proves that one- and two-state systems admit no
interference witness. Three states suffice. The checker finds maps with

```text
r(E(0)) = r(0),
r(F(0)) = r(0),
r(F(E(0))) != r(0).
```

Thus two extensions can each pass when tested alone from the original packet
while their composite destroys the inherited obligation. The second extension
was never certified on the intermediate packet reached by the first.

## Exact composition criterion

If replay preservation is a global typed condition

```text
r o E = r,    r o F = r,
```

then it composes immediately:

```text
r o F o E = r o E = r.
```

The checker exhaustively verifies this for every Boolean replay predicate and
every pair of endomaps on three states.

For partial or source-local certificates, the weakest cross-condition is not
an arbitrary higher cell. It is coverage of the reachable intermediate:

```text
F preserves replay on image(E | admitted source packets).
```

In a richer Marici object this coverage may itself require a transported
obligation witness, especially when `E` changes the representation in which
replay is stated. But the finite attack does not justify declaring independent
coherence data when globally typed replay morphisms are already available.

## Disposition

Repairability is compositional as a morphism law. It fails to compose when it
is recorded merely as a pointwise test result. The candidate missing Marici
piece is therefore typed certificate scope--domain, reachable image, and
transport of the protected obligation--rather than a free-standing coherence
primitive.

This is a finite-cutoff theorem and counterexample. It does not establish the
correct replay object for stochastic, quantum, or adaptive Marici carriers.

## Verification

```text
python research/sontag/checkers/replay_preservation_composition.py
```
