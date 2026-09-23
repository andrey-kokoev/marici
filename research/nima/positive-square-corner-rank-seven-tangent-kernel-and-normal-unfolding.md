# The positive-square target singularity has a tangent kernel and a normal first-order unfolding

At the `w₄=0`, `t−u=0` corner of the four-cell source square, the two exact positive controls previously gave target-Jacobian ranks **A=8, B=7, C=8, D=7**. A new exact differential test characterizes the obstruction more sharply at both points:

* The rank-seven cells B and D each have a **one-dimensional target-Jacobian kernel** with nonzero `w₄` component and **zero `t−u` component**. The six-dimensional tangent space to the common source corner maps with rank six. Thus the lost direction is tangent to the `t−u=0` hypersurface, not a missing slope-gap normal.
* Along a perturbation **transverse to the slope-gap hypersurface**, `t=u+ε`, the exact left-null × first-Jacobian-variation × right-null pairing is **nonzero** for both B and D at both controls. Since the unperturbed rank is seven, their Jacobian determinants have a **simple zero in this transverse direction**.
* Perturbing only `w₄=ε` while keeping `t=u` gives a **zero first-order pairing** at both controls. This is consistent with the singularity persisting along the slope-gap face, rather than being caused only by its intersection with `w₄=0`.

This is the local differential pattern of a **blow-down-like degeneracy** (a tangent direction collapses on a divisor whose normal unfolds the Jacobian). It is **not** a proven analytic normal form: only two exact positive corner points and these transverse variations were checked. In particular, no pushed-corner residue, globally valid triangulation, or image form is inferred from the source-square incidence signs.

Checker: `research/nima/checkers/check_nine_point_corner_target_rank_unfolding.py`; certificate: `research/nima/results/nine-point-corner-target-rank-unfolding.json`.
