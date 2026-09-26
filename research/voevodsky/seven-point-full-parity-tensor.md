# Complete seven-point parity tensor comparison at two rational inputs

Fresh run: `uv run --with sympy python research/voevodsky/checkers/check_seven_point_full_parity_tensor.py` passes.

This replaces sampled mixed components by an exact complete tensor certificate. A single flavor of the NNMHV superamplitude occupies Lambda^4(Q^7), dimension35. Each of the six source terms has the form w*v tensor v tensor v tensor v, where v lists all4x4 minors of the two supermomentum rows and two eta-converted R rows. For the NMHV side, form all3x3 complementary minors after swapping spinors, including each Hodge-complement sign. Both sides retain their Parke-Taylor prefactors.

Let T be their difference. The ordinary Euclidean coefficient-space norm obeys

||T||^2 = sum_(r,s) w_r*w_s*(v_r dot v_s)^4.

Every number is rational and evaluated exactly. This norm is positive definite, irrespective of the signs of individual weights; zero therefore certifies EVERY ordered four-flavor tensor entry is zero. It is not a random projection or a modular zero test. The metric is merely a computational coefficient-space inner product, not a Lorentzian physical norm.

At each of the two previously saved kinematic inputs, the norm of the difference is exactly zero while both amplitude norms are strictly positive. This covers all35^4=1,500,625 flavor-grouped coefficients at each point. Removing one NMHV term gives a strictly positive norm, independently matching that omitted term's norm; the checker detects this deliberate negative control.

Results include normalized term vectors, exact weights, norm contractions, negative controls, and checker source hashes in results/seven-point-full-parity-tensor.json. The checker currently imports the earlier parity checker, which reruns and refreshes its sampled-component artifact before the full comparison; no hidden cached amplitudes are used.

Remaining distinction: complete fermionic equality at two fixed bosonic inputs is NOT equality as a rational function of all kinematics. Next reduce the tensor using supermomentum constraints and prove the remaining rational coefficient identities symbolically, or derive an independent analytic parity argument with explicitly verified conventions. Positive-cell realization of all six terms remains another geometric task. The older nine-point contour work remains parked, not declared complete.
