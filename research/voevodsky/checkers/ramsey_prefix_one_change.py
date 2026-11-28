"""Select four-port prefixes with a one-link continuation from predecessor alone. Old ports individually maximal."""
import gzip,json
from itertools import combinations,islice
from collections import Counter
from ramsey_retention_slice import CAT,D,decode,check


def run(idx):
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    I=[0];V=(1<<27)-1
    for j,n in enumerate(a):I.extend([q|1<<j for q in I if not q&n]);
    def maximal(g,sets):return [s for s in sets if all(s&(n|1<<j) for j,n in enumerate(g))]
    S=maximal(a,I);qs=[q for q in I if q.bit_count()>=4];allq=(1<<len(qs))-1;by=[sum(1<<j for j,q in enumerate(qs) if q>>i&1) for i in range(27)];size={k:sum(1<<j for j,q in enumerate(qs) if q.bit_count()==k) for k in range(4,8)};cache={}
    def miss(s):
        if s not in cache:
            tmp=allq;t=s
            while t:
                b=t&-t;t-=b;tmp &= ~by[b.bit_length()-1]
            cache[s]=tmp
        return cache[s]
    M=list(map(miss,S));N=[{j for j in range(i+1,len(S)) if not m&M[j]&size[7]} for i,m in enumerate(M)];assert all(m&size[7] for m in M);repairs=[]
    for u,v in combinations(range(27),2):
        if a[u]>>v&1 or a[u]&a[v]:continue
        e=(1<<u)|(1<<v);g=a[:];g[u]|=1<<v;g[v]|=1<<u;opts=maximal(g,(s for s in I if s&e!=e));repairs.append((e,by[u]&by[v],[(s,miss(s)) for s in opts]))
    counts=Counter();edges=Counter();samples=[];tight_counts=[[],[]];common=None
    for i in range(len(S)):
        for j in N[i]:
            ij=N[i]&N[j]
            for k in ij:
                for l in ij&N[k]:
                    p=(i,j,k,l);ms=[M[x] for x in p];m,n,o,h=ms;pair=(m&n)|(o&h)|((m|n)&(o|h));triple=((m&n)&(o|h))|((o&h)&(m|n));four=m&n&o&h
                    counts['seven_safe']+=1
                    if (triple&size[6])|(four&size[5]):continue
                    counts['legal_prefixes']+=1;T=((m|n|o|h)&size[7])|(pair&size[6])|(triple&size[5])|(four&size[4]);rows=[S[x] for x in p];assert all(T&b for b in M);passed=False
                    for e,broken,options in repairs:
                        if any(r&e==e for r in rows):continue
                        left=T&~broken;fifths=[s for s,b in options if not b&left];
                        if not fifths:continue
                        passed=True;edges[e]+=1;counts['prefix_edge_fifth_triples']+=len(fifths);samples.append(dict(prefix=rows,edge=[u for u in range(27) if e>>u&1],fifths=fifths));
                    if passed:common=set(rows) if common is None else common.intersection(rows)
                    counts['extendible_prefixes']+=passed;tight_counts[int(passed)].append(T.bit_count())
    bounds=[(min(c),max(c)) if c else None for c in tight_counts];out=dict(record=idx,triangle_safe_edges=len(repairs),counts=counts,common_starting_rows=sorted(common or []),extendible_by_edge={str(tuple(i for i in range(27) if e>>i&1)):v for e,v in edges.items()},tight_count_range_failure_success=bounds,witnesses=samples);print({k:v for k,v in out.items() if k!='witnesses'});return out
if __name__=='__main__':
    out=run(42706);(D.parent/'ramsey_prefix_one_change.json').write_text(json.dumps(out,indent=2)+'\n')
