"""Test elementary typed grade-raising maps on sparse raw-q support unions."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_cross_grade_descriptor_shifts.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def key(d):return json.dumps(d,separators=(',',':'))
def support(group,sg):
 maps=[];descs={}
 for c in group['certificates']:
  m={}
  for t in c['raw_q_terms']:k=key(t['descriptor']);m[k]=q(t['coefficient']);descs[k]=t['descriptor']
  maps.append(m)
 out=set()
 for b in sg['sparse_basis']:
  lam=[q(x) for x in b['combination_on_echelon_certificates']]
  for k in set().union(*map(set,maps)):
   if sum(lam[i]*maps[i].get(k,Fraction()) for i in range(3)):out.add(k)
 return out,descs
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());sp=json.loads((RES/'cosmology_sparse_raw_q_certificates.json').read_text());u7,d7=support(raw['groups'][0],sp['groups'][0]);u8,d8=support(raw['groups'][1],sp['groups'][1]);tests=[]
 for kind,index in [('q_order',None)]+[('multiindex',i) for i in range(5)]:
  shifted=set()
  for k in u7:
   d=list(d7[k]);d[3]=list(d[3]);d[4]=list(d[4])
   if kind=='q_order':d[2]+=1
   else:d[3][index]+=1
   shifted.add(key(d))
  ov=len(shifted&u8);tests.append({'shift':kind if index is None else f'{kind}_{index}','source_count':len(shifted),'overlap':ov,'missing':len(shifted-u8),'target_extra':len(u8-shifted),'contained':shifted<=u8})
 best=max(tests,key=lambda x:x['overlap']);out={'schema':'marici.voevodsky.cosmology-cross-grade-descriptor-shifts.v1','status':'elementary_grade_shift_family_tested','tests':tests,'best_shift':best,'decision':'No elementary grade-raising shift is promoted unless its shifted grade-7 support is contained in grade-8 support.','claim_boundary':'Tests cover q-order and five single multiindex increments only; linear combinations or basis changes are not excluded.','next_gate':('derive-contained-cross-grade-shift' if best['contained'] else 'classify-cross-grade-support-replacement'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
