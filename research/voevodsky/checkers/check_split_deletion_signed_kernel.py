"""Split square-row deletion kills a one-dimensional signed comparison."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1),((1,1),2))
def evaluate(m):return tuple(sum(rows[i][0][j]*m[i] for i in range(5)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(5))
def retract(m):return (m[0],m[1]+m[4],m[2],m[3]+m[4])
def include(m):return m+(Q(0),)
def sub(a,b):return tuple(a[i]-b[i] for i in range(len(a)))
kernel=(Q(0),-Q(1),Q(0),-Q(1),Q(1))
assert retract(kernel)==(0,0,0,0) and evaluate(kernel)==((0,0),0)
# First four columns of retraction are the identity: rank 4, nullity 1.
assert all(retract(tuple(Q(int(i==j)) for i in range(5)))==tuple(Q(int(i==j)) for i in range(4)) for j in range(4))
proofs=[(Q(0),Q(1)-z,Q(0),Q(1)-z,z) for z in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))]
assert all(min(p)>=0 and evaluate(p)==((1,1),2) and retract(p)==(0,1,0,1) for p in proofs)
for a,b in combinations(proofs,2):
 d=sub(b,a)
 assert d==tuple((b[4]-a[4])*v for v in kernel)
 assert retract(d)==(0,0,0,0) and d!=(0,)*5
 assert include(retract(a))==include(retract(b))
 assert a==tuple(include(retract(a))[i]+a[4]*kernel[i] for i in range(5))
report={'passed':True,'positive_proof_packets':len(proofs),'pairwise_nonzero_signed_deltas_killed':10,'split_retraction_rank':4,'signed_kernel_dimension':1,'kernel_basis':list(map(str,kernel)),'minimal_packet_recovery':'retain deleted-row multiplier z and old retracted packet; history additionally needs row-introduction and comparison-edge records','scope':'Exact square x+y<=2 redundant row, not general row deletion, historical proof identity, source issuer authority or analytic role correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/split-deletion-signed-kernel.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
