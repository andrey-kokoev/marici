"""Extract the proved algebraic group part and the open physical parity part."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 d=json.loads(Path(a.input).read_text());c=d['all_check_categories'];t=d['actual_target_transport'];n=d['native_bar_source_and_action']
 required={k:c[k] for k in ('group_operation_comparison_has_zero_class','group_operation_comparison_is_closed','group_operation_integral_homotopy_equation','native_bar_group_chain_equivariance','native_endpoint_group_chain_equivariance','R_dihedral_transport_in_full_relative_algebra')}
 assert all(v>0 for v in required.values())
 assert 'no physical parity selected' in t['endpoint_labels']
 assert 's(W)=-W+' in n['decomposable_reflection']
 out={'schema':'marici.nima.candidate-group-reflection-split.v1','status':'passed',
  'proved_algebraic_group_checks':required,
  'reflection_formula':n['decomposable_reflection'],
  'physical_transport_status':t['endpoint_labels'],
  'conclusion':'group-operation zero-class and integral homotopy are proved on the native candidate; only selection/transport of physical reflection parity remains for the group field'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
