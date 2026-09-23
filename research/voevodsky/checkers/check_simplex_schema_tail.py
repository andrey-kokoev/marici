"""Exact simplex proposal backend; arithmetic certificates checked separately."""
from fractions import Fraction as Q
from pathlib import Path
import json,time
from sympy import Rational
from sympy.solvers.simplex import linprog, InfeasibleLPError
from check_schema_relative_tail_lp import rows,pull,fixtures
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
MS=(3,4,8,16)
def rat(x):return Rational(x.numerator,x.denominator)
def lp(c,A=None,b=None,E=None,f=None):
 def mat(a):return None if a is None else [[rat(Q(v)) for v in row] for row in a]
 def vec(a):return None if a is None else [rat(Q(v)) for v in a]
 if A is None:A=[[Q(0)]*len(c)];b=[Q(0)]
 value,x=linprog(vec(c),mat(A),vec(b),mat(E),vec(f))
 return Q(str(value)),[Q(str(v)) for v in x]
def certify(state,query):
 rs=rows(state);m=state['m'];objective=[Q(0)]*m
 if query['kind']=='membership':
  d=2+len(state['audits'])
  for i,v in enumerate(map(Q,query['point'])):
   a=pull(m,state['audits'],[Q(int(i==j)) for j in range(d)])
   rs.extend([(a,v),(tuple(-x for x in a),-v)])
 else:objective=list(pull(m,state['audits'],list(map(Q,query['objective']))))
 A=[list(a) for a,b in rs];b=[b for a,b in rs];packet={'state':state,'query':query}
 try:
  value,x=lp([-v for v in objective],A,b)
 except InfeasibleLPError:
  # Independently solve for a normalized Farkas ray. Nonnegativity rows are
  # explicit in rs, so the certificate has no implicit variable-bound terms.
  E=[[a[j] for a in A] for j in range(m)]+[b]
  _,w=lp([Q(0)]*len(rs),E=E,f=[Q(0)]*m+[Q(-1)])
  packet.update(status='EMPTY',weights=[[i,str(v)] for i,v in enumerate(w) if v])
  return packet
 E=[[a[j] for a in A] for j in range(m)]
 upper,w=lp(b,E=E,f=objective)
 assert upper==-value
 packet.update(status='FEASIBLE_OPTIMUM',x=list(map(str,x)),value=str(-value),weights=[[i,str(v)] for i,v in enumerate(w) if v])
 return packet
if __name__=='__main__':
 start=time.perf_counter();packets=[certify(s,q) for s,q in fixtures(MS)]
 report={'backend':'sympy exact rational simplex','m_values':MS,'elapsed_seconds':time.perf_counter()-start,'packets':packets,
 'scope':'Source rows and dual LP materialized. Exact simplex replaces exhaustive active-set enumeration; no polynomial-time or large-m performance claim.'}
 (OUT/'simplex-schema-tail.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='packets'},indent=2))
