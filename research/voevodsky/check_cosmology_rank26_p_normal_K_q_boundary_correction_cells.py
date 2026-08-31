"""Test vertical boundary transport modulo T+S_K by exact correction-cell reduction."""
from __future__ import annotations
import json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_family_necessity as family
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_boundary_correction_A{A-2}_to_A{A}.json'
def count(n):return len(base.monomials_at_most(n))
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def qdesc():
 out=[]
 for qi,name in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append((name,kp,levels,exp))
 return out
def main():
 assert A in (14,16) and base.PRIME==32003
 source=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{A-2}.json').read_text());target=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{A}.json').read_text())
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*count(A);nK=64*count(A-4);qrows=special[nI+nK:];descriptors=qdesc();qkey={d:i for i,d in enumerate(descriptors)}
 pivots={};family.add_basis(tangent+special[nI:nI+nK],pivots);target_lookup={(r['k_pole'],*r['exponent']):r for r in target['records']};failures=[];supports=[]
 for s in source['records']:
  kp=s['k_pole'];i,j=s['exponent'];t=target_lookup[(kp,i,j+2)];row={}
  for term in s['terms']:
   key=(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+2));qi=qkey[key]
   for c,v in qrows[qi].items():add(row,c,term['coefficient']*v)
  for term in t['terms']:
   key=(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']));qi=qkey[key]
   for c,v in qrows[qi].items():add(row,c,-term['coefficient']*v)
  supports.append(len(row));res=base.reduce_row(row,pivots)
  if res:failures.append({'k_pole':kp,'source':[i,j],'target':[i,j+2],'residual_support':len(res)})
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-correction-cells.v1','status':'vertical_boundary_correction_cells_verified' if not failures else 'vertical_boundary_correction_cells_falsified','from_ambient':A-2,'to_ambient':A,'rows_tested':len(source['records']),'base_exact_differences':len(source['records'])-len(failures),'raw_difference_support_min':min(supports),'raw_difference_support_max':max(supports),'failures':failures,'decision':'Translated source and target q-lift representatives differ by T+S_K-exact correction cells.' if not failures else 'Vertical transport fails even modulo T+S_K.','limitations':['single prime','finite adjacent degrees','existence verified by reduction without retaining base coefficients','not a source-natural formula'],'passed':not failures}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
