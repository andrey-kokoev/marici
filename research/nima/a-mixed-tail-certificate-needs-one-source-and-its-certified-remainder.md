# A mixed tail certificate needs one source and its certified remainder

## Result

An explicit mixed construction now couples the actual finite source/evidence protocol to Grothendieck's rational dominated-tail controls. It produces two false positive certificates when different interface obligations are erased, and a compatible, authorized positive control when all obligations are retained.

This is a new declared mathematical control coupling. It is **not** a discovered calibration law for the actual prime tail or the signed analytical task.

The target is the strict universal bound

    F(x,y) = -sum_{n>=1} 2^-n (x_n+y_n) > -31/32

on the source-authorized current tail carrier. A finite primal point alone cannot prove this universal claim; a dual lower bound plus the suffix estimate can.

## 1. A genuine joint source model, not juxtaposed certificates

The existing source origin is b in {0,1}. It selects the two normalized tail carriers:

| Source origin | Channel 0 | Channel 1 |
|---|---|---|
| 0 | even support | adjacent capacity |
| 1 | adjacent capacity | even support |

Even support means zero mass on odd slots and unit caps elsewhere. Adjacent capacity retains all slots with unit caps and the interval bound `ceil((j-i)/2)`. Both are exactly the carriers of the independently replayed rational LP packets.

The enriched mathematical source consists of an admitted base protocol state together with a pair of tails in the corresponding carriers. Initialization admits any such pair. Its transitions are explicit:

- an accepted source(2,m) halves **both actual tails**;
- all other accepted or rejected base actions leave them unchanged;
- the base protocol itself is unmodified.

The scale is one before that event and one half afterwards. Every atom and interval cap scales with it. Thus the improved calibration is not silently imposed on an unchanged tail: an admitted constructor maps old admitted tails to new admitted tails. Scaling preserves support and all the linear inequalities. Every base transition preserves the origin-dependent choice of carriers.

A truthful accepted origin audit supplies the calibration witness for a channel. Each finite proof packet binds its channel, origin, current cut, scale, run context and new task hash. The numerical task has its own identity; the old protocol's issue(0/1) is not relabeled as a tail certificate.

A separate `publish-tail-bound` constructor requires a delivered source-origin receipt at a post-cut state, coherent calibration witnesses, and a strict certified combined lower bound. Truthful audited outcomes and source-authoritative current ports remain assumptions, not properties supplied by hashes.

## 2. Freeze before the mixed test

The fixed cutoff is m=4. Each channel carries four primal and fourteen dual entries. Numerators and denominators are limited to 32 bits. The runtime also retains the fixed 70-row behavioral kernel, source bindings, current local-view tuple and at most a two-bit origin-possibility mask. It does not consult concrete history words during assembly.

For each normalized channel the certified suffix is

    sum_{n>4} 2^-n x_n <= 1/16.

At scale s it is s/16. This follows from the global atom cap, not finite sampling.

The finite LPs and suffixes give:

| Carrier | Finite optimum | Full-tail lower bound |
|---|---:|---:|
| Even support | -5/16 | -3/8 |
| Adjacent capacity | -5/8 | -11/16 |

The constructor checks primal feasibility, dual feasibility and matching finite objectives with exact rational arithmetic. It then applies the independently justified suffix bound.

## 3. Attack one: independently valid bounds from incompatible origins

Take the channel-zero even-support packet from origin zero and the channel-one even-support packet from origin one. Each packet has a local source realization and a valid exact numerical certificate.

Adding their displayed full-tail lower bounds gives

    -3/8 - 3/8 = -3/4 > -31/32.

A scalar-only assembler would certify success.

But no common source origin authorizes both calibrations. The joint constructor rejects the combination as `INCOMPATIBLE_SOURCE`.

This is not merely a typing objection. For either actual origin, the admitted zero-extended m=8 primal pair has objective

    -255/256 < -31/32.

It is a concrete full-tail feasible counterexample to the claimed universal bound. Zero extension is admitted by the support restrictions and right-endpoint-monotone capacities.

There can still be particular tails that happen to satisfy both stronger even-support restrictions. Their existence does not authorize replacing the entire source carrier by that smaller subset. The missing common witness concerns the source's **guaranteed calibration constraints**, not whether some benign primal pair exists.

## 4. Attack two: coherent origins but an omitted remainder

Use the correct even-support and adjacent-capacity packets from one origin at unit scale. Their finite optima sum to

    -5/16 - 5/8 = -15/16 > -31/32.

Omitting the suffix would again yield a false certificate. The same admitted m=8 pair refutes it.

With both certified remainders included, the lower bound is instead

    -15/16 - 1/16 - 1/16 = -17/16.

The constructor correctly reports `NO_STRICT_CERTIFICATE`. Coherent provenance alone does not repair an invalid finite-to-infinite numerical inference.

## 5. Compatible, authorized positive control

Execute the admitted acquisition/delivery workflow and the source operation that halves both tails. Use both channel packets from the same origin at the resulting cut. Their combined certified lower bound is

    (1/2)(-17/16) = -17/32 > -31/32.

The constructor accepts for either origin. A delivered source receipt is required; a numerically adequate packet without that authorization would still be rejected.

The control therefore checks numerical validity, common-source compatibility and execution authority together. It is not a reinterpretation of a backward relation or of the original issue label.

## 6. Ownership transport and orientation

The numerical mode depends on origin and the scale on the source cut. The checked source-coordinate comparison maps preserve these values and the delivered receipt.

The mixed constructor is evaluated on all 70 states of each of the 52 independently generated ownership decompositions. All 2,704 comparison maps preserve its results, giving 189,280 mixed-verdict transport checks.

All 1,260 base transitions are checked against the enriched tail-update rule. Exactly 64 transition entries halve the tails; all remaining entries preserve the scale. This binds the infinite-carrier constructor to the actual finite operation guards.

There is also a direction control: a source(2,0) edge goes from the unscaled cut to the half-scale cut, so its transpose admits a predecessor query. At the resulting state the same forward label is rejected as already used. Backward compatibility does not authorize inverse scaling or permit a half-scale certificate to be rebound to an unscaled cut.

## 7. Verification and limits

Fresh headless checks replay the owning rational tail verifier, the relational/live-witness verifier and the decomposition constructor. The new independent mixed verifier imports neither the mixed producer nor an LP solver. It checks the exact numerical packets, source realizations and reachable publishing cuts, explicit finite counterexamples, scale preservation, regrouping, and the reverse-action control.

Both mixed checks pass:

    python research/nima/checkers/check_mixed_source_tail_certificate.py
    python research/nima/checkers/verify_mixed_source_tail_certificate.py

Wrong task context, wrong cut, wrong carrier mode, missing suffix and a corrupted dual are also rejected.

Artifacts:

- `research/nima/results/mixed-source-tail-certificate-contract.json`
- `research/nima/results/mixed-source-tail-certificate-packet.json`
- `research/nima/results/mixed-source-tail-certificate.json`
- `research/nima/results/mixed-source-tail-certificate-verification.json`

The result corroborates the mixed DPC for this explicitly declared control. It does not establish a universally minimal interface, authenticate received records, implement delayed communication, or prove a source-history/calibration correspondence for the actual analytical task.

The structural lesson is sharper than separate certificate validity: the numerical inference must be valid for the carrier authorized by the **same coherent source execution**, including its current scale and objective remainder. Even then, mathematical truth and authority to publish remain separate obligations.
