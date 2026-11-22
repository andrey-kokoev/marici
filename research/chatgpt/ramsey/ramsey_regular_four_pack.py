"""Every maximal-support port on a 6-regular core consumes degree capacity at each of its vertices. Enumerate disjoint packings before applying any non-neighbourhood obligations; compute smallest row-family refutations of all packs."""
from ramsey_global_five_basis import minimum,D,json,decode,inds,bits
from collections import Counter

def run():
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for idx,line in enumerate(lines,1):
        H=decode(line)
        if not all(s.bit_count()==6 for s in H):continue
        I=inds(H);M=sorted(s for s in I if all(s>>i&1 or s&h for i,h in enumerate(H)));adj=[sum(1<<j for j in range(i+1,len(M)) if not M[i]&M[j]) for i in range(len(M))];T=[s for s in I if s.bit_count() in (4,5,6) and s not in H];miss=[sum(1<<j for j,t in enumerate(T) if not t&s) for s in M];mask={k:sum(1<<j for j,t in enumerate(T) if t.bit_count()==k) for k in (4,5,6)};levels=[len(M),0,0,0];glob=set();patterns={k:set() for k in mask};first=None;best=None;sz=Counter();pass6=pass5=0
        for i,N in enumerate(adj):
            for j in bits(N):
                levels[1]+=1;N2=N&adj[j]
                for k in bits(N2):
                    levels[2]+=1
                    for l in bits(N2&adj[k]):
                        levels[3]+=1;S=[M[v] for v in (i,j,k,l)];sz[tuple(sorted(s.bit_count() for s in S))]+=1;a,b,c,d=[miss[v] for v in (i,j,k,l)];ab=a&b;tw=ab|(a&c)|(b&c);x=(tw|((a|b|c)&d))&mask[6];y=((ab&c)|(tw&d))&mask[5];z=ab&c&d&mask[4];glob.add(x|y|z)
                        for h,u in zip((4,5,6),(z,y,x)):patterns[h].add(u)
                        pass6+=not x;pass5+=not(x|y);key=(x.bit_count(),y.bit_count(),z.bit_count())
                        if best is None or key<best:best=key;first=dict(ports=S,missed_six=[T[v] for v in bits(x)],missed_five=[T[v] for v in bits(y)],missed_four=[T[v] for v in bits(z)])
        def cert(P):return minimum(P,T)['rows'] if P and 0 not in P else None
        out.append(dict(record=idx,levels=levels,shapes={str(k):v for k,v in sz.items()},pass6=pass6,pass5=pass5,legal=0 in glob,minimum_rows=cert(glob),six_only=cert(patterns[6]),best=first));print(idx,levels,dict(sz),pass6,pass5,best,flush=True)
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_regular_four_pack.json').write_text(json.dumps(z)+'\n')
