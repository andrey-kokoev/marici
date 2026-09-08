# v25: corrected Morse-chain evaluation

**Plan completed:** [`rzk-coefficient-interface-v26.md`](rzk-coefficient-interface-v26.md)
formalizes the six native endpoint directions in the line-valued first
conductor quotient with all individual Rees factors retained.

`rzk/36-corrected-morse-fibre-evaluation.rzk.md` formalizes the finite image
calculation in task 5.

Of the five terms of the corrected boundary, only two meet nonzero sparse
columns. Rzk represents their images as opposite copies of

    Pi_+ z tensor ell_+,
    Pi_+ = X13 X15 X35,

using the exact 18-coordinate polynomial monomial. Their sum is proved zero in
the finite-coefficient evaluation setoid. The minus-line image is absent.

The module also represents all thirteen terms of the corrected Morse homotopy.
Because the comparison has only degree-one components, each degree-two term
maps to zero; structural recursion proves the same for every finite integral
combination of these terms.

A fresh 75-file headless closure passed in 46.01 seconds. Evidence:
`results/36-corrected-morse-fibre-evaluation.typecheck.json`.

Scope: the cancellation of the two resulting polynomial target expressions is
now checked internally. Their extraction from the complete 2,338-state source
and the multiplication `X13 X15 * X35 = Pi_+` remain imported through the
certificate-backed sparse data rather than independently reconstructed from
the Rust source differential.

Task 6, the six-direction map into the first conductor quotient `I/I^2`, is the
remaining finite formalization target.
