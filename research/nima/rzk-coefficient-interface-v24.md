# v24: sparse endpoint-derived comparison

**Next checkpoint:** [`rzk-coefficient-interface-v25.md`](rzk-coefficient-interface-v25.md)
checks that the two nonzero corrected-boundary images cancel and that every
corrected degree-two Morse term maps to zero.

`rzk/35-relative-sparse-comparison.rzk.md` completes the typed sparse-data part
of task 4. It is generated directly from
`research/chatgpt/relative_morse_fibre_comparison_certificate.json`.

The generator groups the certificate's 44 matrix entries by source index and
checks that there are exactly 22 source columns with exactly two entries each.
It then emits:

- 22 distinct source-column constructors;
- the full 18-coordinate natural polynomial monomial on every entry;
- the certified endpoint-line label;
- the two target coordinates of the physical primitive z;
- the common negative sign.

Thus the map lands in finite integral sums on
`L_+ or L_- x F x polynomial-monomial`; endpoint lines remain formal labels,
not inverse monomials.

A fresh 74-file headless closure passed in 54.55 seconds. Evidence:

- `results/35-relative-sparse-comparison.typecheck.json`
- `results/relative-sparse-comparison-generation.json`

Scope: Rzk checks that the complete sparse map datum is well typed and retains
all exponents and line labels. It does not yet reconstruct the other 2,316
zero source columns or replay the complete source differential, so the global
chain-map assertion still depends on the incoming certificate. The corrected
Morse-chain evaluation is the next independently executable finite check.
