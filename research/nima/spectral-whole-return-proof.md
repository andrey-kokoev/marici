# Whole-Tick return extension of the checked spectral local core

## Test scope

Use exactly the standard-complex local witness of `uniform-local-core-proof.md`: `H_j=pi(I-P_j)/2`, `U_j(t)=exp(-it H_j)`. No new generator or per-Tick analytic profile is chosen.

The return interpretation is the external metric whole-record interpretation described in `contracts/spectral-whole-return-test.v1.json`. It is not a Cubical-pointwise state map. This matches the previously proposed whole-section metric route: whole records, ordered traversal, exact endpoints, continuity, local generator laws, reconstruction and schedule-swap coherence. We additionally check faithfulness at fixed source.

## Construct the return, rather than assume it

For source s, put `v=P_R P_L e_s`. For a schedule r, let `(a,b)` be its two operations in reversed order. Define on the real interval `[0,2]`:

- `gamma_r,s(t)=U_a(t)v` for `0<=t<=1`;
- `gamma_r,s(t)=U_b(t-1)P_a v` for `1<=t<=2`.

The first expression at the seam is `U_a(1)v=P_a v`; the second is `U_b(0)P_a v=P_a v`. Hence the definition is well-defined and continuous by the finite closed-cover pasting lemma. Each piece uses the already-proved continuous unitary local dynamics.

The start is v. The finish is `P_b P_a P_R P_L e_s=e_s`, because `(a,b)` lists the two commuting involutions. Every state on either piece has norm one.

On the interiors of the two pieces, `i gamma'=H_a gamma` and `i gamma'=H_b gamma`, respectively. Both generators preserve the appropriate factor algebras as proved for the local core. No differentiability at the switching time is claimed. The convention is positive continuation in reversed operation order, not the inverse-phase time reversal of a forward trajectory.

## Interpretation of the whole retained record

For a Tick t at fixed source s with ordered tags `(r,q)`, define `F_s(t)=(gamma_r,s,gamma_q,s)`.

The source theorem `TickRetainedStructure.AtSource.tick-equiv-tags` identifies the **entire** retained Bool Tick with its ordered tag pair, including the dependent return-section field and its witnesses. In particular, `rebuild-tags` and `observation-factors` are full-record equalities, not extraction of an unproved summary.

Consequently:

- `F_s(t)=F_s(rebuild(tags(t)))` by the reconstruction equality;
- equal tag pairs give equal pairs of paths;
- exchanging the two tags exchanges the two interpreted paths.

These coherence laws alone would admit arbitrary adapters, as the audit showed. Here the paths are not arbitrary: the formula above is fixed by the same source-linearized spectral operators, the native double-flip target, and the reversed native schedule.

There is also a converse distinguishing the records. At time 1, the two possible return schedules have distinct seam states: reversing left-first applies R first and gives `P_L e_s`, whereas reversing right-first applies L first and gives `P_R e_s`. These are distinct delta basis vectors for every Bool pair s. Thus equality of paths implies equality of schedule tags. Equality of pairs of paths implies equality of both tags and hence, by `tags-injective`, equality of whole Ticks. This establishes fixed-source faithfulness, not merely matching endpoints.

Factorwise relabeling covariance follows from the local-core covariance. Factor exchange conjugates L to R and R to L, exchanges source coordinates and schedule names, and therefore carries each piece of this path to the corresponding piece for the exchanged source.

## Result and composition

For this specific witness f, the declared external-path return predicate `R_ext(f)` holds in standard complex semantics. Together with the already-proved `L(f)`, this supplies `exists f (L(f) and R_ext(f))` by the same-witness introduction rule checked in `TickLiftOutcomeSplit.extend-local-witness`.

This closes the **clarified standard-C4 external-path existence claim**. It does not close a stronger reading in which the dependent Cubical section must be decoded pointwise into separated states. That reading remains subject to the earlier no-go theorem. It also does not discharge the separate operational completion implementation, ScheduledNormBound, source uniqueness, or a ten-topic observable law.

## Evidence standard

The all-time and whole-record argument is the mathematical proof above, using the existing Agda source-classification theorem. `check_spectral_whole_return.py` supplies exact rational-complex checks for all four source labels, both return orders, all ordered tag pairs, seam/endpoints, unitary sample states, factor exchange, and the distinct seam-state witness of faithfulness. Samples do not prove continuity or all-time unitarity; those use the analytic argument and the previous local-core theorem.
