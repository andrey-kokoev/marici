"""Reduce unresolved second-tangent targets against the full special image mod p."""
from __future__ import annotations
import hashlib,json,os,sys
from collections import Counter
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_second_direction_full_image_membership.json';P=32003
def axpy(r,b,a):
 for c,v in b.items():
  z=(r.get(c,0)-a*v)%P
  if z:r[c]=z
  else:r.pop(c,None)
def reduce_row(row,basis,insert=False):
 r={c:v%P for c,v in row.items() if v%P}
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:
    q=pow(r[p],-1,P);r={c:(v*q)%P for c,v in r.items()};basis[p]=r
   return r
  axpy(r,b,r[p])
 return r
def main():
 prior=json.loads((RES/'cosmology_second_tangent_normal_exact_replay.json').read_text());wanted=set(prior['unresolved_target_ids']);assert len(wanted)==390
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);t1=tuple(gate['integral_unit_normals']['p_tangent_difference']);t2=(3,0,-1);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);old=base.PRIME
 try:
  base.PRIME=P;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);D2,_=adapter.derivative_rows(cols,point,t2)
 finally:base.PRIME=old
 source=T+raw[nI:nI+nK]+raw[nI+nK:];basis={};max_support=0
 for row in source:
  rem=reduce_row(row,basis,True);max_support=max(max_support,len(rem))
 records={}
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for rec in json.loads((RES/name).read_text())['records']:
   tid=rec['source_certificate']['canonical_target_id']
   if tid in wanted:records[tid]=(family,tr.target_desc(family,rec))
 assert set(records)==wanted;index={d:i for i,d in enumerate(all_desc)};membership=Counter();residual_support=Counter();nonmembers=[]
 for tid,(family,d) in records.items():
  rem=reduce_row(D2[index[d]],basis,False);key=f'{family}:{"in" if not rem else "out"}';membership[key]+=1;residual_support[len(rem)]+=1
  if rem:
   digest=hashlib.sha256(';'.join(f'{c}:{rem[c]}' for c in sorted(rem)).encode()).hexdigest()
   nonmembers.append({'target_id':tid,'family':family,'residual_support':len(rem),'residual_sha256':digest})
 out={'schema':'marici.voevodsky.cosmology-second-direction-full-image-membership.v1','status':('all_unresolved_targets_in_full_image_mod_32003' if not nonmembers else 'second_tangent_nonmembers_witnessed_mod_32003'),'field':P,'source_rows':len(source),'source_image_rank':len(basis),'max_echelon_row_support':max_support,'targets_tested':390,'membership_census':dict(sorted(membership.items())),'residual_support_census':{str(k):v for k,v in sorted(residual_support.items())},'nonmember_count':len(nonmembers),'nonmembers':nonmembers,'decision':('All targets vanish in the full modular quotient; characteristic-zero reconstruction remains required.' if not nonmembers else 'Each nonzero modular residual proves the corresponding rational target is outside the full special image. By D_n2=D_nx-D_t2 and exact nx absorption, the derived-normal class has the same nonzero set.'),'scope':'Full A12 labelled algebraic source image over F_32003; no geometric or exceptional comparison. Modular membership does not by itself certify rational membership when residual is zero.','next_gate':('construct-second-direction-exact-certificates' if not nonmembers else 'transport-second-direction-nonzero-classes'),'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='nonmembers'},indent=2))
if __name__=='__main__':main()
