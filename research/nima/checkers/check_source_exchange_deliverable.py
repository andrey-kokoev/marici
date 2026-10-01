# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Final scoped acceptance audit and conditional finite-sample falsifier design."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from math import ceil
from pathlib import Path
import io
import json
import runpy

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/source-exchange-deliverable.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    resource=runpy.run_path(str(HERE/'check_exchange_resource_accounting.py'))
audit=resource['audit']; end=audit['result']; ledger=resource['result']
assert ledger['status']=='passed' and end['status']=='passed'
assert len(end['fresh_support_checks'])==8
assert all(v['status']=='passed' for v in end['fresh_support_checks'].values())
assert end['objective_complete'] is False
assert len(end['open_gates'])==3 and len(ledger['uncosted'])==6

# Analytic test design, not measured frequencies or Monte Carlo evidence.
# Independent shots and dark controls; fixed model calibration/phase statistics.
obs=end['predicted_detector_moments']; det=end['detector_parameters']
M=obs['prepared_reference'][0]-det['b']
assert M>0
v_echo=obs['exchange_echo'][1]; v_alt=obs['quarter_turn_echo'][1]
v_ref=obs['prepared_reference'][1]; v_rect=obs['exchange_rectangle'][1]
v_dark=det['ve']; epsilon=.001
# Echo statistic: mean(signal)-mean(dark), expectation +/-M.
# Chebyshev: P(wrong sign)<= (v_signal+v_dark)/(n*M^2).
n_echo=ceil((max(v_echo,v_alt)+v_dark)/(epsilon*M*M))
echo_bound=(max(v_echo,v_alt)+v_dark)/(n_echo*M*M)
assert echo_bound<=epsilon
# Rectangle statistic: mean(signal)-(mean(reference)+mean(dark))/2.
# Expectations +/-M/2 for exchange rectangle versus flat identity. Independent
# n-shot batches; flat identity has the reference variance in this model.
n_rectangle=ceil((4*max(v_rect,v_ref)+v_ref+v_dark)/(epsilon*M*M))
rectangle_bound=(4*max(v_rect,v_ref)+v_ref+v_dark)/(n_rectangle*M*M)
assert rectangle_bound<=epsilon
result={
 'status':'passed',
 'classification':'conditional_source_exchange_deliverable_validated_native_physical_selection_open',
 'acceptance':{
   'native_matrix_response_preparation_map':'checked with explicit trace gain and attached coherent memory',
   'source_witness_boundary_validation':'checked for137 comparisons',
   'faithful_packet_covariance_and_history':'checked',
   'event_composition_and_reference_transport':'checked within declared contract',
   'native_shared_leg_operator_factorization':'rejected by109 rectangles',
   'physical_readout_and_resources':'conditional detector and ideal resource model; overhead remains open',
   'absolute_electromagnetic_coupling':'not derived',
   'native_instrument_selection':'not derived'},
 'finite_sample_design':{
   'per_hypothesis_error_bound':epsilon,
   'echo_shots_per_signal_and_dark_batch':n_echo,'echo_bound':echo_bound,
   'rectangle_shots_per_signal_reference_and_dark_batch':n_rectangle,'rectangle_bound':rectangle_bound,
   'method':'Chebyshev bounds on independent sample means; uses declared population variances',
   'scope':'No experimental data; no systematic phase/gain uncertainty included; per test and hypothesis, not a familywise guarantee'},
 'checks':{'full_resource_and_eight_support_checks_fresh':True,'conditional_chain_acceptance':True,
           'open_claims_preserved':True,'finite_sample_bounds':True},
 'conclusion':'A native-response-seeded, boundary-validated source-labelled exchange experiment with explicit preparation/readout, resource ledger and falsifiers is delivered conditionally. It is not a derivation of source-selected physical dynamics or absolute coupling.',
 'objective_complete':False,
 'next_constructor':'Supply an independently justified source-to-instrument action or an actual calibrated apparatus contract that selects memory, preparation gain and pulse; a passing conditional compiler cannot supply that selection itself.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
