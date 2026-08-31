"""Solve every top-three-degree full-source boundary identity exactly over Q."""
from __future__ import annotations
import json,os,sys
if '--ambient' in sys.argv: os.environ['MARICI_AMBIENT']=sys.argv[sys.argv.index('--ambient')+1]
if '--prime' in sys.argv: os.environ['MARICI_FIELD_PRIME']=sys.argv[sys.argv.index('--prime')+1]
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
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json';P=32003
def main():
 assert A in (12,14,16,18)
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME
 for p in exact.PS:
  base.PRIME=p;sp=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));packets[p]={'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:],'dx':dx}
 base.PRIME=P;T=packets[P]['T'];SK=packets[P]['S_K'];Q=packets[P]['Q'];dx=packets[P]['dx'];piv={};nodes={};creation=[]
 for kind,rows in [('T',T),('S_K',SK),('Q',Q)]:
  for i,r in enumerate(rows):dag.add_pivot(r,piv,nodes,creation,(kind,i))
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for e in base.monomials_at_most(A-4):Kdesc.append((kp,lev,e))
 levels=(1,1,2,1,1);nI=4*len(base.monomials_at_most(A));records=[];cache={};tdesc,skdesc=compat.descriptors(A);qdesc=[d for d in tdesc if d[0]=='q'];descs={'T':tdesc,'S_K':skdesc,'Q':qdesc}
 for kp in (0,1):
  for e in [e for e in base.monomials_at_most(A-4) if sum(e)>=A-6]:
   ti=nI+Kdesc.index((kp,levels,e));targetm=dx[ti];rem,tr=dag.trace(targetm,piv);assert not rem;pending={}
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
   assert recon==target;word=[]
   for (k,i),a in zip(origins,coef):
    if not a:continue
    d=descs[k][i];word.append({'kind':k,'descriptor':[d[0],d[1],list(d[2]),d[3],d[4],list(d[5])],'numerator':a.numerator,'denominator':a.denominator})
   records.append({'k_pole':kp,'exponent':list(e),'dimension':len(erows),'equations':len(cols),'rank':rank,'full_reconstruction':True,'max_denominator':max(a.denominator for a in coef),'exact_word':word})
 base.PRIME=orig
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-all.v1','status':'all_boundary_targets_verified_over_Q','ambient_relation_degree':A,'targets_verified':len(records),'dimension_max':max(r['dimension'] for r in records),'equations_max':max(r['equations'] for r in records),'max_denominator':max(r['max_denominator'] for r in records),'records':records,'decision':'Every top-three-degree K target has an exact rational full-source identity.','limitations':['finite ambient degree','p=32003-selected source closures','four-prime CRT integer reconstruction','does not yet prove direct/composite rational coherence'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
