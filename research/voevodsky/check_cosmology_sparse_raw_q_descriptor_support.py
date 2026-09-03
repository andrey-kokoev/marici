"""Classify descriptor support of the sparse raw-q certificate bases."""
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_sparse_raw_q_descriptor_support.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def key(d):return json.dumps(d,separators=(',',':'))
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());sp=json.loads((RES/'cosmology_sparse_raw_q_certificates.json').read_text());groups=[];unions=[]
 for rg,sg in zip(raw['groups'],sp['groups']):
  maps=[];descs={}
  for c in rg['certificates']:
   m={}
   for t in c['raw_q_terms']:k=key(t['descriptor']);m[k]=q(t['coefficient']);descs[k]=t['descriptor']
   maps.append(m)
  supports=[]
  for b in sg['sparse_basis']:
   lam=[q(x) for x in b['combination_on_echelon_certificates']];ks=set().union(*[set(m) for m in maps]);v={k:sum(lam[i]*maps[i].get(k,Fraction()) for i in range(3)) for k in ks};supports.append({k for k,a in v.items() if a})
  union=set().union(*supports);inter=set.intersection(*supports);unions.append(union);gc=Counter(descs[k][2]+sum(descs[k][3])+1 for k in union);par=Counter(tuple(e%2 for e in descs[k][4]) for k in union);groups.append({'grade':rg['grade'],'basis_supports':[len(x) for x in supports],'support_union':len(union),'support_intersection':len(inter),'relation_grade_census':{str(k):v for k,v in sorted(gc.items())},'exponent_parity_census':{str(k):v for k,v in sorted(par.items())}})
 overlap=len(unions[0]&unions[1]);out={'schema':'marici.voevodsky.cosmology-sparse-raw-q-descriptor-support.v1','status':'sparse_descriptor_support_classified','groups':groups,'cross_grade_exact_descriptor_overlap':overlap,'grade7_union_contained_in_grade8_union':unions[0]<=unions[1],'decision':'Sparse certificate supports are classified by relation grade and exponent parity; exact cross-grade overlap tests whether grade 8 extends the grade-7 support family.','claim_boundary':'Support depends on the selected sparse basis and canonical raw-q descriptor normalization.','next_gate':'derive-or-falsify-cross-grade-support-extension','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
