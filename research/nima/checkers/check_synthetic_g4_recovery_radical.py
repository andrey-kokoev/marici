"""Hostile test of fixture-only recovery, quotient, and radical declarations."""
import copy,json
from pathlib import Path
ROOT=Path('research/nima')
contract=json.loads((ROOT/'contracts/g4-radial-interface-candidate.v1.json').read_text())
assert contract['status']=='test_fixture_only'
labels={'prime','grade','shell','ordered_pair','theta_label'}
source_labels={'prime','grade','shell','ordered_pair','theta_label'}

def validate(c,recovered=source_labels):
 e=[]
 r=c['radial_recovery']; cyc=c['cycle_policy']; gr=c['green_radical']; gf=c['green_form']
 if r['mode']!='full_state_retained' or set(recovered)!=source_labels: e.append('readout_only_recovery')
 if not cyc['chosen_independently_of_source_coefficients']: e.append('adaptive_cycle_quotient')
 if cyc['mode']!='quotient_by_Z1' or cyc['cycle_space']!='interval_cycle_space_Z1': e.append('undeclared_common_history_quotient')
 if gr['definition']!='form_radical_on_declared_feature_range' or gf['metric']!='declared_full_polarized_metric':
  e.append('interval_cycle_promoted_to_green_radical')
 if c['return_map']['placement'][-1]!='before_label_codiagonalization': e.append('labels_erased_before_return_test')
 return e

baseline=validate(contract)
readout=copy.deepcopy(contract)
adaptive=copy.deepcopy(contract);adaptive['cycle_policy']['chosen_independently_of_source_coefficients']=False
renamed=copy.deepcopy(contract);renamed['green_radical']['definition']='interval_cycle_space_Z1'
late=copy.deepcopy(contract);late['return_map']['placement'][-1]='after_label_codiagonalization'
hostile={
 'readout_only':validate(readout,{'prime','grade'}),
 'adaptive_cycle':validate(adaptive),
 'cycle_renamed_radical':validate(renamed),
 'late_return':validate(late),
}
assert baseline==[]
assert hostile['readout_only']==['readout_only_recovery']
assert hostile['adaptive_cycle']==['adaptive_cycle_quotient']
assert hostile['cycle_renamed_radical']==['interval_cycle_promoted_to_green_radical']
assert hostile['late_return']==['labels_erased_before_return_test']
unresolved=[contract['green_form']['matrix_rank_witness'],contract['green_radical']['range_nondegeneracy_witness']]
out={'schema':'marici.synthetic-g4-recovery-radical.v1','status':'passed_with_external_witness_blocker',
 'contract_status':'test_fixture_only','baseline_errors':baseline,'hostile_results':hostile,
 'unresolved_external_witnesses':unresolved,
 'claim_boundary':'Pass checks declaration shape and hostile-test sensitivity only. Radical equality and range nondegeneracy remain unproved until the two external witnesses are supplied.'}
(ROOT/'results/synthetic-g4-recovery-radical.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
