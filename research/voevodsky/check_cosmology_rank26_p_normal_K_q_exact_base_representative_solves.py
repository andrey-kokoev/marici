"""Exact-Q solves for canonical, median, and maximal interior base closures."""
from __future__ import annotations
import json,os,sys
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
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;ALL=os.environ.get('MARICI_ALL_SHIFTS')=='1';OUT=RES/f"cosmology_rank26_p_normal_K_q_exact_base_{'all_shifts' if ALL else 'representatives'}_a{A}.json";P=32003
def addm(row,c,v,p=P):
 x=(row.get(c,0)+v)%p
 if x:row[c]=x
 else:row.pop(c,None)
def addq(row,c,v):
 x=row.get(c,Fraction(0))+v
 if x:row[c]=x
 else:row.pop(c,None)
def qdescs(A):return [d for d in compat.descriptors(A)[0] if d[0]=='q']
def shift_desc(d,s):f,k,l,axis,mark,e=d;return(f,k,l,axis,mark,(e[0]+s[0],e[1]+s[1]))
def solve_rect(rows,target,cols):
 m=len(rows);M=[[Fraction(rows[j].get(c,0)) for j in range(m)]+[Fraction(target.get(c,0))] for c in cols];r=0;piv=[]
 for j in range(m):
  k=next((k for k in range(r,len(M)) if M[k][j]),None)
  if k is None:continue
  M[r],M[k]=M[k],M[r];q=M[r][j];M[r]=[x/q for x in M[r]]
  for k in range(len(M)):
   if k!=r and M[k][j]:q=M[k][j];M[k]=[x-q*y for x,y in zip(M[k],M[r])]
  piv.append(j);r+=1
 assert all(any(row[:-1]) or not row[-1] for row in M)
 coeff=[Fraction(0)]*m
 for i,j in enumerate(piv):coeff[j]=M[i][-1]
 return coeff,len(piv)
def main():
 assert A in (12,14,16)
 sol=json.loads((RES/'cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.json').read_text());census=json.loads((RES/f'cosmology_rank26_p_normal_K_q_exact_template_base_closure_census_a{A}.json').read_text());oldq=qdescs(14);qA=qdescs(A);qmap={d:i for i,d in enumerate(qA)};protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME
 for p in exact.PS:
  base.PRIME=p;sp=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));packets[p]={'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:],'dx':dx}
 base.PRIME=P;T=packets[P]['T'];SK=packets[P]['S_K'];Q=packets[P]['Q'];dx=packets[P]['dx'];piv={};nodes={};creation=[]
 for i,x in enumerate(T):dag.add_pivot(x,piv,nodes,creation,('T',i))
 for i,x in enumerate(SK):dag.add_pivot(x,piv,nodes,creation,('S_K',i))
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for e in base.monomials_at_most(A-4):Kdesc.append((kp,lev,e))
 shifts=base.monomials_at_most(A-7);levels=(1,1,2,1,1);nI=4*len(base.monomials_at_most(A));results={}
 for kp in (0,1):
  maxs=[tuple(x['shift']) for x in census['results'][f'k{kp}']['maximal_records']];chosen=list(shifts) if ALL else []
  if not ALL:
   for s in [(0,0),shifts[len(shifts)//2],maxs[0]]:
    if s not in chosen:chosen.append(s)
  template=[(oldq[x['row_index']],Fraction(x['numerator'],x['denominator'])) for x in sol['results'][f'k{kp}']['source_coefficients'] if x['kind']=='Q'];records=[]
  for s in chosen:
   modular=dict(dx[nI+Kdesc.index((kp,levels,s))]);exact_target=exact.exact_row([packets[p]['dx'][nI+Kdesc.index((kp,levels,s))] for p in exact.PS])
   for d,a in template:
    qi=qmap[shift_desc(d,s)];am=a.numerator*pow(a.denominator,-1,P)%P
    for c,v in Q[qi].items():addm(modular,c,-am*v)
    qr=exact.exact_row([packets[p]['Q'][qi] for p in exact.PS])
    for c,v in qr.items():addq(exact_target,c,-a*v)
   rem,tr=dag.trace(modular,piv);assert not rem;pending={}
   for p,a in tr:dag.add_value(pending,p,a)
   origins=[]
   for p in reversed(creation):
    a=pending.pop(p,0)
    if not a:continue
    node=nodes[p];origkey=tuple(node['origin'])
    if origkey not in origins:origins.append(origkey)
    for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
   assert not pending;erows=[exact.exact_row([packets[p][k][i] for p in exact.PS]) for k,i in origins];cols=sorted(set(exact_target).union(*(r.keys() for r in erows)));coef,rank=solve_rect(erows,exact_target,cols);recon={}
   for a,r in zip(coef,erows):
    for c,v in r.items():addq(recon,c,a*v)
   assert recon==exact_target;records.append({'shift':list(s),'source_rows':len(erows),'equations':len(cols),'rank':rank,'full_reconstruction':True,'max_denominator':max(a.denominator for a in coef)})
  results[f'k{kp}']=records
 base.PRIME=orig
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-exact-base-all-shifts.v1' if ALL else 'marici.voevodsky.cosmology-rank26-p-normal-K-q-exact-base-representatives.v1','status':'all_interior_base_closures_verified_over_Q' if ALL else 'representative_interior_base_closures_verified_over_Q','ambient_relation_degree':A,'results':results,'decision':'Every corrected interior target admits an exact rational T+S_K word.' if ALL else 'Canonical, median, and maximal representative corrected targets admit exact rational T+S_K words.','limitations':([] if ALL else ['representative shifts only'])+['closures selected at p=32003','four-prime CRT integer reconstruction'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
