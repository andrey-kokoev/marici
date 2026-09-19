import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/aspect/scc'))
from categorical_compiler import compile_diagram
from formula_synthesizer import synthesize_bridges

DIAGRAM=ROOT/'research/nima/contracts/evans-euler-comparison-structure.v1.json'
FORMULAS=ROOT/'research/nima/contracts/evans-euler-low-moment-formula-system.v1.json'
HOSTILE=ROOT/'research/nima/results/low-cumulants-do-not-select-det3-operator.json'
OUT=ROOT/'research/nima/results/evans-euler-comparison-structure-audit.json'

def load(path):
 return json.loads(path.read_text(encoding='utf-8'))

def main():
 categorical=compile_diagram(load(DIAGRAM))
 formulas=synthesize_bridges(load(FORMULAS))
 hostile=load(HOSTILE)
 fiber=categorical['fibers'][0]['comparisons'][0]
 promotion=categorical['promotions'][0]
 checks={
  'diagram_well_typed':not categorical['errors'],
  'same_profile_not_realization_equivalence':fiber['same_profile'] and not fiber['verified_equivalent'],
  'common_operator_promotion_refused':not promotion['admitted'],
  'connected_coordinate_underdetermined':formulas['bridge_status']=='underdetermined' and 'common_operator_from_low_readouts.connected_coordinate' in formulas['missing_source_formulas'],
  'exact_hostile_passes':hostile.get('passed') is True and hostile['checks']['different_fredholm_determinant'],
  'common_operator_claim_missing_source': 'source_constructor_K_G_a' in categorical['inverse_design']['common_operator_claim']['missing'],
  'packet_clutching_claim_missing_source': 'source_constructor_F_Ev' in categorical['inverse_design']['packet_clutching_claim']['missing'],
  'packet_clutching_is_less_assumptive':len(categorical['inverse_design']['packet_clutching_claim']['missing']) < len(categorical['inverse_design']['common_operator_claim']['missing'])
 }
 assert all(checks.values()),checks
 out={'schema':'marici.nima.evans-euler-comparison-structure-audit.v1','classification':'common_operator_realization_not_admitted_packet_clutching_is_the_less_assumptive_open_structure','checks':checks,'categorical':categorical,'formula_synthesis':formulas,'hostile_ref':'research/nima/results/low-cumulants-do-not-select-det3-operator.json','next_constructor':'Construct the source map F_Ev from the transverse Evans carrier to the joint response graph, without assuming a common Schatten operator. Then compile the induced line clutching, cutoff variance, completion topology, and noncollapse cell.','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'classification':out['classification'],'checks':checks,'common_operator_missing':categorical['inverse_design']['common_operator_claim']['missing'],'packet_clutching_missing':categorical['inverse_design']['packet_clutching_claim']['missing'],'passed':True},indent=2))
if __name__=='__main__':main()
