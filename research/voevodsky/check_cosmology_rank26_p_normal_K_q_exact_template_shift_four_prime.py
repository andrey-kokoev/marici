"""Validate exact rational q-template shifts modulo four primes at A12/A14/A16."""
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
import check_cosmology_rank26_p_normal_K_family_necessity as family
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_exact_template_shift_four_prime_a{A}.json'
def add(row,c,v,p):
 x=(row.get(c,0)+v)%p
 if x:row[c]=x
 else:row.pop(c,None)
def qdescs(A):return [d for d in compat.descriptors(A)[0] if d[0]=='q']
def shift_desc(d,s):
 f,k,l,axis,mark,e=d;return (f,k,l,axis,mark,(e[0]+s[0],e[1]+s[1]))
def main():
 assert A in (12,14,16)
 sol=json.loads((RES/'cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.json').read_text());oldq=qdescs(14);newq=qdescs(A);qmap={d:i for i,d in enumerate(newq)};protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();orig=base.PRIME;perprime={}
 for p in exact.PS:
  base.PRIME=p;special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));SK=special[nI:nI+nK];Q=special[nI+nK:];piv={};family.add_basis(T+SK,piv);Kdesc=[]
  for kp in range(charts.K_DEPTH):
   for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    for e in base.monomials_at_most(A-4):Kdesc.append((kp,lev,e))
  levels=(1,1,2,1,1);summary={}
  for kp in (0,1):
   template=[]
   for item in sol['results'][f'k{kp}']['source_coefficients']:
    if item['kind']!='Q':continue
    template.append((oldq[item['row_index']],Fraction(item['numerator'],item['denominator'])))
   tested=0
   for s in base.monomials_at_most(A-7):
    row=dict(dx[nI+Kdesc.index((kp,levels,s))])
    for d,a in template:
     qi=qmap[shift_desc(d,s)];am=(a.numerator*pow(a.denominator,-1,p))%p
     for c,v in Q[qi].items():add(row,c,-am*v,p)
    assert not base.reduce_row(row,piv);tested+=1
   summary[f'k{kp}']={'q_template_rows':len(template),'shifts_verified':tested,'all_reduce_to_base':True}
  perprime[str(p)]=summary
 base.PRIME=orig
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-exact-template-shift-four-prime.v1','status':'exact_q_template_shifts_valid_modulo_four_primes','ambient_relation_degree':A,'primes':list(exact.PS),'per_prime':perprime,'decision':'Every interior shift of the exact rational q template lies in the T+S_K quotient at all four primes.','limitations':['modular validation is not an exact rational base correction','top three boundary degrees excluded'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
