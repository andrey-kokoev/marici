# Retaining the source history does not uniquely designate macro-events

**Iteration 2 of the requested ten-turn work-net run.**

**Strength:** exact parse correspondence, an unbounded ambiguity family and a same-source-tree witness. Not a no-go for choosing a deterministic policy, nor a physical information-cost or emission theorem.

[Previous memory result](CONTROLLER-MEMORY.md) · [Checker](check_parse_ambiguity.py) · [Receipt](results/parse-ambiguity.v1.json)

## 1. Fresh state and question

The preceding turn found sixteen predictive classes for the supplied segmented controller. Given pair and vertex, a local parse-state bit suffices as an encoding, but the current actuator profile cannot reconstruct it.

This turn asks whether the missing state can instead be recovered from the full primitive history, including an actual retained assembly tree. The answer is negative for unique recovery of every intended macro history. A relation of all possible parses is constructible without selecting one.

## 2. Construct all compatible parses

Use the candidate's supplied macro dictionary, its owner-labelled primitive words and its pair labels. The new parser considers every matching macro-word prefix, recursively retains every matching suffix, and returns the complete sequence of macro IDs. Each result retains its primitive expansion and completion-marker sequence.

This is a finite combinatorial correspondence relative to the supplied dictionary. It does not assign a physical amplitude to a parse or declare a macro boundary to be an actual event. Unmatched words have no complete parse; this does not erase the original source record.

The checker rejects unsewn primitive words, distinguishes an unfinished composite from a complete parse, and excludes a foreign-pair branch. Empty input has the mathematical empty parse for recursion; no empty supplied family is passed to the source ledger, whose API deliberately excludes that case.

## 3. An exact exponential family

Consider the primitive return word

    w = (AB,BC,CB,BA),

starting and ending at A. In the first output it has two macro parses:

    AB ; BC ; CA,     with CA=(CB,BA),
    AC ; CA,          with AC=(AB,BC).

Their primitive words, owner labels, initial vertex, final vertex and output pair are identical. Their primitive-step completion markers differ:

    (1,1,0,1) versus (0,1,0,1).

In the second output the analogous alternatives are

    AC ; CB ; BA,
    AC ; CA.

For w repeated n times, each return block permits this choice independently, and returns to A before the next block. The other two-edge portion in each pair has a forced parse. No macro-word crosses these return-block boundaries. Hence, for either fixed pair,

    number of parses = 2^n,
    macro-count generating polynomial = (z^2+z^3)^n.

There are exactly binomial(n,k) parses with 2n+k macro-events. The checker enumerates both pairs through n=8 and verifies these formulas, while the independent block factorization proves the all-n statement.

Even supplying the total macro-event count is insufficient in general: at n=2 there are two different completion histories with five macro-events. The two extremes, shortest and longest macro parses, have 2n and 3n events on the same primitive input.

Therefore more primitive lookahead cannot recover an arbitrary original parse: the alternative interpretations already agree on the complete repeated primitive word. A deterministic policy can still select one. The obstruction is to calling that selection a uniquely recovered source datum.

## 4. One actual source assembly tree admits both frontiers

The ambiguity is not solely caused by forgetting the source's parent records. Using the existing `RetainedSuccessorLedger`, construct the registered tree

    ((AB * BC) * (CB * BA))

with unit coefficient leaves. Its operands and parent-slot bindings are retained. The single existing tree admits the two first-output macro frontiers

    [AB, BC, (CB*BA)]
    [(AB*BC), (CB*BA)].

Both frontiers consist of actual nodes of that same tree. Their concatenation gives the same retained primitive word and coefficient. The first regards the AB*BC node as assembly of two macro-events; the second designates it as the single macro AC.

For the second output, cutting above or below the CB*BA node gives the corresponding ambiguity. No distinct source execution IDs or different assembly trees are equated in this test: the same source tree is kept, and the alternative **macro-frontier designation** is attached separately.

The source tree supplies possible cuts, not a rule selecting which cuts are the events of this candidate controller. Explicit operation-type markers, an execution policy or another source witness could supply that rule, but it is additional data not present in the tested unmarked tree.

## 5. Predictive memory and accumulated history are different resources

The previous local parse bit describes a current predictive state. Retaining which of the 2^n parse histories was intended across n loops requires n binary designations in this particular family. A fixed-size predictive state is not a reconstruction of the accumulated choice history.

This is a cardinality statement, not Shannon entropy without an ensemble, a thermodynamic bound or a physical qubit count. The output-pair tag is already fixed in the 2^n calculation.

Keeping **all** parses avoids an arbitrary choice but requires care with coefficients. A bookkeeping map that copies a single coefficient c into all compatible parse records is injective onto its equal-copy image, with mean-value decoder. Its unweighted squared counting norm is

    2^n |c|^2,

not |c|^2. Independently modifying one parse leaves that equal-copy image, which the checker detects. No physical normalization, probability assignment or coherent sum over parses is supplied by this construction.

The source tree and all designated histories remain retained. Neither parse count nor its growth is a count of emitted particles.

## 6. Refined next test

The broad work-net frontier remains open. The next nonredundant test is to operate on the **whole retained parse relation**, rather than silently select a frontier:

1. construct its continuation and source-forgetting maps;
2. test whether equal-copy source coefficients remain in a transport-compatible image;
3. check whether the synchronized reference mode survives there;
4. distinguish sum, average, conditional selection and normalized preparation before any scalar readout.

If that relation does not support the desired transport, identify the precise additional weighting or selection operation and its source obligation. Do not interpret a newly chosen policy as a derived event clock.

## Reproduce

```sh
python research/scattering/seed-composition/check_parse_ambiguity.py
python research/scattering/seed-composition/check_parse_ambiguity.py --check
python research/scattering/seed-composition/check_controller_memory.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker freshly recomputes the preceding controller audit, uses the actual path ledger for the same-tree witness, verifies the parse census and negative controls, and hashes its dependencies. It writes only its own receipt; `--check` is read-only. Existing work-net contracts and formal outcomes are unchanged.
