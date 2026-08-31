"""Back-substitute the minimum marked-q singleton expansion to an original T row."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_minimum_source_expansion.json'
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 samples=json.loads((RES/'cosmology_rank26_p_normal_marked_q_expansion_samples.json').read_text()); assert samples['passed']
 minimum=samples['samples']['minimum']; assert minimum['column']==3420 and minimum['trace_length']==1 and minimum['expansion']==[{'pivot_column':3420,'coefficient':1,'pivot_origin':'T','origin_row_index':4914}]
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); tangent=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); ordered=[None]*len(columns)
 for label,column in columns.items():ordered[column]=label
 dt,checked=adapter.derivative_rows(columns,point,tangent); assert checked==29904
 source_row=dt[4914]; assert source_row=={3420:base.PRIME-1}
 coefficient=base.PRIME-1
 reconstructed={column:(coefficient*value)%base.PRIME for column,value in source_row.items()}
 assert reconstructed=={3420:1}
 local_marked_index=4914-4704; rows_per_mark=5040; mark_index=local_marked_index//rows_per_mark
 assert mark_index==0 and rees.NAMES[mark_index]=='g1'
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-minimum-source-expansion.v1','status':'minimum_singleton_is_negative_of_one_original_p_tangent_row','field':base.PRIME,'ambient_relation_degree':14,'target_column':3420,'target_label':minimum['label'],'original_generator':{'kind':'T_p_tangent_derivative_row','global_row_index':4914,'relation_family':'marked_q_multiplication','marked_family_local_index':local_marked_index,'active_mark':'g1','source_row':{'3420':base.PRIME-1}},'source_expansion':{'coefficient':coefficient,'identity':'e_3420 = - T_4914 in F_32003'},'exact_reconstruction_verified':True,'decision':'The minimum normalized-pivot certificate back-substitutes completely: no special rows or nested pivots are needed; the target basis column is the negative of one original g1 p-tangent derivative relation.','limitations':['one minimum representative','single prime presentation','does not back-substitute longer traces'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
