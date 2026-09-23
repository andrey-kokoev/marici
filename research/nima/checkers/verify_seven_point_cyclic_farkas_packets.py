"""Independent exact replay of sparse fibre-wide cyclic-to-full Farkas packets."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results'
K=tuple((-1)**j*comb(6,j) for j in range(7));assert K==(1,-6,15,-20,15,-6,1)
assert all(sum(K[j]*(j+1)**degree for j in range(7))==0 for degree in range(6))
def minor(x,y,i,j):
 return (x[i]*y[j]-x[j]*y[i],K[i]*y[j]-K[j]*y[i],x[i]*K[j]-x[j]*K[i])
def verify(case):
 x,y=[[Q(v) for v in row] for row in case['source_rows']];assert len(x)==len(y)==7
 assert all(minor(x,y,i,j)[0]>0 for i,j in combinations(range(7),2))
 allowed={(i,i+1) for i in range(6)}|{(0,6)}
 expected=set(combinations(range(7),2))-allowed
 assert len(case['certificates'])==14
 used=set()
 for item in case['certificates']:
  i,j=(int(z)-1 for z in item['minor']);assert (i,j) in expected and (i,j) not in used;used.add((i,j))
  p,q=[tuple(int(z)-1 for z in e) for e in item['cyclic_edges']]
  assert p!=q and p in allowed and q in allowed
  a,b=map(Q,item['coefficients']);gamma=Q(item['constant']);assert min(a,b,gamma)>=0
  L=minor(x,y,i,j);P=minor(x,y,*p);T=minor(x,y,*q)
  assert all(L[d]==a*P[d]+b*T[d]+(gamma if d==0 else 0) for d in range(3))
 assert used==expected
 return len(used)
def main():
 packet=json.loads((N/'seven-point-cyclic-farkas-packets.json').read_text());assert packet['negative_control_rejected'] and len(packet['cases'])==7
 assert [c['negative_initial_columns'] for c in packet['cases']]==list(range(7))
 assert sum(verify(c) for c in packet['cases'])==98
 # Reject unrestricted cyclic sufficiency independently of producer flags.
 bx=list(map(Q,[1,1,0,-1,-1,-1,2]));by=list(map(Q,[0,1,1,1,0,-2,1]));z=(Q(-1,20),Q(1,20))
 allowed={(i,i+1) for i in range(6)}|{(0,6)}
 assert all(sum(a*b for a,b in zip(minor(bx,by,*p),(1,*z)))>=0 for p in allowed)
 assert sum(a*b for a,b in zip(minor(bx,by,0,5),(1,*z)))==Q(-43,20)
 refused=[]
 for name in ('corrupt-weight','negative-constant','missing-minor','changed-source'):
  bad=copy.deepcopy(packet['cases'][0]);item=bad['certificates'][0]
  if name=='corrupt-weight':item['coefficients'][0]=str(Q(item['coefficients'][0])+1)
  if name=='negative-constant':item['constant']='-1'
  if name=='missing-minor':bad['certificates'].pop()
  if name=='changed-source':bad['source_rows'][0][0]='-1'
  try:verify(bad)
  except (AssertionError,ValueError,KeyError):refused.append(name)
  else:raise AssertionError(name+' was accepted')
 result={'passed':True,'admitted_targets':7,'whole_fibre_noncyclic_implications':98,'mutations_rejected':refused,
         'scope':'Finite target certificates only; universal cyclic redundancy remains open.'}
 (N/'seven-point-cyclic-farkas-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
