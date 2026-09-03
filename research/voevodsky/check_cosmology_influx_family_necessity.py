"""Test whether every grade-eight collapse direction requires the new influx family."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_cross_grade_support_replacement as r
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_influx_family_necessity.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def rank(rows):
 b=[]
 for raw in rows:
  v=[Fraction(x) for x in raw]
  for p,w in b:
   a=v[p];v=[x-a*y for x,y in zip(v,w)]
  p=next((i for i,x in enumerate(v) if x),None)
  if p is not None:
   a=v[p];v=[x/a for x in v];b.append((p,v));b.sort()
 return len(b)
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());sp=json.loads((RES/'cosmology_sparse_raw_q_certificates.json').read_text());u7,d7=r.support(raw['groups'][0],sp['groups'][0]);u8,d8=r.support(raw['groups'][1],sp['groups'][1]);shifted=set()
 for k in u7:
  d=list(d7[k]);d[3]=list(d[3]);d[4]=list(d[4]);d[2]+=1;shifted.add(r.key(d))
 influx=sorted(u8-shifted);assert len(influx)==60;cs=raw['groups'][1]['certificates'];maps=[]
 for c in cs:maps.append({r.key(t['descriptor']):q(t['coefficient']) for t in c['raw_q_terms']})
 forms=[tuple(maps[i].get(k,Fraction()) for i in range(3)) for k in influx];rr=rank(forms);chosen=[]
 for k,v in zip(influx,forms):
  if rank([x[1] for x in chosen]+[v])>len(chosen):chosen.append((k,v))
  if len(chosen)==rr:break
 out={'schema':'marici.voevodsky.cosmology-influx-family-necessity.v1','status':('influx_restriction_injective' if rr==3 else 'collapse_directions_avoiding_influx_exist'),'influx_descriptor_count':len(influx),'restriction_rank':rr,'collapse_space_dimension':3,'restriction_kernel_dimension':3-rr,'per_echelon_certificate_influx_support':[sum(bool(m.get(k,Fraction())) for k in influx) for m in maps],'three_descriptor_detection_witness':[{'descriptor':d8[k],'coefficient_form':[{'numerator':x.numerator,'denominator':x.denominator} for x in v]} for k,v in chosen],'decision':('Every nonzero grade-eight collapse direction uses at least one influx-family row.' if rr==3 else 'Some collapse directions avoid the influx family.'),'claim_boundary':'Necessity is for this canonical raw-q coefficient representation modulo T and raw-K; it is not invariant under changing the raw-q generating family.','next_gate':'classify-three-descriptor-influx-detector','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
