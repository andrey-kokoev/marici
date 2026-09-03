"""Exact-solve all 248 A12 nonmarked K parity seeds over Q using only T+S_K."""
from __future__ import annotations
import json,os,sys
os.environ['MARICI_AMBIENT']='12'
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
import cosmology_exact_source_certificate as certificate
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_nonmarked_K_exact_seeds_a12.json';P=32003
def main():
 assert rees.AMBIENT==12
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME;nI=4*len(base.monomials_at_most(12));nK=64*len(base.monomials_at_most(8))
 for p in exact.PS:
  base.PRIME=p;sp=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);packets[p]={'T':T,'S_K':sp[nI:nI+nK],'dx':dx}
 base.PRIME=P;piv={};nodes={};creation=[]
 for kind in ('T','S_K'):
  for i,r in enumerate(packets[P][kind]):dag.add_pivot(r,piv,nodes,creation,(kind,i))
 Kdesc=[(kp,lev,e) for kp in range(charts.K_DEPTH) for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)) for e in base.monomials_at_most(8)]
 marked=(1,1,2,1,1);seeds=[(kp,lev,e) for kp in (0,1) for lev in product((1,2),repeat=5) if lev!=marked for e in ((0,0),(0,1),(1,0),(1,1))];assert len(seeds)==248
 records=[];cache={}
 for kp,lev,e in seeds:
  ti=nI+Kdesc.index((kp,lev,e));rem,tr=dag.trace(packets[P]['dx'][ti],piv);assert not rem;pending={}
  for p,a in tr:dag.add_value(pending,p,a)
  origins=[]
  for p in reversed(creation):
   a=pending.pop(p,0)
   if not a:continue
   node=nodes[p];k=tuple(node['origin'])
   if k not in origins:origins.append(k)
   for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
  assert not pending;erows=[]
  for k,i in origins:
   ck=(k,i)
   if ck not in cache:cache[ck]=exact.exact_row([packets[p][k][i] for p in exact.PS])
   erows.append(cache[ck])
  target=exact.exact_row([packets[p]['dx'][ti] for p in exact.PS]);cols=sorted(set(target).union(*(r.keys() for r in erows)));coef,rank=solver.solve_rect(erows,target,cols);recon={}
  for a,r in zip(coef,erows):
   for c,v in r.items():solver.addq(recon,c,a*v)
  assert recon==target
  descriptor={'family':'K','k_pole':kp,'levels':list(lev),'exponent':list(e)}
  cert=certificate.make(descriptor,origins,erows,target,cols,coef,Path(__file__))
  records.append({'k_pole':kp,'levels':list(lev),'exponent':list(e),'dimension':len(erows),'equations':len(cols),'rank':rank,'max_denominator':max((a.denominator for a in coef),default=1),'full_reconstruction':True,'source_certificate':cert})
 base.PRIME=orig
 out={'schema':'marici.voevodsky.cosmology-nonmarked-K-exact-seeds-a12.v1','status':'all_248_nonmarked_parity_seeds_verified_over_Q','ambient_relation_degree':12,'targets_verified':len(records),'dimension_max':max(r['dimension'] for r in records),'equations_max':max(r['equations'] for r in records),'max_denominator':max(r['max_denominator'] for r in records),'records':records,'decision':'Every nonmarked pole/level/parity seed has an exact rational T+S_K contraction.','limitations':['closures selected by F_32003 pivot order','four-prime CRT reconstruction with exact post-verification','unbounded promotion additionally uses constructor naturality and orbit coverage'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
