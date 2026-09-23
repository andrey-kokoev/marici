"""One-variable Fourier--Motzkin compiler with proof-carrying compaction.
All displayed public coordinates are explicitly constrained nonnegative.
LP is a certificate proposer only; verify_audit_elimination imports no solver.
"""
from fractions import Fraction as Q
from joint_audit_tail_interface import lp,dot
from sympy.solvers.simplex import UnboundedLPError,InfeasibleLPError
PROPOSAL_ERRORS=(UnboundedLPError,InfeasibleLPError,AssertionError,ValueError,ZeroDivisionError)

def eliminate(rows,index):
 positive=[i for i,(a,b) in enumerate(rows) if a[index]>0]
 negative=[i for i,(a,b) in enumerate(rows) if a[index]<0]
 zero=[i for i,(a,b) in enumerate(rows) if a[index]==0]
 assert positive and negative # source audit caps ensure both
 recipes=[[(i,Q(1))] for i in zero]+[[(i,1/rows[i][0][index]),(j,-1/rows[j][0][index])] for i in positive for j in negative]
 out=[]
 for recipe in recipes:
  a=tuple(sum(w*rows[i][0][k] for i,w in recipe) for k in range(len(rows[0][0])));b=sum(w*rows[i][1] for i,w in recipe)
  assert a[index]==0
  out.append({'normal':list(map(str,a[:index]+a[index+1:])),'upper':str(b),'origin':[[i,str(w)] for i,w in recipe]})
 return out,{'positive':len(positive),'negative':len(negative),'zero':len(zero),'raw_rows':len(out)}

def compile_projection(rows,index,prune=True):
 raw,counts=eliminate(rows,index);candidates={}
 for row in raw:
  a=tuple(map(Q,row['normal']));b=Q(row['upper']);scale=next((abs(v) for v in a if v),abs(b) if b else Q(1))
  a=tuple(v/scale for v in a);b/=scale
  if not any(a) and b>=0:continue
  value={'normal':list(map(str,a)),'upper':str(b),'origin':[[i,str(Q(w)/scale)] for i,w in row['origin']]}
  if a not in candidates or b<Q(candidates[a]['upper']):candidates[a]=value
 final=list(candidates.values());d=len(rows[0][0])-1;refusals=[]
 # Keep explicit nonnegativity: the LP proposer uses nonnegative variables.
 mandatory={tuple(Q(-int(k==j)) for k in range(d)) for j in range(d)}
 if prune:
  for row in list(final):
   if tuple(map(Q,row['normal'])) in mandatory and Q(row['upper'])==0:continue
   others=[r for r in final if r is not row]
   try:answer=lp([tuple(map(Q,r['normal'])) for r in others],[Q(r['upper']) for r in others],tuple(map(Q,row['normal'])))
   except PROPOSAL_ERRORS as error:
    refusals.append({'stage':'prune','exception':type(error).__name__});continue # no certified implication: retain the row
   if answer['status']=='INCONSISTENT' or Q(answer['value'])<=Q(row['upper']):final.remove(row)
 assert all(any(tuple(map(Q,r['normal']))==a and Q(r['upper'])==0 for r in final) for a in mandatory)
 # Final, not intermediate, presentation proves every eliminated inequality.
 # If proof proposal fails, restore that valid raw row and retry. Thus solver
 # failure affects compaction only, not completeness of exact elimination.
 while True:
  implications=[];cache={};retry=False
  A=[tuple(map(Q,r['normal'])) for r in final];b=[Q(r['upper']) for r in final]
  for row in raw:
   key=(tuple(map(Q,row['normal'])),Q(row['upper']))
   if key in cache:continue
   answer=None
   for i,(a,bound) in enumerate(zip(A,b)):
    if not any(a) and bound<0:
     weights=[Q(0)]*len(A);weights[i]=-1/bound;answer={'status':'INCONSISTENT','multipliers':list(map(str,weights))};break
    nz=next((j for j,v in enumerate(a) if v),None)
    scale=key[0][nz]/a[nz] if nz is not None else Q(0)
    if scale>=0 and all(scale*v>=w for v,w in zip(a,key[0])) and scale*bound<=key[1]:
     weights=[Q(0)]*len(A);weights[i]=scale;answer={'status':'BOUND','multipliers':list(map(str,weights))};break
   if answer is None:
    try:
     answer=lp(A,b,key[0]);assert answer['status']=='INCONSISTENT' or Q(answer['value'])<=key[1]
    except PROPOSAL_ERRORS as error:
     refusals.append({'stage':'final-implication','exception':type(error).__name__});final.append(row);retry=True;break
   cache[key]=len(implications);implications.append({'normal':list(map(str,key[0])),'upper':str(key[1]),'proof':answer})
  if not retry:break
 return {'retired_position':index,'counts':{**counts,'canonical_rows':len(candidates),'final_rows':len(final)},'rows':final,'implications':implications,'raw_implication_indices':[cache[(tuple(map(Q,r['normal'])),Q(r['upper']))] for r in raw],'proposal_refusals':refusals}

def extend(rows,index,public):
 lower=[];upper=[]
 for a,b in rows:
  coefficient=a[index];constant=b-dot(a[:index]+a[index+1:],public)
  if coefficient>0:upper.append(constant/coefficient)
  elif coefficient<0:lower.append(constant/coefficient)
  else:assert constant>=0
 lo=max(lower);hi=min(upper);assert lo<=hi
 h=(lo+hi)/2;fine=public[:index]+(h,)+public[index:]
 assert all(dot(a,fine)<=b for a,b in rows)
 return fine,(lo,hi)
