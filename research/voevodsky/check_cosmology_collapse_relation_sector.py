"""Locate which cumulative relation sector causes the four-to-one target collapse."""
from __future__ import annotations
import json,os,sys
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as ex
import check_cosmology_source_word_axis_square_transport as tr
import check_cosmology_filtered_classification_transport as clf
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_collapse_relation_sector.json'
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
 r=dict(r)
 while r and min(r) in b:add(r,b[min(r)],-r[min(r)])
 return r
def rank(rows):
 b={}
 for r in rows:insert(r,b)
 return len(b)
def main():
 oldA=rees.AMBIENT;oldp=base.PRIME;rees.AMBIENT=14
 try:
  _,cols=rees.column_packet();ibp,K,q=tr.descs(14);alls=ibp+K+q;nA=len(alls);nK=len(K);descs=alls+K+q;grades=[clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in ex.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,(1,-1,0));D2,_=adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  exact=[ex.exact_row([pack[p]['source'][i] for p in ex.PS]) for i in range(len(descs))];idx={d:i for i,d in enumerate(alls)};c=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());groups=[]
  for g in (7,8):
   records=[x for x in c['A14_transports'] if x['grade']==g and x['axis_square']=='x2'];targets=[ex.exact_row([pack[p]['target'][idx[tuple([r['descriptor'][0],r['descriptor'][1],r['descriptor'][2],tuple(r['descriptor'][3]),tuple(r['descriptor'][4])])]] for p in ex.PS]) for r in records];basis={};stages=[]
   bounds=[('T',0,nA),('raw_K',nA,nA+nK),('raw_q',nA+nK,len(descs))]
   for name,lo,hi in bounds:
    for i in range(lo,hi):
     if grades[i]<=g:insert(exact[i],basis)
    stages.append({'after_sector':name,'relation_rank':len(basis),'target_quotient_rank':rank([reduce(t,basis) for t in targets])})
   canonical_basis={}
   for i in sorted((i for i in range(len(descs)) if grades[i]<=g),key=lambda i:(grades[i],i)):insert(exact[i],canonical_basis)
   groups.append({'grade':g,'raw_target_rank':4,'stages':stages,'same_packet_canonical_order_rank':len(canonical_basis)})
  expected=c['A14_filtered_ranks'];mismatch=[{'grade':x['grade'],'computed_relation_rank':x['stages'][-1]['relation_rank'],'reference_relation_rank':expected[str(x['grade'])]} for x in groups if x['stages'][-1]['relation_rank']!=expected[str(x['grade'])]]
  ok=not mismatch
  out={'schema':'marici.voevodsky.cosmology-collapse-relation-sector.v1','status':('cumulative_relation_sector_localized' if ok else 'packet_alignment_mismatch'),'groups':groups,'rank_mismatches':mismatch,'decision':('Canonical packet alignment is restored; the staged target ranks localize the collapse.' if ok else 'The cumulative reconstruction disagrees with canonical A14 ranks, so sector attribution is not admitted.'),'claim_boundary':'Sector localization does not identify unique generators inside the effective sector.','next_gate':('extract-minimal-collapse-relations-in-first-effective-sector' if ok else 'reconcile-A14-source-packet-indexing'),'passed':ok};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
 finally:base.PRIME=oldp;rees.AMBIENT=oldA
if __name__=='__main__':main()
