"""Exact retained-frame engine for the declared rational tail-control family.

Ambient carrier: 0<=x_n<=1, n>=1. Objective -sum 2^-n x_n.
Frames are finite-support closed linear inequalities. This is not a parser
or admission authority for arbitrary analytical prime-tail evidence.
"""
from fractions import Fraction as Q
import hashlib,json
from sympy import Rational
from sympy.solvers.simplex import linprog,InfeasibleLPError
CONTEXT={'source':'bounded-sequence-control-v1','objective':'minus-dyadic-sum','admission':'declared exact fixture constraints; no physical authentication'}
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
CONTEXT_ID=digest(CONTEXT)
def sp(q):return Rational(q.numerator,q.denominator)
def genesis():return {'context':CONTEXT_ID,'frames':[]}
def row(coefficients,bound):return {'coefficients':{str(n):str(Q(v)) for n,v in coefficients.items()},'upper':str(Q(bound))}
def frame(state,label,rows):
 return {'context':CONTEXT_ID,'parent':digest(state),'label':label,'rows':rows}
def append(state,f):
 if state['context']!=CONTEXT_ID or f['context']!=CONTEXT_ID:raise ValueError('foreign context')
 if f['parent']!=digest(state):raise ValueError('nonextending evidence lineage')
 if not f['rows']:raise ValueError('empty frame')
 for r in f['rows']:
  Q(r['upper'])
  for n,v in r['coefficients'].items():
   if str(int(n))!=n or int(n)<1:raise ValueError('invalid coordinate')
   Q(v)
 # A contradictory conjunction is retained and classified, not silently
 # replaced by the last individually feasible frame.
 return {'context':CONTEXT_ID,'frames':state['frames']+[f]}
def compile_state(state):
 rows=[r for f in state['frames'] for r in f['rows']]
 m=max([1]+[int(n) for r in rows for n in r['coefficients']])
 A=[[Q(int(i==j)) for j in range(m)] for i in range(m)];b=[Q(1)]*m
 for r in rows:
  A.append([Q(r['coefficients'].get(str(n),'0')) for n in range(1,m+1)]);b.append(Q(r['upper']))
 return m,A,b
def evaluate(state,threshold):
 m,A,b=compile_state(state);c=[-Q(1,2**n) for n in range(1,m+1)];AA=[list(map(sp,r)) for r in A];bb=list(map(sp,b))
 out={'state_digest':digest(state),'horizon':m,'threshold':str(threshold)}
 try:
  value,primal=linprog(list(map(sp,c)),AA,bb)
  px=list(map(lambda t:Q(str(t)),primal))
  if not (all(t>=0 for t in px) and all(sum(a*t for a,t in zip(row,px))<=bound for row,bound in zip(A,b))):
   # A solver return is not admission. Require a checked Farkas certificate
   # before interpreting a failed primal candidate as inconsistency.
   raise InfeasibleLPError('returned candidate fails exact feasibility')
 except InfeasibleLPError:
  # Farkas: y>=0, A^T y>=0 and b.y<=-1 contradict Ax<=b,x>=0.
  dualA=[[-sp(A[i][j]) for i in range(len(A))] for j in range(m)]+[bb]
  _,y=linprog([0]*len(A),dualA,[0]*m+[-1])
  fy=[Q(str(t)) for t in y]
  assert all(t>=0 for t in fy) and all(sum(A[i][j]*fy[i] for i in range(len(A)))>=0 for j in range(m)) and sum(t*v for t,v in zip(b,fy))<0
  return {**out,'status':'EVIDENCE_CONSISTENCY_FAILURE','farkas':list(map(str,y))}
 _,y=linprog(bb,[[-sp(A[i][j]) for i in range(len(A))] for j in range(m)],list(map(sp,c)))
 dy=[Q(str(t)) for t in y];v=Q(str(value))
 assert all(t>=0 for t in dy) and all(sum(A[i][j]*dy[i] for i in range(len(A)))>=-c[j] for j in range(m))
 assert sum(t*p for t,p in zip(c,px))==v==-sum(t*p for t,p in zip(b,dy))
 epsilon=Q(1,2**m);infimum=v-epsilon
 # All frame coordinates <=m. Appending x_n=1 for n>m is feasible and
 # attains exactly the dyadic tail -2^-m. Thus the infinite optimum is exact.
 status='UNIVERSAL_THRESHOLD_SEPARATION' if infimum>threshold else 'ADMITTED_COUNTEREXAMPLE'
 return {**out,'status':status,'primal':list(map(str,primal)),'dual':list(map(str,y)),'finite_optimum':str(v),'tail_error':str(epsilon),'infinite_primal_tail':1,'infinite_optimum':str(infimum)}
