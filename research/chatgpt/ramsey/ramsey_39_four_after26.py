"""Exact joint-border audit on the 26-prefix of the published path to 29."""
from ramsey_39_pattern_three_choices import Random, add, options
from itertools import combinations
from collections import Counter

def main():
    pairs=[];ind=[0];r=Random(39)
    for n in range(21): pairs,ind=add(n,r.choice(options(n,pairs,ind)),pairs,ind)
    for n,L in enumerate([[1,4,6,8,13,19],[1,7,8,11,13,18],[7,9,10,16,18,20,22],[7,9,10,17,18,19],[2,10,11,13,15,16,18]],21):
        p=sum(1<<(x-1) for x in L);assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind)
    opts=options(26,pairs,ind);N=len(opts);inds={k:[s for s in ind if s.bit_count()==k] for k in (5,6,7)}
    miss={k:[sum(1<<b for b,s in enumerate(ss) if not p&s) for p in opts] for k,ss in inds.items()}
    # path: sorted original type indices; edges: signs internal to added block.
    count=Counter();winners=set();example=[]
    def visit(path,edges):
        count[len(path)]+=1
        if len(path)==4:
            winners.update(path)
            if not example: example.extend(opts[p] | (e<<26) for p,e in zip(path,edges))
            return
        for q in range(path[-1] if path else 0,N):
            signs=[0]
            for j,p in enumerate(path):
                plus=not(opts[p]&opts[q]);minus=not(miss[7][p]&miss[7][q]);signs=[x|(v<<j) for x in signs for v in range(2) if (plus if v else minus)]
                if not signs:break
            for e in signs:
                def invalid():
                    for i,j in combinations(range(len(path)),2):
                        pattern=(e>>i&1)+(e>>j&1)+(edges[j]>>i&1)
                        if pattern==3 or (pattern==0 and miss[6][q]&miss[6][path[i]]&miss[6][path[j]]):return True
                    return len(path)==3 and not(e or any(edges)) and bool(miss[5][q]&miss[5][path[0]]&miss[5][path[1]]&miss[5][path[2]])
                if not invalid():visit(path+[q],edges+[e])
    visit([],[]);print('counts',count,'first choices reaching 30',len(winners),'of',N)
    for n,p in enumerate(example,26):
        assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind);print(n+1,[i+1 for i in range(n) if p>>i&1])
if __name__=='__main__':main()
