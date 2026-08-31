"""Verify every interior monomial shift of exact canonical source words over Q at A12/A14/A16."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
VRES=ROOT/'research'/'voevodsky'/'results';BRES=ROOT/'research'/'benincasa'/'results';A=rees.AMBIENT;OUT=BRES/f'cosmology_physical_half_twist_seed_exact_interior_a{A}.json';PS=exact.PS
def add(row,c,v):
 x=row.get(c,Fraction(0))+v
 if x:row[c]=x
 else:row.pop(c,None)
def qdescs(A):return [d for d in compat.descriptors(A)[0] if d[0]=='q']
def shift_desc(d,s):
 f,k,l,axis,mark,e=d;return (f,k,l,axis,mark,(e[0]+s[0],e[1]+s[1]))
def main():
 assert A in (12,14,16)
 sol=json.loads((BRES/'cosmology_physical_half_twist_seed_exact_rational_minor.json').read_text());d14,sk14=compat.descriptors(14);q14=qdescs(14);dA,skA=compat.descriptors(A);qA=qdescs(A);old={'T':d14,'S_K':sk14,'Q':q14};new={'T':{d:i for i,d in enumerate(dA)},'S_K':{d:i for i,d in enumerate(skA)},'Q':{d:i for i,d in enumerate(qA)}};protocol=json.loads((VRES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME
 for p in PS:
  base.PRIME=p;rees.charts.GAMMA=-pow(2,-1,p)%p;special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));packets[p]={'T':T,'S_K':special[nI:nI+nK],'Q':special[nI+nK:],'dx':dx}
 base.PRIME=orig;levels=(1,1,2,1,1);Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for e in base.monomials_at_most(A-4):Kdesc.append((kp,lev,e))
 nI=4*len(base.monomials_at_most(A));cache={};results={}
 for kp in (0,1):
  tested=0;rejected=[];max_verified=-1
  for shift in base.monomials_at_most(A-7):
   items=sol['results'][f'k{kp}']['source_coefficients'];shifted=[(item,shift_desc(old[item['kind']][item['row_index']],shift)) for item in items]
   missing=[{'kind':item['kind'],'row_index':item['row_index'],'shifted_descriptor':repr(desc)} for item,desc in shifted if desc not in new[item['kind']]]
   if missing:rejected.append({'shift':list(shift),'missing':missing});continue
   recon={}
   for item,desc in shifted:
    kind=item['kind'];idx=new[kind][desc];ck=(kind,idx)
    if ck not in cache:cache[ck]=exact.exact_row([packets[p][kind][idx] for p in PS])
    a=Fraction(item['numerator'],item['denominator'])
    for c,v in cache[ck].items():add(recon,c,a*v)
   ti=nI+Kdesc.index((kp,levels,shift));target=exact.exact_row([packets[p]['dx'][ti] for p in PS]);assert recon==target;tested+=1;max_verified=max(max_verified,sum(shift))
  results[f'k{kp}']={'shifts_verified':tested,'maximum_shift_degree_verified':max_verified,'requested_maximum_shift_degree':A-7,'rejected_shift_count':len(rejected),'rejected_shifts':rejected,'all_admissible_full_reconstructions':True}
 out={'schema':'marici.benincasa.cosmology-physical-half-twist-seed-exact-interior-shifts.v1','status':'physical_half_twist_all_interior_shifts_verified_over_Q','physical_gamma':'-1/2','ambient_relation_degree':A,'results':results,'decision':'Every descriptor-admissible monomial shift in the requested range reconstructs exactly; shifts whose source descriptors exceed the finite presentation are explicitly rejected.','limitations':['finite ambient degree','four-prime CRT rational row reconstruction under the standard unique-height bound','top three boundary degrees excluded'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
