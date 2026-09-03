#!/usr/bin/env python3
"""Lift the exact scalar solution to the finite cube at cutoff 14."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';sol=json.loads((R/'cosmology_rees_scalar_joint_tail_solve.json').read_text())
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
A=14;rows=g['construct'](A);lev=(1,1,1,1,1);target={(2,(0,1,1,1,1,1,(0,0))):F(3)}
def add(dst,src,c):
 for k,v in src.items():dst[k]=dst.get(k,F(0))+c*v
 for k in [k for k,v in dst.items() if not v]:del dst[k]
res=dict(target);expanded=0
for z in sol['solution']:
 label=eval(z['label'],{'__builtins__':{}},{});block,axis,i,j=label;kp=1 if block=='boundary' else 0;c=F(z['coefficient'])
 for t in range(j+1):
  cy=c*comb(j,t)*F((-3)**(j-t));key=('shift2',('twisted_derivative',kp,lev,axis,(i,t)));add(res,rows[key],-cy);expanded+=1
basis={};used_max_degree=0
def reduce(row,insert=False):
 global used_max_degree
 while row:
  q=min(row);x=row[q]
  if q not in basis:
   if insert:
    basis[q]={k:v/x for k,v in row.items()};used_max_degree=max(used_max_degree,max(sum(k[-1]) for grade,k in row))
   return row
  for k,v in basis[q].items():row[k]=row.get(k,F(0))-x*v
  row={k:v for k,v in row.items() if v}
 return {}
for (shape,label),row in rows.items():
 if shape=='shift2' and label[0] in ('q_multiplication','K_multiplication'):reduce(dict(row),True)
nf=reduce(dict(res));assert not nf
out={'schema':'marici.benincasa.cosmology-rees-lift-scalar-preimage.v1','cutoff':A,'scalar_solution_terms':len(sol['solution']),'expanded_XY_derivative_terms':expanded,'multiplication_basis_rank':len(basis),'exact_cube_residual_zero':True,'maximum_monomial_degree_seen_in_multiplication_rows':used_max_degree,'disposition':'tau has an exact preimage in the original fixed-pole relation presentation at cutoff 14','passed':True};(R/'cosmology_rees_lift_scalar_preimage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
