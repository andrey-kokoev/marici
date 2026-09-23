"""Nontrivial Farkas mixtures, positive surplus and two reference changes."""
from fractions import Fraction as Q
from pathlib import Path
import json
def mv(M,v):return tuple(sum(Q(x)*Q(y) for x,y in zip(row,v)) for row in M)
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def shifted(r,n,d,c):return add(tuple(a-b*Q(d) for a,b in zip(r,n)),c)
A=((-1,),(1,));r=(Q(0),Q(1));s=Q(0)
M=((1,0),(0,1),(1,1));d=Q(1,4);c=(Q(0),Q(1,2),Q(1,3))
B=mm(M,A);u=shifted(mv(M,r),tuple(row[0] for row in B),d,c)
N=((1,0,0),(0,1,1));e=-Q(1,8);k=(Q(1,5),Q(2,5))
C=mm(N,B);v=shifted(mv(N,u),tuple(row[0] for row in C),e,k)
composite=mm(N,M);margin=add(mv(N,c),k)
assert C==mm(composite,A)
assert v==shifted(mv(composite,r),tuple(row[0] for row in C),d+e,margin)
assert margin==(Q(1,5),Q(37,30)) and all(x>=0 for x in c+k+margin)
assert s+d+e==Q(1,8)
# Demand exact nonnegative multiplier and surplus plus transported reference.
def check(M,d,c,N,e,k,claimed):
 if any(a<0 for row in M+N for a in row) or any(x<0 for x in c+k):return False
 b=mm(M,A);w=shifted(mv(M,r),tuple(row[0] for row in b),d,c)
 target=shifted(mv(N,w),tuple(row[0] for row in mm(N,b)),e,k)
 return target==claimed
assert check(M,d,c,N,e,k,v)
assert not check(M,d,(Q(-1),)+c[1:],N,e,k,v)
assert not check(M,d,c,N,e,k,tuple(v[i]+Q(int(i==0),8) for i in range(2)))
assert not check(M,d,c,((1,0,0),(0,-1,1)),e,k,v)
# A numerical total of c is insufficient: N uses only its first component
# for output 0 and merges components 1,2 for output 1.
changed=(c[0]+Q(1,6),c[1]-Q(1,6),c[2]);assert sum(changed)==sum(c)
assert add(mv(N,changed),k)!=margin
report={'passed':True,'intermediate_normals':[list(row) for row in B],'final_normals':[list(row) for row in C],'intermediate_residuals':list(map(str,u)),'final_residuals':list(map(str,v)),'composite_surplus':list(map(str,margin)),'combined_reference_shift':str(d+e),'refusals':['negative-surplus','wrong-ref-shift-or-residual','negative-multiplier','equal-total-surplus-unequal-transport'],'scope':'One finite fixed-chart rational Farkas pair; not universal source identity, historical authorization or analytic cofiber.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-surplus-transport.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
