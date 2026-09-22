# Adelic coherence needs a global realizability gate

## Correction

The earlier version tested positivity rather than pairwise rational realizability. Its real report |r|=1 was already incompatible with its 2-adic report. That argument and its checker are superseded here. We do not equate pairwise existential admission with transition or cycle coherence.

## Conjecture and exact falsification

Conjecture: for local constraints on a rational source under one common height budget, nonempty pairwise source fibers imply a nonempty joint source fiber.

Fix nonzero r=a/b in reduced form with b>0 and H(r)=max(|a|,b)<=6. Admit three local constraints:

- infinity: 1/3 <= r <= 1/2;
- place 2: |r|_2=2;
- place 3: |r|_3=3.

Other places are unrestricted subject to the height budget. Each pair has an independently checked rational witness under that same budget:

| Pair | Witness | Height |
| --- | --- | --- |
| infinity, 2 | 1/2 | 2 |
| infinity, 3 | 1/3 | 3 |
| 2, 3 | 1/6 | 6 |

Yet no rational satisfies all three constraints. The finite-place constraints force the reduced denominator to be divisible by 6. The height budget forces b=6. The real interval then forces 2<=a<=3, but neither integer is coprime to 6. Contradiction.

This is a bounded-height obstruction, not an unrestricted local-to-global failure. The previously stated witness 5/12 was incorrect: its 2-adic norm is 4, not 2.

## Exact joint-admission threshold

Joint realizability holds if and only if the height budget N is at least 30.

In reduced form the finite-place constraints require v_2(b)=v_3(b)=1, so b=6k with gcd(k,6)=1. Below 30 the only possible denominator is 6, already excluded above. At denominator 30, the interval requires 10<=a<=15; exactly 11 and 13 are coprime to 30. Thus 11/30 and 13/30 are joint witnesses of height 30, and no smaller-height witness exists.

The guarantee is a common rational witness satisfying every local constraint and the height bound. It is not obtained by identifying the different pairwise witnesses. This exact threshold is arithmetic complexity, not elapsed time.

## Verification

The checker exhaustively enumerates all 46 nonzero reduced rational sources of height at most 6, checks the pair witnesses, and verifies an empty triple intersection. An independent enumeration through height 30 certifies that the joint fiber is exactly {11/30,13/30}, hence empty below 30. It rejects the old 5/12 witness and checks the full product formula and adelic height identity for every enumerated candidate, using all primes up to the relevant height bound; larger primes necessarily contribute one.

    python research/voevodsky/checkers/check_adelic_coherence_global_obstruction.py

Artifact: `results/adelic-coherence-global-obstruction.json`.

## Consequences and boundaries

A shared height budget and pairwise rational witnesses do not supply a common rational witness. Pairwise witnesses can refer to different sources. Admission must retain and intersect joint source fibers rather than discard their correlations.

This does not refute a conjecture that already assumes a nonempty common source fiber. It establishes no necessity or dispensability of periodic tact-time. Transition maps, cycle identities, source provenance, physical realization and information-arrival deadlines remain separate obligations. The product formula is necessary but is not a sufficient diagonal-realizability test.
