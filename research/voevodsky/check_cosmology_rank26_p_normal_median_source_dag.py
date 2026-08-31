"""Back-substitute the median singleton through the pivot DAG to original S/T rows."""
from __future__ import annotations
import hashlib,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_median_source_dag.json'
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 samples=json.loads((RES/'cosmology_rank26_p_normal_marked_q_expansion_samples.json').read_text()); target=samples['samples']['median']; column=target['column']; assert column==9560 and target['trace_length']==186
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); t=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,t)
 pivots={}; nodes={}; creation=[]
 for i,row in enumerate(special):dag.add_pivot(row,pivots,nodes,creation,('S',i))
 for i,row in enumerate(tangent):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 residue,target_trace=dag.trace({column:1},pivots); assert not residue and len(target_trace)==186
 pending={}
 for p,a in target_trace:dag.add_value(pending,p,a)
 source_coeffs={}; active_nodes=active_edges=max_depth=0
 for p in reversed(creation):
  a=pending.pop(p,0)
  if not a:continue
  active_nodes+=1; node=nodes[p]; max_depth=max(max_depth,node['depth']); dag.add_value(source_coeffs,tuple(node['origin']),a*node['raw_coefficient'])
  for q,b in node['dependencies']:dag.add_value(pending,q,a*b); active_edges+=1
 assert not pending and dag.combine_source(source_coeffs,special,tangent)=={column:1}
 counts=Counter(k for k,_ in source_coeffs); digest=hashlib.sha256(); coeffs=[]
 for (kind,index),a in sorted(source_coeffs.items()):coeffs.append({'kind':kind,'row_index':index,'coefficient':a}); digest.update(f'{kind}:{index}:{a};'.encode())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-median-source-dag.v1','status':'median_singleton_expanded_to_original_S_T_rows','field':base.PRIME,'ambient_relation_degree':14,'target_column':column,'target_label':target['label'],'normalized_pivot_trace_length':len(target_trace),'active_pivot_DAG':{'nodes':active_nodes,'dependency_edges_traversed':active_edges,'maximum_recorded_depth':max_depth},'original_source_expansion':{'nonzero_source_rows':len(source_coeffs),'S_rows':counts['S'],'T_rows':counts['T'],'coefficient_sha256':digest.hexdigest(),'coefficients':coeffs},'identity':f'e_{column} = sum a_i S_i + sum b_j T_j in F_32003','exact_source_row_reconstruction_verified':True,'decision':'The median normalized expansion back-substitutes completely to original relation generators.','limitations':['one representative','single prime','presentation-dependent coefficient list','not a uniform template'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='original_source_expansion'}|{'source_summary':{k:v for k,v in out['original_source_expansion'].items() if k!='coefficients'}},indent=2))
if __name__=='__main__':main()
