"""Two dependent exact redundant rows: rank-two kernel, two deletion orders."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1),((1,1),2),((2,1),3))
def image(m):return tuple(sum(rows[i][0][j]*m[i] for i in range(6)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(6))
def direct(v):a,x,b,y,z,w=v;return (a,x+z+2*w,b,y+z+w)
def via_second(v):a,x,b,y,z,w=v;return (a,x+w,b,y,z+w)
def via_first(v):a,x,b,y,z,w=v;return (a,x+z,b,y+z,w)
def first_then_second(v):a,x,b,y,w=via_first(v);return (a,x+2*w,b,y+w)
def second_then_first(v):a,x,b,y,z=via_second(v);return (a,x+z,b,y+z)
k1=(Q(0),-Q(1),Q(0),-Q(1),Q(1),Q(0))
k2=(Q(0),-Q(2),Q(0),-Q(1),Q(0),Q(1))
assert direct(k1)==direct(k2)==(0,0,0,0)
assert via_first(k1)==(0,0,0,0,0) and via_second(k2)!= (0,0,0,0,0)
assert via_second(tuple(k2[i]-k1[i] for i in range(6)))==(0,0,0,0,0)
assert image(k1)==image(k2)==((0,0),0)
proofs=[]
for z,w in product((Q(0),Q(1,2),Q(1)),repeat=2):
 v=(Q(0),Q(2)-z-2*w,Q(0),Q(1)-z-w,z,w)
 if min(v)<0:continue
 assert image(v)==((2,1),Q(3))
 assert direct(v)==first_then_second(v)==second_then_first(v)==(0,2,0,1)
 base=direct(v)+(Q(0),Q(0))
 assert v==tuple(base[i]+z*k1[i]+w*k2[i] for i in range(6))
 proofs.append(v)
assert len(proofs)>=3
report={'passed':True,'positive_packets':len(proofs),'signed_kernel_dimension':2,'kernel_basis':[list(map(str,k1)),list(map(str,k2))],'second_first_kernel_generator':'k2-k1','first_first_kernel_generator':'k1','both_deletion_orders_same_old_packet':True,'reconstruction':'old packet plus separately labelled original z,w coefficients along k1,k2','scope':'Exact fixed square with r1:x+y<=2,r2:2x+y<=3; mathematical packet recovery, not historical deletion-order equivalence, source owner or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/two-split-row-kernel-filtration.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
