"""Reconstruct dependency minors over integers by four-prime CRT and solve exactly over Q."""
from __future__ import annotations
import hashlib,json,math,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.json';PS=(32003,32009,32027,32029)
def crt_signed(vals):
 M=math.prod(PS);x=0
 for a,p in zip(vals,PS):m=M//p;x=(x+a*m*pow(m,-1,p))%M
 return x if x<=M//2 else x-M
def exact_row(rows):
 keys=set().union(*(r.keys() for r in rows));return {k:v for k in keys if (v:=crt_signed([r.get(k,0) for r in rows]))}
def solve(A,b):
 n=len(A);M=[[Fraction(x) for x in row]+[Fraction(y)] for row,y in zip(A,b)]
 for c in range(n):
  p=next(r for r in range(c,n) if M[r][c]);M[c],M[p]=M[p],M[c];q=M[c][c];M[c]=[x/q for x in M[c]]
  for r in range(n):
   if r==c or not M[r][c]:continue
   q=M[r][c];M[r]=[x-q*y for x,y in zip(M[r],M[c])]
 return [M[i][-1] for i in range(n)]
def add_fraction(row,c,v):
 x=row.get(c,Fraction(0))+v
 if x:row[c]=x
 else:row.pop(c,None)
def main():
 assert rees.AMBIENT==14
 minor=json.loads((RES/'cosmology_rank26_p_normal_K_q_seed_dependency_minor.json').read_text());protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={}
 original=base.PRIME
 for p in PS:
  base.PRIME=p;special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(14));nK=64*len(base.monomials_at_most(10));packets[p]={'T':T,'S_K':special[nI:nI+nK],'Q':special[nI+nK:],'dx':dx}
 base.PRIME=original;results={};global_max=0
 for kp in (0,1):
  info=minor['results'][f'k{kp}'];gens=[(g['kind'],g['row_index']) for g in info['source_generators']];cols=info['retained_column_indices'];source=[]
  for kind,index in gens:
   r=exact_row([packets[p][kind][index] for p in PS]);global_max=max(global_max,max(map(abs,r.values()),default=0));source.append(r)
  ti=info['target_row_index'];target=exact_row([packets[p]['dx'][ti] for p in PS]);global_max=max(global_max,max(map(abs,target.values()),default=0));n=len(gens);assert n==len(cols)
  A=[[source[j].get(c,0) for j in range(n)] for c in cols];b=[target.get(c,0) for c in cols];coeff=solve(A,b);recon={}
  for a,row in zip(coeff,source):
   for c,v in row.items():add_fraction(recon,c,a*v)
  assert recon=={c:Fraction(v) for c,v in target.items()};digest=hashlib.sha256();qterms=[]
  for (kind,index),a in zip(gens,coeff):
   digest.update(f'{kind}:{index}:{a.numerator}/{a.denominator};'.encode())
   if kind=='Q':qterms.append({'q_row_index':index,'numerator':a.numerator,'denominator':a.denominator})
  results[f'k{kp}']={'minor_dimension':n,'exact_nonsingular':True,'full_target_reconstruction':True,'source_coefficient_sha256':digest.hexdigest(),'max_abs_source_numerator':max(abs(a.numerator) for a in coeff),'max_source_denominator':max(a.denominator for a in coeff),'source_coefficients':[{'kind':k[0],'row_index':k[1],'numerator':a.numerator,'denominator':a.denominator} for k,a in zip(gens,coeff)],'q_coefficients':qterms}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-seed-exact-rational-minor.v1','status':'canonical_seed_identities_verified_over_Q','crt_primes':list(PS),'max_abs_reconstructed_integer_row_entry':global_max,'results':results,'decision':'Both canonical seed identities are solved and fully reconstructed over exact rational arithmetic on source-derived dependency minors.','limitations':['minor selected by modular pivot closure','integer row reconstruction uses four-prime CRT and requires entries below half modulus product','degree-14 canonical seeds only'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
