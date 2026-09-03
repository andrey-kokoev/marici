"""Construct pole-order filtration and falsify its promotion to DNC filtration."""
from __future__ import annotations
import json,os,sys
from collections import Counter
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_source_word_axis_square_transport as transport
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_pole_order_filtration_candidate.json'
def column_grade(label):return label[0]+sum(label[1:-1])
def generator_grade(desc):
 if desc[0]=='IBP':return desc[1]+sum(desc[2])+1
 if desc[0]=='K':return desc[1]+sum(desc[2])+1
 if desc[0]=='q':return desc[2]+sum(desc[3])+1
 raise AssertionError(desc)
def dnc_admissible(x):return all(x.get(k) for k in ('center_ideal','rees_parameter','special_fiber_map','filtration_to_I_adic_proof'))
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();inverse={i:l for l,i in columns.items()};raw=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);ibp,K,q=transport.descs(12);nI=len(ibp);nK=len(K);packets={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:]};descs={'T':ibp+K+q,'S_K':K,'Q':q};violations=[];census={};transport_failures=0
 for kind in ('T','S_K','Q'):
  grades=Counter()
  assert len(packets[kind])==len(descs[kind])
  for i,(row,desc) in enumerate(zip(packets[kind],descs[kind])):
   g=generator_grade(desc);grades[g]+=1
   bad=[column_grade(inverse[c]) for c in row if column_grade(inverse[c])>g]
   if bad and len(violations)<20:violations.append({'kind':kind,'index':i,'generator_grade':g,'bad_column_grades':bad})
   for axis in (0,1):transport_failures+=generator_grade(transport.shift(desc,axis))!=g
  census[kind]={str(g):n for g,n in sorted(grades.items())}
 assert not violations and transport_failures==0
 c0=Counter(column_grade(label) for label in columns);candidate={'center_ideal':None,'rees_parameter':None,'special_fiber_map':None,'filtration_to_I_adic_proof':None};assert not dnc_admissible(candidate)
 out={'schema':'marici.voevodsky.cosmology-pole-order-filtration-candidate.v1','status':'exhaustive_transport_preserved_pole_filtration_not_DNC','filtration':'F_g C0 is spanned by columns with k_pole+sum(q_levels)<=g; F_g C1 is spanned by generators whose incidence rows have maximum pole grade <=g','C0_grade_census':{str(g):n for g,n in sorted(c0.items())},'C1_grade_census':census,'incidence_rows_checked':sum(len(v) for v in packets.values()),'filtration_violations':len(violations),'transport_checks':2*sum(len(v) for v in packets.values()),'transport_failures':transport_failures,'exhaustive':True,'strongest_falsification':{'candidate':'identify pole-order filtration with DNC filtration','residual':'No center ideal, Rees parameter, special-fiber map, or proof relating pole grade to an I-adic filtration is present.','fabricated_DNC_record_rejected':True},'surviving_scope':'A finite exhaustive increasing pole-order filtration of the algebraic presentation, preserved by incidence and squared-axis transport.','first_missing_typed_object':'A declared DNC center ideal and Rees construction mapping pole grade to its I-adic filtration.','acceptance_test':'Name the center ideal from source geometry, construct the Rees module and generic/special fiber maps, then prove the algebraic pole filtration agrees with the induced I-adic filtration.','disposition':'Retain pole filtration; do not populate DNC_filtration. Continue to the independent executable exceptional-specialization interface audit.','next_gate':'audit-exceptional-specialization-interface','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
