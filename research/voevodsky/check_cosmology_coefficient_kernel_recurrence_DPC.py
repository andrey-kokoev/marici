"""DPC test of the all-even coefficient-kernel recurrence conjecture."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_coefficient_kernel_recurrence_DPC.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());a16=json.loads((RES/'cosmology_A16_raw_q_detector.json').read_text());a18=json.loads((RES/'cosmology_A18_raw_q_detector.json').read_text());ids=a16['target_order'];K14=[]
 for c in raw['groups'][1]['certificates']:
  m={x['target_id']:q(x['coefficient']) for x in c['target_coefficients']};K14.append([m.get(i,Fraction()) for i in ids])
 def basis(d):return [[q(x) for x in row] for row in d['relation_basis']]
 K16,K18=basis(a16),basis(a18);assert a18['target_order']==ids and K14==K16==K18 and len(K14)==3
 out={'schema':'marici.voevodsky.cosmology-coefficient-kernel-recurrence-DPC.v1','status':'finite_recurrence_corroborated_not_established','conjecture':'The canonical three-dimensional coefficient-relation kernel is unchanged under every even x2 ambient shift from A14 onward.','attempted_construction':'Compare exact canonical echelon relation bases at A14, A16, and A18 in one fixed target order.','exact_witness':{'ambient_indices':[14,16,18],'target_order':ids,'common_relation_basis':[[enc(x) for x in row] for row in K14]},'DPC_disposition':'corroborated_at_two_successive_steps; all-even theorem not established','falsifier':'At the first later even A, a rank other than three or any changed normalized relation-basis coefficient falsifies the recurrence.','surviving_alternatives':['eventual change after A18','stable kernel with changing detector coordinates','basis stability caused by finite interpolation range only'],'next_discriminating_test':'Construct A20 grade-eight x4 targets and compare their exact relation basis.','next_gate':'test-coefficient-kernel-recurrence-A20','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='exact_witness'},indent=2))
if __name__=='__main__':main()
