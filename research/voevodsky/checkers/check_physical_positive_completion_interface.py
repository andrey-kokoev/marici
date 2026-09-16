"""Audit the ordered bridge from internal charts to physical positive completion."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).parents[1];P=ROOT/'physical-positive-completion-interface.json';OUT=ROOT/'results'/'physical-positive-completion-interface.json'
def first_open(gates):
 for g in gates:
  if g['status'] is not True:return g['id']
 return None
def admit(gates):
 by={g['id']:g for g in gates}
 for g in gates:
  for dep in g.get('depends_on',[]):
   if dep not in by or by[dep]['status'] is not True:return False,'dependency:'+dep
  if g['status'] is not True:return False,g['id']
 return True,'admitted'
def main():
 d=json.loads(P.read_text());g=d['ordered_gates'];evidence_ok=all(Path(x['evidence']).exists() for x in g if x['status'] is True);fo=first_open(g)
 completed=copy.deepcopy(g)
 for x in completed:x['status']=True
 checks={'declared_first_open_is_computed':fo==d['first_open_gate'],'established_evidence_exists':evidence_ok,'current_interface_refused_at_common_subfeature':admit(g)==(False,'packet_independent_physical_common_subfeature'),'complete_fixture_admitted':admit(completed)==(True,'admitted'),'mosco_dependencies_explicit':set(g[-1]['depends_on'])=={'packet_independent_physical_common_subfeature','uniform_physical_residual_tail_bound','positive_sonin_endpoint_coupling'}}
 out={'schema':'marici.voevodsky.physical-positive-completion-interface-check.v1','checks':checks,'passed':all(checks.values()),'established':[x['id'] for x in g if x['status'] is True],'open':[x['id'] for x in g if x['status'] is not True],'first_open_gate':fo};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
