"""Exact budgeted linear-test constructor. Bit masks encode vectors over F_2."""
from functools import lru_cache,reduce
from itertools import combinations
from pathlib import Path
from operator import xor
import json
from ramsey_cell_decoder_polynomial import obstructions

class Separator:
    def __init__(self,dim,directions):
        self.ds=tuple(sorted(set(directions)));self.dim=dim
        assert all(0<=x<1<<dim for x in self.ds)
        self.cuts=[sum(1<<i for i,x in enumerate(self.ds) if (x&h).bit_count()%2) for h in range(1<<dim)]
        self.full=(1<<len(self.ds))-1

    @lru_cache(None)
    def build(self,m,k):
        if not m:return ()
        if not k:return None
        # Larger cuts first; failure of the residual budget means try the next one.
        seen=set()
        for h in sorted(range(1,len(self.cuts)),key=lambda h:-(m&self.cuts[h]).bit_count()):
            r=m&~self.cuts[h]
            if r==m or r in seen:continue
            seen.add(r);tail=self.build(r,k-1)
            if tail is not None:return (h,)+tail
        return None

def verify_decoder(rows,hs):
    free=(3,5,6,7);table={}
    labels=[j|sum(((h>>free.index(j))&1)<<(3+k) for k,h in enumerate(hs)) if j in free else j for j in range(8)]
    for u,v in combinations(range(24),2):
        key=(u//8,v//8,labels[u%8]^labels[v%8]);color=rows[u]>>v&1
        assert table.setdefault(key,color)==color

if __name__=='__main__':
    base=Path(__file__).parent
    for name in ['4bit_25','5bit_26','6bit_26','6bit_27_from_catalogue']:
        rows=json.loads((base/f'ramsey_38_cell_{name}.json').read_text())['rows'];dim,B=obstructions(rows,3,3);s=Separator(dim,B);hs=next(res for k in range(dim+1) if (res:=s.build(s.full,k)) is not None);verify_decoder(rows,hs);print(name,'minimum extra masks:',hs)
    s=Separator(5,[1,2,3,4,7,8,9,11,16,17,18,28]);assert s.build(s.full,1) is None;hs=s.build(s.full,2);assert hs and s.cuts[hs[0]]|s.cuts[hs[1]]==s.full;print('strict trap: maximum-cut first bit',max(range(32),key=lambda h:s.cuts[h].bit_count()),'recovered pair',hs)
    B=[sum(1<<i for i,x in enumerate((3,5,6,7)) if x in q) for q in combinations(range(8),4) if reduce(xor,q)==0];s=Separator(4,B)
    # Independent check: mark every subset of every cover achievable with two tests.
    feasible={0}
    for c,d in combinations(s.cuts,2):
        u=c|d;m=u
        while m:feasible.add(m);m=(m-1)&u
    for m in range(s.full+1):assert (s.build(m,2) is not None)==(m in feasible)
    print('two-bit feasible / tested:',len(feasible),'/',s.full+1)
