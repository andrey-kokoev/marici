"""Single DPC audit of symmetric raw jets of orders three through six."""
from __future__ import annotations
import json,math,os,sys
from collections import Counter
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_higher_jet_degree_six_audit.json';P=32003
def reduce_sparse(row,basis,insert=False):
 r={c:v%P for c,v in row.items() if v%P}
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:q=pow(r[p],-1,P);r={c:(v*q)%P for c,v in r.items()};basis[p]=r
   return r
  a=r[p]
  for c,v in b.items():
   z=(r.get(c,0)-a*v)%P
   if z:r[c]=z
   else:r.pop(c,None)
 return r
def monomials(k):return [(i,j,k-i-j) for i in range(k+1) for j in range(k-i+1)]
def directional_basis(k):
 mons=monomials(k);basis={};out=[]
 for a in range(-4,5):
  for b in range(-4,5):
   v=(1,a,b);row={i:pow(v[0],e[0],P)*pow(v[1]%P,e[1],P)*pow(v[2]%P,e[2],P)%P for i,e in enumerate(mons)};before=len(basis);reduce_sparse(row,basis,True)
   if len(basis)>before:out.append(v)
   if len(out)==len(mons):return mons,out
 raise AssertionError((k,len(out),len(mons)))
def derivative_rows(cols,point,direction,order):
 samples=adapter.sampled_rows(cols,point,direction);w=rees.interpolation_weights(order);return [rees.combine(rows,w) for rows in zip(*samples,strict=True)]
def main():
 old=base.PRIME;base.PRIME=P
 try:
  gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,(1,-1,0));source=T+raw[nI:nI+nK]+raw[nI+nK:];image={}
  for row in source:reduce_sparse(row,image,True)
  targets=[];desc_index={d:i for i,d in enumerate(all_desc)}
  for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
   for rec in json.loads((RES/name).read_text())['records']:targets.append((family,desc_index[tr.target_desc(family,rec)]))
  assert len(targets)==1224;census={};examples=[];total=0;nonzero=0
  for order in range(3,7):
   mons,dirs=directional_basis(order);oc=Counter();raw_counts=[]
   for ci,d in enumerate(dirs):
    rows=derivative_rows(cols,point,d,order);raw_counts.append(sum(bool(r) for r in rows))
    for family,i in targets:
     rem=reduce_sparse(rows[i],image,False);oc[f'{family}:{"nonzero" if rem else "zero"}']+=1;total+=1
     if rem:
      nonzero+=1
      if len(examples)<30:examples.append({'order':order,'basis_index':ci,'direction':d,'family':family,'target_index':i,'residual_support':len(rem)})
   census[str(order)]={'symmetric_dimension':len(mons),'directional_basis_size':len(dirs),'targets_tested':len(dirs)*len(targets),'raw_nonzero_row_min':min(raw_counts),'raw_nonzero_row_max':max(raw_counts),'quotient_census':dict(sorted(oc.items()))}
 finally:base.PRIME=old
 assert total==1224*sum(math.comb(k+2,2) for k in range(3,7))==90576
 out={'schema':'marici.voevodsky.cosmology-higher-jet-degree-six-audit.v1','problem':'Does any raw xyz derivative of orders three through six survive the unchanged relation quotient?','bold_conjecture':'At least one higher symmetric derivative has a nonzero quotient class and can remain a candidate for a higher connecting mechanism.','named_rivals':['every higher derivative is exact in the unchanged image','the interpolation degree bound makes orders above six identically zero','raw higher derivatives do not define connecting maps without a sourced jet extension'],'risky_consequences':['a spanning directional basis exists for each Sym^k(Q^3), k=3..6','at least one of 90,576 bounded modular residuals is nonzero','a higher-order extension and admissibility rule is separately defined'],'strongest_falsification':{'field':P,'source_image_rank':len(image),'orders':census,'total_residuals':total,'nonzero_residuals':nonzero,'examples':examples},'disposition':{'status':('higher_jet_modular_survivors_found' if nonzero else 'all_higher_jet_residuals_zero_mod_32003'),'claim_boundary':'This tests raw derivative membership in the unchanged algebraic quotient; no higher connecting morphism or geometric class is defined.','degree_exhaustion':'Orders above six vanish by the verified interpolation degree bound.'},'next_gate':('classify-higher-jet-modular-survivors' if nonzero else 'test-higher-jet-exact-membership'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
