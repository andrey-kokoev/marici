"""Local factor test for arbitrary closed walks. Resolve a stationary face step by ALL three centroid-edge ports of that face and sum closed proton traces (not amplitudes before squaring)."""
from ramsey_face_crossing_loop_phase import D,json,F,A,read_operator,product,tr
from itertools import product as tuples
from collections import Counter

def run():
    root=D.parents[1];data=lambda n:json.loads((root/f'strominger/results/common-three-carrier-protocol/{n}.json').read_text());e,p=map(data,['electron','proton']);N=read_operator(e['operators']['N'],8);L=read_operator(e['operators']['L'],8);Q=read_operator(p['operators']['N'],36);assert product(Q,Q)==Q and tr(Q)==A(1);assert product(L,N)==product(N,L)==N
    block=lambda M,i,j,k:{(a,b):z for (a,b),z in M.items() if a//k==i and b//k==j};weight={}
    for i in range(4):
        l=block(L,i,i,2);assert product(l,l)==l and tr(l)==A(1)
        for j in range(4):
            b=block(N,j,i,2);v=tr(product(block(N,i,j,2),b));q=F(1,4) if i==j else F(1,12);assert v==A(q);weight[i,j]=q
    for j in range(12):assert tr(block(Q,j,j,3))==A(F(1,12))
    counts=Counter()
    for k in range(1,7):
        for w in tuples(range(4),repeat=k):
            edges=list(zip(w,w[1:]+w[:1]));s=sum(i==j for i,j in edges);v=F(1)
            for edge in edges:v*=weight[edge]
            assert v==3**s*F(1,12)**k;counts[k]+=1
    return dict(words_by_length=counts,stationary_single_port='1/12',stationary_three_port_sum='1/4',out_and_back='1/144',out_stay_back='1/576')
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_face_walk_refinement.json').write_text(json.dumps(out)+'\n')
