"""Rooted partner link: six-set compatibility plus five-set tests involving the root are ordinary edges. A surviving triangle must cover every remaining five-set. Self-loops allow repeated supports."""
from ramsey_port_union_hierarchy import D,json,decode,inds,bits
from collections import Counter

def run(on_failure=None,on_triangle_free=None):
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];summary=Counter();examples={}
    for r in json.loads((D/'ramsey_port_union_hierarchy.json').read_text()):
        G=decode(lines[r['parent']-1]);V=[x for x in range(22) if x!=r['deleted']];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];I=inds(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));T={k:[t for t in I if t.bit_count()==k] for k in (5,6)};q,p=([sum(1<<j for j,t in enumerate(T[k]) if not s&t) for s in M] for k in (5,6));adj=[sum(1<<j for j,b in enumerate(p) if not a&b) for a in p];h=Counter()
        for a,A in enumerate(M):
            verts=list(bits(adj[a]));link={b:sum(1<<c for c in bits(adj[a]&adj[b]) if not q[a]&q[b]&q[c]) for b in verts};anyedge=any(link.values());triangle=False;ok=False;common=None;num=0;patterns={} if on_failure else None
            for b in verts:
                for c in bits(link[b]&~((1<<b)-1)):
                    for d in bits(link[b]&link[c]&~((1<<c)-1)):
                        triangle=True;miss=q[b]&q[c]&q[d];common=miss if common is None else common&miss;num+=1
                        if patterns is not None:patterns.setdefault(miss,(M[b],M[c],M[d]))
                        if not miss:ok=True;break
                    if ok:break
                if ok:break
            tag='pass' if ok else 'no_edge' if not anyedge else 'no_triangle' if not triangle else 'shared_row' if common else 'distributed';h[tag]+=1
            if tag=='no_triangle' and on_triangle_free:on_triangle_free(r,A,M,link,T)
            if tag=='distributed' and on_failure:on_failure(r,A,T[5],patterns,num)
            if tag not in examples:examples[tag]=dict(parent=r['parent'],deleted=r['deleted'],first=A,partners=len(verts),edges=sum((v&~((1<<b)-1)).bit_count() for b,v in link.items()),triangles_seen=num,shared=T[5][next(bits(common))] if common else None)
        assert h['pass']==r['first'][1];summary.update(h);out.append(h)
    return dict(summary=summary,examples=examples,per_core=out)
if __name__=='__main__':
    out=run();print(out['summary'],out['examples']);(D/'ramsey_first_link_obstructions.json').write_text(json.dumps(out)+'\n')
