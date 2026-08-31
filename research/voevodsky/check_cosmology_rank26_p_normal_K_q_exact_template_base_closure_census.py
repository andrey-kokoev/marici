"""Census T+S_K source dependency closures for every exact-q-template interior shift."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_exact_template_base_closure_census_a{A}.json';P=base.PRIME
def add(row,c,v):
 x=(row.get(c,0)+v)%P
 if x:row[c]=x
 else:row.pop(c,None)
def qdescs(A):return [d for d in compat.descriptors(A)[0] if d[0]=='q']
def shift_desc(d,s):
 f,k,l,axis,mark,e=d;return (f,k,l,axis,mark,(e[0]+s[0],e[1]+s[1]))
def main():
 assert A in (12,14,16) and P==32003
 sol=json.loads((RES/'cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.json').read_text());oldq=qdescs(14);qA=qdescs(A);qmap={d:i for i,d in enumerate(qA)};protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));SK=special[nI:nI+nK];Q=special[nI+nK:];piv={};nodes={};creation=[]
 for i,r in enumerate(T):dag.add_pivot(r,piv,nodes,creation,('T',i))
 for i,r in enumerate(SK):dag.add_pivot(r,piv,nodes,creation,('S_K',i))
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for e in base.monomials_at_most(A-4):Kdesc.append((kp,lev,e))
 levels=(1,1,2,1,1);results={}
 for kp in (0,1):
  template=[]
  for item in sol['results'][f'k{kp}']['source_coefficients']:
   if item['kind']=='Q':template.append((oldq[item['row_index']],Fraction(item['numerator'],item['denominator'])))
  records=[]
  for s in base.monomials_at_most(A-7):
   row=dict(dx[nI+Kdesc.index((kp,levels,s))])
   for d,a in template:
    qi=qmap[shift_desc(d,s)];am=a.numerator*pow(a.denominator,-1,P)%P
    for c,v in Q[qi].items():add(row,c,-am*v)
   residual,tr=dag.trace(row,piv);assert not residual;pending={}
   for p,a in tr:dag.add_value(pending,p,a)
   source={};active=edges=depth=0
   for p in reversed(creation):
    a=pending.pop(p,0)
    if not a:continue
    node=nodes[p];active+=1;depth=max(depth,node['depth']);dag.add_value(source,tuple(node['origin']),a*node['raw_coefficient'])
    for q,b in node['dependencies']:dag.add_value(pending,q,a*b);edges+=1
   assert not pending;cols=set(row)
   for kind,i in source:cols.update((T if kind=='T' else SK)[i])
   records.append({'shift':list(s),'source_rows':len(source),'T_rows':sum(k[0]=='T' for k in source),'S_K_rows':sum(k[0]=='S_K' for k in source),'retained_columns':len(cols),'active_nodes':active,'edges':edges,'maximum_depth':depth})
  results[f'k{kp}']={'shifts':len(records),'source_rows_min':min(r['source_rows'] for r in records),'source_rows_max':max(r['source_rows'] for r in records),'columns_min':min(r['retained_columns'] for r in records),'columns_max':max(r['retained_columns'] for r in records),'depth_max':max(r['maximum_depth'] for r in records),'maximal_records':[r for r in records if r['source_rows']==max(x['source_rows'] for x in records)]}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-exact-template-base-closure-census.v1','status':'all_interior_base_dependency_closures_censused','field':P,'ambient_relation_degree':A,'results':results,'decision':'All corrected targets have bounded source closures suitable for exact rational minor solves.','limitations':['closure selected by p=32003 pivot order','census is not exact rational verification'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
