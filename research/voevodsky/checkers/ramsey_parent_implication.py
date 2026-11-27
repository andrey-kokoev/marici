from ramsey_alternate_endpoint import *
from ramsey_five_port_multi import sevens
from itertools import chain

def run():
    found=[]
    for f in json.loads(C.read_text())['families'][:64]:
        S=grow(f['rows'],1);es=f['eligible'];enc=lambda p:sum(1<<e for e in es if all(p>>i&1 for i in ports[e]));a=graph(9,S,0);ws={}
        for q in sevens(a):ws.setdefault(enc(sum(1<<(j-9) for j in q if j>=9)),list(q))
        clauses=sorted(m for m in ws if not any(t!=m and t&m==t for t in ws));states=[sum(1<<e for j,e in enumerate(es) if m>>j&1) for m in range(1<<len(es))];legal=[c for c in states if all(c&m for m in clauses)];assert legal==[c for c in states if verdict(graph(9,S,c))];
        if not legal:continue
        for k,p,e,pred in f['targets']:
            if pred or len({(c>>e)&1 for c in legal})!=2:continue
            solutions=[]
            for g,v in [(0,0),(9,8)]:
                T=terms(S,g)
                for h in range(32):
                    if any(v in s for i,s in enumerate(S) if h>>i&1):continue
                    missed=[enc(q) for q in T if not h&q];internal=enc(h);local=lambda c:not(internal&c) and all(m&c for m in missed)
                    for expect in (0,1):
                        bad={c for c in states if bool(local(c))!=((c>>e)&1==expect)}
                        if bad.intersection(legal):continue
                        assert all(bool(local(c))==verdict(build({g:tuple(i+1 for i in range(5) if h>>i&1)},S,c)) for c in legal)
                        core=next(s for n in range(len(clauses)+1) for s in combinations(clauses,n) if not any(all(c&m for m in s) for c in bad));solutions.append(dict(endpoint=g,probe=h,success_if_red=expect,internal=internal,missed=missed,parent_clauses=core,clique_witnesses=[ws[m] for m in core],counterfactual=min(bad) if bad else None))
            if solutions:found.append(dict(rows=f['rows'],target=(k,p,e),solutions=solutions))
    assert len(found)==2;out=dict(protocol_sha=sha256((D.parent/'ramsey_parent_implication_protocol.md').read_bytes()).hexdigest(),results=found);print(out);save(D.parent/'ramsey_parent_implications.json',out)
if __name__=='__main__':run()
