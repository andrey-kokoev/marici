"""Explain each saved cycle by the incidence of core vertices and independent tens, without testing compatibility-graph isomorphism."""
from ramsey312_google_two_step import *
from collections import Counter
import functools,operator

def intervals(p,n):return sum(bool(p>>i&1 and not p>>((i-1)%n)&1) for i in range(n))
def main():
 rows=json.loads((D/'ramsey312_circular_exchange_cycles.json').read_text());T=list(sets(F,10));out=[];seen={}
 for r in rows:
    d=tuple(r['d']);c=tuple(r['cycle']);n=len(c);q=r['q'];h=F^sum(1<<i for i in d);common=functools.reduce(operator.and_,c);assert common
    if (d,c) in seen:continue
    seen[d,c]=True;cols={v:sum(1<<i for i,s in enumerate(c) if s>>v&1) for v in bits(h)};freq=Counter();rep={};badcol=[v for v,p in cols.items() if intervals(p,n)>1];windows=[sum(1<<((i+j)%n) for j in range(q)) for i in range(n)]
    for t in T:
        if t&~h:continue
        p=(1<<n)-1
        for v in bits(t):p&=~cols[v]
        if p:freq[p]+=1;rep.setdefault(p,t)
    assert all(any(not p&~w for w in windows) for p in freq);maximal=[p for p in freq if not any(p!=z and p&z==p for z in freq)];joint=sum(w in freq for w in windows);gap=[]
    for i,w in enumerate(windows):
        ends=(1<<i)|(1<<((i+q-1)%n));assert any(p&ends==ends for p in freq)
        if w not in freq:gap.append(i)
    # Held-Karp optimal tour count up to rotation/reversal using support masks only.
    @functools.lru_cache(None)
    def tour(i,rest):
        if not rest:return (c[i]^c[0]).bit_count(),1
        costs=[((c[i]^c[j]).bit_count()+v,k) for j in bits(rest) for v,k in [tour(j,rest^(1<<j))]];z=min(v for v,k in costs);return z,sum(k for v,k in costs if v==z)
    length,count=tour(0,(1<<n)-2);bound=2*sum(p not in (0,(1<<n)-1) for p in cols.values());assert length==bound;print('hamming tour',length,count//2,'common',list(bits(common)),'window count range',min(freq[w] for w in windows),max(freq[w] for w in windows));out.append(dict(d=d,cycle=c,q=q,hamming_length=length,optimal_orders=count//2,common=common,noninterval=badcol,columns=cols,window_counts=[freq[w] for w in windows],maximal=[dict(p=p,t=rep[p],count=freq[p]) for p in sorted(maximal)]));print(d,q,'noninterval',badcol,'full windows',joint,'/',n,'missing',gap,'maximal',len(maximal))
 (D/'ramsey312_cycle_incidence.json').write_text(json.dumps(out));print('unique',len(out))
if __name__=='__main__':main()
