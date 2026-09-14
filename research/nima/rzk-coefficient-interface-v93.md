# v93: tangential coefficient-amplitude calibration

`rzk/121-tangential-coefficient-amplitude-calibration.rzk.md` gives the first
coefficient-valued amplitude formula over the existing constructive integer
ring:

`A_beta(a,b,c) = - beta (a + (b + c))`.

The module proves that the calibration depends only on the total trace
coordinate. Consequently two coefficient representatives with equal total
`a+b+c` have equal calibrated amplitudes, formalizing the established fact that
the scalar readout kills their trace difference.

This remains a calibration target, not an identification with the physical
supported-residue amplitude. That identification requires the missing physical
Gysin/residue comparison.

The transitive closure contains eight files. A fresh combined Rzk check passes
all 143 reported declarations (155 checker steps including parameter/assumption
commands). The target module adds no `#assume` declarations.
