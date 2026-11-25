"""Necessary single-side test: enumerate compatible common rows with exact local degrees."""
from ramsey310_fixed_exclusive_kernel import residual,kernel
import json
from pathlib import Path

def possible(A,E,cache=None,accept=None,triples=False):
    U=E[0]|E[-1]
    if cache is None:
        C,adj,_=kernel(A,E)
        inc=[sum(1<<i for i,s in enumerate(C) if s>>v&1) for v in range(27)]
    else:C,adj,inc=cache.kernel(E)
    ub=[9-a.bit_count()-sum(s>>v&1 for s in E) for v,a in enumerate(A)]
    assert len(E) in (1,2)
    lb=[max(0,x-(2-len(E))) if U>>v&1 else max(0,x-2) for v,x in enumerate(ub)]
    chosen=[];ids=[]
    assert not triples or cache is not None
    def visit(pool,k,lo,hi):
        if not k:return max(lo)<=0 and (accept is None or accept(tuple(chosen)))
        for v in range(27):
            if hi[v]<0 or lo[v]>k:return False
            if hi[v]==0:pool &= ~inc[v]
            if lo[v]==k:pool &= inc[v]
        if pool.bit_count()<k:return False
        # Every completion includes a row covering any still-mandatory vertex.
        # Branch on the first such row under a fixed order; keep noncovering rows eligible.
        opts=pool;size=pool.bit_count()
        for v in range(27):
            if lo[v]<=0:continue
            p=pool&inc[v];n=p.bit_count()
            if n<lo[v]:return False
            if n<size:opts=p;size=n
        while opts:
            b=opts&-opts;opts^=b;pool^=b;i=b.bit_length()-1;s=C[i];m=pool&adj[i]
            if triples:
                for j in ids:m &= ~cache.triple_block(min(i,j),max(i,j))
            if m.bit_count()>=k-1:
                hit=[s>>v&1 for v in range(27)]
                chosen.append(s);ids.append(i)
                if visit(m,k-1,[x-y for x,y in zip(lo,hit)],[x-y for x,y in zip(hi,hit)]):return True
                chosen.pop();ids.pop()
        return False
    return visit((1<<len(C))-1,7,lb,ub)

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]/'results'
    for f in ['ramsey310_codegree7_joint.jsonl','ramsey310_codegree7_five_hits.jsonl']:
        for r in map(json.loads,(root/f).read_text().splitlines()):
            if 'rows' in r:
                A=residual(r['record']);E=r['rows'][7:];print(json.dumps(dict(record=r['record'],sides=[dict(rows=e,passes=possible(A,e)) for e in (E[:2],E[2:])])),flush=True)
