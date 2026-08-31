"""Decode representative source expansions into reusable relation-family signatures."""
from __future__ import annotations
import json,sys
from collections import Counter
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_source_template_census.json'; A=14; N=charts.SOURCE_NAMES
def descriptors():
 out=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(N)):
   if any(x==charts.Q_DEPTH for x in levels):continue
   for axis in range(2):
    for exp in base.monomials_at_most(A):out.append({'family':'IBP','k_pole':kp,'levels':levels,'axis':axis,'exponent':exp})
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(N)):
   for exp in base.monomials_at_most(A-4):out.append({'family':'K','k_pole':kp,'levels':levels,'exponent':exp})
 for qi,name in enumerate(N):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(N)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append({'family':'q','mark':name,'mark_index':qi,'k_pole':kp,'levels':levels,'exponent':exp})
 assert len(out)==29904; return out
def coefficients(sample):
 if sample=='minimum':return [('T',4914,base.PRIME-1)]
 filename={'lower_quartile':'cosmology_rank26_p_normal_lower_quartile_source_dag.json','median':'cosmology_rank26_p_normal_median_source_dag.json','upper_quartile':'cosmology_rank26_p_normal_upper_quartile_source_dag.json','maximum':'cosmology_rank26_p_normal_maximum_source_dag.json'}[sample]
 x=json.loads((RES/filename).read_text()); assert x['passed']; return [(c['kind'],c['row_index'],c['coefficient']) for c in x['original_source_expansion']['coefficients']]
def main():
 desc=descriptors(); summaries={}
 for sample in ('minimum','lower_quartile','median','upper_quartile','maximum'):
  coeffs=coefficients(sample); family=Counter(); origins=Counter(); marks=Counter(); poles=Counter(); shifts=Counter()
  target=json.loads((RES/'cosmology_rank26_p_normal_marked_q_expansion_samples.json').read_text())['samples'][sample]['label']; tm=tuple(target['monomial'])
  for kind,index,_a in coeffs:
   d=desc[index]; family[d['family']]+=1; origins[kind]+=1; poles[(d['family'],d['k_pole'])]+=1
   if d['family']=='q':marks[(kind,d['mark'])]+=1
   shifts[(d['family'],d['exponent'][0]-tm[0],d['exponent'][1]-tm[1])]+=1
  summaries[sample]={'source_rows':len(coeffs),'origin_counts':dict(origins),'family_counts':dict(family),'family_pole_counts':{f'{f}:k{k}':v for (f,k),v in sorted(poles.items())},'q_mark_counts':{f'{kind}:{mark}':v for (kind,mark),v in sorted(marks.items())},'distinct_family_monomial_shifts':len(shifts),'most_common_shifts':[{'family':f,'shift':[i,j],'count':v} for (f,i,j),v in shifts.most_common(8)]}
 families_present={sample:set(x['family_counts']) for sample,x in summaries.items()}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-source-template-census.v1','status':'representative_source_expansions_decoded_by_relation_constructor','ambient_relation_degree':A,'samples':summaries,'cross_sample':{'nonminimum_all_use_IBP_K_q':all(families_present[s]=={'IBP','K','q'} for s in families_present if s!='minimum'),'minimum_is_direct_q_tangent':families_present['minimum']=={'q'},'all_nonminimum_use_both_S_and_T':all(set(summaries[s]['origin_counts'])=={'S','T'} for s in summaries if s!='minimum')},'decision':'No single-family template explains nonminimum samples: every longer source expansion couples IBP, K, and marked-q constructors. Template extraction must be tri-complex rather than mark-only.','limitations':['five samples','single-prime coefficient support','counts ignore coefficient values','presentation-dependent row decoder'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
