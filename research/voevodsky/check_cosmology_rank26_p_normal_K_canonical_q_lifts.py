"""Extract q-only provenance for canonical K residuals at poles 0 and 1."""
from __future__ import annotations
import hashlib,json,sys
from collections import Counter
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_family_necessity as family
import check_cosmology_rank26_p_normal_source_template_census as census
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_canonical_q_lifts.json'; P=base.PRIME
def add(d,k,v):
 v=(d.get(k,0)+v)%P
 if v:d[k]=v
 else:d.pop(k,None)
def insert(row,pivots,prov=None):
 row=dict(row); prov=dict(prov or {})
 while row:
  p=max(row); a=row[p]
  if p not in pivots:
   inv=pow(a,P-2,P); pivots[p]=({c:v*inv%P for c,v in row.items()},{k:v*inv%P for k,v in prov.items()}); return True
  pr,pc=pivots[p]
  for c,v in pr.items():add(row,c,-a*v)
  for k,v in pc.items():add(prov,k,-a*v)
 return False
def reduce_with_prov(row,pivots):
 row=dict(row); prov={}
 while row:
  p=max(row); assert p in pivots; a=row[p]; pr,pc=pivots[p]
  for c,v in pr.items():add(row,c,-a*v)
  for k,v in pc.items():add(prov,k,-a*v)
 return prov
def main():
 assert rees.AMBIENT==14 and P==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,td); dx,_=adapter.derivative_rows(columns,point,nx); Ktargets=dx[480:4704]; qrows=special[4704:]
 pivots={}
 for row in tangent+special[480:4704]:insert(row,pivots)
 base_pivots={p:(dict(r),{}) for p,(r,_c) in pivots.items()}
 for qi,row in enumerate(qrows):insert(row,pivots,{qi:1})
 descK=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(rees.AMBIENT-4):descK.append((kp,levels,exp))
 all_desc=census.descriptors(); qdesc=all_desc[4704:]; lifts={}; target_levels=(1,1,2,1,1)
 for kp in (0,1):
  index=descK.index((kp,target_levels,(0,0))); prov=reduce_with_prov(Ktargets[index],pivots)
  # Identity: target + sum(prov_i q_i) belongs to base.
  check=dict(Ktargets[index])
  for qi,a in prov.items():
   for c,v in qrows[qi].items():add(check,c,a*v)
  residue=base.reduce_row(check,{p:dict(r) for p,(r,_c) in base_pivots.items()}); assert not residue
  marks=Counter(qdesc[i]['mark'] for i in prov); poles=Counter(qdesc[i]['k_pole'] for i in prov); digest=hashlib.sha256()
  coeff=[]
  for i,a in sorted(prov.items()):coeff.append({'q_row_index':i,'coefficient':a}); digest.update(f'{i}:{a};'.encode())
  lifts[f'k{kp}']={'target_K_row_index':index,'target':{'k_pole':kp,'q_levels':list(target_levels),'exponent':[0,0]},'q_rows':len(prov),'q_mark_counts':dict(marks),'q_pole_counts':{str(k):v for k,v in sorted(poles.items())},'coefficient_sha256':digest.hexdigest(),'coefficients':coeff,'reconstruction_mod_T_plus_S_K':True}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-canonical-q-lifts.v1','status':'canonical_pole0_pole1_q_lifts_extracted','field':P,'ambient_relation_degree':14,'identity_convention':'target K derivative + listed special q combination lies in T+S_K','lifts':lifts,'decision':'Canonical marked-q lifts exist at both residual pole levels with exact reconstruction.','limitations':['single prime','canonical monomial only','pivot-order-dependent q coefficients','monomial-shift generation not yet tested'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({**out,'lifts':{k:{x:y for x,y in v.items() if x!='coefficients'} for k,v in lifts.items()}},indent=2))
if __name__=='__main__':main()
