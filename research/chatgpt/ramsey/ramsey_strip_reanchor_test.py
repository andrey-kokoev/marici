"""Compare composing row pairings with transporting one colored row to the other. Enumerate column permutations only; no strip/census data."""
from itertools import permutations
X=(1,2,3,4);src='BRNN';dst='BNRN';I=X
compose=lambda p,q:tuple(p[j-1] for j in q)
def inv(p):return tuple(p.index(i)+1 for i in X)
def moved(p):return sum(i!=j for i,j in zip(X,p))
def rowpair(w):
 p=list(X);i,j=w.index('B'),w.index('R');k,l=[n for n,c in enumerate(w) if c=='N'];p[i],p[j]=p[j],p[i];p[k],p[l]=p[l],p[k];return tuple(p)
a,b=map(rowpair,(src,dst));raw=compose(b,a);valid=[]
for h in permutations(X):
 if not all(src[i-1]==dst[h[i-1]-1] for i in X):continue
 assert compose(h,compose(a,inv(h)))==b
 repair=compose(h,inv(raw));assert compose(repair,raw)==h
 valid.append((h,compose(h,h)==I,repair,moved(repair)))
print('raw',raw,'(transport, involution, post-correction, correction support)',valid);assert valid==[((1,3,2,4),True,(4,2,3,1),2),((1,3,4,2),False,(2,4,3,1),3)]
