"""Apply the unchanged two-round partition to each legal 21st column."""
from collections import defaultdict
from ramsey_delayed_address_move import moves,build

def run(rows):
    V=range(len(rows));d=list(map(int.bit_count,rows))
    def step(x):return [sum((x[i]-x[j])**2 for j in V if rows[i]>>j&1) for i in V]
    e=step(d);groups=defaultdict(int)
    for i,key in enumerate(zip(e,step(e))):groups[key]|=1<<i
    legal=moves(rows)[2]; hits=[p for p in legal if all((p&g) in (0,g) for g in groups.values())];return len(groups),legal,hits

def add(rows,p):return [r|((p>>i&1)<<len(rows)) for i,r in enumerate(rows)]+[p]
def ids(p):return [i for i in range(p.bit_length()) if p>>i&1]
if __name__=='__main__':
    r=[g&((1<<20)-1) for g in build()[:20]];_,ps,retained=run(r)
    for p in ps:
        g,legal,hits=run(add(r,p));print(ids(p),p in retained,g,len(legal),list(map(ids,hits)))
