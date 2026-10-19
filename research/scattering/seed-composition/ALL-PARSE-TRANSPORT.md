# All-parse history transport closes, but its fixed primitive clock is not the macro clock

**Iteration 3 of the requested ten-turn work-net run.**

**Strength:** exact retained-prefix transport identities and a finite readout-spectrum obstruction. Not a physical-clock identification or a no-go for every retained-history representation.

[Previous ambiguity result](PARSE-AMBIGUITY.md) · [Checker](check_all_parse_transport.py) · [Receipt](results/all-parse-transport.v1.json)

## 1. Fresh question and carrier

The last turn constructed all compatible macro parses and found 2^n of them on the repeated primitive return (AB,BC,CB,BA)^n. It did not assign a selected parse or a probability distribution.

Now retain **partial** composites as well as completed macro histories, so every step consumes exactly one primitive arrow. A macro choice is made when its first primitive is consumed, not in anticipation of the next unread arrow. This avoids counting an extra future choice at the end of a complete input word.

The source domain is the primitive-prefix language admitted by the supplied pair dictionary. It is not the unrestricted glued graph: branches excluded by that dictionary are not silently claimed to have become native dynamics.

For each pair the lazy parser has seven boundary/pending states. Exact labelled transition comparison merges one pair of predictively equivalent states, giving six prefix contexts. The primitive label and completion marker remain in the transition records, and full histories remain outside the finite endpoint summary.

## 2. Positive result: the equal-copy image is transport-compatible

At primitive depth n let X_n have one coordinate for each admitted primitive prefix, and Y_n one coordinate for every compatible tagged parse prefix. Define

    R_n : X_n -> Y_n

by copying a source-word coefficient to all of its parses. Let E_source extend admitted primitive prefixes and E_parse extend tagged parses. The exact square is

    R_(n+1) E_source = E_parse R_n.

Every tagged child has a unique tagged predecessor; erasing its tags gives the same primitive-prefix predecessor. Hence both sides copy the same coefficient. This proves the identity at every finite depth. The checker additionally builds all matrices and verifies the square through eight primitive steps in both pairs.

The map D_n that averages within each retained source-word fiber satisfies

    D_n R_n = I.

Thus the equal-copy encoding is faithful and has an exact decoder. An arbitrary independent assignment to parse records is a larger carrier, not automatically source data in this image. Neither this identity nor the decoder establishes a physical isometry or a probability law.

## 3. Sum and mean are different readouts

The sum of equal-copy parse coefficients is the source coefficient multiplied by the parse-fiber cardinality. On n repeated four-step loops, that factor is 2^n.

The mean restores one coefficient per source word. It must be taken **within each retained source-word fiber before endpoint aggregation**. A blind average of all records ending at a vertex is not substituted for this operation.

For the six predictive prefix contexts in each pair, derive two matrices:

- W: aggregate all parser transitions, retaining their multiplicities;
- G: count each admitted primitive continuation once, after source-word multiplicity has been removed.

The checker verifies that each primitive label has at most one destination from any G-context. Therefore an erased primitive word determines a unique G-context: G counts source words rather than additional nondeterministic parse choices.

Each matrix has seven nonzero arcs. In W, one arc has weight two and the other six have weight one. In G all seven have weight one. The doubled arc is the ambiguous first primitive: AB in the first pair and CB in the second. Exact labelled-loop products give W multiplier 2^n and G multiplier one on the same repeated primitive word.

This difference comes from parsing. It is not an emitted-particle count, a physical branching ratio, or a derived normalization prescription. Unchanged-copy source extension can itself branch; no unitarity of either counting update is asserted.

## 4. The reference oscillatory mode does not survive as a uniform primitive-step mode of these readouts

For each pair and for both derived matrices, exact rational arithmetic gives

    rank(G^2+G+I)=6,
    rank(W^2+W+I)=6.

Thus neither finite endpoint readout has a nonzero vector with eigenvalue omega or its conjugate, where omega^2+omega+1=0. In particular, neither can contain a nonzero embedded copy of the reference two-dimensional oscillatory plane with its existing step T satisfying T^2+T+I=0.

The synchronized macro-step identity established earlier is **not retracted**. It advances one completed displayed edge; this turn advances one primitive arrow and retains unfinished displayed edges. Those clocks differ because macro-edges have different primitive lengths.

No phase omega^k was assigned to an individual retained path merely because an aggregate macro operator has an omega eigenvector. Retained unchanged-copy extension and an aggregate eigenvalue are different constructions. The obstruction here is computed from the actual primitive-step readout matrices.

Nor is this a claim that every infinite history-space realization lacks the desired mode. The tested recipients are precisely the finite six-context sum and source-word-mean endpoint readouts under a common primitive-step clock.

## 5. Updated gate

The all-parse relation removes the need to choose a parse merely to preserve source coefficients: its equal-copy transport closes. It does not turn macro-event period three into a primitive or physical period three.

The next executable test is to retain the primitive-step generating variable in the boundary return operator, rather than evaluate it away. The earlier segmented construction already has the clock-aware form

    F(z)=z A + z^2 B D,

with F(1)=K. Test whether a boundary transport relation for the reference plane exists with this grading intact, and identify exactly which weighting or clock change it would require. Do not infer physical time from either counter.

The dictionary, correlated preparation, metric, two-face transport and independent physical outputs remain separate obligations. Existing work-net contracts, retained residuals and formal outcomes are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_all_parse_transport.py
python research/scattering/seed-composition/check_all_parse_transport.py --check
python research/scattering/seed-composition/check_parse_ambiguity.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker freshly recomputes the preceding parse/controller construction, validates labelled quotient squares, retained transport, fiber decoders and exact full-rank polynomial tests. It writes only its own receipt; `--check` compares read-only. Source-owner physical suites and formal proof admission are not claimed.
