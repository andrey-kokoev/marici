"""Exhaust rooted triangle-free cores in increasing order around fixed induced 2K2. Search connected min-degree-two collision cores; insist on a maximal triangle-free core for a stronger stress test. Verify top diversity exhaustively."""
from ramsey_neighbourhood_square import D,json,inds,bits,combinations,Counter,grow
from itertools import combinations_with_replacement

def rooted(n):
    profiles=[p for p in range(16) if p&3!=3 and p&12!=12];m=n-4
    for ps in combinations_with_replacement(profiles,m):
        if not any(p.bit_count()==2 for p in ps):continue
        H=[2,1,8,4]+list(ps)
        for j,p in enumerate(ps,4):
            for i in bits(p):H[i]|=1<<j
        if any(h.bit_count()<2 for h in H[:4]):continue
        pairs=[(i,j) for i,j in combinations(range(4,n),2) if not H[i]&H[j]]
        def gen(h):
            if h==len(pairs):
                if min(map(int.bit_count,H))>=2:yield H
                return
            i,j=pairs[h];yield from gen(h+1)
            if not H[i]&H[j]:
                H[i]^=1<<j;H[j]^=1<<i;yield from gen(h+1);H[i]^=1<<j;H[j]^=1<<i
        yield from gen(0)

def test(H,three=False):
    I=inds(H);alpha=max(map(int.bit_count,I));k=alpha+1;ends=[(0,2),(0,3),(1,2),(1,3)]
    for rot in ((1,2,3,0),(3,1,0,2)):
        S=[1<<a|1<<b|(H[x]&~(15|H[a]|H[b])) for (a,b),x in zip(ends,rot)];G=grow(H,S)
        if max(map(int.bit_count,G))>k:continue
        maximum=[s for s in I if s.bit_count()==alpha];hit=lambda s:sum(bool(s&t) for t in S)
        if any(hit(s)<3 for s in maximum):continue
        bad=[s for s in I if s.bit_count()+4-hit(s)>k]
        if bad and (not three or any(s.bit_count()==alpha-1 for s in bad)):return dict(core=list(H),alpha=alpha,ports=S,donors=rot,max_sets=maximum,bad=bad,blue=max(map(int.bit_count,inds(G))))

def run(three=False):
    out={};counts=Counter()
    for n in range(5,11):
        for H in rooted(n):
            if any(not(H[i]>>j&1 or H[i]&H[j]) for i,j in combinations(range(n),2)):continue
            counts[n]+=1;r=test(H,three)
            if r:out=r;break
        if out:break
    return dict(rooted_counts=counts,witness=out)
def lift_check(H):
    out=[]
    for _ in range(5):
        n=len(H);h=H[4];H=[v|((1<<n) if h>>i&1 else 0) for i,v in enumerate(H)]+[h];r=test(H);assert r and r['blue']==r['alpha']+2 and all((H[i]>>j&1 or H[i]&H[j]) for i,j in combinations(range(n+1),2));out.append([n+1,r['alpha'],r['blue']])
    return out
if __name__=='__main__':
    z=dict(any_failure=run(),three_port_failure=run(True));z['twin_checks']=lift_check(z['any_failure']['witness']['core']);print(z);(D/'ramsey_copy_exchange_counter.json').write_text(json.dumps(z)+'\n')
