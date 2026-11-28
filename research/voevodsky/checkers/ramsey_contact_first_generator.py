"""Fixed four installed rows only. Filter edge marks using unmeetable demands; grow a fifth support from surviving demands."""
import json,gzip
from itertools import combinations,islice
from ramsey_retention_slice import D,CAT,decode,check

def audit():
    idx=42706;rows=[[3,9,15,17,18,22,23],[0,2,8,9,14,18,24],[5,11,13,16,17,19,25],[0,2,4,7,12,19,26]];rows=[sum(1<<i for i in r) for r in rows]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    I=[0];V=(1<<27)-1
    for i,n in enumerate(a):I.extend([q|1<<i for q in I if not q&n])
    load=lambda q:q.bit_count()+sum(not q&s for s in rows);assert max(map(load,I))==8;T=sorted((q for q in I if load(q)==8),key=lambda q:(q.bit_count(),q));S=[s for s in I if all(s&(n|1<<i) for i,n in enumerate(a))];full=(1<<len(S))-1;hit={q:sum(1<<j for j,s in enumerate(S) if s&q) for q in T}
    def intersection(qs):
        m=full
        for q in qs:m&=hit[q]
        return m
    def conflict(qs):
        assert not intersection(qs);pre=[full]
        for q in qs:pre.append(pre[-1]&hit[q]);
        rem=[];tail=full
        for j in reversed(range(len(qs))):
            if pre[j]&tail:rem.append(qs[j]);tail&=hit[qs[j]]
        return rem
    def grow(qs,graph):
        def solve(s,avail):
            left=[q&avail for q in qs if not q&s];
            if not left:return s
            c=min(left,key=int.bit_count)
            while c:
                b=c&-c;c^=b;res=solve(s|b,avail&~(b|graph[b.bit_length()-1]))
                if res is not None:return res
                avail^=b
            return None
        return solve(0,V)
    def labels(q):return [i for i in range(27) if q>>i&1]
    candidates={ (1<<i)|(1<<j) for i,j in combinations(range(27),2) if not a[i]>>j&1 and not a[i]&a[j] and not any(s>>i&1 and s>>j&1 for s in rows)};n=len(candidates);trace=[];passed=[];edge=0
    while candidates:
        residual=[q for q in T if not edge or q&edge!=edge]
        if not intersection(residual):
            core=conflict(residual);prev=len(candidates);candidates={e for e in candidates if any(q&e==e for q in core)};trace.append(dict(demands=list(map(labels,core)),before=prev,after=len(candidates)))
        else:
            i,j=labels(edge);g=a[:];g[i]|=1<<j;g[j]|=1<<i;s=grow(residual,g)
            if s is not None:
                G=g+[0]*6
                for k,t in enumerate(rows+[s],27):
                    G[k]=t|1<<32;G[-1]|=1<<k
                    for h in range(27):G[h]|=int(bool(t>>h&1))<<k
                assert check(G,(1<<33)-1,3,9);all_rows=[t for t in I if t&edge!=edge and all(t&q for q in residual)];assert s in all_rows
                passed.append(dict(edge=[i,j],generated_row=labels(s),remaining_demands=len(residual),total_legal_fifth_rows=len(all_rows)))
            candidates.remove(edge)
        if candidates:edge=min(candidates)
    out=dict(record=idx,original_rows=list(map(labels,rows)),tight_before=len(T),triangle_safe_edges=n,conflict_filters=trace,passed=passed);print(n,len(T),[(len(t['demands']),t['before'],t['after']) for t in trace],passed);(D.parent/'ramsey_contact_first_generator.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
