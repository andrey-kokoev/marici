"""Produce exact finite LP primal/dual packets for the scoped theorem controls."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
from sympy import Rational
from sympy.solvers.simplex import linprog
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sp(q):return Rational(q.numerator,q.denominator)
def fq(z):return Q(str(z))
def data(mode,m):
 c=[-Q(1,2**n) for n in range(1,m+1)];A=[];b=[]
 for n in range(1,m+1):
  A.append([Q(int(j==n)) for j in range(1,m+1)]);b.append(Q(0 if mode=='even_support' and n%2 else 1))
 for i in range(m):
  for j in range(i+1,m+1):
   A.append([Q(int(i<n<=j)) for n in range(1,m+1)])
   cap=(j-i+1)//2 if mode=='adjacent_capacity' else sum(mode!='even_support' or n%2==0 for n in range(i+1,j+1))
   b.append(Q(cap))
 return c,A,b
packets=[]
for mode in ('all_slots','even_support','adjacent_capacity'):
 for m in (2,4,8,16):
  c,A,b=data(mode,m)
  optimum,primal=linprog(list(map(sp,c)),[list(map(sp,row)) for row in A],list(map(sp,b)))
  dual_cost,dual=linprog(list(map(sp,b)),[[sp(-A[i][j]) for i in range(len(A))] for j in range(m)],list(map(sp,c)))
  assert optimum==-dual_cost
  packets.append({'mode':mode,'m':m,'primal':list(map(str,primal)),'dual':list(map(str,dual)),'finite_optimum':str(optimum),'uniform_tail_error':str(Q(1,2**m)),'full_lower':str(fq(optimum)-Q(1,2**m)),'full_upper':str(optimum)})
proof=HERE.parent/'witness-or-separator-for-dominated-tail-carriers.md'
out={'schema':'dominated-tail-witness-separator.v1','scope':'Exact rational controls of the general theorem, not a new actual-prime task result.','objective':'sum -2^(-n) x_n, n>=1','reference_relaxation_infimum':'-1','known_full_optima':{'all_slots':'-1','even_support':'-1/3','adjacent_capacity':'-2/3'},'packets':packets,'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),proof)}}
(R/'tail-witness-separator.json').write_text(json.dumps(out,indent=2)+'\n')
print('Constructed',len(packets),'exact primal/dual packets; independent Fraction replay required.')
