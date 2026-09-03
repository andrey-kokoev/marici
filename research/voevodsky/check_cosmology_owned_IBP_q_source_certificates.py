"""Independent owned regeneration of IBP and q exact source certificates."""
from __future__ import annotations
import json,os,sys
os.environ['MARICI_AMBIENT']='12'
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
import cosmology_exact_source_certificate as certificate
RES=ROOT/'research'/'voevodsky'/'results';P=32003

def origin_rows(kinds,packets):
 piv={};nodes={};creation=[]
 for kind in kinds:
  for i,row in enumerate(packets[P][kind]):dag.add_pivot(row,piv,nodes,creation,(kind,i))
 return piv,nodes,creation

def exact_solve(target_index,kinds,packets,piv,nodes,creation,cache):
 rem,trace=dag.trace(packets[P]['dx'][target_index],piv);assert not rem
 pending={}
 for p,a in trace:dag.add_value(pending,p,a)
 origins=[]
 for p in reversed(creation):
  a=pending.pop(p,0)
  if not a:continue
  node=nodes[p];origin=tuple(node['origin'])
  if origin not in origins:origins.append(origin)
  for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
 assert not pending
 rows=[]
 for kind,i in origins:
  key=(kind,i)
  if key not in cache:cache[key]=exact.exact_row([packets[p][kind][i] for p in exact.PS])
  rows.append(cache[key])
 target=exact.exact_row([packets[p]['dx'][target_index] for p in exact.PS])
 cols=sorted(set(target).union(*(r.keys() for r in rows)))
 coef,rank=solver.solve_rect(rows,target,cols);recon={}
 for a,row in zip(coef,rows):
  for c,v in row.items():solver.addq(recon,c,a*v)
 assert recon==target
 return origins,rows,target,cols,coef,rank

def summaries_match(records,old_name,keys):
 old=json.loads((RES/old_name).read_text())['records'];assert len(records)==len(old)
 for new,prior in zip(records,old):
  assert all(new[k]==prior[k] for k in keys),(new,prior)

def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())
 point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet();packets={};original_prime=base.PRIME
 nI=4*len(base.monomials_at_most(12));nK=64*len(base.monomials_at_most(8))
 for p in exact.PS:
  base.PRIME=p;raw=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx)
  packets[p]={'T':T,'Q':raw[nI+nK:],'dx':dx}
 base.PRIME=P
 # IBP: sixteen parity representatives.
 piv,nodes,creation=origin_rows(('T',),packets);cache={};ibp=[]
 desc=[(kp,axis,e) for kp in range(charts.K_DEPTH) for axis in range(2) for e in base.monomials_at_most(12)]
 for d in [(kp,axis,e) for kp in range(2) for axis in range(2) for e in ((0,0),(0,1),(1,0),(1,1))]:
  ti=desc.index(d);origins,rows,target,cols,coef,rank=exact_solve(ti,('T',),packets,piv,nodes,creation,cache)
  descriptor={'family':'IBP','k_pole':d[0],'axis':d[1],'exponent':list(d[2])}
  cert=certificate.make(descriptor,origins,rows,target,cols,coef,Path(__file__))
  ibp.append({'descriptor':[d[0],d[1],list(d[2])],'dimension':len(rows),'equations':len(cols),'rank':rank,'max_denominator':max((a.denominator for a in coef),default=1),'source_certificate':cert})
 summaries_match(ibp,'cosmology_IBP_corrected_transport_exact_seeds_a12.json',('descriptor','dimension','equations','rank','max_denominator'))
 # q: 960 marked parity representatives.
 piv,nodes,creation=origin_rows(('T','Q'),packets);cache={};qrecords=[];qdesc=[]
 for qi in range(len(rees.NAMES)):
  for kp in range(charts.K_DEPTH+1):
   for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if lev[qi]==charts.Q_DEPTH:continue
    for e in base.monomials_at_most(11):qdesc.append((qi,kp,lev,e))
 seeds=[(qi,kp,lev,e) for qi in range(5) for kp in range(3) for lev in product((1,2),repeat=5) if lev[qi]==1 for e in ((0,0),(0,1),(1,0),(1,1))]
 for qi,kp,lev,e in seeds:
  ti=nI+nK+qdesc.index((qi,kp,lev,e));origins,rows,target,cols,coef,rank=exact_solve(ti,('T','Q'),packets,piv,nodes,creation,cache)
  descriptor={'family':'q','q_index':qi,'k_pole':kp,'levels':list(lev),'exponent':list(e)}
  cert=certificate.make(descriptor,origins,rows,target,cols,coef,Path(__file__))
  qrecords.append({'q_index':qi,'k_pole':kp,'levels':list(lev),'exponent':list(e),'dimension':len(rows),'equations':len(cols),'rank':rank,'max_denominator':max((a.denominator for a in coef),default=1),'full_reconstruction':True,'source_certificate':cert})
 summaries_match(qrecords,'cosmology_q_exact_seeds_a12.json',('q_index','k_pole','levels','exponent','dimension','equations','rank','max_denominator','full_reconstruction'))
 base.PRIME=original_prime
 outputs=[('cosmology_IBP_exact_source_certificates_a12.json',ibp),('cosmology_q_exact_source_certificates_a12.json',qrecords)]
 for name,records in outputs:
  (RES/name).write_text(json.dumps({'schema':'marici.voevodsky.owned-exact-source-certificates.v1','records':records,'certificate_count':len(records),'all_replayed':True,'summary_match':True},indent=2)+'\n')
 print(json.dumps({'IBP_certificates':len(ibp),'q_certificates':len(qrecords),'all_exact_replays':True,'all_prior_summaries_match':True,'passed':True},indent=2))
if __name__=='__main__':main()
