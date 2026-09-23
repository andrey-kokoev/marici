# The nine-point authored history screen leaves one transported-spinor four-mass candidate

## Exact authored-index census

The PRIMARY all-n NNMHV nested-R formula (arXiv:0808.2475, equations `PNNMHVnew`, `generalR`, `Lrep`, `Urep`) compiles at `n=9` to **50** histories, retaining their left/right nesting and boundary substitutions. The paired four-mass cell uses the retained physical labels `(1,2,4,5,6,7,8,9)` and has zero source column at physical `3`. For every history, we collect the EXPLICIT momentum-twistor endpoint envelope of both R factors and all authored transported-spinor/replacement path vertices. Nine histories have no explicit label `3`; exactly TWO envelopes equal the eight retained labels:

- History **9**: outer `(a₁,b₁)=(2,5)`, right-nested inner `(a₂,b₂)=(6,8)`, no active boundary replacement. This is the ordinary-five-bracket product `[9,1,2,4,5][9,5,6,7,8]` (local eight-label form `[8,1,2,3,4][8,4,5,6,7]`).
- History **27**: outer `(2,8)`, left-nested inner `(5,7)`, transported chiral-spinor path `ξ=(9,8,2)`, no boundary replacement. It is a genuine generalized-R term requiring the source's spinor transport, not an ordinary product.

The endpoint envelope is only a **candidate screen**: matching labels is not a proof of fermionic support, contour/positroid equality or canonical-form normalization.

## Independent exclusion of the ordinary standalone candidate

For the complete `χ₁⁴χ₅⁴` component of the starred sourced four-mass ψ, an independent companion-quadratic trace was compared to history 9's complete product of TWO ordinary five-brackets, including each five-bracket's five cyclic denominators. The ratio history9/ψ is `−16/7` on an independent moment-curve momentum-twistor input and a DIFFERENT exact rational on the previously frozen quotient input. Both are nonzero. Thus **history 9 cannot equal the complete starred ψ as a standalone sourced term**. This does not rule out a multi-history identity, nor prove history 27 equals ψ: its generalized transported spinor remains to be translated and its positroid residue verified. An authored nine-point history assignment is therefore NOT YET complete.

Checkers: `research/nima/checkers/check_nine_point_authored_four_pair_history_screen.py`, `research/nima/checkers/check_nine_point_candidate9_vs_four_mass_psi.py`; results: `research/nima/results/nine-point-authored-four-pair-history-screen.json`, `research/nima/results/nine-point-candidate9-vs-four-mass-psi.json`.
