"""Project missing-edge construction to X,Y,Z and the promise of a common neighbour b of U,X. Enumerate right triples meeting five-set diversity and inherited degree caps, then ask whether ANY U and finally V can attach (old fives only). No target inputs. Record gate of first unavoidable second bridge."""
from ramsey_inverse_five_motifs import D,json,graph,inds,bits,Counter

def audit(H):
    I=inds(H);T=[t for t in I if t.bit_count()==5];m={s:sum(1<<i for i,t in enumerate(T) if not s&t) for s in I};lo=sum(1<<i for i,s in enumerate(H) if s.bit_count()==4);R=[s for s in I if s.bit_count()<=4];P=[(y,z) for j,y in enumerate(R) for z in R[j:] if not m[y]&m[z] and not y&z&~lo];out=[]
    for b in bits(lo):
        B=1<<b;stats=Counter();examples={}
        for x in I:
            if not B&x:continue
            us=[u for u in R if u&B and not m[u]&m[x] and not (u&x)&~lo];vs=[v for v in I if not x&v and v.bit_count()<=3]
            for y,z in P:
                yz=y|z
                if B&yz or m[x]&(m[y]|m[z]) or x&yz&~lo or x&y&z:continue
                bridge=x&yz;cat=bridge.bit_count();stats['right',cat]+=1
                U=[u for u in us if not u&yz];
                if not U:continue
                stats['with_u',cat]+=1
                ans=next(((u,v) for v in vs if not v&yz for u in U if not m[u]&m[v] and not u&v&~lo),None)
                if ans:stats['with_v',cat]+=1;examples.setdefault(cat,[*ans,x,y,z]);
        out.append(dict(b=b,stats={f'{k}:{j}':v for (k,j),v in stats.items()},examples=examples))
    N=[sum(1<<j for j in range(i+1,len(I)) if not s&I[j] and not m[s]&m[I[j]]) for i,s in enumerate(I)];return dict(roots=out,disjoint_pairs=sum(n.bit_count() for n in N),disjoint_triangles=sum((N[i]&N[j]).bit_count() for i in range(len(I)) for j in bits(N[i])))
if __name__=='__main__':
    z=[audit(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];
    for i,rs in enumerate(z):print(i+1,rs['disjoint_triangles'],sum((Counter(r['stats']) for r in rs['roots']),Counter()))
    (D/'ramsey_exceptional_bridge_projection.json').write_text(json.dumps(z)+'\n')
