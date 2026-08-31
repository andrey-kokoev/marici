"""Rank gate for uniqueness of canonical q coefficients on fixed descriptor support modulo T+S_K."""
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
import check_cosmology_rank26_p_normal_K_q_boundary_correction_source_words as words
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/f'cosmology_rank26_p_normal_K_q_seed_support_uniqueness_p{base.PRIME}.json'
def main():
 assert rees.AMBIENT==14 and base.PRIME in (32003,32009,32027,32029)
 path=RES/f'cosmology_rank26_p_normal_K_q_canonical_signature_p{base.PRIME}_a14.json'
 if base.PRIME==32003 and not path.exists():path=RES/'cosmology_rank26_p_normal_K_q_canonical_signature_a14.json'
 sig=json.loads(path.read_text());protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(14));nK=64*len(base.monomials_at_most(10));SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=words.qdesc();qkey={d:i for i,d in enumerate(qd)}
 basep={};family.add_basis(T+SK,basep);Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(10):Kdesc.append((kp,levels,exp))
 levels=(1,1,2,1,1);results={}
 for kp in (0,1):
  selected=[];terms=sig['signatures'][f'k{kp}']['terms']
  for t in terms:selected.append(qrows[qkey[(t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent']))]])
  target_raw=dx[nI+Kdesc.index((kp,levels,(0,0)))];fullp={};family.add_basis(T+SK,fullp);rank=family.add_basis(selected,fullp);target_addition=family.add_basis([target_raw],fullp);certificate=dict(target_raw)
  for t,row in zip(terms,selected):
   for c,v in row.items():base.add_value(certificate,c,t['coefficient']*v)
  cert_res=base.reduce_row(certificate,basep)
  results[f'k{kp}']={'selected_q_rows':len(selected),'quotient_rank':rank,'coefficient_kernel_dimension':len(selected)-rank,'target_in_selected_span':target_addition==0,'target_rank_addition':target_addition,'stored_coefficient_certificate_valid':not cert_res,'stored_certificate_residual_support':len(cert_res)}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-seed-support-uniqueness.v1','status':'fixed_support_solution_geometry_computed','field':base.PRIME,'results':results,'decision':'Coefficient reconstruction is well-posed only if kernel dimension is zero; positive dimension identifies finite-field gauge freedom.','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
