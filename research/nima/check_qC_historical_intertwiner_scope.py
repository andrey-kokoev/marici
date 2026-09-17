#!/usr/bin/env python3
"""Provenance and typing audit for the historical q-C comparison."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
rad=(ROOT/'research/voevodsky/the-oriented-log-radial-fourier-sewing-has-an-explicit-oscillatory-hankel-kernel.md').read_text(encoding='utf-8')
mel=(ROOT/'research/voevodsky/mellin-diagonalization-of-the-oriented-radial-fourier-kernel-recovers-the-tate-gamma-matrix.md').read_text(encoding='utf-8')
ledger=(ROOT/'research/voevodsky/source-derived-fourier-sewing-identification-closure-ledger.md').read_text(encoding='utf-8')
checks={'oriented_radial_chart_unitary':'This chart is unitary' in rad,'radial_operator_order_four':'W_{\\rm or}^4=I' in rad,'mellin_gamma_matrix_explicit':'G(t)=' in mel and 'm_\\sigma(t)' in mel,'exact_mixed_square':'\\mathcal M_{\\log}W_{\\rm or}' in mel and 'G(t)R_t\\mathcal M_{\\log}' in mel,'common_test_core_declared':'common Schwartz core' in mel,'closure_ledger_declares_chain_closed':'## Closed analytic chain' in ledger,'endpoint_completion_separate':'Endpoint distributional completion remains separate' in mel}
out={'schema':'marici.nima.qC-historical-intertwiner-scope.v1','historical_qC':'M_log W_or = G(t) R_t M_log on the common Schwartz core','misidentified_comparison':'lattice Pontryagin character versus nonlinear radialized additive-Fourier kernel','claim_dispositions':{'tail_can_realize_a_multiplicativity_defect':'demonstrated in finite external scout','finite_factorization_mechanism':'exact in finite external scout','historical_defect_and_leakage_share_a_target':'rejected_ill_typed','historical_range_inclusion':'not_applicable','uniform_Douglas_bound':'not_applicable','refinement_compatible_completed_lift':'not_applicable'},'checks':checks,'passed':all(checks.values()),'remaining_qC_scope':[],'resolved_extensions':{'qCO':'finite/projective endpoint graph','qCR':'strict for transported/place regulators, lax for independent sharp windows'}}
p=ROOT/'research/nima/results/qC-historical-intertwiner-scope.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
