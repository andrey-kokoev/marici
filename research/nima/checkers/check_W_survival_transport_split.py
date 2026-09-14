"""Separate proved native/endpoint W survival from open physical transport."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 d=json.loads(Path(a.input).read_text());c=d['all_check_categories']
 keys=('decomposable_term_nonzero_in_native_algebra','decomposable_reflection_action_nonzero_at_endpoint','comparison_fibre_endpoint_relative_class_retained','endpoint_integral_detector','primitive_endpoint_orientation')
 checks={k:c[k] for k in keys};assert all(v>0 for v in checks.values())
 scope=' '.join(d['scope'])
 assert 'No physical collar/Verdier identification' in scope
 out={'schema':'marici.nima.W-survival-transport-split.v1','status':'passed',
  'proved_native_endpoint_survival':checks,
  'open_transport':'physical collar/Verdier identification and conormal readout',
  'conclusion':'W is nonzero natively and at the endpoint comparison fibre; only injective/nonannihilating transport to the physical readout remains'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
