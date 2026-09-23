# Supported target-normal forms distinguish the two positive `w₂` neighbors

A, V (vertical physical column 2) and E (label-3-sensitive physical column 3) share the same positive `w₂=0` source boundary. Their oriented meromorphic source-pole signs are **A −, V +, E +**, and their complete boundary fermionic numerator is the same. In the one-dimensional target normal quotient at each of three exact regular positive controls, write `h=n_cell w₂`. The pushed **meromorphic leading germ** of `σ_cell K·dw₂/w₂` is `σ_cell K·dh/h`, but a positive cell occupies only the half-space **`h/n_cell>0`**.

The exact normal-side signs give two different *supported* local pictures:

* **A+E:** A and E occupy the **same** target-normal half-space. Their leading `−K/h+K/h` contributions **cancel there**.
* **A+V:** A and V occupy **opposite** half-spaces. A is the only one of this pair supported on its side; V is supported on the other. Their meromorphic residues have opposite signs, but there is **no pointwise two-cell overlap** in either interior half-space.

Thus an algebraic cofactor-residue cancellation does not determine whether positive image sectors glue across a boundary or overlap and subtract. This support distinction is first-order near three verified boundary points and does **not** choose a global positive contour, account for other sheets/cells, or prove the nine-point canonical form.

Checker: `research/nima/checkers/check_nine_point_competing_w2_neighbors_support_sensitive_forms.py`; certificate: `research/nima/results/nine-point-competing-w2-neighbors-support-sensitive-forms.json`.
