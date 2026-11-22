"""Complete common INDUCED (3,5) template search on folded partner links. Enumerate all witnesses in the smallest host; deduplicate by induced isomorphism; keep embeddings in all remaining hosts."""
from itertools import combinations
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits

def embedding(E,P):
    F=(1<<len(E))-1
    def go(cs,a):
        if not cs:return a
        i=min(cs,key=lambda i:(cs[i].bit_count(),-sum(P[i]>>j&1 for j in cs)));rest={j:s for j,s in cs.items() if j!=i}
        for v in bits(cs[i]):
            ns={j:s&(E[v] if P[i]>>j&1 else F^(E[v]|1<<v)) for j,s in rest.items()}
            if all(ns.values()):
                b=go(ns,{**a,i:v})
                if b:return b
    return go({i:sum(1<<j for j,e in enumerate(E) if p.bit_count()<=e.bit_count() and len(P)-p.bit_count()<=len(E)-e.bit_count()) for i,p in enumerate(P)}, {})

def run():
    hard=json.loads((D/'ramsey_uniform_partner_search.json').read_text());fold={(r['parent'],r['first']):r for r in json.loads((D/'ramsey_partner_fractional_coloring.json').read_text())};drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();templates=[];out=[];count=0
    for h,r in enumerate(hard):
        p,A=r['parent'],r['first'];G=decode(lines[p-1]);vs=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(vs) if G[x]>>y&1) for x in vs];V=fold[p,A]['vertices'];rows=[t for t in inds(H) if t.bit_count()==6 or t.bit_count()==5 and not t&A];miss=[sum(1<<j for j,t in enumerate(rows) if not s&t) for s in V];E=[sum(1<<j for j,y in enumerate(miss) if not x&y) for x in miss];
        if h==0:
            bad=[sum(1<<i for i in u) for u in combinations(range(len(V)),5) if all(not(E[i]>>j&1) for i,j in combinations(u,2))];
            for u in combinations(range(len(V)),12):
                U=sum(1<<i for i in u)
                if any(U&s==s for s in bad):continue
                count+=1;P=[sum(1<<j for j,y in enumerate(u) if E[x]>>y&1) for x in u];
                if not any(embedding(Q,P) for Q in templates):templates.append(P)
        matches={}
        for i,P in enumerate(templates):
            a=embedding(E,P)
            if not a:continue
            w=[a[j] for j in range(12)];assert all(bool(E[w[j]]>>w[k]&1)==bool(P[j]>>k&1) for j,k in combinations(range(12),2));matches[i]=[V[j] for j in w]
        original=dict(matches)
        if len(matches)<len(templates):
            W=sorted(set(V)|{x for x,y in fold[p,A]['folds']});mw=[sum(1<<j for j,t in enumerate(rows) if not s&t) for s in W];EW=[sum(1<<j for j,y in enumerate(mw) if not x&y) for x in mw];
            for i,P in enumerate(templates):
                if i in original:continue
                a=embedding(EW,P)
                if a:original[i]=[W[a[j]] for j in range(12)]
        out.append(dict(parent=p,first=A,matches=matches,original=original));print(h,len(V),list(matches),list(original),flush=True)
    return dict(templates=templates,smallest_host_witness_count=count,hosts=out)
if __name__=='__main__':
    z=run();print(z['templates'],z['smallest_host_witness_count']);(D/'ramsey_common_partner_pattern.json').write_text(json.dumps(z)+'\n')
