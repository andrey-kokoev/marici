"""Forward decomposition of K2,3 minus ux. Fix left supports U,V. The two ordinary right ports use maximal independent supports outside U|V; exceptional X may meet U but not V, and X|U must hit every old five-set. Enumerate the successive right-hand partner tests. No completed target as input."""
from ramsey_inverse_five_motifs import D,json,graph,inds,bits,Counter
from functools import lru_cache

def analyze(H):
    I=sorted(inds(H));T={k:[s for s in I if s.bit_count()==k] for k in (4,5)};ms={s:tuple(sum(1<<i for i,t in enumerate(T[k]) if not t&s) for k in (4,5)) for s in I};F=(1<<len(H))-1
    @lru_cache(None)
    def maximal(ban):return [s for s in I if not s&ban and all(s>>i&1 or H[i]&s for i in bits(F^ban))]
    stages=Counter();ex=None;right=Counter();left=[]
    for v in I:
        if v.bit_count()>3:continue
        for u in I:
            if u.bit_count()>4 or ms[u][1]&ms[v][1]:continue
            stages['left']+=1;B=maximal(u|v);P=[(y,z) for i,y in enumerate(B) for z in B[i:] if not ms[y][1]&ms[z][1]]
            if not P:continue
            stages['ordinary_pair']+=1;X=[x for x in maximal(v) if not ms[x][1]&ms[u][1]]
            if not X:continue
            stages['exceptional_partner']+=1;k=0;twogood=0
            for y,z in P:
                for x in X:
                    if ms[x][1]&(ms[y][1]|ms[z][1]):continue
                    twogood+=1
                    if ms[x][0]&ms[y][0]&ms[z][0]:continue
                    k+=1
                    if ex is None:ex=[u,v,x,y,z]
            if twogood:stages['all_pairs']+=1
            if k:stages['full']+=1;left.append([u,v]);right['ways']+=k
    return dict(stages=stages,example=ex,left=left,ways=right['ways'])
def check_bridges():
    ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in json.loads((D/'ramsey_inverse_five_motifs.json').read_text())['rows']:
        if r['motif']!=62:continue
        G=graph(ls[r['target']-1]);d=r['deleted'];V=list(bits(d));x=next(i for i in V if (G[i]&d).bit_count()==1);u,=[i for i in V if (G[i]&d).bit_count()==2 and not G[x]&G[i]&d and not G[x]>>i&1];v,=bits(G[x]&G[u]);assert (G[v]&~d).bit_count()==4 and G[v].bit_count()==6;out.append(dict(**r,missing=[x,u],bridge=v))
    return out
if __name__=='__main__':
    z=[analyze(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];print([(r['stages'],r['example']) for r in z]);(D/'ramsey_missing_cross_edge.json').write_text(json.dumps(z)+'\n');(D/'ramsey_missing_cross_edge_bridges.json').write_text(json.dumps(check_bridges())+'\n')
