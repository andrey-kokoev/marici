# Label-three fourth-power cancellation filter for all 50 n=9 authored histories

Compile **all 50** n=9 histories from the primary source `PNNMHVnew`. For each, reconstruct the outer ordinary-five-bracket fermionic row and the inner row from BOTH terms of either `generalR` (left nested with transported ξ) or `defxi` (right nested). The source's `Lrep`/`Urep` replacements affect explicit **denominator spinors**, not the fermionic delta. Adjacent momentum-super-twistor incidence converts `θ_i` to χ coefficients. Check the resulting ordinary history 9 and corrected transported history 27 against their independently computed pair ratios.

To test necessary cancellation of dependence on physical label 3, form the eight-dimensional per-flavor Plücker vector `v_h(p)=A_h(3)B_h(p)−A_h(p)B_h(3)` for `p∈{1,2,4,5,6,7,8,9}`. The contribution to the component containing χ₃ **in each of the four distinct flavors** is the fourth tensor power `v_h⊗v_h⊗v_h⊗v_h`. If a sum is independent of χ₃, this sector must vanish.

On **two independent exact rational generic inputs**, the same nine histories `(7,8,9,13,19,27,28,29,49)` have zero `v_h`; the other **41** fall into **18 distinct projective rays**, including six repeated groups:

- `(3,30,37,45)`; `(4,31,42,47)`; `(5,32,34,43,44,48)`;
- `(10,11,12)`; `(14,15,16,17,18)`; `(20,21,22,23,24,25,26)`.

The remaining 12 label-three-active histories `(0,1,2,6,33,35,36,38,39,40,41,46)` occupy singleton rays. On EACH witness, a reproducible **18×18 nonzero minor modulo 1,000,003** certifies that the 18 distinct fourth-power rays are linearly independent over the rationals (the selected degree-four monomials are in the result JSON). Thus, for finite scalar coefficients at either witness, χ₃⁴ cancellation forces a **separate zero net coefficient in every ray group**; in particular singleton-ray histories cannot individually participate with nonzero coefficient at that input. The six repeated groups are only candidate blocks, NOT proven to cancel their mixed-χ₃ components or to yield the four-mass invariant. Repeated grouping at two inputs does not by itself establish symbolic proportionality over all kinematics. **Superseding mixed-sector check:** `research/nima/checkers/check_nine_point_mixed_label3_cancellation_rank.py` finds FULL rank 41 after including components with χ₃ in two flavors at both exact witnesses. Thus no nonzero combination of the 41 active histories can eliminate χ₃ generically; repeated fourth-power rays do not produce a full cancellation. See `research/nima/full-label-three-restriction-rules-out-all-fifty-authored-history-span.md`.

This is an exact necessary fermionic condition; it does not determine the sourced bosonic R prefactors, find a successful history subset, prove a global n=9 identity, or settle amplitude-form/image coverage.

Checker: `research/nima/checkers/check_nine_point_label3_history_cancellation_rank.py`; witnesses: `research/nima/results/nine-point-label3-history-cancellation-rank.json` and `research/nima/results/nine-point-label3-history-cancellation-rank-witness2.json`.
