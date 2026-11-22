"""Why does pair consistency suffice? Seek a linear order at each port on which every other port-value's residual neighbourhood is an interval. Test pruned lists for laminarity, plus direct three-neighbourhood Helly and legal triangle extension."""
from ramsey_rooted_square_propagation import D,json,decode,inds,bits,test,Counter,product,combinations
from itertools import permutations

def audit(dom,L,E):
    ports=[]
    for k,F in enumerate(L):
        js=[j for j in range(4) if j!=k];U=list(bits(F));rows=[{E[j,k][i]&F for i in bits(L[j])} for j in js];sets=set.union(*rows);order=None
        for seq in permutations(U):
            if all(max(v for v,i in enumerate(seq) if s>>i&1)-min(v for v,i in enumerate(seq) if s>>i&1)+1==s.bit_count() for s in sets):order=[dom[k][i] for i in seq];break
        bad=[(a,b,c) for a,b,c in product(*rows) if a&b and a&c and b&c and not a&b&c];tri=dead=0
        i,j,h=js
        for a in bits(L[i]):
            for b in bits(L[j]&E[i,j][a]):
                for c in bits(L[h]&E[i,h][a]&E[j,h][b]):
                    tri+=1;dead+=not(E[i,k][a]&E[j,k][b]&E[h,k][c]&F)
        ports.append(dict(size=len(U),interval=order,laminar=all(not(a&b) or a&b in (a,b) for a,b in combinations(sets,2)),partition=all(not(a&b) for a,b in combinations(sets,2)),neighbourhoods=len(sets),nonhelly=len(bad),triangles=tri,stranded=dead,sets=[[dom[k][i] for i in bits(s)] for s in sorted(sets)]))
    return ports

def run():
    prev=json.loads((D/'ramsey_rooted_square_propagation.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];last=None
    for r in prev:
        if not r['pc']:continue
        idx=r['record'];
        if idx!=last:
            H=decode(lines[idx-1]);I=inds(H);T=[[t for t in I if t.bit_count()==k] for k in (4,5,6)];miss={s:[sum(1<<j for j,t in enumerate(ts) if not t&s) for ts in T] for s in I};last=idx
        res=[];test(H,I,miss,r['seed'],lambda d,l,e:res.extend(audit(d,l,e)));out.append(dict(record=idx,seed=r['seed'],ports=res))
    return out
if __name__=='__main__':
    z=run();ps=[p for r in z for p in r['ports']];print(Counter((bool(p['interval']),bool(p['nonhelly']),bool(p['stranded'])) for p in ps));print('interval seeds',sum(all(p['interval'] for p in r['ports']) for r in z),'triangles',sum(p['triangles'] for p in ps),'stranded',sum(p['stranded'] for p in ps));(D/'ramsey_square_residual_helly.json').write_text(json.dumps(z)+'\n')
