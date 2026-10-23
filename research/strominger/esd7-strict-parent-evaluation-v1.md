# Conditional evaluation on the source strict joint-graph diagram

## Result

The [edgewise refinement](esd7-simplicial-refinement-v1.md) is now evaluated symbolically on the source's reversible parent chart diagram, including F006 and all1807 cells.

**21 checks pass**, covering64,736 restriction adjacencies and5,421 retained readout squares. This is an exact conditional consequence of the declared chart identities, not newly generated numerical operators or an independent proof of the source analytic theorems.

## Source diagram and domain

The [consolidated source](../voevodsky/consolidated-four-presentation-analytic-pyramid-position.md) defines

    C_ij = S_j R_i,
    R_i S_i = I_D,
    S_i R_i = I_on_S_i(D).

Use one common admitted observer core D restricted to the chart and readout domains. The chart carriers are correlated essential images of this same D. Chart4 is the full response `(B,Q,A,C)`, with inverse extracting the all-seam coordinate B—not the scalar finite-part trace.

The [profile](contracts/esd7-strict-parent-profile.v1.json) freezes these assumptions and declares **no extension to independently completed bulk spaces**. This matters: the [joint-graph source](../voevodsky/the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md) explicitly warns that endpoint transport need not be a bounded row on the independently completed regular bulk.

The checker verifies a symbolic corollary of those identities. It does not prove analytic inverses, continuity, common-domain density or the parent source programme afresh.

## Evaluation rather than invented matrices

The evaluator type-checks every operator application. Programs are stored in execution order; for example `[R1,S4]` denotes the operator `S4 R1`.

Every parent path reduces through the declared image identities. Both triangular and tetrahedral reduction routes agree in this **strict chart diagram**. Every fine-face restriction is checked internally: each newly adjacent pair of retained parent occurrences agrees with the original intervening subpath. Checking only the two outer endpoints would be weaker.

Repeated parent positions and complete execution programs remain in the result even when the reduced operator is an identity. Normal forms do not replace occurrence histories.

## F006

F006 retains21 parent positions:

    (1,2,3,4,4,...,4),

with18 occurrences of chart4. Its nonidentity route is

    C12; C23; C34,

which reduces to `C14 = S4 R1`. The17 repeated-chart identity steps are omitted only from the executable operator program, not from the retained occurrence list.

This evaluates its lifted parent tetrahedral comparison. It does not identify F006 with a single H123 or H234 prototype label, and it does not silently change the previously declared reverse-cumulative fine orientation into a native physical traversal.

## Endpoint and residual retention

For a fixed source-observer observable F on D, define its chart readout by `F_i = F R_i`. Then

    F_j C_ij = F R_j S_j R_i = F R_i = F_i.

The implementation retains separate labels for `ell_plus`, `ell_minus` and an arbitrary fixed source residual observable. Endpoint evaluations are understood on the physical analytic observer core. Regulator parameters must be fixed consistently when choosing a residual observable.

The residual observable is **not set to zero**. Strict equality of reconstructed chart transitions must not be confused with vanishing of a finite-cutoff analytical remainder. Nor does preservation of one observer residual identify all proof-relevant face modifications in another analytical presentation.

Controls reject scalar-chart inversion, uncorrelated completed carriers, an unsupported completion extension, inverse use outside the declared images, dropped endpoints/residuals, wrong initial types, mismatched cancellations and corrupted shared-face restrictions.

## What is and is not now established

Conditionally established: the entire structural refinement admits evaluation in the source strict reversible chart diagram, preserving any declared common-source readout by pullback. F006 is included.

Still open:

- identification with the intended regulator-dependent analytical face/tetrahedral witnesses;
- intertwining with the native44-channel field and its P/N/E readouts;
- domain/completion extensions beyond the restricted correlated source images;
- the114-record producer and the physical evolution interpretation.

A strict diagram can have commuting chart maps without supplying the intended nontrivial analytical homotopies. The next gate is that **witness-preserving comparison**, not another arbitrary numerical fixture or a claim that source analytic theorems have been reproved.

## Reproduce

```sh
python research/strominger/checkers/check_esd7_strict_parent_evaluation.py
```

- [Evaluator](checkers/esd7_strict_parent_evaluation.py).
- [All-cell programs, occurrence histories and reductions](results/esd7-strict-parent-evaluation.json).
- [Verification receipt](results/esd7-strict-parent-evaluation-verification.json).
