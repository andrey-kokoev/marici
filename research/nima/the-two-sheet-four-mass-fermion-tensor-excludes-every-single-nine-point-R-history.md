# The two-sheet four-mass fermion tensor excludes every single nine-point R history

The primary all-n NNMHV formula (arXiv:0808.2475, `PNNMHVnew` and `generalR`) expresses EACH authored nine-point history as a product of an ordinary R and another ordinary or generalized R. Every R carries **one** Grassmann degree-four delta whose bosonic coefficients are the same across the four supersymmetry flavors; the transported chiral spinor and boundary replacements are bosonic. Thus a SINGLE history has a decomposable rank-one degree-eight flavor tensor, even after any flavor-blind momentum-twistor change of Grassmann coordinates.

The starred four-pair invariant has a different exact algebraic invariant. At a generic `Y0` fibre it is the sum of two solutions `C_i z=0`, each contributing weight `s_i=source_density(C_i)/J_z(C_i)` times its degree-eight fermionic delta. Choose two pairs of retained local labels, `X=(1,5)` and `Y=(2,6)`. Write `x_i=det(C_i[:,X])` and `y_i=det(C_i[:,Y])`. The three coefficients obtained by assigning all four flavors to X, all four to Y, or two flavors to each obey

    F_XXXX=Σ_i s_i x_i⁴,  F_YYYY=Σ_i s_i y_i⁴,
    F_XXYY=Σ_i s_i x_i² y_i²,
    F_XXXX F_YYYY − F_XXYY²
       =s_1 s_2 (x_1² y_2²−x_2² y_1²)².

For ONE R×R history the left-hand rank-one minor vanishes identically. The checker independently reconstructs both four-pair fibre sheets and their full eight-by-eight `J_z` at TWO distinct rational external targets; the right-hand side is nonzero at both. Therefore the COMPLETE starred four-mass invariant **cannot equal any one authored nine-point nested-R term**, including the remaining explicit-endpoint candidate history 27 with transported path `(9,8,2)`. This supersedes mere endpoint matching as an identification test. The earlier independent numerical comparison already excluded ordinary history 9.

This does **not** exclude a sum of histories, an equivalent global amplitude representation or a non-BCFW Yangian invariant contributing only through residue identities. Nor does it prove that endpoint-support screening exhausts all mechanisms by which terms with label 3 could cancel. A next test is whether the fixed-coefficient two-candidate sum can reproduce the rank-two tensor and its external pole; the global nine-point amplitude/form and image coverage remain open.

Checker: `research/nima/checkers/check_nine_point_four_mass_vs_single_history_fermion_rank.py`; result: `research/nima/results/nine-point-four-mass-vs-single-history-fermion-rank.json`.
