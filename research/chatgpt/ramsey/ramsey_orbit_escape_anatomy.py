"""Exhaust the escape routes when one of five obligation orbits is relaxed. Unordered supports quotient colour names, then quotient by actual old-core automorphisms. Record precisely which rows must fail and how many independently repairable pieces split each orbit."""
from ramsey_three_color_orbit_proof import D,json,graph,inds,bits,autos
from collections import Counter
from itertools import combinations

def run():
    H=graph((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()[5]);I=sorted(inds(H));A=autos(H);O=json.loads((D/'ramsey_three_color_orbit_proof.json').read_text())[5]['kernel'];T=sum(O,[]);ms=[sum(1<<j for j,t in enumerate(T) if not s&t) for s in I];maps=[{s:sum(1<<p[i] for i in bits(s)) for s in I} for p in A];out=[]
    for L in O:
        drop=sum(1<<T.index(t) for t in L);keep=((1<<len(T))-1)^drop;adj=[sum(1<<j for j in range(i,len(I)) if not x&I[j] and not a&ms[j]&keep) for i,(x,a) in enumerate(zip(I,ms))];count=0;reps=set();patterns=Counter();details={};common=set(range(18));sizes=Counter();
        for i,N in enumerate(adj):
            for j in bits(N):
                for k in bits(N&adj[j]):
                    S=(I[i],I[j],I[k]);v=(ms[i]&ms[j])|(ms[i]&ms[k])|(ms[j]&ms[k]);assert v and v&~drop==0;miss=tuple(T[h] for h in bits(v));key=min(tuple(sorted(p[s] for s in S)) for p in maps);rep=min(tuple(sorted(p[t] for t in miss)) for p in maps);reps.add(key);count+=1;patterns[rep]+=1;sizes[tuple(sorted(s.bit_count() for s in S))]+=1;details.setdefault(rep,S)
        # Smallest part of the removed orbit which suffices to block every escape.
        ps=list(patterns);allmiss={tuple(sorted(p[t] for t in pat)) for pat in ps for p in maps};minimal=[p for p in allmiss if not any(set(q)<set(p) for q in allmiss)];cores=[]
        for d in range(1,len(L)+1):
            cores=[c for c in combinations(L,d) if all(set(c)&set(m) for m in minimal)]
            if cores:break
        root,=[i for i,h in enumerate(H) if h.bit_count()==4];sig=lambda t:(int(bool(t>>root&1)),(t&H[root]).bit_count(),max((t&h).bit_count() for h in H),sum((t&h).bit_count()==3 for h in H));signature=sig(L[0]);assert {t for t in I if t.bit_count()==5 and sig(t)==signature}==set(L)
        out.append(dict(orbit=L,signature=signature,count=count,inequivalent=len(reps),profiles={str(k):v for k,v in sizes.items()},patterns=[dict(missed=k,count=v,example=details[k]) for k,v in patterns.items()],smallest_restoration=d,restorations=cores));print(len(L),count,len(reps),Counter(len(m) for m in minimal),d,len(cores),dict(sizes))
    return out
if __name__=='__main__':(D/'ramsey_orbit_escape_anatomy.json').write_text(json.dumps(run())+'\n')
