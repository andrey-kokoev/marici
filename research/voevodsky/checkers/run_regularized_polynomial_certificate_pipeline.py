from __future__ import annotations
import json,runpy,sys
from pathlib import Path

STEPS=[
 ('scout_and_export','research/voevodsky/checkers/scout_legendre_ritz_schur.py'),
 ('exact_decimal_span','research/voevodsky/checkers/check_interval_polynomial_coefficients.py'),
 ('exact_span_concentration_trace_sensitivity','research/voevodsky/checkers/check_interval_exact_span_trace.py'),
 ('multiplier_localization','research/voevodsky/checkers/check_interval_multiplier_supremum.py'),
 ('exterior_nonnegative','research/voevodsky/checkers/check_interval_exterior_multiplier_nonnegative.py'),
 ('endpoint_tail','research/voevodsky/checkers/check_interval_endpoint_legendre_tail.py'),
 ('lower_form_sensitivity','research/voevodsky/checkers/check_interval_regularized_lower_form_sensitivity.py'),
 ('cutoff_matrix_sensitivity','research/voevodsky/checkers/check_interval_cutoff_form_matrix_sensitivity.py'),
 ('directed_continuum_certificate','research/voevodsky/checkers/check_arb_cutoff_form_legendre_matrix.py'),
]
RESULTS=[
 'research/voevodsky/results/regularized_polynomial_scout.json',
 'research/voevodsky/results/regularized_polynomial_coefficients.json',
 'research/voevodsky/results/interval_polynomial_coefficients.json',
 'research/voevodsky/results/interval_exact_span_trace.json',
 'research/voevodsky/results/interval_multiplier_supremum.json',
 'research/voevodsky/results/interval_exterior_multiplier_nonnegative.json',
 'research/voevodsky/results/interval_endpoint_legendre_tail.json',
 'research/voevodsky/results/interval_regularized_lower_form_sensitivity.json',
 'research/voevodsky/results/interval_cutoff_form_matrix_sensitivity.json',
 'research/voevodsky/results/arb_cutoff_form_legendre_matrix.json',
]

def main():
 completed=[]
 if '--summarize-only' not in sys.argv:
  for name,path in STEPS:
   print(json.dumps({'pipeline_step':name,'path':path,'status':'starting'}))
   runpy.run_path(path,run_name='__main__');completed.append(name)
 else:
  completed=['summarize_existing_artifacts']
 missing=[p for p in RESULTS if not Path(p).is_file()]
 statuses={}
 for path in RESULTS:
  if Path(path).is_file():
   data=json.loads(Path(path).read_text(encoding='utf-8'))
   statuses[path]=True if path.endswith('regularized_polynomial_coefficients.json') else bool(data.get('passed',False))
 final_path='research/voevodsky/results/arb_cutoff_form_legendre_matrix.json'
 final=json.loads(Path(final_path).read_text(encoding='utf-8')) if Path(final_path).is_file() else {}
 complete=not missing and all(statuses.values()) and bool(final.get('continuum_positivity_verified',False))
 result={'schema':'marici.voevodsky.regularized-polynomial-pipeline.v2',
  'completed_steps':completed,'required_artifacts':RESULTS,'missing_artifacts':missing,
  'artifact_pass_statuses':statuses,'coded_form_continuum_certificate_complete':complete,
  'rh_criterion_source_identity_verified':False,
  'continuum_certificate_complete':complete,
  'scope':'coded cutoff-250 and uncut first-prime support-window form',
  'rh_implication':False,'passed':complete}
 rendered=json.dumps(result,indent=2,sort_keys=True)
 Path('research/voevodsky/results/regularized_polynomial_pipeline.json').write_text(rendered+'\n',encoding='utf-8')
 print(rendered)
if __name__=='__main__':main()
