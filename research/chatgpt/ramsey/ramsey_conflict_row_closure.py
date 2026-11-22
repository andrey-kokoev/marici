"""Saturate positive hitting obligations by red-edge conflict resolution; eliminate redundant supersets after each parallel round. Check existence and construct by shrinking a hitting set after closure."""
from ramsey_rectangle_holdout import run as holdout,D,json,bits,combinations,Counter

def minimal(rows):
    out=[]
    for s in sorted(set(rows),key=lambda s:(s.bit_count(),s)):
        if not any(t&s==t for t in out):out.append(s)
    return out

def solve(H,rows):
    T=minimal(rows);rounds=[]
    while 0 not in T:
        new=set(T)
        for a,b in combinations(T,2):
            for x in bits(a&~b):
                for y in bits(b&~a&H[x]):new.add((a^(1<<x))|(b^(1<<y)))
        U=minimal(new)
        if U==T:break
        rounds.append(U);T=U
    if 0 in T:return None,rounds
    s=(1<<len(H))-1
    for i in range(len(H)):
        v=s^(1<<i)
        if all(t&v for t in T):s=v
    assert all(s&t for t in rows) and all(not s&H[i] for i in bits(s));return s,rounds

def run():
    hist=Counter();examples={}
    def visit(tag,H,T):
        s,rounds=solve(H,T);assert s is None;hist[tag,len(rounds)]+=1;examples.setdefault(tag,dict(initial=T,rounds=rounds))
    holdout(visit);checks=0
    for g in range(8):
        H=[0]*3
        for i,(x,y) in enumerate(combinations(range(3),2)):
            if g>>i&1:H[x]|=1<<y;H[y]|=1<<x
        for f in range(256):
            T=list(bits(f));s,_=solve(H,T);assert (s is not None)==any(all(v&t for t in T) and all(not H[i]&v for i in bits(v)) for v in range(8));checks+=1
    return dict(hist={str(k):v for k,v in hist.items()},small=checks,examples=examples)
if __name__=='__main__':
    out=run();print(out['hist'],out['small']);(D/'ramsey_conflict_row_closure.json').write_text(json.dumps(out)+'\n')
