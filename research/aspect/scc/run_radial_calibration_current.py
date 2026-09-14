#!/usr/bin/env python3
"""Record the current synthetic radial-calibration SCC boundary."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
paths={
 'companion':ROOT/'research/voevodsky/results/radial_synthetic_calibration_companion.json',
 'metric':ROOT/'research/voevodsky/results/radial_metric_rh_interface.json',
 'shadow':ROOT/'research/voevodsky/results/radial_calibrated_four_trace_shadow.json'}
# Checkers are authoritative for schemas; tolerate their exact result filenames by loading source contracts directly for structural readback.
comp=json.loads((ROOT/'research/voevodsky/contracts/radial-synthetic-calibration-companion.v1.json').read_text())
shadow=json.loads((ROOT/'research/voevodsky/contracts/radial-calibrated-four-trace-shadow.v1.json').read_text())
checks={
 'synthetic_only':comp.get('status')=='synthetic_complete_not_physical',
 'shadow_not_source_identification':shadow.get('status')=='synthetic_shadow_complete_not_aspect_trace_binding',
 'rank_four':shadow.get('metric_disposition',{}).get('pullback_to_R26')=='positive_semidefinite_rank_4',
 'kernel_retained':shadow.get('metric_disposition',{}).get('full_record_metric_preserved') is False and shadow.get('metric_disposition',{}).get('classification')=='pseudometric_on_R26_metric_on_R26_mod_kernel'}
out={'schema':'marici.scc.radial-calibration-current.v1','passed':all(checks.values()),'checks':checks,'coherent_prefix':['synthetic_26_coordinate_record_and_covariance','wilson_holonomy_quotient_descent','real_covariance_isometry','four_scalar_shadow_with_exact_covariance_pushforward'],'first_obstruction':{'layer':'calibrated_record_four_trace_comparison','required_map':'R^26 <-> Y_P plus Y_Q plus Y_M plus Y_J','requirements':['evaluable_rule','units','gauge_equivariance','Real_equivariance','covariance_transport','quotient_kernel_and_rank']},'blocked_successors':['jointly_faithful_source_trace_identification','radial_noise_whitened_metric_descent_to_four_trace_target','Evans_Green_RH_chain'], 'finite_shadow':{'rank':4,'kernel_dimension':22,'disposition':'not faithful on calibrated 26-coordinate metric; retain kernel or prove intended quotient'},'physical_promotion':False,'rh_implication':False}
p=ROOT/'research/aspect/results/radial_calibration_current.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
