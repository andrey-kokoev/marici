"""Exact outward quantization of giant directed component fractions to denominator 10^40."""
from fractions import Fraction as F
import json,sys
sys.set_int_max_str_digits(0)
D=10**40
def qlo(x):
 x=F(x);return F(x.numerator*D//x.denominator,D)
def qhi(x):
 x=F(x);return F(-((-x.numerator*D)//x.denominator),D)
def qiv(v):
 old=(F(v[0]),F(v[1]));new=(qlo(old[0]),qhi(old[1]));assert new[0]<=old[0]<=old[1]<=new[1];return old,new
files=['research/grothendieck/results/interval-undilated-septic-moments.json','research/grothendieck/results/interval-c-one-prime-and-jets.json']
count=0;max_added=F(0)
for path in files:
 data=json.load(open(path))
 for r in data['rows']:
  fields=['interval'] if 'interval' in r else ['f0','prime']+list(r.get('jets',{}).keys())
  for key in fields:
   v=r['jets'][key] if key not in r else r[key]
   old,new=qiv(v);count+=1;max_added=max(max_added,(new[1]-new[0])-(old[1]-old[0]))
assert count==39 and max_added<=F(2,D)
print(json.dumps({'schema':'marici.nima.fixed-precision-outward-quantization.v1','status':'passed','decimal_places':40,'interval_count':count,'max_added_width':float(max_added),'contains_every_source_interval':True,'claim_boundary':'quantization transport only; constants, tail, and Gram assembly remain separate'},sort_keys=True))
