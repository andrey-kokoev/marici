# Paired-tower claim poset

## Question

How should the `2(3+2+1)+1` apparatus report its result without promoting a
weaker optical signature into a stronger physical conclusion?

## Combined gate

The instrument evaluates five independent facts:

1. whether both local marginals are flat;
2. whether a coherent outer sewing operation produces a joint fringe;
3. whether the phase environment is independent or correlated;
4. whether source coherence crosses the ideal Bell threshold;
5. whether full herald-normalized efficiency and the Bell causal contract
   support an observed violation.

It then reports only the strongest admitted claim.

## Exact fixtures

The checker freezes five cases:

- coherence `3/5`, efficiency `19/20`: relational coherence, Bell-local;
- coherence `4/5`, efficiency `9/10`: ideal Bell eligibility but
  detector-incomplete;
- coherence `4/5`, efficiency `19/20`: detector-complete Bell nonlocality;
- perfectly correlated phase environment: relational environment channel,
  not a Bell certificate;
- classical comparison with no coherent sewing: no relational-coherence
  claim.

## Logical structure

Detector-complete Bell nonlocality implies a relational port in this
instrument. The converses fail:

- relational coherence does not imply Bell nonlocality;
- ideal Bell eligibility does not imply an observed Bell violation;
- a joint fringe does not exclude a correlated environment;
- scalar record correlation does not imply coherent sewing.

The result space is therefore a typed partially ordered set, not a single
visibility score. The coherent-constructor branch is ordered from relational
coherence through Bell eligibility to detector-complete Bell nonlocality. A
correlated environment channel is a separate branch until another intervention
distinguishes shared noise from a source-authorized coherent port.

## Deutschian explanation

Each level states a different fact about possible transformations. A
relational environment channel says the phase relation survives a shared
transformation. Relational coherence says an admitted coherent sewing
constructor can expose it. Bell eligibility says the source state supports an
incompatible four-setting family. Detector-complete Bell nonlocality says the
entire realized apparatus defeats the Bell-local bound without deleting
outcomes.

## Disposition

This combined checker closes the principal claim-promotion routes found in the
session. It does not compress source, constructor, environment, causal layout,
and detector completion into one fitted visibility.

## Verification

Run:

```text
python research/aspect/checkers/check_paired_tower_claim_ladder.py
```
