# Two external four-bracket walls require trace before specialization

## Falsified residue shortcut

A visible `1/⟨1234⟩` or `1/⟨5678⟩` in the complete starred four-mass ψ expression does **not** authorize multiplying by that bracket and immediately substituting zero in all other factors. Two exact one-parameter rational external datasets make each named bracket vanish linearly while their auxiliary quadratic has nonzero leading coefficient and **nonzero discriminant** on the wall. Yet the other factors are not all units:

- At `⟨1234⟩=0`, the matrix representing the denominator of the chosen auxiliary `β=(n0+n1α)/(d0+d1α)` becomes singular in the two-root quotient algebra. The α chart no longer supplies a safe pointwise β substitution on both branches.
- At `⟨5678⟩=0`, **all four** B-containing cyclic five-bracket matrices become nonunits in that quotient algebra. Removing only the explicit `1/⟨5678⟩` does not isolate a simple residue.

These are exact matrix-determinant statements, not approximate limits. They do NOT determine whether the complete sourced rational component has a pole, whether apparent divergences cancel, or its eventual residue. The valid next computation is the complete two-sheet trace over a local Laurent field in the deformation parameter (or a different regular auxiliary chart) **before** taking the wall limit. A symbolic full-trace attempt exceeded the execution budget and was not promoted to evidence. The already proved intrinsic source-coordinate `w2=0` residue is a different object and does not license an external pole claim.

Checker: `research/nima/checkers/check_four_mass_external_pole_wall_admissibility.py`; result: `research/nima/results/four-mass-external-pole-wall-admissibility.json`.
