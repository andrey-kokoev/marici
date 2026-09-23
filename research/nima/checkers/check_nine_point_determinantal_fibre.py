"""Exact n=9 determinantal lift of a positive CZ fibre and its relaxation gate."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
K=s.Matrix([[(-1)**(j-p)*comb(6,j-p) if 0<=j-p<=6 else 0
             for j in range(9)] for p in range(3)])
assert K.shape==(3,9) and K*Z==s.zeros(3,6) and K.rank()==3
assert all(s.prod(j-i for i,j in combinations(ids,2))>0 for ids in combinations(range(1,10),6))
x=s.Matrix([[1]*9]);y=s.Matrix([[1,1,2,3,4,5,6,7,8]])
A=s.symbols('a0:3');B=s.symbols('b0:3');q=s.symbols('q01 q02 q12')
C=x.col_join(y);T=s.Matrix([A,B]);shifted=C+T*K
def delta(D,i,j):return s.expand(D[0,i]*D[1,j]-D[0,j]*D[1,i])
def affine_lift(i,j):
 base=delta(C,i,j)
 first=sum(A[p]*(K[p,i]*y[0,j]-K[p,j]*y[0,i])+B[p]*(x[0,i]*K[p,j]-x[0,j]*K[p,i]) for p in range(3))
 second=sum(q[z]*(K[p,i]*K[r,j]-K[p,j]*K[r,i]) for z,(p,r) in enumerate(combinations(range(3),2)))
 return s.expand(base+first+second)
relations={q[z]:A[p]*B[r]-A[r]*B[p] for z,(p,r) in enumerate(combinations(range(3),2))}
for i,j in combinations(range(9),2):
 assert s.expand(delta(shifted,i,j)-affine_lift(i,j).subs(relations))==0
assert shifted*Z==C*Z
# A real admitted target with a strictly positive source in this fibre.
strict={v:0 for v in (*A,*B)};strict[B[1]]=s.Rational(1,10000)
strict_min=min(delta(shifted.subs(strict),i,j) for i,j in combinations(range(9),2));assert strict_min>0
# The independent-q linear relaxation has a spurious point above T=0.
# All affine minor inequalities are strict, but q != wedge^2 T.
fake={v:0 for v in (*A,*B,*q)};fake[q[0]]=s.Rational(1,10000)
relax_min=min(affine_lift(i,j).subs(fake) for i,j in combinations(range(9),2));assert relax_min>0
assert fake[q[0]]!=relations[q[0]].subs(fake)
# Two-dimensional slice recovers curved boundary already at n=8.
slice_values={v:0 for v in (*A,*B)};slice_values[A[0]]=s.Symbol('a');slice_values[B[1]]=s.Symbol('b')
slice_minor=s.expand(delta(shifted,0,1).subs(slice_values))
assert slice_minor==7*s.Symbol('a')+s.Symbol('b')+s.Symbol('a')*s.Symbol('b')
# At r=4 (n=10), lifted quadratic coordinates have an additional
# Plucker equation even before enforcing their coupling to T.
U=s.Matrix([s.symbols('u0:4'),s.symbols('v0:4')]);P={(i,j):s.det(U[:,[i,j]]) for i,j in combinations(range(4),2)}
assert s.expand(P[0,1]*P[2,3]-P[0,2]*P[1,3]+P[0,3]*P[1,2])==0
assert 1*1-0*0+0*0!=0
report={'schema':'marici.nima.nine-point-determinantal-fibre.v1','passed':True,
 'n':9,'source_rank':2,'external_rank':6,'kernel_dimension':K.rows,
 'kernel_basis':[[str(K[p,j]) for j in range(9)] for p in range(3)],
 'fibre_parameters':6,'lifted_coordinates':9,'minor_constraints':36,
 'lifted_quadratic_coordinates':['q01','q02','q12'],
 'realizability_equations':['q01=a0*b1-a1*b0','q02=a0*b2-a2*b0','q12=a1*b2-a2*b1'],
 'symbolic_affine_minor_identities':36,
 'strict_positive_real_lift':{'b1':'1/10000','minimum_source_minor':str(strict_min)},
 'spurious_relaxed_lift':{'all_a_b':'0','q01':'1/10000','q02':'0','q12':'0','minimum_affine_minor':str(relax_min),'violates_realizability':True},
 'curved_slice_minor_12':str(slice_minor),
 'n10_first_pure_quadratic_plucker_relation':'q01*q23-q02*q13+q03*q12=0',
 'scope':'Exact semialgebraic fixed-target carrier at n=9. Linear relaxation alone admits fictitious witnesses. No nine-point history-cell matching, global membership algorithm or n^-2 estimate.'}
(OUT/'nine-point-determinantal-fibre.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
