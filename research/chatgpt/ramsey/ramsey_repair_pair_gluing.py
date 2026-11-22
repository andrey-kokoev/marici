"""Does knowing exactly which pairs coexist in some repair suffice to recognize extendible partial supports? Build the co-occurrence graph, enumerate its maximal cliques, compare to maximal legal repairs. Certify smallest bad faces by exhaustive subsets of spurious cliques."""
from itertools import combinations
from collections import Counter
from ramsey_fork_audit_uniform import D,json,inds,grow
from ramsey_final_miss_levels import bits

def test(H,M,mins):
    legal=set(s for s in M if any(m&s==m for m in mins));A=[0]*len(H);V=0
    for s in legal:
        V|=s
        for v in bits(s):A[v]|=s^(1<<v)
    def cliques(q,p,x):
        if not p|x:yield q;return
        pivot=max(bits(p|x),key=lambda v:(A[v]&p).bit_count());todo=p&~A[pivot]
        for v in bits(todo):
            b=1<<v;yield from cliques(q|b,A[v]&p,A[v]&x);p^=b;x|=b
    cs=set(cliques(0,V,0));extra=cs-legal;assert legal<=cs or all(any(s&c==s for c in cs) for s in legal);bad=None
    for c in extra:
        for k in range(3,(bad.bit_count() if bad else c.bit_count()+1)):
            for t in combinations(bits(c),k):
                s=sum(1<<v for v in t)
                if not any(s&m==s for m in legal):bad=s;break
            else:continue
            break
    return dict(legal=len(legal),spurious=len(extra),witness=bad,pair_extensions=[next(m for m in sorted(legal) if m&(1<<a|1<<b)==1<<a|1<<b) for a,b in combinations(bits(bad or 0),2)])

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);M=[s for s in inds(H) if all(s>>v&1 or s&r for v,r in enumerate(H))];src=json.loads((D/'ramsey_compulsory_kernel_test.json').read_text());out=[]
    for r in src['triples']:
        if r['minima']:out.append(dict(fixed=r['triple'],minima=len(r['minima']),**test(H,M,r['minima'])))
    return out
if __name__=='__main__':
    out=run();print(Counter((r['minima']==1,(r['witness'] or 0).bit_count()) for r in out));print(next((r for r in out if r['witness']),None));(D/'ramsey_repair_pair_gluing.json').write_text(json.dumps(out)+'\n')
