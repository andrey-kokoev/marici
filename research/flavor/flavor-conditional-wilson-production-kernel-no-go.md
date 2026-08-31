# Conditional-Wilson production-kernel no-go: WP1092

## Question

Does the conditional Wilson \(B\)-line flag derive the six-branch
production/decay kernel to physical16?

## Prior degeneracy

WP1074's six localized soft branches have dimensions

\[
(6,8,1,4,2,2),
\]

hence dimension-weighted soft distribution

\[
q=\frac1{23}(6,8,1,4,2,2).
\]

WP1075's event target is six weights \(1/4\), and \(q\neq(1/4)^6\).

## Conditional-flag boundary

WP1084 and WP1089 show that a second-stage \(B\)-doublet operation, if a
source selected its oriented adjoint ray, would act on the complementary
\(B\)-doublet while preserving the localized quartet. Such an operation has:

- no soft-branch-to-physical16 coupling entries;
- no event-reweighting entries;
- no gain-law output.

Six event weights require a six-row branch-to-physical16 production matrix.
The conditional internal \(B\)-flag supplies zero such rows.

## Classification

Negative gate. Wilson phases, \(B\)-line labels, quartet preservation, or
representation support are not production couplings. Conditional on a
source-selected oriented \(B\)-flag, the operation may preserve the localized
quartet, but it does not derive the production/decay kernel.

The remaining gate is a source-derived branch-to-physical16 coupling matrix,
event reweighting law, channel selection, and gain law.

Checker: `research/flavor/checkers/wp1092_conditional_wilson_production_kernel_no_go.py`

Result: `results/wp1092_conditional_wilson_production_kernel_no_go.json`
