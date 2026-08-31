"""Factor representative tangent corrections against target pole and g1 level."""
from __future__ import annotations
import json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import check_cosmology_rank26_p_normal_source_template_census as census
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_tangent_envelope.json'
def main():
 prior=json.loads((RES/'cosmology_rank26_p_normal_tricomplex_block_template.json').read_text()); assert prior['passed']
 sample_packet=json.loads((RES/'cosmology_rank26_p_normal_marked_q_expansion_samples.json').read_text()); desc=census.descriptors(); records={}
 for sample in ('minimum','lower_quartile','median','upper_quartile','maximum'):
  label=sample_packet['samples'][sample]['label']; target_k=label['k_pole']; g1_level=label['q_levels'][0]; tangent=[]
  for kind,index,_a in census.coefficients(sample):
   if kind!='T':continue
   d=desc[index]; tangent.append(d)
  poles=sorted({d['k_pole'] for d in tangent}); families=sorted({d['family'] for d in tangent}); qmarks=sorted({d['mark'] for d in tangent if d['family']=='q'}); qpoles=sorted({d['k_pole'] for d in tangent if d['family']=='q'})
  assert poles and max(poles)<=target_k
  assert set(qmarks)<= {'g1'}
  assert bool(qmarks)==(g1_level==2)
  records[sample]={'target_k_pole':target_k,'target_g1_level':g1_level,'T_source_rows':len(tangent),'T_families':families,'T_poles':poles,'T_q_marks':qmarks,'T_q_poles':qpoles,'pole_envelope_holds':True,'q_support_rule_holds':True}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-tangent-envelope.v1','status':'sample_dependent_tangent_corrections_obey_target_typed_envelope','samples':records,'observed_rules':{'pole_envelope':'every T source row has k_pole <= target k_pole','marked_q_support':'T marked-q rows use only g1','g1_activation':'T marked-q correction is present exactly when target g1 level is 2'},'decision':'The tangent correction is sample-dependent but not arbitrary: its pole support is bounded by the target pole, and its marked-q component is controlled by the target g1 level. Family counts and coefficients remain unfactored.','strength':'five-sample support rule, not a universal theorem','limitations':['five representatives','single prime','does not predict IBP/K family multiplicities','does not predict coefficients or monomial shifts'],'next_leaf':'test the target-typed envelope on additional non-quantile singleton columns before promoting it to a reusable conjecture','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
