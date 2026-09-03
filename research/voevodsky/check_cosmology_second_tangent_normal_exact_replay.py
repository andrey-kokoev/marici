"""Replay certificate-local exact spans for a second tangent and unit normal."""
from __future__ import annotations
import json,os,sys,math
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_second_tangent_normal_exact_replay.json';LOCAL=RES/'cosmology_second_direction_local_exact_words.json'
def add(out,row,a):
 for c,v in row.items():
  z=out.get(c,Fraction())+a*v
  if z:out[c]=z
  else:out.pop(c,None)
def solve_local(rows,target):
 n=len(rows)
 if n==0:return [] if not target else None
 M=[{c:Fraction(v) for c,v in row.items()} for row in rows];order=list(range(n));piv=[]
 for r in range(n):
  col=min((c for i in range(r,n) for c,v in M[i].items() if v),default=None)
  if col is None:return None
  p=next(i for i in range(r,n) if M[i].get(col));M[r],M[p]=M[p],M[r];order[r],order[p]=order[p],order[r];q=M[r][col];M[r]={c:v/q for c,v in M[r].items()}
  for i in range(n):
   if i==r or not M[i].get(col):continue
   q=M[i][col];row=dict(M[i]);add(row,M[r],-q);M[i]=row
  piv.append(col)
 A=[[Fraction(rows[j].get(c,0)) for j in range(n)] for c in piv];b=[Fraction(target.get(c,0)) for c in piv]
 # square elimination
 aug=[A[i]+[b[i]] for i in range(n)]
 for c in range(n):
  p=next((i for i in range(c,n) if aug[i][c]),None)
  if p is None:return None
  aug[c],aug[p]=aug[p],aug[c];q=aug[c][c];aug[c]=[v/q for v in aug[c]]
  for i in range(n):
   if i!=c and aug[i][c]:q=aug[i][c];aug[i]=[x-q*y for x,y in zip(aug[i],aug[c])]
 coef=[aug[i][-1] for i in range(n)];recon={}
 for a,row in zip(coef,rows):add(recon,row,a)
 return coef if recon=={c:Fraction(v) for c,v in target.items()} else None
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);t1=tuple(gate['integral_unit_normals']['p_tangent_difference']);t2=(3,0,-1);n2=(-2,0,1);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);packets={};old=base.PRIME
 try:
  for p in exact.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);D2,_=adapter.derivative_rows(cols,point,t2);N2,_=adapter.derivative_rows(cols,point,n2);packets[p]={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:],'t2':D2,'n2':N2}
 finally:base.PRIME=old
 cache={}
 def erow(kind,i):
  key=(kind,i)
  if key not in cache:cache[key]=exact.exact_row([packets[p][kind][i] for p in exact.PS])
  return cache[key]
 files=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')];decode={'T':all_desc,'S_K':K,'Q':q};index={d:i for i,d in enumerate(all_desc)};fail={'t2':0,'n2':0};fail_ids={'t2':set(),'n2':set()};fail_family={'t2':{},'n2':{}};examples=[];local_words=[];tested=0
 for family,name in files:
  for record in json.loads((RES/name).read_text())['records']:
   tested+=1;c=record['source_certificate'];rows=[erow(k,i) for k,i in c['source_basis']];ti=index[tr.target_desc(family,record)]
   for kind in ('t2','n2'):
    coef=solve_local(rows,erow(kind,ti))
    if coef is None:
     fail[kind]+=1;fail_ids[kind].add(c['canonical_target_id']);fail_family[kind][family]=fail_family[kind].get(family,0)+1
     if len(examples)<20:examples.append({'family':family,'target_id':c['canonical_target_id'],'direction':kind,'local_basis_size':len(rows)})
    elif kind=='t2':
     terms=[{'kind':k,'row_index':i,'numerator':a.numerator,'denominator':a.denominator} for (k,i),a in zip(c['source_basis'],coef) if a]
     local_words.append({'target_id':c['canonical_target_id'],'family':family,'word_terms':terms})
 assert tested==1224 and fail_ids['t2']==fail_ids['n2'] and len(local_words)==834
 LOCAL.write_text(json.dumps({'schema':'marici.voevodsky.second-direction-local-exact-words.v1','records':local_words},indent=2)+'\n')
 complete=not any(fail.values())
 out={'schema':'marici.voevodsky.cosmology-second-tangent-normal-exact-replay.v1','status':('full_normal_torsor_zero_on_certified_local_spans' if complete else 'certificate_local_spans_do_not_settle_second_direction'),'directions':{'second_tangent':[3,0,-1],'derived_unit_normal':[-2,0,1]},'certificates_tested':tested,'local_exact_replay_failures':fail,'failure_family_census':fail_family,'coincident_failure_sets':True,'unresolved_target_ids':sorted(fail_ids['t2']),'local_word_file':str(LOCAL.relative_to(ROOT)).replace('\\','/'),'examples':examples,'decision':('Both new directions are exactly absorbed for every certified target; nx plus the two tangent generators covers the integral unit-normal torsor.' if complete else 'Failure in a certificate-local span is not a nonzero quotient witness; full-image membership remains required for the listed targets.'),'scope':'Exact characteristic-zero labelled algebraic presentation; no geometric normal bundle or exceptional map.','next_gate':('classify-full-normal-torsor-zero-consequence' if complete else 'compute-second-direction-full-image-membership'),'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
