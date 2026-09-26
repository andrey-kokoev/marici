# First interaction-net-inspired continuation probe

A finite linear rewrite prototype now uses the four actual shared-facet EB/FB sheet records. Each record retains its family, consumed-source identity, normalized wall residue, and two exact off-face fermionic component values at e=1. Wall residues and off-face values are distinct observations; the prototype does not identify them.

The rule consumes one same-family EB/FB pair and produces a remainder carrying their summed component values and zero pole. Both possible orders give identical normal forms, and every step preserves the two-component observer. Reusing a consumed pair is rejected. Crucially, simply deleting the pole-cancelling pairs also gives an order-independent answer, but destroys the nonzero components: confluence by itself is insufficient.

The normal form still contains two independent symbolic family weights alpha,beta. Setting beta=0 or beta=1 leaves local poles cancelled but produces different component answers. Thus this experiment locates an explicit information-retention obligation without pretending to infer physical contour weights.

This is NOT yet a principal-port interaction net, a translation of Voevodsky's implementation, or a full-superform semantics theorem. Next implement the retained-remainder rule with actual linear ports and specify the observer before testing more contexts. Extending to arbitrary target functions and all fermionic components is a separate obligation.

Checker: `research/nima/checkers/check_four_cell_continuation_rewrite_probe.py`.
Result: `research/nima/results/four-cell-continuation-rewrite-probe.json`.
