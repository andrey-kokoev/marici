"""Three-color the projected facets. Decode inclusion-minimal obstructions without using any saved support cycle or positive deletion label."""
from ramsey312_google_two_step import *
import igraph as ig
from collections import Counter
from itertools import combinations

def main():
 stats=Counter();out=[];tot=Counter()
 for line in open(sys.argv[1]):
    lhs,rhs=line.split(';');t,d,n,*s=map(int,lhs.split());es=[tuple(map(int,x.split(':'))) for x in rhs.split()];assert n==len(s);tot[t]+=1
    def test(V,k):
        with Solver(name='g4') as sl:
            for i in V:sl.add_clause([k*i+c+1 for c in range(k)])
            for i,j in es:
                if i in V and j in V:
                    for c in range(k):sl.add_clause([-k*i-c-1,-k*j-c-1])
            return sl.solve()
    V=set(range(n));
    if test(V,3):continue
    four=test(V,4);assert four
    for i in range(n):
        if not test(V-{i},3):V.remove(i)
    v=sorted(V);G=ig.Graph(n=len(v),edges=[(v.index(i),v.index(j)) for i,j in es if i in V and j in V]);m=len(v);q=m//3;H=ig.Graph(n=m,edges=[(i,j) for i,j in combinations(range(m),2) if q<=j-i<=m-q]);iso,perm,_=H.isomorphic_vf2(G,return_mapping_12=True) if m==3*q+1 else (False,None,None);stats[(tuple(bits(t)),m,iso)]+=1;out.append(dict(triple=list(bits(t)),extra=list(bits(d)),facets=n,circular=iso,kernel=[s[v[i]] for i in (perm if iso else range(m))]))
 print('totals',tot,'critical',stats);(D/'ramsey312_blind_center_kernels.json').write_text(json.dumps(out));
if __name__=='__main__':main()
