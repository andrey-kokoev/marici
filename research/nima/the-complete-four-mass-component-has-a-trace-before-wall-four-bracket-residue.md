# The complete four-mass component has a trace-before-wall four-bracket residue

## Exact external pole

Take `z1=e1,z2=e2,z3=e3,z4=e4`, and integer rows `z6=(2,3,5,7)`, `z7=(3,5,7,11)`, `z8=(5,8,13,21)`, with `z5=z6+z7+z8+εe1`. Then `⟨5678⟩=-10ε`. A visible `1/⟨5678⟩` in the starred four-mass ψ cannot be specialized at the wall on its own: the previous exact checker found FOUR other B-side cyclic denominators noninvertible there, though the two-root quadratic discriminant is nonzero.

This obstruction is resolved by calculating in the **local rational quadratic algebra before specializing**. Form the complete ψ prefactor and both COMPLETE five-bracket component numerators/denominators as rational two-by-two companion matrices over `Q(ε)`. Invert every matrix off the wall, independently expand each entry into a bounded exact Laurent series, multiply all factors, then trace. The full `χ1⁴χ5⁴` two-sheet component has

    Tr(component) = (2/325) ε^-1 + O(1)
                  = (-4/65) ⟨5678⟩^-1 + O(1).

The second equality uses `⟨5678⟩=-10ε`. This is a **genuine nonzero SIMPLE EXTERNAL FOUR-BRACKET POLE** of the complete sourced supercomponent, not an untraced single-sheet guess. Rigour of the bounded calculation: each factor's actual Laurent valuation is computed and the worst individual expansion precision needed for a coefficient through `ε^-1` is four; runs retaining up to powers fourteen and twenty agree on the entire principal part and constant term. An independently implemented direct rational quadratic-field evaluation at `ε=1/100000` also approaches the certified residue at a checked exact error bound. The ψ prefactor and all ten cyclic denominators are included.

The previously proved generic-simple-fibre complete-fermion identity transports this rational sourced component (subject to its audited overall orientation/Berezin normalization) to the normalized `Y0` extraction wherever the corresponding rational identity applies. **Direct symbolic Y0 fibre elimination across the wall and an arbitrary-Y global bosonic target-form coefficient have not been computed.** The result does not assign the cell to an authored nine-point generalized-R history or establish positive image coverage.

Checker: `research/nima/checkers/check_four_mass_5678_local_Laurent_trace.py`; result: `research/nima/results/four-mass-5678-local-Laurent-trace.json`.
