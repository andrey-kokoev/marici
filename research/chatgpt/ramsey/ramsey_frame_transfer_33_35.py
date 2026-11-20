"""Freeze the eight-frame rule. Check restrictions and embeddings in two cyclic witnesses."""
from itertools import combinations
from math import comb
from ramsey_eight_frame_readout import G,mul,inv


def cyclic(n,ds):return [{j for j in range(n) if (j-i)%n in ds} for i in range(n)]
def monos(a,k,red):return [set(t) for t in combinations(range(len(a)),k) if all((j in a[i])==red for i,j in combinations(t,2))]

def main():
    S={(2,0),(0,1),(1,1)}
    frame=[{j for j,h in enumerate(G) if mul(inv(g),h) in S} for g in G]
    assert not monos(frame,3,True)
    for k in (3,4,5):
        bad=monos(frame,k,False)
        counts=[sum(not any(f<=set(t) for f in bad) for t in combinations(range(8),n)) for n in range(9)]
        m=max(i for i,v in enumerate(counts) if v); print('k, blue witness count, max order in frame, subsets:',k,len(bad),m,counts[m])
    cycle=cyclic(5,{1,4});large=cyclic(13,{1,5,8,12});assert not monos(cycle,3,True) and not monos(cycle,3,False) and not monos(large,3,True) and not monos(large,5,False)
    # Explicitly count embeddings via adjacency and nonadjacency at each new vertex.
    def maps(a,b,path=()):
        i=len(path)
        if i==len(a):return 1
        return sum(maps(a,b,path+(j,)) for j in range(len(b)) if j not in path and all((h in a[i])==(v in b[j]) for h,v in enumerate(path)))
    sf=maps(frame,frame);sl=maps(large,large);em=maps(frame,large);print('automorphism counts:',sf,sl,'induced frame copies in 13:',em//sf);assert em%sf==0
    print('cycle order in frame:',maps(cycle,frame)//maps(cycle,cycle))

if __name__=='__main__':main()
