# v124: unit-pairing free-cokernel extension

The all-degree detector immediately identifies a minimal algebraic extension:
adjoin the constant monomial `1`. Its detector pairing is exactly one.

For every target polynomial `f`,
`f = (f-lambda(f)1) + lambda(f)1`; the first summand lies in `ker(lambda)`.
Thus the target splits integrally as the detector kernel plus the free unit
line. Since the L2-completed image lies in the kernel, adjoining `1` kills
exactly the free cokernel in every degree.

This extension does not alter the torsion quotient. The D12--D28 Smith data are
cross-checked accordingly. It is an algebraic target extension, not yet a
global road-Cech chain column: the remaining geometric task is to realize this
unit column compatibly with the road overlaps and physical coherence.

Evidence is `results/soft-axis-unit-detector-extension.json` from
`checkers/check_soft_axis_unit_detector_extension.py`.
`rzk/152-soft-d1-unit-detector-extension.rzk.md` passes all eight declarations
without assumptions.
