"""Minimum exact recognition modulo mandatory six-set screen. Remove singleton failures, decompose residual constraints with disjoint row vocabularies, solve each cardinality optimum and its backbone."""
from ramsey_shared_row_fidelity import audit,minimum,D,json,bits,decode,Counter
from statistics import median

def intrinsic(P,T):
    f=sum(s for s in P if s.bit_count()==1);cs=[]
    for s in sorted((s for s in P if not f&s),key=int.bit_count):
        if all(s&t!=t for t in cs):cs.append(s)
    groups=[]
    for s in cs:
        touched=[(v,g) for v,g in groups if v&s];groups=[(v,g) for v,g in groups if not v&s];v=s;g=[s]
        for w,l in touched:v|=w;g.extend(l)
        groups.append((v,g))
    rows=[T[i] for i in bits(f)];components=[]
    for v,g in groups:
        res=minimum(g,T);rows+=res['rows'];components.append(dict(size=v.bit_count(),patterns=len(g),basis=res['rows'],always=res['all_min']))
    mask=sum(1<<i for i,t in enumerate(T) if t in rows);assert all(mask&s for s in P);return dict(rows=rows,forced=[T[i] for i in bits(f)],components=components,pattern_count=len(P))

def run():
    prev=json.loads((D/'ramsey_shared_row_fidelity.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in prev:
        p=r['parent'];G=decode(lines[p-1]);V=[i for i in range(22) if i!=r['deleted']];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];z=audit(H,set(),intrinsic);assert sorted(z['forced'])==sorted(r['forced']) and len(z['rows'])<=r['warm']+len(r['extra']);out.append(dict(parent=p,deleted=r['deleted'],augmented=r['warm']+len(r['extra']),**z))
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_intrinsic_attachment_basis.json').write_text(json.dumps(z)+'\n');n=[len(r['rows']) for r in z];print(sum(n),min(n),median(n),max(n),sum(len(c['always']) for r in z for c in r['components']),sum(len(r['components']) for r in z));print(Counter(len(r['rows'])-len(r['forced']) for r in z));print(sum(r['augmented']==len(r['rows']) for r in z));
