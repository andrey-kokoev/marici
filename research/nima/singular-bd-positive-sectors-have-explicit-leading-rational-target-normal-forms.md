# Explicit leading rational target-normal forms on the B/D blow-down sectors

At each of two exact positive slope-face target planes, the **entire positive B and D face fibres** have affine normal target jets `n_i(λ)=a_i+λb_i` with nonzero `Δ_i=det(a_i,b_i)`. Their leading target-normal map

```
η=(X,Y)=v(a_i+λb_i),        v=t−u>0,
```

is invertible inside each cell's positive normal sector. Set `D_i=det(η,b_i)` and `N_i=det(a_i,η)`. The exact leading inverse is `v=D_i/Δ_i`, `λ=N_i/D_i`. Write the five source-face weights along the affine fibre as `w_j(λ)=p_j+r_jλ` for `j=4,…,8`. After factoring out the common six-dimensional corner base-chart contribution, the **leading normal two-form density** is

```
−σ_i r₄ Δ_i D_i³
─────────────────────────────────────── ,     σ_B=+1, σ_D=−1.
 w₂u ∏_{j=4}^8 (p_j D_i+r_j N_i)
```

An exact checker independently substitutes `η=v n_i(λ)` into this rational expression and recovers the oriented source form divided by the normal Jacobian, for **both cells at both target planes**. The resulting target-normal densities are **nonzero, homogeneous of degree −2**, and supported on the cells' previously certified **disjoint positive first-order normal sectors**. They exhibit explicitly why cancellation of the paired singular **source-face currents** cannot be replaced by pointwise cancellation of these leading image densities at matched source parameters.

This is a **linearized local normal-map calculation**, not the full nonlinear pushed eight-form; the common six-dimensional base measure, fermionic numerator, other inverse sheets/cells, and global image canonical form remain to be assembled. In particular, no global pole-survival theorem follows from two normal-sector controls.

Checker: `research/nima/checkers/check_nine_point_singular_bd_leading_target_normal_forms.py`; certificate: `research/nima/results/nine-point-singular-bd-leading-target-normal-forms.json`.
