"""Construct exact raw-q certificates for the grade-7/8 four-to-one collapse."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_collapse_relation_sector as s
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_raw_q_collapse_certificates.json'
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def insert(r,b):
 r={c:Fraction(v) for c,v in r.items()}
 while r:
  p=min(r)
  if p not in b:
   q=1/r[p];b[p]={c:v*q for c,v in r.items()};return
  add(r,b[p],-r[p])
def reduce(r,b):
 r={c:Fraction(v) for c,v in r.items()}
 while r and min(r) in b:add(r,b[min(r)],-r[min(r)])
 return r
def insert_track(r,combo,b):
 r={c:Fraction(v) for c,v in r.items()};w=dict(combo)
 while r:
  p=min(r)
  if p not in b:
   q=1/r[p];b[p]=({c:v*q for c,v in r.items()},{i:v*q for i,v in w.items()});return None
  br,bw=b[p];a=r[p];add(r,br,-a);add(w,bw,-a)
 return w
def relations(rows):
 b={};out=[]
 for i,r in enumerate(rows):
  d=insert_track(r,{i:Fraction(1)},b)
  if d is not None:out.append(d)
 return out
def enc(v):return {'numerator':v.numerator,'denominator':v.denominator}
def main():
 oldA=s.rees.AMBIENT;oldp=s.base.PRIME;s.rees.AMBIENT=14
 try:
  _,cols=s.rees.column_packet();ibp,K,q=s.tr.descs(14);alls=ibp+K+q;nA=len(alls);nK=len(K);descs=alls+K+q;grades=[s.clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in s.ex.PS:
   s.base.PRIME=p;raw=list(s.rees.raw_relations(point,cols));T,_=s.adapter.derivative_rows(cols,point,(1,-1,0));D2,_=s.adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  s.base.PRIME=oldp;exact=[s.ex.exact_row([pack[p]['source'][i] for p in s.ex.PS]) for i in range(len(descs))];idx={d:i for i,d in enumerate(alls)};c=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());groups=[]
  for g in (7,8):
   tk={}
   for i in range(nA+nK):
    if grades[i]<=g:insert(exact[i],tk)
   qids=[i for i in range(nA+nK,len(descs)) if grades[i]<=g];qb={}
   for i in qids:insert_track(reduce(exact[i],tk),{i:Fraction(1)},qb)
   records=[x for x in c['A14_transports'] if x['grade']==g and x['axis_square']=='x2'];rawtargets=[s.ex.exact_row([pack[p]['target'][idx[tuple([r['descriptor'][0],r['descriptor'][1],r['descriptor'][2],tuple(r['descriptor'][3]),tuple(r['descriptor'][4])])]] for p in s.ex.PS]) for r in records];pre=[reduce(t,tk) for t in rawtargets];full=[reduce(x,{p:r for p,(r,w) in qb.items()}) for x in pre];deps=relations(full);assert len(deps)==3;certs=[]
   for dep in deps:
    u={}
    for j,a in dep.items():add(u,pre[j],a)
    sol={};r=dict(u)
    while r:
     p=min(r);br,bw=qb[p];a=r[p];add(r,br,-a);add(sol,bw,a)
    certs.append({'target_coefficients':[{'target_id':records[j]['target_id'],'coefficient':enc(a)} for j,a in sorted(dep.items())],'raw_q_support_count':len(sol),'raw_q_terms':[{'descriptor':descs[i],'coefficient':enc(a)} for i,a in sorted(sol.items())]})
   groups.append({'grade':g,'certificate_count':len(certs),'certificates':certs})
  out={'schema':'marici.voevodsky.cosmology-raw-q-collapse-certificates.v1','status':'exact_raw_q_certificates_constructed','groups':groups,'decision':'Three independent exact target relations per grade are reconstructed entirely from raw-q rows after quotienting by T and raw-K.','claim_boundary':'The echelon certificates are exact but not proven support-minimal.','next_gate':'minimize-raw-q-collapse-certificate-support','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'support_counts':[[c['raw_q_support_count'] for c in x['certificates']] for x in groups],'passed':True},indent=2))
 finally:s.base.PRIME=oldp;s.rees.AMBIENT=oldA
if __name__=='__main__':main()
