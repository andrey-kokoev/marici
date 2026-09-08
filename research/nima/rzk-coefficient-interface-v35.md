# v35: corrected alternating/Rees annihilator

**Actual-source update:** [`rzk-coefficient-interface-v36.md`](rzk-coefficient-interface-v36.md)
retains the two copies of the shared branch normal and proves their excess
difference is a primitive nonboundary cycle.

`rzk/45-alternating-rees-annihilator.rzk.md` updates the coefficient model after
the nonflat graph substitution `u_s=t_s X_s`.

The old independent-normal product is explicitly classified as carrying both
positive- and negative-sheet occurrence support; its image therefore has the
mixed-zero support tag. It must not be used as a specialized principal
annihilator.

The module instead encodes the seven minimal generator modes of

    (tau_plus tau_minus, tau_plus I_plus, tau_minus I_minus):

- one common-conductor generator with all six Rees factors;
- three positive occurrence generators with `tau_plus`;
- three negative occurrence generators with `tau_minus`.

It also retains six proper nonempty inactive subsets on each branch, giving the
twelve labelled top-boundary ambiguity families. Their branch labels are not
collapsed into a free rank-twelve module over the glued ring.

A fresh 74-file headless closure passed in 38.42 seconds. Evidence:
`results/45-alternating-rees-annihilator.typecheck.json`.

Scope: Rzk checks the corrected typed generator/support data and the mixed-sheet
vanishing mechanism. The theorem that these generators form the exhaustive
annihilator, and the decomposition of top boundary homology into six copies of
each branch ideal, remain supported by the incoming all-polynomial argument
and checker rather than reconstructed in type theory.

Module 44 remains valid over its independent-normal packet, but its principal
Delta conclusion is not transported through this nonflat base change.
