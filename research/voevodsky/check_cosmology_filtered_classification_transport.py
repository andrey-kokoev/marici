"""Classify twelve filtered classes and test their two A14 transports exactly."""
from __future__ import annotations
import json,os,sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as ex
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_filtered_classification_transport.json'
def grade(d):
 if d[0] in ('IBP','K'):return d[1]+sum(d[2])+1
 return d[2]+sum(d[3])+1
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def reduce(row,basis,insert=False):
 r={c:Fraction(v) for c,v in row.items() if v}
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:inv=1/r[p];r={c:v*inv for c,v in r.items()};basis[p]=r
   return r
  add(r,b,-r[p])
 return r
def encode_label(x):return list(x) if isinstance(x,tuple) else x
def build(A,requests,point):
 oldA=rees.AMBIENT;rees.AMBIENT=A
 try:
  _,cols=rees.column_packet();inverse={i:l for l,i in cols.items()};ibp,K,q=tr.descs(A);alls=ibp+K+q;nI=len(ibp);nK=len(K);packets={};oldp=base.PRIME
  for p in ex.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,(1,-1,0));D2,_=adapter.derivative_rows(cols,point,(3,0,-1));packets[p]={'source':T+raw[nI:nI+nK]+raw[nI+nK:],'target':D2}
  base.PRIME=oldp;descs=alls+K+q;grades=[grade(d) for d in descs];allowed=[i for i,g in enumerate(grades) if g<=8];exact={i:ex.exact_row([packets[p]['source'][i] for p in ex.PS]) for i in allowed};ordered=sorted(allowed,key=lambda i:(grades[i],i));basis={};cursor=0;idx={d:i for i,d in enumerate(alls)};out=[];ranks={}
  for g in (6,7,8):
   while cursor<len(ordered) and grades[ordered[cursor]]<=g:reduce(exact[ordered[cursor]],basis,True);cursor+=1
   ranks[str(g)]=len(basis)
   for tid,d,axis in requests:
    if grade(d)!=g:continue
    target=ex.exact_row([packets[p]['target'][idx[d]] for p in ex.PS]);rem=reduce(target,basis,False);terms=[{'column_label':encode_label(inverse[c]),'numerator':v.numerator,'denominator':v.denominator} for c,v in sorted(rem.items())];out.append({'target_id':tid,'axis_square':axis,'descriptor':d,'grade':g,'residual_support':len(rem),'residual_terms':terms})
  return ranks,out
 finally:rees.AMBIENT=oldA
def main():
 bad=json.loads((RES/'cosmology_filtered_violation_full_image.json').read_text())['nonmembers'];ids={x['target_id'] for x in bad};gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);descs={}
 for r in json.loads((RES/'cosmology_q_exact_source_certificates_a12.json').read_text())['records']:
  tid=r['source_certificate']['canonical_target_id']
  if tid in ids:descs[tid]=tr.target_desc('q',r)
 assert len(descs)==12;req12=[(tid,d,'base') for tid,d in descs.items()];req14=[(tid,tr.shift(d,a),('x2' if a==0 else 'y2')) for tid,d in descs.items() for a in (0,1)];r12,c12=build(12,req12,point);r14,c14=build(14,req14,point);assert len(c12)==12 and len(c14)==24 and all(x['residual_support'] for x in c12+c14)
 grade_census=Counter(grade(d) for d in descs.values());qi_census=Counter(d[1] for d in descs.values());orbit_signatures={(d[1],d[2],d[3],tuple(e%2 for e in d[4])) for d in descs.values()};swaps=0;values=set(descs.values())
 for d in values:
  e=d[4];sw=('q',d[1],d[2],d[3],(e[1],e[0]));swaps+=sw in values
 out={'schema':'marici.voevodsky.cosmology-filtered-classification-transport.v1','status':'twelve_classes_persist_under_both_generating_A14_transports','grade_census':dict(sorted(grade_census.items())),'q_index_census':dict(sorted(qi_census.items())),'parity_orbit_count':len(orbit_signatures),'xy_swap_closed_targets':swaps,'A12_filtered_ranks':r12,'A14_filtered_ranks':r14,'A12_classes':c12,'A14_transports':c14,'decision':'All twelve exact filtered classes persist under both squared-axis generators at A14. Each descriptor defines a parity-orbit candidate; all-even persistence still requires exclusion of later-degree killers.','claim_boundary':'Canonical residual coordinates use the ordered exact row-echelon convention. Algebraic pole filtration only; no DNC, Bockstein, or geometric class.','next_gate':'test-filtered-class-persistence-A16-and-induction','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('A12_classes','A14_transports')},indent=2))
if __name__=='__main__':main()
