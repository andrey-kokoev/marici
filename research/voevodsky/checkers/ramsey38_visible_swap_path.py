"""Does a visible same-tail exchange relation give the column path, before any ordering?"""
from ramsey38_excel_fold_transport import graph,gzip,json,Counter,combinations,prev,sys
from functools import lru_cache
P=prev.out/'ramsey38_visible_swap_path_protocol.json';R=prev.out/'ramsey38_visible_swap_path.json'
protocol=dict(start=310321,records=128,roots='least degree-seven root per consecutive record',mask='Every unordered pair of outside rows, withholding both complete supports. Anchor 1 is the root, never exchanged. Test necessary seven-column subpath, not full width-eight formula.',adjacency='Two columns are neighbors iff two distinct visible size-three outside supports have exactly the same two other labels and differ precisely by these columns. This is a pair of observed alternatives, NOT a certified edit. No ordering or thresholds fitted.',primary='Exact path P7 on ALL seven columns (unique up to reversal). Separately count looser existence of spanning path and multiplicities, not credit as exact.',prediction='Among held-out size-three row pairs with exactly two shared labels, test if their differing columns are adjacent. Compare observed hits with edge density |E|/21 under a uniform column permutation per query. Repeated masks are not independent samples.')

def edges(rows):
    triples=set(m for m in rows if m.bit_count()==3);return frozenset(a^b for a,b in combinations(triples,2) if (a^b).bit_count()==2)
@lru_cache(None)
def path_count(E):
    def walk(last,mask):
        if mask==127:return 1
        return sum(walk(bit,mask|bit) for bit in (1<<i for i in range(7)) if not mask&bit and last|bit in E)
    return sum(walk(1<<i,1<<i) for i in range(7))//2

def run():
    assert json.loads(P.read_text())==protocol
    line=frozenset(3<<i for i in range(6));assert path_count(line)==1 and path_count(line|{65})==7 and path_count(frozenset())==0
    cnt=Counter();hist=Counter();out=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,w in enumerate(f,1):
            if i<protocol['start']:continue
            if i>=protocol['start']+protocol['records']:break
            g=graph(w.strip());u=next((v for v in sorted(g) if len(g[v])==7),None);cnt['records']+=1
            if not u:continue
            L=sorted(g[u]);rows={v:sum(1<<k for k,x in enumerate(L) if x in g[v]) for v in g.keys()-set(L)-{u}};c=Counter()
            for x,y in combinations(sorted(rows),2):
                E=edges(m for v,m in rows.items() if v!=x and v!=y);n=path_count(E);hist[len(E)]+=1;c['masks']+=1;c['spanning']+=n>0;c['exact_P7']+=bool(n and len(E)==6);c['unique_spanning']+=n==1
                s,t=rows[x],rows[y]
                if s.bit_count()==t.bit_count()==3 and (s&t).bit_count()==2:
                    c['eligible']+=1;c['hits']+=(s^t) in E;c['null_numerator']+=len(E);c['empty_when_eligible']+=not E
            cnt.update(c);out.append(dict(record=i,root=u,counts=dict(c)))
    print(cnt,hist);prev.save(R,dict(protocol_sha=prev.sha(P.read_bytes()),counts=dict(cnt),uniform_expected=cnt['null_numerator']/21,edges_per_mask=dict(hist),records=out))
if __name__=='__main__':{'freeze':lambda:prev.save(P,protocol),'test':run}[sys.argv[1]]()
