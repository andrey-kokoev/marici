# v20: normalization-conductor roof coefficient data

**Final currently executable checkpoint:**
[`rzk-coefficient-interface-v21.md`](rzk-coefficient-interface-v21.md) checks
the conditional graded-Leibniz exactness theorem and records the remaining
physical hypotheses explicitly.

`rzk/31-normalization-conductor-roof.rzk.md` formalizes the additive coefficient
content of the two-sheet normalization sequence. A glued coefficient is a
conductor coefficient together with independent positive- and negative-sheet
augmentation components.

Rzk defines `nu`, the sheet-difference augmentation `rho`, and checks:

- `rho o nu = 0`;
- equality of sheet-center coefficients for every element in `ker(rho)`;
- a canonical glued lift of every kernel element, with all four component
  equations checked;
- an explicit section proving coefficient-level surjectivity of `rho`;
- the left leg `a_C` of the physical roof and its primitive normalization.

This is the exact additive model underlying
`0 -> B -> B_+ (+) B_- -> C_cond -> 0`. It deliberately does not select a
sheet section for the physical comparison.

A fresh 72-file headless closure passed in 30.52 seconds. Evidence:
`results/31-normalization-conductor-roof.typecheck.json`.

Scope: this supplies exact coefficient data and names the three roof objects.
It does not implement localization of a category at quasi-isomorphisms, hence
does not turn the roof into an internal Rzk derived morphism. It also does not
supply the missing physical-Q or physical-to-jet comparison.
