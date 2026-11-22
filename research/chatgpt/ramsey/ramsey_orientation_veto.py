"""Project maximum independent rows to seed-incidence profiles. A row using <=2 colors in one orientation vetoes it. Independent derivation by adjacent palette anchored at common endpoint, or opposite palette excluding whole seed. Test joint veto vs conflicting demands on sampled 27-vertex catalogue."""
import gzip
from itertools import combinations
from ramsey_square_level_transfer import D,json,graph,inds,bits,Counter
from ramsey_copy_three_reduction import prove

def run():
    sample=json.loads((D/'ramsey_square_level_transfer.json').read_text())['8'];ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();tables=[{u:c for u,c in r['table']} for r in prove()];ends=[5,9,6,10];out=[]
    for rec in sample:
        H=graph(ls[rec['record']-1]);n=len(H);I=inds(H);T=[t for t in I if t.bit_count()==7];small=[t for t in I if t.bit_count()==5];edges=[(i,j) for i,j in combinations(range(n),2) if H[i]>>j&1 and max(H[i].bit_count(),H[j].bit_count())<=6];rows=[]
        for (a,b),(c,d) in combinations(edges,2):
            if len({a,b,c,d})<4 or (H[a]|H[b])&(1<<c|1<<d):continue
            V=(a,b,c,d);W=sum(1<<v for v in V);Z=((1<<n)-1)&~(W|H[a]|H[b]|H[c]|H[d]);invis=next((t for t in small if not t&~Z),None);fails=[];collision=sum(1<<i for i in range(n) if (H[i]&W).bit_count()==2);cats=Counter()
            for table in tables:
                classes=[0]*4
                for i in range(n):
                    if W>>i&1:continue
                    prof=sum(1<<j for j,v in enumerate(V) if H[i]>>v&1);color=table[prof];
                    if color:classes[color.bit_length()-1]|=1<<i
                S=[cls|sum(1<<V[j] for j in bits(e)) for cls,e in zip(classes,ends)];bad={t for t in T if sum(bool(t&s) for s in S)<=2};fails.append(bad)
                for t in bad:
                    palette=[i for i,s in enumerate(S) if s&t];assert len(palette)==2;u,v=palette;common=ends[u]&ends[v];expected=sum(1<<V[j] for j in bits(common));assert t&W==expected
                    assert collision&t
                    cats['adjacent' if common else 'opposite']+=1
            shared=fails[0]&fails[1];tag='invisible' if invis else 'both pass' if not any(fails) else 'one pass' if not all(fails) else 'same veto' if shared else 'split veto';rows.append(dict(seed=W,tag=tag,collision=collision,counts=list(map(len,fails)),categories=cats,anchored=[sum(bool(t&W) for t in s) for s in fails],common=len(shared),witnesses=[min(s) if s else None for s in fails],joint=min(shared) if shared else None))
        assert sum(r['tag'] in ('both pass','one pass') for r in rows)==rec['counts'].get('successful_seeds',0);out.append(dict(record=rec['record'],rows=rows))
    return out
if __name__=='__main__':
    z=run();rows=[r for e in z for r in e['rows']];print(Counter(r['tag'] for r in rows),sum((r['categories'] for r in rows),Counter()));(D/'ramsey_orientation_veto.json').write_text(json.dumps(z)+'\n')
