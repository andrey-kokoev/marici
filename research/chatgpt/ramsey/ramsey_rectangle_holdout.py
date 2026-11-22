"""Independent random cores. For every repairable maximal triple in sampled cores test minimal impossible commitments. At blocker fixed points test rectangle certificate and all binary obligations. Precomputed row bitsets."""
from ramsey_blocker_transfer_countersearch import *
from collections import Counter

def classify(H,s,live,T):
    rows=sorted({t&live for t in T if not t&s},key=int.bit_count);rows=[t for i,t in enumerate(rows) if all(t&u!=u for u in rows[:i])];pairs={t for t in rows if t.bit_count()==2};red=[(i,j) for i,j in combinations(bits(live),2) if H[i]>>j&1];rect=any(all((1<<x|1<<y) in pairs for x in a for y in b) for a,b in combinations(red,2) if not set(a)&set(b));binary=[t for t in rows if t.bit_count()<=2];sat=any(a&live==a and all(a&t for t in binary) for a in inds(H));return rect,sat,rows

def run(on_escape=None):
    rng=Random(1923);counts=Counter();examples={}
    for num in range(120):
        n=12+num%3;H=[0]*n;E=list(combinations(range(n),2));rng.shuffle(E)
        for x,y in E:
            if not H[x]&H[y] and rng.random()<.7:H[x]|=1<<y;H[y]|=1<<x
        I=inds(H);k=max(map(int.bit_count,I))+2;M=[s for s in I if all(s>>i&1 or s&t for i,t in enumerate(H))];F=(1<<n)-1;N={0:0}
        for s in sorted(I):
            if s:N[s]=N[s^(s&-s)]|H[(s&-s).bit_length()-1]
        counts['cores']+=1;T0=[s for s in I if k-4<=s.bit_count()<=k-2];miss={s:sum(1<<i for i,t in enumerate(T0) if not s&t) for s in M};sizes={z:sum(1<<i for i,t in enumerate(T0) if t.bit_count()==z) for z in range(k-4,k-1)}
        for q in combinations_with_replacement(M,3):
            a,b,c=[miss[s] for s in q];ab=a&b;twos=ab|(a&c)|(b&c);tr=ab&c
            if twos&sizes[k-2] or tr&sizes[k-3]:continue
            tight=((a|b|c)&sizes[k-2])|(twos&sizes[k-3])|(tr&sizes[k-4]);legal=[m for m in M if not tight&miss[m]]
            if not legal:continue
            counts['repairable']+=1;false={s for s in I if all(s&~m for m in legal)};T=[T0[i] for i in bits(tight)]
            for s in false:
                if any(s^(1<<i) in false for i in bits(s)):continue
                counts['minimal_bad']+=1;live=F^N[s]
                while all(live&t for t in T):
                    ban=sum(1<<v for v in bits(live) if any(not t&live&~H[v] for t in T));
                    if not ban:
                        rect,sat,rows=classify(H,s,live,T);tag='rectangle' if rect else 'higher' if sat else 'binary_only';counts[tag]+=1;examples.setdefault(tag,dict(H=H,k=k,fixed=q,commit=s,live=live,rows=rows,legal=legal))
                        if on_escape:on_escape(tag,H,rows)
                        break
                    live^=ban
        if 'higher' in examples and 'rectangle' in examples:break
    return dict(counts=counts,examples=examples)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_rectangle_holdout.json').write_text(json.dumps(out)+'\n')
