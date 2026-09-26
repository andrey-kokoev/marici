# Exact source-R normalization calibration

Freshly audited the inherited fermion-row reconstruction in `research/nima/checkers/check_nine_point_label3_history_cancellation_rank.py` and the primary source generalR formula. The inherited rank checks deliberately omit bosonic denominators: they cannot certify amplitude normalization.

Implemented an isolated exact rational kinematics/ordinary-R evaluator in `checkers/nine_point_source_r.py`, without importing the long side-effecting geometric checker chain. Region coordinates are reconstructed from adjacent twistor incidence; theta coefficients use the adjacent lambda-row inverse. The direct source numerator row is compared to the cyclic five-bracket row, and the COMPLETE prefactor is calibrated by p*scale^4=q, not just row proportionality.

An initial denominator transcription contracted the theta-oriented row directly with lambda and FAILED at(a,b)=(2,4), with normalization ratio35/89001. This exposed a real convention error that the fermionic-rank-only comparison would miss. Correct denominator contractions use L*epsilon*lambda for the chosen matrix conventions. With that correction, all15 admissible ordinary R factors at each of two distinct rational moment-curve inputs pass:30 exact full-row and normalization checks. The second input uses nonuniform parameters1,2,4,7,11,16,22,29,37 rather than a mere translated copy.

Reproduce: `uv run --with sympy python research/voevodsky/checkers/check_nine_point_ordinary_r_normalization.py`. Result: `results/nine-point-ordinary-r-normalization.json`.

Next extend this SAME calibrated convention to generalized inner R factors and Lrep/Urep spinors, replacing explicit boundary spinors in both numerator angle factors and denominator contractions while leaving fermionic theta rows as prescribed. First verify right-inner factors with no boundary update reduce to ordinary R, and independently calibrate transported inner factors. Only then sum the50 terms for chosen components. No full n=9 amplitude normalization or equality to the four-cell fork is claimed yet.
