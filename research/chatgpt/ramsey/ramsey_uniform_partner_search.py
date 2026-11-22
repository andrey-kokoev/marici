"""Exact Hall-ratio >=3 decision on small folded links. For k>=4 choose 3k vertices, with at most k in every maximal independent family. Complete SAT search up to n/3. Uniform witness can be trimmed to size 3*alpha."""
from ramsey_capacity_transfer_78 import D,json,inds,decode,bits
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
from functools import lru_cache

def classify(V,E):
    n=len(V);F=(1<<n)-1;G=[F&~(1<<i|e) for i,e in enumerate(E)]
    def families(s,p,x):
        if not p|x:yield s;return
        u=max(bits(p|x),key=lambda i:(p&G[i]).bit_count());
        for i in bits(p&~G[u]):
            b=1<<i;yield from families(s|b,p&G[i],x&G[i]);p^=b;x|=b
    fam=sorted(families(0,F,0),key=int.bit_count,reverse=True);tests=[]
    for k in range(4,n//3+1):
        # At most n-3k omissions: any independent family larger than n-2k immediately rules this k out.
        if fam[0].bit_count()>n-2*k:break
        C=CardEnc.atleast(list(range(1,n+1)),3*k,encoding=EncType.seqcounter);top=C.nv;clauses=C.clauses.copy()
        for s in fam:
            if s.bit_count()<=k:break
            C=CardEnc.atmost([i+1 for i in bits(s)],k,top_id=top,encoding=EncType.seqcounter);top=C.nv;clauses+=C.clauses
        with Solver(name='g4',bootstrap_with=clauses) as sat:
            ok=sat.solve();tests.append(k)
            if ok:
                model=set(sat.get_model());u=sum(1<<i for i in [i for i in range(n) if i+1 in model][:3*k]);al=max((u&s).bit_count() for s in fam);assert al<=k;return dict(k=k,alpha=al,witness=[V[i] for i in bits(u)],families=len(fam),tests=tests)
    return dict(k=None,families=len(fam),tests=tests)

def embed(E,P):
    n=len(E);F=(1<<n)-1
    def go(cand,used,assign):
        if not cand:return assign
        i=min(cand,key=lambda i:(cand[i].bit_count(),-P[i].bit_count()));
        for v in bits(cand[i]):
            b=1<<v;cs={j:s&~b&(E[v] if P[i]>>j&1 else F) for j,s in cand.items() if j!=i}
            if all(cs.values()):
                w=go(cs,used|b,{**assign,i:v})
                if w:return w
        return None
    return go({i:sum(1<<j for j,e in enumerate(E) if e.bit_count()>=p.bit_count()) for i,p in enumerate(P)},0,{})

def run(limit):
    prior=json.loads((D/'ramsey_partner_threshold_pricing.json').read_text());fold={(r['parent'],r['first']):r for r in json.loads((D/'ramsey_partner_fractional_coloring.json').read_text())};drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    templates=[]
    for r in prior:
        if r['n']>limit:continue
        p,A=r['parent'],r['first'];G=decode(lines[p-1]);surv=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(surv) if G[x]>>y&1) for x in surv];V=fold[p,A]['vertices'];rows=[t for t in inds(H) if t.bit_count()==6 or t.bit_count()==5 and not A&t];m=[sum(1<<j for j,t in enumerate(rows) if not t&s) for s in V];E=[sum(1<<i for i,b in enumerate(m) if not b&a) for a in m];res=None
        if len(V)>46:
            for P in templates:
                a=embed(E,P)
                if a:
                    from itertools import combinations
                    U=list(a.values());assert all(any(E[i]>>j&1 for i,j in combinations(five,2)) for five in combinations(U,5));res=dict(k=4,witness=[V[i] for i in U],families='embedding');break
        if res is None:res=classify(V,E)
        if len(V)<=46 and res['k']==4:
            U=[V.index(s) for s in res['witness']];templates.append([sum(1<<j for j,w in enumerate(U) if E[v]>>w&1) for v in U])
        out.append(dict(parent=p,first=A,n=len(V),**res));print(p,A,len(V),res['k'],res['families'],flush=True);(D/'ramsey_uniform_partner_search.json').write_text(json.dumps(out)+'\n')
if __name__=='__main__':
    import sys
    run(int(sys.argv[1]) if len(sys.argv)>1 else 46)
