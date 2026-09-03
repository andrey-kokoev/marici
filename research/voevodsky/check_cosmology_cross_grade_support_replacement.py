"""Classify lost and new descriptors under the best q-order grade shift."""
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_cross_grade_support_replacement.json'
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
def census(keys,descs):
 return {'count':len(keys),'relation_grade':dict(sorted(Counter(descs[k][2]+sum(descs[k][3])+1 for k in keys).items())),'parity':{str(k):v for k,v in sorted(Counter(tuple(e%2 for e in descs[k][4]) for k in keys).items())},'multiindex_zero_count':dict(sorted(Counter(sum(x==0 for x in descs[k][3]) for k in keys).items())),'exponent_boundary_axes':dict(sorted(Counter(sum(e==0 for e in descs[k][4]) for k in keys).items()))}
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());sp=json.loads((RES/'cosmology_sparse_raw_q_certificates.json').read_text());u7,d7=support(raw['groups'][0],sp['groups'][0]);u8,d8=support(raw['groups'][1],sp['groups'][1]);shifted={};
 for k in u7:
  d=list(d7[k]);d[3]=list(d[3]);d[4]=list(d[4]);d[2]+=1;shifted[key(d)]=d
 lost=set(shifted)-u8;new=u8-set(shifted);all_desc={**d8,**shifted};lc=census(lost,all_desc);nc=census(new,all_desc);out={'schema':'marici.voevodsky.cosmology-cross-grade-support-replacement.v1','status':'q_order_replacement_classified','matched':len(set(shifted)&u8),'lost':lc,'new':nc,'same_feature_censuses':{f:lc[f]==nc[f] for f in ('relation_grade','parity','multiindex_zero_count','exponent_boundary_axes')},'decision':'Lost and new q-order-shift descriptors are compared across grade, parity, multiindex sparsity, and exponent-boundary features.','claim_boundary':'Matching coarse censuses would not construct a descriptor bijection; differing censuses falsify control by that feature alone.','next_gate':'test-typed-replacement-bijection-on-surviving-features','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
