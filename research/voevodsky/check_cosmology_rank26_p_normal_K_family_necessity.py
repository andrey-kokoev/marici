"""Retain source grading and census which special families absorb nx K-derivative rows modulo full tangent relations."""
from __future__ import annotations
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_family_necessity.json'
SLICES={'IBP':(0,480),'K':(480,4704),'q':(4704,29904)}
def add_basis(rows,pivots):
 added=0
 for row in rows:
  r=base.reduce_row(row,pivots)
  if r:
   p=max(r); a=r[p]; inv=pow(a,base.PRIME-2,base.PRIME); pivots[p]={c:v*inv%base.PRIME for c,v in r.items()}; added+=1
 return added
def containment(rows,pivots):
 zero=0; residual=[]
 for row in rows:
  r=base.reduce_row(row,pivots)
  if not r:zero+=1
  else:residual.append(len(r))
 return {'rows':len(rows),'absorbed':zero,'nonabsorbed':len(rows)-zero,'residual_support_min':min(residual) if residual else 0,'residual_support_max':max(residual) if residual else 0}
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); tangent_dir=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,tangent_dir); dx,_=adapter.derivative_rows(columns,point,nx); target=dx[slice(*SLICES['K'])]
 candidates=[('T_plus_S_K',['K']),('T_plus_S_K_IBP',['K','IBP']),('T_plus_S_K_q',['K','q']),('T_plus_all_S',['K','IBP','q'])]; results={}
 for name,families in candidates:
  start=time.time(); pivots={}; tangent_rank=add_basis(tangent,pivots); additions={}
  for family in families:additions[family]=add_basis(special[slice(*SLICES[family])],pivots)
  results[name]={'special_families':families,'tangent_rank':tangent_rank,'special_rank_additions':additions,'basis_rank':len(pivots),'target_nx_K':containment(target,pivots),'elapsed_seconds':round(time.time()-start,3)}
 assert results['T_plus_all_S']['target_nx_K']['nonabsorbed']==0
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-family-necessity.v1','status':'graded_family_necessity_census_complete','field':base.PRIME,'ambient_relation_degree':14,'target':'all 4224 nx K-family derivative rows','candidates':results,'decision':'reported from exact containment counts','limitations':['single prime','degree 14','full tangent family retained in every candidate','family necessity does not yet construct coefficients'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
