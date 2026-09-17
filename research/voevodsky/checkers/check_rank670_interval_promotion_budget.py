#!/usr/bin/env python3
"""Turn the rank-670 scout margin into explicit interval-error targets."""
import json,math
from pathlib import Path
n=670;lam=2.6065344444974488e-8;schur=1.0656733950262529e-7;cond=131226040.60123262
# If every symmetric entry error is <=eps, ||E||_2 <= n eps.
entry_for_half_margin=lam/(2*n);spectral_budget=lam/2
# Schur block of size 510 gets its own simple Gershgorin target.
schur_entry_for_half_margin=schur/(2*(n-160))
out={'schema':'marici.voevodsky.rank670-interval-promotion-budget.v1','dimension':n,'floating_min_eigenvalue':lam,'rank160_condition_number':cond,'rank510_over_rank160_schur_min':schur,'sufficient_uniform_entry_radius_for_half_full_margin':entry_for_half_margin,'sufficient_full_matrix_error_norm':spectral_budget,'sufficient_uniform_schur_entry_radius_for_half_schur_margin':schur_entry_for_half_margin,'recommended_strategy':'directed panel chunks plus floating-Cholesky preconditioning; do not invert the ill-conditioned rank160 block in intervals','passed':entry_for_half_margin>1e-11,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'rank670_interval_promotion_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
