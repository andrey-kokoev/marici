"""DPC test of A16 persistence and the all-even no-killer inference."""
from __future__ import annotations
import json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_source_word_axis_square_transport as tr
import check_cosmology_filtered_classification_transport as classify
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_filtered_A16_persistence_induction.json'
def shift(d,path):
 for a in path:d=tr.shift(d,a)
 return d
def main():
 prior=json.loads((RES/'cosmology_filtered_violation_full_image.json').read_text());ids={x['target_id'] for x in prior['nonmembers']};gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);descs={}
 for r in json.loads((RES/'cosmology_q_exact_source_certificates_a12.json').read_text())['records']:
  tid=r['source_certificate']['canonical_target_id']
  if tid in ids:descs[tid]=tr.target_desc('q',r)
 paths={(0,0):'xx',(0,1):'xy',(1,0):'yx',(1,1):'yy'};req=[(tid,shift(d,p),label) for tid,d in descs.items() for p,label in paths.items()];ranks,classes=classify.build(16,req,point);assert len(classes)==48 and all(x['residual_support'] for x in classes)
 lookup={(x['target_id'],x['axis_square']):x for x in classes};mixed_equal=0
 for tid in ids:
  a=lookup[(tid,'xy')];b=lookup[(tid,'yx')];assert a['descriptor']==b['descriptor'] and a['residual_terms']==b['residual_terms'];mixed_equal+=1
 support=Counter(x['residual_support'] for x in classes);contract={'filtered_quotient_maps_induced_by_axis_shifts':True,'exponent_parity_preserved':True,'A12_A14_A16_nonvanishing_checked':True,'injectivity_of_filtered_quotient_maps':False,'colon_or_saturation_no_killer_theorem':False,'direct_sum_decomposition_excluding_later_same_parity_generators':False}
 out={'schema':'marici.voevodsky.cosmology-filtered-A16-persistence-induction.v1','problem':'Do A12/A14/A16 persistence and parity preservation prove all-even survival of the twelve filtered classes?','bold_conjecture':'Finite path persistence plus parity-orbit transport excludes every later same-grade killer.','named_rivals':['later source generators in the same parity sector kill a transported class','filtered quotient maps are not injective','a colon/saturation theorem supplies the missing no-killer result'],'risky_consequences':['all 48 A16 path classes are nonzero','mixed paths agree','each filtered quotient transport map is injective'],'strongest_falsification':{'A16_filtered_ranks':ranks,'A16_nonzero_paths':len(classes),'mixed_path_equalities':mixed_equal,'residual_support_census':{str(k):v for k,v in sorted(support.items())},'induction_contract':contract},'disposition':{'status':'finite_persistence_verified_all_even_induction_blocked','surviving_scope':'Twelve classes persist on every tested path through A16.','first_missing_typed_object':'An injectivity or colon/saturation theorem for squared-axis multiplication on the grade-bounded quotient.','acceptance_test':'Prove (im d1 at grade g : x^2)=im d1 and similarly for y^2 on each relevant parity sector, or compute an equivalent injective quotient transport.'},'A16_classes':classes,'next_gate':'test-filtered-quotient-colon-saturation','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='A16_classes'},indent=2))
if __name__=='__main__':main()
