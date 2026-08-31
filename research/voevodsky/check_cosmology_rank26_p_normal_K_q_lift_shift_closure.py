"""Test whether two canonical q-lifts generate all 132 K residual identities by monomial shifts."""
from __future__ import annotations
import json,sys
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
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_q_lift_shift_closure.json'
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 canonical=json.loads((RES/'cosmology_rank26_p_normal_K_canonical_q_lifts.json').read_text()); assert canonical['passed']
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,td); dx,_=adapter.derivative_rows(columns,point,nx); targets=dx[480:4704]; qrows=special[4704:]
 pivots={}; family.add_basis(tangent+special[480:4704],pivots)
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(rees.AMBIENT-4):Kdesc.append((kp,levels,exp))
 Kindex={d:i for i,d in enumerate(Kdesc)}
 qdesc=census.descriptors()[4704:]; qkey={(d['mark'],d['k_pole'],tuple(d['levels']),tuple(d['exponent'])):i for i,d in enumerate(qdesc)}
 target_levels=(1,1,2,1,1); summaries={}; total=0; failures=[]
 for kp in (0,1):
  coeffs=canonical['lifts'][f'k{kp}']['coefficients']; template=[]
  for item in coeffs:
   d=qdesc[item['q_row_index']]; template.append((d,item['coefficient']))
  tested=0; missing=0; bad=0
  for shift in base.monomials_at_most(10):
   ti=Kindex[(kp,target_levels,shift)]; row=dict(targets[ti]); shifted=[]
   for d,a in template:
    exp=(d['exponent'][0]+shift[0],d['exponent'][1]+shift[1]); key=(d['mark'],d['k_pole'],tuple(d['levels']),exp)
    if key not in qkey:missing+=1; shifted=[]; break
    shifted.append((qkey[key],a))
   if not shifted:failures.append({'k_pole':kp,'shift':list(shift),'kind':'missing_shifted_q_row'}); continue
   for qi,a in shifted:
    for c,v in qrows[qi].items():add(row,c,a*v)
   residue=base.reduce_row(row,pivots); tested+=1; total+=1
   if residue:
    bad+=1; failures.append({'k_pole':kp,'shift':list(shift),'kind':'nonzero_residue','support':len(residue)})
  summaries[f'k{kp}']={'template_q_rows':len(template),'shifts_expected':66,'shifts_tested':tested,'missing_shift_rows':missing,'nonzero_residues':bad}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-lift-shift-closure.v1','status':'two_canonical_q_lifts_generate_all_132_residual_identities' if not failures else 'canonical_q_lifts_not_shift_closed','field':base.PRIME,'ambient_relation_degree':14,'summaries':summaries,'total_shifted_identities_verified':total-len([f for f in failures if f['kind']=='nonzero_residue']),'failures':failures,'decision':'The two canonical q-lifts form uniform monomial-shift templates for the complete residual family.' if not failures else 'Canonical lift shift closure fails; retain row-dependent corrections.','limitations':['single prime','degree-14 cutoff','identity verified modulo T+S_K','does not prove compatibility across ambient degrees'],'passed':not failures}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
