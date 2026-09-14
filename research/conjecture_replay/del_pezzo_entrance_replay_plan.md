# Del Pezzo entrance conjecture-space replay

## Frozen entrance

The replay origin is the first passed reconstruction of the global surface

\[
S:W^2=G(a,b,h)\subset\mathbf P(1,1,1,2),
\]

recorded by `research/voevodsky/results/global_del_pezzo_double_cover.json`.
The historical cutoff is the modification time of that result.  The explanatory theorem written immediately afterward is admitted only as a restatement of the result.  Later artifacts are hidden from policy construction and used solely as holdout observations.

At the cutoff the established boundary data are:

- the infinity quartic is a section of a global degree-two del Pezzo surface;
- `r_a`, `r_b`, and Geiser are global involutions;
- `r_a` has E7 eigenspace ranks `(3,4)`;
- the source support plane still lacks a common global marking;
- the explicit next target is to identify the invariant rank-three E7 lattice and locate `span(e6,v_alg)`.

## Ten-iteration execution plan

1. Freeze and machine-check the entrance snapshot and holdout boundary.
2. Reconstruct the admissible conjecture inventory using only pre-cutoff evidence and the entrance result.
3. Type each conjecture by four possible resolution relations `++,+-,-+,--` and explicit guards.
4. Reconstruct the actual post-entrance observation sequence without feeding it into the policy.
5. Define realization-cost proxies from checker/runtime/artifact complexity and report sensitivity.
6. Define probability models: uninformative, empirical leave-one-out, and interval/robust.
7. Build the guarded provenance quiver and enumerate compatible resolution policies.
8. Compute optimistic, expected, minimax, and Pareto policies at the frozen entrance.
9. Replay holdout observations, measuring rank, regret, information gain, and calibration.
10. Audit hindsight leakage, publish the reproducible report, and state what the machinery predicted.

## Non-leakage rule

A conjecture is historically admissible only when its statement is derivable from a pre-cutoff artifact or from an explicit open target in the entrance result. Later filenames, formulas, and outcomes may appear only in the holdout table. Policy parameters inferred from the holdout must be clearly marked retrospective and evaluated by leave-one-out or sensitivity analysis.
