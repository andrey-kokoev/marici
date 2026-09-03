"""Exact kernel dimensions for squared-axis maps on grade-bounded quotients."""
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
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_filtered_quotient_colon_saturation.json'
def gdesc(d):
 if d[0] in ('IBP','K'):return d[1]+sum(d[2])+1
 return d[2]+sum(d[3])+1
def gcol(l):return l[0]+sum(l[1:-1])
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def insert(row,basis):
 r={c:Fraction(v) for c,v in row.items() if v}
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   inv=1/r[p];basis[p]={c:v*inv for c,v in r.items()};return True
  add(r,b,-r[p])
 return False
def build(A,point):
 oldA=rees.AMBIENT;rees.AMBIENT=A
 try:
  _,cols=rees.column_packet();inv={i:l for l,i in cols.items()};ibp,K,q=tr.descs(A);alls=ibp+K+q;nI=len(ibp);nK=len(K);pack={};oldp=base.PRIME
  for p in ex.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,(1,-1,0));pack[p]=T+raw[nI:nI+nK]+raw[nI+nK:]
  base.PRIME=oldp;descs=alls+K+q;ordered=sorted((i for i,d in enumerate(descs) if gdesc(d)<=8),key=lambda i:(gdesc(descs[i]),i));exact={i:ex.exact_row([pack[p][i] for p in ex.PS]) for i in ordered};basis={};cursor=0;states={}
  for g in (6,7,8):
   while cursor<len(ordered) and gdesc(descs[ordered[cursor]])<=g:insert(exact[ordered[cursor]],basis);cursor+=1
   columns=[i for i,l in inv.items() if gcol(l)<=g];states[g]={'basis':dict(basis),'image_rank':len(basis),'columns':columns,'quotient_dim':len(columns)-len(basis)}
  return cols,inv,states
 finally:rees.AMBIENT=oldA
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);data={A:build(A,point) for A in (12,14,16)};checks=[]
 for A,B in ((12,14),(14,16)):
  colsA,invA,statesA=data[A];colsB,invB,statesB=data[B]
  for g in (6,7,8):
   for axis,label in ((0,'x2'),(1,'y2')):
    mapped=[]
    for i in statesA[g]['columns']:
     l=list(invA[i]);e=list(l[-1]);e[axis]+=2;l[-1]=tuple(e);mapped.append(colsB[tuple(l)])
    union=dict(statesB[g]['basis'])
    for j in mapped:insert({j:1},union)
    intersection=len(mapped)+statesB[g]['image_rank']-len(union);kernel=intersection-statesA[g]['image_rank'];assert kernel>=0
    checks.append({'source_A':A,'target_A':B,'grade':g,'axis':label,'source_columns':len(mapped),'source_image_rank':statesA[g]['image_rank'],'target_image_rank':statesB[g]['image_rank'],'source_quotient_dim':statesA[g]['quotient_dim'],'intersection_dimension':intersection,'induced_kernel_dimension':kernel})
 kernels=sum(x['induced_kernel_dimension'] for x in checks);all_injective=kernels==0
 out={'schema':'marici.voevodsky.cosmology-filtered-quotient-colon-saturation.v1','status':('tested_squared_axis_quotient_maps_injective_through_A16' if all_injective else 'filtered_quotient_transport_kernels_found'),'exact_checks':checks,'total_kernel_dimension':kernels,'decision':('Both axis maps are injective at grades 6-8 for A12->A14 and A14->A16 over Q.' if all_injective else 'Nonzero exact kernels falsify finite-step colon saturation for the listed maps.'),'induction_boundary':'Finite exact injectivity through A16 does not prove uniform colon saturation for every even A.','next_gate':('derive-uniform-filtered-colon-saturation' if all_injective else 'classify-filtered-transport-kernels'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
