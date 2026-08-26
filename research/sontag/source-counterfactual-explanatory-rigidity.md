# Source-counterfactual explanatory rigidity

## Pressure and bounded conjecture

The operator objected that the replay-composition result was settling for an
explanatory minimum and asked for a harder Deutsch-style attack. The pressure
is non-evidential. Its weakest consequential conjecture is:

> Replay preservation on one actual source orbit does not identify a repair
> mechanism. A satisfactory explanation must survive an independently
> admitted family of source counterfactuals, and the mechanism must transform
> naturally with that family.

The falsifier is uniqueness from actual-orbit replay alone.

## Rival mechanisms

The source bit is `s` and the realization bit is `y`. Consider:

```text
relational corrector: y := s
lookup rival:         y := 1
```

On the actual case `s=1`, both produce the correct realization. Both can be
made invariant under an arbitrary constant replay predicate. Neither actual
fit nor freely chosen invariance explains why the relational mechanism is the
right one.

Admit the source substitution that flips both source and its correctly
transported realization. The relational corrector commutes with this
substitution. The lookup rival does not. Equivalently, testing replay over both
source values selects `y:=s` uniquely among all four Boolean mechanisms.

## Deutsch-style disposition

The harder-to-vary content is not the sentence “replay is preserved.” Its
terms can be varied until any mechanism passes. The content is the relational
dependency of realization on source, exposed by counterfactual transformations
that were fixed independently of the rival mechanisms.

This changes the Marici candidate. A protected obligation cannot be merely a
predicate attached to one packet. It needs:

1. a source family or source-variation category;
2. transport of obligations along admitted source variations;
3. naturality of the claimed repair dynamics under that transport;
4. enough interventions to separate rival generative mechanisms.

Authority still matters because it determines which source variations are
admitted. But authority cannot manufacture explanatory rigidity by choosing
the variation family after seeing the rival.

## What remains open

The Boolean test is a finite-cutoff theorem. It does not prove that naturality
is sufficient for explanation generally: multiple natural mechanisms can
survive a weak intervention category. The next hostile question is whether the
admitted source variations are jointly faithful on mechanisms, or whether a
new rival survives every currently available counterfactual.

## Verification

```text
python research/sontag/checkers/source_counterfactual_explanatory_rigidity.py
```
