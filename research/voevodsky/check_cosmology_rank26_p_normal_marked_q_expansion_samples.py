"""Explicit normalized S+T expansions for representative marked-q singleton columns."""
from __future__ import annotations
import hashlib,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_marked_q_expansion_samples.json'
def add_pivot(row,pivots,origins,origin):
 row=dict(row)
 while row:
  p=max(row); a=row[p]
  if p not in pivots:
   inv=pow(a,base.PRIME-2,base.PRIME); pivots[p]={c:v*inv%base.PRIME for c,v in row.items()}; origins[p]=origin; return
  for c,v in pivots[p].items(): base.add_value(row,c,-a*v)
def trace(row,pivots):
 row=dict(row); out=[]
 while row:
  p=max(row); a=row[p]; existing=pivots.get(p)
  if existing is None:return row,out
  out.append((p,a))
  for c,v in existing.items():base.add_value(row,c,-a*v)
 return row,out
def reconstruct(trace_data,pivots):
 row={}
 for p,a in trace_data:
  for c,v in pivots[p].items():base.add_value(row,c,a*v)
 return row
def label_json(label):
 kp,*rest=label; exp=rest.pop(); return {'k_pole':kp,'q_levels':rest,'monomial':list(exp)}
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 prior=json.loads((RES/'cosmology_rank26_p_normal_marked_q_singletons.json').read_text()); assert prior['passed']
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); ny=tuple(protocol['integral_unit_normals']['ny']); t=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); ordered=[None]*len(columns)
 for label,column in columns.items():ordered[column]=label
 special=list(rees.raw_relations(point,columns)); dx,_=adapter.derivative_rows(columns,point,nx); dy,_=adapter.derivative_rows(columns,point,ny); dt,_=adapter.derivative_rows(columns,point,t)
 pivots={}; origins={}
 for i,row in enumerate(special):add_pivot(row,pivots,origins,('S',i))
 for i,row in enumerate(dt):add_pivot(row,pivots,origins,('T',i))
 assert len(pivots)==11603
 singleton_columns=sorted({next(iter(r)) for r in dx[4704:] if r}|{next(iter(r)) for r in dy[4704:] if r})
 assert len(singleton_columns)==9450
 lengths=[]
 for c in singleton_columns:
  residue,tr=trace({c:1},pivots); assert not residue; lengths.append((len(tr),c))
 lengths.sort(); positions={'minimum':0,'lower_quartile':len(lengths)//4,'median':len(lengths)//2,'upper_quartile':3*len(lengths)//4,'maximum':len(lengths)-1}
 samples={}
 for name,pos in positions.items():
  length,column=lengths[pos]; residue,tr=trace({column:1},pivots); assert not residue and reconstruct(tr,pivots)=={column:1}
  origin_counts=Counter(origins[p][0] for p,_ in tr)
  samples[name]={'column':column,'label':label_json(ordered[column]),'trace_length':length,'pivot_origin_counts':dict(origin_counts),'expansion':[{'pivot_column':p,'coefficient':a,'pivot_origin':origins[p][0],'origin_row_index':origins[p][1]} for p,a in tr],'reconstruction_verified':True}
 digest=hashlib.sha256()
 for length,column in lengths:digest.update(f'{column}:{length};'.encode())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-marked-q-expansion-samples.v1','status':'representative_singleton_expansions_retained_and_reconstructed','field':base.PRIME,'ambient_relation_degree':14,'fixed_basis_rank':len(pivots),'singleton_columns':len(singleton_columns),'trace_length_census':{'minimum':lengths[0][0],'median':lengths[len(lengths)//2][0],'maximum':lengths[-1][0],'mean_numerator':sum(x for x,_ in lengths),'mean_denominator':len(lengths),'length_profile_sha256':digest.hexdigest()},'samples':samples,'certificate_contract':'For each sample, e_column=sum coefficient*pivot_row over the fixed normalized S+T basis; reconstruction is checked exactly in F_32003.','limitations':['five representative columns, not all 9450 expansions retained','pivot expansions are normalized-basis certificates rather than original-source-row coefficients','single prime','order dependent'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='samples'}|{'sample_summary':{k:{'column':v['column'],'trace_length':v['trace_length'],'pivot_origin_counts':v['pivot_origin_counts']} for k,v in samples.items()}},indent=2))
if __name__=='__main__':main()
