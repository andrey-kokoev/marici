"""Two-row projection obstruction: each blue six must be hit by at least one of two marked rows. Derive witnesses without installing the first four."""
from itertools import combinations,product,islice
import gzip,json
from ramsey_retention_slice import CAT,D,decode

def bits(s):return [i for i in range(s.bit_length()) if s>>i&1]
def ind(a):
    I=[0]
    for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
    return I

def pair_obstructions(a,mark,req):
    I=ind(a);tri=[s for s in I if not s&mark and s.bit_count()==3];sets=set(I);cs=[[s|r for s in tri if s|r in sets] for r in req];qs={k:[q for q in I if q.bit_count()==k] for k in (4,5,6)};out=[]
    for i,j in combinations(range(4),2):
        unions={s|t for s,t in product(cs[i],cs[j])};remain=unions.copy();cert=[]
        while remain:
            q=max(qs[6],key=lambda q:sum(not q&u for u in remain));new={u for u in remain if u&q}
            if len(new)==len(remain):break
            cert.append(q);remain=new
        if not remain:
            for q in cert[:]:
                others=[x for x in cert if x!=q]
                if all(any(not u&x for x in others) for u in unions):cert=others
            out.append(dict(pair=[i,j],domain_sizes=[len(cs[i]),len(cs[j])],sixes=cert))
    return out

def audit():
    p=D.parent;prior=json.loads((p/'ramsey_face_layer52.json').read_text());idx=149539
    with gzip.open(CAT.parent/'r37_21.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    b=decode((CAT/'r35_13.g6').read_text().strip());records=[]
    # Speed up discovery by using the original full first-side routine on this record.
    from functools import lru_cache
    I=ind(a);sets=set(I);levels={k:[q for q in I if q.bit_count()==k] for k in (4,5,6)}
    @lru_cache(None)
    def miss(s,k):return sum(1<<j for j,q in enumerate(levels[k]) if not s&q)
    for _,_,q,t,_,np,_ in [r for r in prior['rows'] if r[1]==idx and r[5]]:
        R=bits(8191^(q|t));ds=[4+(b[i]&(8191^(q|t))).bit_count() for i in R];found=0
        for ls in product(*[[i for i,v in enumerate(a) if v.bit_count()==d] for d in ds]):
            if len(set(ls))<5 or any((a[ls[i]]>>ls[j]&1)!=(b[R[i]]>>R[j]&1) for i,j in combinations(range(5),2)):continue
            mark=sum(1<<i for i in ls);tri=[s for s in I if s.bit_count()==3 and not s&mark];req=lambda g:[sum(1<<v for r,v in zip(R,ls) if b[h]>>r&1) for h in bits(g)];cs=sorted(([s|r for s in tri if s|r in sets] for r in req(q)),key=len)
            def rec(rows):
                if len(rows)==4:return True
                for s in cs[len(rows)]:
                    if any(miss(s,7-n)&__import__('functools').reduce(int.__and__,(miss(h,7-n) for h in group)) for n in range(1,len(rows)+1) for group in combinations(rows,n)):continue
                    if rec(rows+[s]):return True
                return False
            if not rec([]):continue
            found+=1;reqs=req(t);obs=pair_obstructions(a,mark,reqs);records.append(dict(q=q,t=t,mark=ls,req=reqs,blocked=obs))
        assert found==np
    from ramsey_cube_construct35 import G,cells,corner
    controls=[]
    for z,c in enumerate(cells):
        if c.count('*')!=2:continue
        four=G[z]&G[34];Q=G[34]&~four;T=G[z]&~four;H=bits(((1<<35)-1)&~(G[z]|G[34]|1<<z|1<<34));loc=lambda s:sum(1<<j for j,h in enumerate(H) if s>>h&1);aa=[loc(G[h]) for h in H];mark=loc(((1<<35)-1)^__import__('functools').reduce(int.__or__,(G[h] for h in bits(four))));assert len(H)==21 and mark.bit_count()==5
        for g in [Q,T]:
            rs=[loc(G[h])&mark for h in bits(g)];assert not pair_obstructions(aa,mark,rs);controls.append([z,g])
    print([(r['q'],r['mark'],[(s['pair'],len(s['sixes'])) for s in r['blocked']]) for r in records],len(controls));(p/'ramsey_face_pair_obstruction.json').write_text(json.dumps(dict(record=idx,failures=records,cube_sides=controls),indent=2)+'\n')
if __name__=='__main__':audit()
